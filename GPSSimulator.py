import json
from PySide6.QtCore import QTimer, QObject, Signal, QDateTime

class GPSSimulator(QObject):
    location_updated = Signal(float, float)

    def __init__(self, gps_json_path, update_interval=1000):
        super().__init__()
        self.gps_json_path = gps_json_path
        self.update_interval = update_interval  # Time between emissions in ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_position)

        self.gps_data = []
        self.route_index = 0
        self.load_data()

    def load_data(self):
        try:
            with open(self.gps_json_path, 'r') as f:
                new_data = json.load(f)

            # Add QDateTime objects to new points
            for point in new_data:
                if 'qdatetime' not in point:
                    point['qdatetime'] = QDateTime.fromString(point['timestamp'], "yyyy-MM-dd HH:mm:ss")

            self.gps_data = new_data

        except Exception as e:
            print("Failed to load GPS data:", e)

    def start_simulation(self):
        self.timer.start(self.update_interval)

    def stop_simulation(self):
        self.timer.stop()

    def update_position(self):
        # Reload file to get newly added points
        self.load_data()

        if self.route_index < len(self.gps_data):
            point = self.gps_data[self.route_index]
            lat = point["latitude"]
            lon = point["longitude"]
            self.location_updated.emit(lat, lon)
            self.route_index += 1
        else:
            # No new points to emit yet
            pass
