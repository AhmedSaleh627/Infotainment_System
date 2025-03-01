import sys
import io
import folium
import platform
import subprocess

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QSizePolicy, QGraphicsPixmapItem, QGraphicsScene, QVBoxLayout, QTextEdit, QMessageBox
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import QIcon, QPixmap, QPainter, QColor, QPen, QFont
from PySide6.QtCore import QTimer, QDateTime, Qt, QRectF, QPointF, QSize, QPropertyAnimation, QUrl

from drawing_widget import DrawingWidget
from update_checker import UpdateChecker
from ui_form import Ui_Widget




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

        self.web_view = None
        self.map_initialized = False
        self.is_locked = True
        self.open_rf = False
        self.open_lf = False
        self.open_rb = False
        self.open_lb = False
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
        self.ui.car.setIcon(self.colorize_icon('assets/icons/all_closed.png', QColor("#FF0000")))
        self.ui.car.setIconSize(QSize(130, 130))
        self.ui.RF.clicked.connect(self.toggle_RF)
        self.ui.LF.clicked.connect(self.toggle_LF)
        self.ui.RB.clicked.connect(self.toggle_RB)
        self.ui.LB.clicked.connect(self.toggle_LB)
        self.ui.trunk.setIcon(self.colorize_icon('assets/icons/car_trunk.png', QColor("#FFFFFF")))
        self.ui.trunk.setIconSize(QSize(30, 30))
        self.ui.back.setIcon(self.colorize_icon('assets/icons/car_bacl.png', QColor("#FFFFFF")))
        self.ui.back.setIconSize(QSize(30, 30))
        self.ui.light.setIcon(self.colorize_icon('assets/icons/light.png', QColor("#FFFFFF")))
        self.ui.light.setIconSize(QSize(30, 30))
        self.ui.wiper.setIcon(self.colorize_icon('assets/icons/wiper.png', QColor("#FFFFFF")))
        self.ui.wiper.setIconSize(QSize(30, 30))
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
        
        self.ui.youtubeBtn.clicked.connect(self.show_youtube_page)



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


    @staticmethod
    def colorize_icon(icon_path, color):
        pixmap = QPixmap(icon_path)
        colored_pixmap = QPixmap(pixmap.size())
        colored_pixmap.fill(Qt.transparent)

        painter = QPainter(colored_pixmap)
        painter.setCompositionMode(QPainter.CompositionMode_Source)
        painter.drawPixmap(0, 0, pixmap)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(colored_pixmap.rect(), color)
        painter.end()

        return QIcon(colored_pixmap)

    def update_car_icon(self):
        """
        Updates the car icon based on which doors are open.
        """
        door_state = {
            "RF": self.open_rf,
            "LF": self.open_lf,
            "RB": self.open_rb,
            "LB": self.open_lb
        }

        # Mapping door combinations to the corresponding image file
        door_combinations = {
            (False, False, False, False): "all_closed.png",
            (True, False, False, False): "rf_opened.png",
            (False, True, False, False): "lf_opened.png",
            (False, False, True, False): "rb_opened.png",
            (False, False, False, True): "lb_opened.png",

            (True, True, False, False): "lf_rf_opened.png",
            (False, False, True, True): "lb_rb_opened.png",
            (True, False, True, False): "rf_rb_opened.png",
            (False, True, False, True): "lf_lb_opened.png",
            (False, True, True, False): "lf_rb_opened.png",
            (True, False, False, True): "rf_lb_opened.png",

            (True, True, True, False): "lb_closed.png",
            (True, False, True, True): "lf_closed.png",
            (False, True, True, True): "rf_closed.png",
            (True, True, False, True): "rb_closed.png",
            (True, True, True, True): "all_opened.png"
        }

        # Get the corresponding image
        current_state = (self.open_rf, self.open_lf, self.open_rb, self.open_lb)
        icon_path = f'assets/icons/{door_combinations[current_state]}'

        # Determine car color
        car_color = QColor("#FF0000") if current_state == (False, False, False, False) else QColor("#00FF00")

        # Update the icon with the appropriate color
        self.ui.car.setIcon(self.colorize_icon(icon_path, car_color))
        self.ui.car.setIconSize(QSize(130, 130))


    def toggle_RF(self):
        self.open_rf = not self.open_rf

        self.update_car_icon()

    def toggle_LF(self):
        self.open_lf = not self.open_lf

        self.update_car_icon()

    def toggle_RB(self):
        self.open_rb = not self.open_rb

        self.update_car_icon()

    def toggle_LB(self):
        self.open_lb = not self.open_lb

        self.update_car_icon()


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
            folium_map = folium.Map(location=[31.257196646654524, 29.98070623246377], zoom_start=30)
            folium.Marker(
                location=[31.257196646654524, 29.98070623246377],
                popup='My Location',
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(folium_map)
            map_html = folium_map._repr_html_()
            self.web_view = QWebEngineView(self)
            self.web_view.setHtml(map_html)
            self.web_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.web_view.setGeometry(self.ui.mapPage.rect())
            self.ui.mapPage.layout().addWidget(self.web_view)
            self.map_initialized = True
        self.ui.stackedWidget.setCurrentIndex(2)

    def show_youtube_page(self):
        """Shows the YouTube page with embedded web view."""
        if not hasattr(self, 'youtube_initialized') or not self.youtube_initialized:
            self.initialize_youtube_view()
        self.ui.stackedWidget.setCurrentWidget(self.ui.youtubePage)
    
    def initialize_youtube_view(self):
        """Initializes the YouTube web view once."""
        self.youtube_view = QWebEngineView()
        self.youtube_view.setUrl(QUrl("https://www.youtube.com"))
        
        # Set up layout if not exists
        if self.ui.youtubePage.layout() is None:
            layout = QVBoxLayout(self.ui.youtubePage)
            layout.setContentsMargins(0, 0, 0, 0)
        
        self.ui.youtubePage.layout().addWidget(self.youtube_view)
        self.youtube_initialized = True

