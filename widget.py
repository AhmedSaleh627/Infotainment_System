import sys
import io
import folium
from PySide6.QtWidgets import QApplication, QWidget, QSizePolicy
from PySide6.QtWebEngineWidgets import QWebEngineView
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Initialize the web view and map variables to avoid reinitialization
        self.web_view = None
        self.map_initialized = False

        # Connect buttons to their respective methods
        self.ui.homeBtn.clicked.connect(self.show_home_page)
        self.ui.calendarBtn.clicked.connect(self.show_calendar_page)
        self.ui.mapBtn.clicked.connect(self.show_map_page)

    def show_home_page(self):
        # Show the home page in the stacked widget
        self.ui.stackedWidget.setCurrentIndex(2)  # Assuming homePage is index 0

    def show_calendar_page(self):
        # Show the calendar page in the stacked widget
        self.ui.stackedWidget.setCurrentIndex(0)  # Assuming calendarPage is index 1

    def show_map_page(self):
        # Check if the map has already been initialized
        if not self.map_initialized:
            # Create a Folium map centered on a specific location (e.g., Alexandria, Egypt)
            folium_map = folium.Map(location=[31.257196646654524, 29.98070623246377], zoom_start=30)

            # Add a marker for your location
            folium.Marker(
                location=[31.257196646654524, 29.98070623246377],  # Your location
                popup='My Location',  # Popup text when the marker is clicked
                icon=folium.Icon(color='blue', icon='info-sign')  # Marker style
            ).add_to(folium_map)

            # Save the Folium map to an in-memory byte stream
            map_html = folium_map._repr_html_()  # Get the HTML representation of the map

            # Create a QWebEngineView instance only if not already created
            self.web_view = QWebEngineView(self)

            # Set the byte stream as the content for the QWebEngineView
            self.web_view.setHtml(map_html)

            # Set the size policy to Expanding both horizontally and vertically
            self.web_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            # Set the geometry to cover the full page
            self.web_view.setGeometry(self.ui.mapPage.rect())

            # Add the QWebEngineView widget to the mapPage
            self.ui.mapPage.layout().addWidget(self.web_view)

            # Mark the map as initialized
            self.map_initialized = True

        # Set the current index of the stacked widget to the map page
        self.ui.stackedWidget.setCurrentIndex(1)  # Assuming mapPage is index 2

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
