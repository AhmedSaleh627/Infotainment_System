import sys
import io
import folium
import platform
import subprocess
import numpy as np
import json  # Add this import at the top

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QSizePolicy, QGraphicsPixmapItem, QGraphicsScene, QVBoxLayout, QTextEdit, QMessageBox
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import QIcon, QPixmap, QPainter, QColor, QPen, QFont
from PySide6.QtCore import QTimer, QDateTime, Qt, QRectF, QPointF, QSize, QPropertyAnimation

from drawing_widget import DrawingWidget
from update_checker import UpdateChecker
from DMS import DrowsinessDetector

from ui_form import Ui_Widget

from navigation_simulator import NavigationSimulator



class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initialize_system()



    def initialize_system(self):
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.update_checker = UpdateChecker()
        self.ui.check_updates_btn.clicked.connect(self.check_for_updates)
        self.ui.update_now_btn.clicked.connect(self.update_now)
        self.detector = DrowsinessDetector(
                    "assets/AI_Models/best.pt",
                    31.248818720920042, 29.969674052607445,
                    "xxxx",
                    "xxxx",
                    "+201207955600", "+14159917415"
                )
        self.detector.log_update.connect(self.update_log)
        self.detector.drowsiness_detected.connect(self.on_drowsiness_detected)
        # Start detection automatically
        self.ui.dms_Updates.append("Starting Drowsiness Detection...")
        self.detector.frame_ready.connect(self.update_camera_feed)
        self.detector.start()
        self.web_view = None
        self.map_initialized = False
        # 31.254432625016356, 29.990215430955605
        # Start and destination coordinates
        start_lat, start_lon = 31.25715824560256, 29.980877224491945  # Home
        end_lat, end_lon = 31.254432625016356, 29.990215430955605 # Work
        # Create the simulator with route-based navigation
        self.simulator = NavigationSimulator(start_lat, start_lon, end_lat, end_lon)
        self.simulator.location_updated.connect(self.update_marker)  # Connect to update function
        self.is_locked = True
        self.is_seatbelt = True
        self.is_powered=False
        self.ui.power.clicked.connect(self.toggle_power)
        self.ui.homeBtn.clicked.connect(self.show_home_page)
        self.ui.fotaBtn.clicked.connect(self.show_fota_page)
        self.ui.calendarBtn.clicked.connect(self.show_calendar_page)
        self.ui.wifiBtn.clicked.connect(self.show_wifi_page)
        self.ui.mapBtn.clicked.connect(self.show_map_page)
        self.ui.lockBtn.clicked.connect(self.toggle_lock)
        self.ui.seatbeltBtn.clicked.connect(self.toggle_seatbelt)
        self.ui.refreshButton.clicked.connect(self.scan_wifi)
        self.scan_wifi()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_date_time)
        self.timer.start(1000)
        self.update_date_time()
        self.ui.progressBar.setValue(0)
        self.progress_value = 0
        self.progress_timer = QTimer(self)
        self.progress_timer.timeout.connect(self.simulate_progress)
        self.progress_timer.start(100)
        self.update_progress_style(self.progress_value)
        # Store the reference to the DrawingWidget here, so it persists between page transitions
        self.current_drawing_widget = None





    def update_log(self, message):
        """Update the log display with new messages."""
        self.ui.dms_Updates.append(message)

    def on_drowsiness_detected(self, address):
        """Handle drowsiness detected signal."""
        self.ui.dms_Updates.append(f"DROWSINESS ALERT! Address: {address}")

    def closeEvent(self, event):
        """Ensure the detector stops when the application is closed."""
        self.detector.stop_detection()
        event.accept()
    def update_camera_feed(self, image):
        """Update QLabel with the latest frame."""
        scaled_image = image.scaled(self.ui.dms_CameraFeed.width(), self.ui.dms_CameraFeed.height(), Qt.KeepAspectRatio)
        self.ui.dms_CameraFeed.setPixmap(QPixmap.fromImage(scaled_image))

    def check_for_updates(self):
        # Check for updates
        update_available = self.update_checker.check_updates()

        # Get the update status message
        status_message = self.update_checker.get_update_status()

        release_notes=self.update_checker.get_release_notes()

        # Update the QTextEdit or QLabel with the status message
        self.ui.status_text.setText(status_message)  # Assuming you have a QTextEdit named updateStatusText
        self.ui.release_notes_text.setText(release_notes)

    def update_now(self):
        update_available = self.update_checker.check_updates()

        apply_update = self.update_checker.apply_updates()

        self.ui.release_notes_text.setText(apply_update)




    def scan_wifi(self):
        """Scans for available Wi-Fi networks and updates the list widget."""
        self.ui.wifiListWidget.clear()
        wifi_list = self.get_wifi_networks()

        if wifi_list:
            self.ui.wifiListWidget.addItems(wifi_list)
        else:
            self.ui.wifiListWidget.addItem("No networks found!")

    def get_wifi_networks(self):
        """Retrieve available Wi-Fi networks based on OS."""
        wifi_networks = []
        os_name = platform.system()

        try:
            if os_name == "Windows":
                output = subprocess.check_output(["netsh", "wlan", "show", "networks"], encoding="utf-8")
                wifi_networks = self.parse_windows_output(output)
            elif os_name == "Linux":
                output = subprocess.check_output(["nmcli", "-t", "-f", "SSID", "dev", "wifi"], encoding="utf-8")
                wifi_networks = output.strip().split("\n")
            else:
                wifi_networks.append("Unsupported OS")
        except Exception as e:
            wifi_networks.append(f"Error: {str(e)}")

        return wifi_networks

    def parse_windows_output(self, output):
        """Extract SSID names from Windows netsh output."""
        wifi_networks = []
        for line in output.split("\n"):
            if "SSID" in line:
                ssid = line.split(":")[-1].strip()
                if ssid:
                    wifi_networks.append(ssid)
        return wifi_networks

    def simulate_progress(self):
        """
        Simulates the progress bar value changing dynamically.
        """
        self.progress_value += 1
        if self.progress_value > 100:
            self.progress_value = 0
        self.ui.progressBar.setValue(self.progress_value)
        self.update_progress_style(self.progress_value)

    def update_progress_style(self, value):
        """
        Dynamically updates the style of the progress bar based on its value.
        """
        if value <= 20:
            color_start = "#ff4e50"
            color_end = "#f9d423"
        elif 21 <= value <= 40:
            color_start = "#f9d423"
            color_end = "#f39c12"
        elif 41 <= value <= 49:
            color_start = "#cddc39"
            color_end = "#8bc34a"
        elif value >= 50:
            color_start = "#76c7c0"
            color_end = "#4CAF50"
        self.ui.progressBar.setStyleSheet(f"""
            QProgressBar {{
                border: 2px solid #555;
                border-radius: 10px;
                background-color: #2d2d30;
                text-align: center;
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 1px;
            }}
            QProgressBar::chunk {{
                background: qlineargradient(
                    spread:pad,
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 {color_start},
                    stop:1 {color_end}
                );
                margin: 2px;
                border-radius: 8px;
            }}
        """)

    def update_date_time(self):
        current_datetime = QDateTime.currentDateTime()
        formatted_datetime = current_datetime.toString("ddd, MMM d, yyyy")
        formatted_time = current_datetime.toString("hh:mm:ss AP")
        display_text = f"""
        <p style='font-size:22px; font-weight:bold; color:white; margin:0; text-align:center;'>{formatted_datetime}</p>
        <p style='font-size:18px; font-weight:normal; color:white; margin:5px 0 0 0; text-align:center;'>{formatted_time}</p>
        """
        self.ui.dateTimeLabel.setText(display_text)

    def toggle_lock(self):
        self.is_locked = not self.is_locked
        if self.is_locked:
            self.ui.lockBtn.setIcon(QIcon('assets/icons/lock.png'))
        else:
            self.ui.lockBtn.setIcon(QIcon('assets/icons/unlock.png'))


    def toggle_power(self):
        self.is_powered = not self.is_powered
        if self.is_powered:
            self.ui.power.setIcon(QIcon('assets/icons/car_on.png'))
        else:
            self.ui.power.setIcon(QIcon('assets/icons/car_shut.png'))



    def toggle_seatbelt(self):
        self.is_seatbelt = not self.is_seatbelt
        if self.is_seatbelt:
            self.ui.seatbeltBtn.setIcon(QIcon('assets/icons/safebelt.png'))
        else:
            self.ui.seatbeltBtn.setIcon(QIcon('assets/icons/no_seatbelt.png'))

    def show_home_page(self):
        # Only create a new DrawingWidget if it doesn't exist already
        if self.current_drawing_widget is None:
            self.current_drawing_widget = DrawingWidget(self)
            self.ui.homePageLayout.addWidget(self.current_drawing_widget)

        self.ui.stackedWidget.setCurrentIndex(1)  # Set homePage as active

    def show_calendar_page(self):
        self.ui.stackedWidget.setCurrentIndex(3)  # Set calendar page as active

    def show_fota_page(self):
        self.ui.stackedWidget.setCurrentIndex(4)  # Set calendar page as active

    def show_wifi_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)  # Set calendar page as active

    def show_map_page(self):
        if not self.map_initialized:
            # Convert Python route coordinates to a JavaScript-friendly format
            route_coords_json = json.dumps(self.simulator.route_coords)  # Convert list of tuples to JSON string

            # Example vehicle positions (replace with real values)
            #31.249831568513677, 29.982195755594645
            vehicle_positions = [
                (31.258319955764655,  29.989407850868474),  # Vehicle 1
                (31.25860276010398, 29.98354532964045),  # Vehicle 2
                (31.249831568513677, 29.982195755594645)   # Vehicle 3
            ]
            vehicle_coords_json = json.dumps(vehicle_positions)  # Convert to JSON format

            # Create an HTML page with Leaflet.js
            map_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Live Map</title>
                <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
                <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
            </head>
            <body>
                <div id="map" style="width: 100%; height: 100vh;"></div>
                <script>
                    var map = L.map('map').setView([{self.simulator.lat}, {self.simulator.lon}], 15);
                    L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
                        attribution: '&copy; OpenStreetMap contributors'
                    }}).addTo(map);

                    // Define car icon (for all vehicles)
                    var carIcon = L.icon({{
                        iconUrl: 'https://cdn-icons-png.flaticon.com/64/744/744465.png',
                        iconSize: [40, 40],
                        iconAnchor: [20, 20],
                        popupAnchor: [0, -20]
                    }});

                    // Add main vehicle marker
                    var marker = L.marker([{self.simulator.lat}, {self.simulator.lon}], {{ icon: carIcon }}).addTo(map);

                    // Parse route coordinates and draw polyline
                    var routeCoords = {route_coords_json};
                    if (routeCoords.length > 0) {{
                        var polyline = L.polyline(routeCoords, {{ color: 'blue', weight: 4 }}).addTo(map);
                        map.fitBounds(polyline.getBounds());
                    }}

                    // Parse vehicle coordinates and add markers (all using car icon)
                    var vehicleCoords = {vehicle_coords_json};
                    vehicleCoords.forEach((coords, index) => {{
                        L.marker([coords[0], coords[1]], {{ icon: carIcon }})
                            .addTo(map)
                            .bindPopup("Vehicle " + (index + 1));
                    }});

                    // Function to update main marker position
                    function updateMarkerPosition(lat, lon) {{
                        marker.setLatLng([lat, lon]);
                        map.setView([lat, lon]);
                    }}

                    window.map = map;
                    window.marker = marker;
                    window.updateMarkerPosition = updateMarkerPosition;
                </script>
            </body>
            </html>
            """

            # Load the HTML into QWebEngineView
            self.web_view = QWebEngineView(self)
            self.web_view.setHtml(map_html)
            self.web_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.web_view.setGeometry(self.ui.mapPage.rect())
            self.ui.mapPage.layout().addWidget(self.web_view)

            self.simulator.start_simulation()
            self.map_initialized = True

        self.ui.stackedWidget.setCurrentIndex(2)


    def inject_javascript(self):
        """Ensure the `map` and `marker` variables are globally accessible."""
        js_code = """
            setTimeout(function() {
                if (typeof L !== 'undefined') {
                    window.map = map;  // Expose `map` globally
                    window.marker = L.marker([%f, %f]).addTo(map);
                } else {
                    console.error("Leaflet (L) or map is not defined yet.");
                }
            }, 1000);
        """ % (self.simulator.lat, self.simulator.lon)

        self.web_view.page().runJavaScript(js_code)


    def update_marker(self, new_lat, new_lon):
        """Move the marker dynamically without resetting zoom or user interactions."""
        if hasattr(self, "web_view") and self.web_view is not None:
            js_code = f"""
            if (typeof window.marker !== 'undefined' && typeof window.map !== 'undefined') {{
                let currentZoom = window.map.getZoom();  // Store zoom level
                let currentCenter = window.map.getCenter();  // Store center
                window.marker.setLatLng([{new_lat}, {new_lon}]);  // Move marker
                window.map.setView(currentCenter, currentZoom);  // Keep same zoom & center
            }} else {{
                console.error("Marker or map is not defined yet.");
            }}
            """

            self.web_view.page().runJavaScript(js_code)


    def update_map(self):
        """Move the marker dynamically without resetting zoom or center."""
        if hasattr(self, "web_view") and self.web_view is not None:
            js_code = f"""
            if (typeof window.marker !== 'undefined' && typeof window.map !== 'undefined') {{
                let currentZoom = window.map.getZoom();
                let currentCenter = window.map.getCenter();
                window.marker.setLatLng([{self.simulator.lat}, {self.simulator.lon}]);
                window.map.setView(currentCenter, currentZoom);  // Keep zoom & center
            }} else {{
                console.error("Marker or map is not defined yet.");
            }}
            """

            self.web_view.page().runJavaScript(js_code)


