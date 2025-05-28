import openrouteservice
from PySide6.QtCore import QTimer, QObject, Signal

API_KEY = "5b3ce3597851110001cf624803ee18469b4e46b1a3545b41bbf1b894"
client = openrouteservice.Client(key=API_KEY)

class NavigationSimulator(QObject):
    location_updated = Signal(float, float)  # Signal to update UI with new coordinates

    def __init__(self, start_lat, start_lon, end_lat, end_lon, update_interval=100):
        super().__init__()
        self.lat = start_lat
        self.lon = start_lon
        self.update_interval = update_interval  # in milliseconds
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_position)

        # Get the route from OpenRouteService
        self.route_coords = self.get_route(start_lat, start_lon, end_lat, end_lon)
        self.route_index = 0  # To track position along the route

    def get_route(self, start_lat, start_lon, end_lat, end_lon):
        """Fetch route coordinates using OpenRouteService."""
        start = (start_lon, start_lat)  # OpenRouteService requires (lon, lat)
        end = (end_lon, end_lat)

        route = client.directions(
            coordinates=[start, end],
            profile="driving-car",
            format="geojson"
        )

        route_coords = route["features"][0]["geometry"]["coordinates"]
        return [(lat, lon) for lon, lat in route_coords]  # Convert to (lat, lon)

    def start_simulation(self):
        self.timer.start(self.update_interval)

    def stop_simulation(self):
        self.timer.stop()

    def update_position(self):
        """Move along the route and emit updated coordinates."""
        if self.route_index < len(self.route_coords):
            self.lat, self.lon = self.route_coords[self.route_index]
            self.route_index += 1
            self.location_updated.emit(self.lat, self.lon)  # Emit signal
        else:
            self.stop_simulation()  # Stop when reaching the destination
