from PySide6.QtCore import QObject, Signal, QThread
from PySide6.QtGui import QImage, QPixmap
import cv2
import time
import requests
from ultralytics import YOLO
from twilio.rest import Client

class DrowsinessDetector(QThread):
    drowsiness_detected = Signal(str)  # Emit when drowsiness is detected
    frame_ready = Signal(QImage)  # Emit a QImage for the QLabel
    log_update = Signal(str)  # Emits log updates for QTextEdit
    def __init__(self, model_path, lat, lon, account_sid, auth_token, to_number, from_number, parent=None):
        super().__init__(parent)
        self.model = YOLO(model_path)
        self.LATITUDE = lat
        self.LONGITUDE = lon
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.to_number = to_number
        self.from_number = from_number
        self.running = False
        self.drowsy_start_time = None
        self.alert_sent = False
        self.cap = None

    def get_address(self):
        """Retrieve address from latitude and longitude using LocationIQ API."""
        API_KEY = 'pk.e0ff0d6fd9860aefd7ba7a3c6b9bd1b2'
        url = f'https://us1.locationiq.com/v1/reverse.php?key={API_KEY}&lat={self.LATITUDE}&lon={self.LONGITUDE}&format=json'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get('display_name', 'Unknown location')
        else:
            self.log_update.emit(f"Error fetching address: {response.status_code}")
            return 'Unknown location'

    def send_alert_call(self, address):
        """Send an alert call via Twilio."""
        client = Client(self.account_sid, self.auth_token)
        twiml_message = f'<Response><Say voice="alice">Driver has been in an accident or is in a drowsy state. Please hurry to the following location: {address}</Say></Response>'
        client.calls.create(
            twiml=twiml_message,
            to=self.to_number,
            from_=self.from_number
        )
        self.log_update.emit(f"Alert call placed! Location: {address}")

    def run(self):
        """Main loop to detect drowsiness and send frames."""
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Error: Could not open webcam.")
            self.log_update.emit("Error: Could not open webcam.")
            return

        self.running = True
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                print("Error: Failed to capture image from webcam.")
                self.log_update.emit("Error: Failed to capture image from webcam.")
                break

            results = self.model(frame)
            drowsy_detected = False

            # Check detection results
            for result in results:
                for box in result.boxes:
                    if box.cls == 1 and box.conf >= 0.7:  # '1' is the drowsiness class
                        drowsy_detected = True
                        print("Drowsiness detected in frame!")
                        break

            if drowsy_detected:
                if self.drowsy_start_time is None:
                    self.drowsy_start_time = time.time()
                    self.log_update.emit("Drowsiness detected! Timer started.")
                    print("Drowsiness detected! Timer started.")
                else:
                    elapsed_time = time.time() - self.drowsy_start_time
                    self.log_update.emit(f"Drowsiness detected for {elapsed_time:.2f} seconds.")
                    print(f"Drowsiness detected for {elapsed_time:.2f} seconds.")

                    if elapsed_time >= 3 and not self.alert_sent:
                        print("Drowsiness detected for 3 seconds! Sending alert...")
                        address = self.get_address()
                        self.drowsiness_detected.emit(address)  # Emit signal to Qt
                        self.send_alert_call(address)
                        self.alert_sent = True
                        self.log_update.emit("ALERT SENT! Waiting for driver response.")

            else:
                self.drowsy_start_time = None  # Reset timer if no drowsiness

            # Draw bounding boxes
            frame_with_boxes = results[0].plot()

            # Convert BGR to RGB for correct colors
            frame_with_boxes = cv2.cvtColor(frame_with_boxes, cv2.COLOR_BGR2RGB)

            # Convert frame to QImage
            height, width, channels = frame_with_boxes.shape
            bytes_per_line = channels * width
            qt_image = QImage(frame_with_boxes.data, width, height, bytes_per_line, QImage.Format_RGB888)

            # Emit frame for display in Qt
            self.frame_ready.emit(qt_image)

        self.cap.release()


    def stop_detection(self):
        """Stop the detection loop."""
        self.running = False
        if self.cap:
            self.cap.release()
