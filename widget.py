import sys
import io
import folium
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QSizePolicy, QGraphicsPixmapItem, QGraphicsScene, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import QIcon, QPixmap, QPainter, QColor, QPen, QFont
from PySide6.QtCore import QTimer, QDateTime, Qt, QRectF, QPointF

from ui_form import Ui_Widget
import math

class DrawingWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_speed = 250   # Start speed at 0
        self.max_speed = 250     # Maximum speed on the gauge
        self.direction = -1       # Controls whether speed is increasing (+1) or decreasing (-1)

        # Timer for simulating speed changes
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_speed)  # Call update_speed() every timer tick
        self.timer.start(50)

    def update_speed(self):
        """
        Simulates speed changes. Increments or decrements the speed value
        based on the direction.
        """
        print(self.current_speed)
        self.current_speed += self.direction * 2  # Adjust speed increment/decrement rate
        if self.current_speed >= self.max_speed:
            self.direction = -1  # Start decreasing speed
        elif self.current_speed <= 0:
            self.direction = 1  # Start increasing speed
        self.update()  # Trigger paintEvent to redraw the widget

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Enable smooth drawing

        # Widget size and center
        width = self.width()
        height = self.height()
        size = min(width, height) - 20
        center = QPointF(width / 2, height / 2)

        # Colors

        background_color = QColor("#333333")  # Dark background
        active_arc_color = QColor("#00FF00")  # Bright green active arc
        inactive_arc_color = QColor("#666666")  # Gray inactive arc
        text_color = QColor("#00FFFF")  # Cyan speed text

        # Arc setup
        arc_rect = QRectF(center.x() - size / 2, center.y() - size / 2, size, size)
        start_angle_inactive_arc = 360 * 16
        start_angle_active_arc = -90*16
        total_span_angle = 270 * 16  # Total span for the arc

        # Draw the inactive arc (background)
        pen_bg = QPen(inactive_arc_color, 15)
        painter.setPen(pen_bg)
        painter.drawArc(arc_rect, start_angle_inactive_arc, total_span_angle)

        # Draw the active arc (green) based on current speed
        speed_span = int((self.current_speed / self.max_speed) * 270) * -16
        pen_fg = QPen(active_arc_color, 15)
        painter.setPen(pen_fg)
        painter.drawArc(arc_rect, start_angle_active_arc, speed_span)

        # Draw speed text
        painter.setPen(text_color)
        painter.setFont(QFont("Arial", 48, QFont.Bold))
        speed_text = f"{self.current_speed}"
        text_width = painter.fontMetrics().horizontalAdvance(speed_text)
        painter.drawText(center.x() - text_width / 2, center.y() + 10, speed_text)

        # Draw "MPH" below speed text
        painter.setFont(QFont("Arial", 20, QFont.Bold))
        painter.drawText(center.x() - 30, center.y() + 50, "MPH")

        # Draw tick marks and numbers
        painter.setPen(QPen(Qt.white, 2))
        tick_font = QFont("Arial", 10, QFont.Bold)
        painter.setFont(tick_font)

        for i in range(0, self.max_speed + 1, 10):
            tick_angle = 135 + (i / self.max_speed) * 270 + 42
            inner_length = size / 2 * 0.85
            outer_length = size / 2

            # Calculate tick start and end points
            x1 = center.x() + inner_length * math.cos(math.radians(tick_angle - 90))
            y1 = center.y() + inner_length * math.sin(math.radians(tick_angle - 90))
            x2 = center.x() + outer_length * math.cos(math.radians(tick_angle - 90))
            y2 = center.y() + outer_length * math.sin(math.radians(tick_angle - 90))
            painter.drawLine(QPointF(x1, y1), QPointF(x2, y2))

            # Draw numbers at ticks (every 20 units)
            if i % 20 == 0:
                number_angle = tick_angle - 90
                label_length = size / 2 * 0.75
                x_text = center.x() + label_length * math.cos(math.radians(number_angle))
                y_text = center.y() + label_length * math.sin(math.radians(number_angle))
                painter.drawText(QPointF(x_text - 10, y_text + 5), str(i))

        painter.end()


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.web_view = None
        self.map_initialized = False
        self.is_locked = True
        self.is_seatbelt = True

        self.ui.homeBtn.clicked.connect(self.show_home_page)
        self.ui.calendarBtn.clicked.connect(self.show_calendar_page)
        self.ui.mapBtn.clicked.connect(self.show_map_page)
        self.ui.lockBtn.clicked.connect(self.toggle_lock)
        self.ui.seatbeltBtn.clicked.connect(self.toggle_seatbelt)

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
