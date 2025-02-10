import sys
import io
import folium
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QSizePolicy, QGraphicsPixmapItem, QGraphicsScene, QVBoxLayout, QTextEdit
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import QIcon, QPixmap, QPainter, QColor, QPen, QFont
from PySide6.QtCore import QTimer, QDateTime, Qt, QRectF, QPointF, QSize, QPropertyAnimation

from drawing_widget import DrawingWidget
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

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
        self.ui.calendarBtn.clicked.connect(self.show_calendar_page)
        self.ui.mapBtn.clicked.connect(self.show_map_page)
        self.ui.lockBtn.clicked.connect(self.toggle_lock)
        self.ui.seatbeltBtn.clicked.connect(self.toggle_seatbelt)

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

        self.ui.stackedWidget.setCurrentIndex(2)  # Set homePage as active

    def show_calendar_page(self):
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
        self.ui.stackedWidget.setCurrentIndex(1)

