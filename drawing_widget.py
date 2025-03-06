import math
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen, QFont
from PySide6.QtCore import QTimer, Qt, QRectF, QPointF


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
        #print(self.current_speed)
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
