# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFrame, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QProgressBar,
    QPushButton, QSizePolicy, QSlider, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1143, 676)
        Widget.setStyleSheet(u"#Widget{\n"
"background-color: #1f232a;\n"
"}")
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainContainer = QWidget(Widget)
        self.mainContainer.setObjectName(u"mainContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainContainer.sizePolicy().hasHeightForWidth())
        self.mainContainer.setSizePolicy(sizePolicy)
        self.mainContainer.setStyleSheet(u"QWidget {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(20, 20, 30, 240), /* Darker, richer background */\n"
"        stop:1 rgba(50, 50, 70, 240) /* Deeper gradient with smoother transition */\n"
"    ); /* Dark gradient for depth */\n"
"}\n"
"\n"
"QLabel {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"        stop:0 rgba(30, 30, 40, 200), /* Darker, more solid color for labels */\n"
"        stop:1 rgba(60, 60, 80, 200) /* A bit darker for added contrast */\n"
"    ); /* Gradient with more substance */\n"
"    color: #F0F0F0; /* Slightly brighter text for better contrast */\n"
"    padding: 14px; /* Added padding for a more comfortable feel */\n"
"    border-radius: 8px; /* Optional: Rounded corners for a smoother look */\n"
"}\n"
"")
        self.horizontalLayout_4 = QHBoxLayout(self.mainContainer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, 0)
        self.stackedWidget = QStackedWidget(self.mainContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.calendarPage = QWidget()
        self.calendarPage.setObjectName(u"calendarPage")
        self.calendarPage.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.calendarPage)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.calendarWidget = QCalendarWidget(self.calendarPage)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setStyleSheet(u"QCalendarWidget QWidget {\n"
"    alternate-background-color: #2E3B4E; /* Dark gray-blue */\n"
"}\n"
"\n"
"/* Style for top navigation area ###############################################*/ \n"
"#qt_calendar_navigationbar {\n"
"    background-color: #1F2733; /* Very dark gray */\n"
"    border: 2px solid #3A506B; /* Dark blue-gray */\n"
"    border-bottom: 0px;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
"/* Style for month change buttons ############################################ */\n"
"#qt_calendar_prevmonth, \n"
"#qt_calendar_nextmonth {\n"
"    border: none;\n"
"    qproperty-icon: none;\n"
"    min-width: 13px;\n"
"    max-width: 13px;\n"
"    min-height: 13px;\n"
"    max-height: 13px;\n"
"\n"
"    border-radius: 5px;\n"
"    background-color: transparent;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth {\n"
"    margin-left: 5px;\n"
"    image: url(assets/icons/arrow-119-48.ico);\n"
"}\n"
"\n"
"#qt_calendar_nextmonth {\n"
"    margin-right: 5px;"
                        "\n"
"    image: url(assets/icons/arrow-19-48.ico);\n"
"}\n"
"\n"
"#qt_calendar_prevmonth:hover, \n"
"#qt_calendar_nextmonth:hover {\n"
"    background-color: #3A506B; /* Dark blue-gray hover */\n"
"}\n"
"\n"
"#qt_calendar_prevmonth:pressed, \n"
"#qt_calendar_nextmonth:pressed {\n"
"    background-color: #1C2430; /* Slightly darker */\n"
"}\n"
"\n"
"/* Style for month and year buttons ######################################## */\n"
"#qt_calendar_yearbutton, \n"
"#qt_calendar_monthbutton {\n"
"    color: #D9E2F1; /* Light gray-blue text */\n"
"    margin: 5px;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    padding: 0px 10px;\n"
"    background-color: #2E3B4E;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:hover, \n"
"#qt_calendar_monthbutton:hover {\n"
"    background-color: #3A506B; /* Dark blue-gray hover */\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:pressed, \n"
"#qt_calendar_monthbutton:pressed {\n"
"    background-color: #1C2430;\n"
"}\n"
"\n"
"/* Style for year input lineEdit #############################"
                        "#########*/\n"
"#qt_calendar_yearedit {\n"
"    min-width: 80px;\n"
"    color: #D9E2F1;\n"
"    background: transparent;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"/* Style for year change buttons ######################################*/\n"
"#qt_calendar_yearedit::up-button {\n"
"	image: url(assets/icons/arrow-151-48.ico);\n"
"    subcontrol-position: right;\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button {\n"
"	image: url(assets/icons/arrow-213-48.ico);\n"
"    subcontrol-position: left;\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button, \n"
"#qt_calendar_yearedit::up-button {\n"
"    width: 10px;\n"
"    padding: 0px 5px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button:hover, \n"
"#qt_calendar_yearedit::up-button:hover {\n"
"    background-color: #3A506B;\n"
"}\n"
"\n"
"/* Style for month select menu ######################################## */\n"
"#calendarWidget QToolButton QMenu {\n"
"    background-color: #1F2733;\n"
"    color: #D9E2F1;\n"
"}\n"
"\n"
"#calendarWidget QToolBu"
                        "tton QMenu::item:selected:enabled {\n"
"    background-color: #3A506B;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"#calendarWidget QToolButton::menu-indicator {\n"
"    nosubcontrol-origin: margin;\n"
"    subcontrol-position: right center;\n"
"    margin-top: 10px;\n"
"    width: 20px;\n"
"}\n"
"\n"
"/* Style for calendar table ########################################## */\n"
"#qt_calendar_calendarview {\n"
"    outline: 0px;\n"
"    border: 2px solid #3A506B;\n"
"    border-top: 0px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    background-color: #1F2733;\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item {\n"
"    color: #D9E2F1; /* Default item text */\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:hover {\n"
"    border-radius: 5px;\n"
"    background-color: #3A506B;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:selected {\n"
"    background-color: #55AA7F; /* Greenish accent */\n"
"    color: #FFFFFF;\n"
"    border-radius: 5px;\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.calendarWidget)

        self.stackedWidget.addWidget(self.calendarPage)
        self.bluetoothPage = QWidget()
        self.bluetoothPage.setObjectName(u"bluetoothPage")
        self.bluetoothList = QListWidget(self.bluetoothPage)
        self.bluetoothList.setObjectName(u"bluetoothList")
        self.bluetoothList.setGeometry(QRect(150, 210, 851, 371))
        self.bluetoothList.setStyleSheet(u"QListWidget {\n"
"    background-color: #2b2b2b;\n"
"    border: 2px solid #555;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    color: #ddd;\n"
"    font-size: 20px;\n"
"    selection-background-color: #0078D7;\n"
"    selection-color: white;\n"
"}\n"
"QListWidget::item {\n"
"    padding: 10px;\n"
"    border-bottom: 1px solid #444;\n"
"}\n"
"QListWidget::item:selected {\n"
"    background-color: #0078D7;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.bluetoothLabel = QLabel(self.bluetoothPage)
        self.bluetoothLabel.setObjectName(u"bluetoothLabel")
        self.bluetoothLabel.setGeometry(QRect(150, 150, 851, 61))
        self.bluetoothLabel.setStyleSheet(u"QLabel {\n"
"    background-color: #2b2b2b;\n"
"    color: #ffffff;\n"
"    font-size: 30px;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"    border-radius: 8px;\n"
"border: 2px solid #555;\n"
"    text-align: center;\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"")
        self.connectButtonBluetooth = QPushButton(self.bluetoothPage)
        self.connectButtonBluetooth.setObjectName(u"connectButtonBluetooth")
        self.connectButtonBluetooth.setGeometry(QRect(820, 540, 181, 41))
        self.connectButtonBluetooth.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.1);  /* Slightly visible background */\n"
"    border: 2px solid transparent;  \n"
"    color: white;  \n"
"    padding: 8px;  /* Increased padding for better look */\n"
"    border-radius: 8px;  \n"
"    font-size: 18px;  \n"
"    font-weight: bold;  /* Make text stand out */\n"
"    text-align: center;\n"
"    letter-spacing: 1px; /* Improve readability */\n"
"    transition: all 0.3s ease-in-out; /* Smooth transitions */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(58, 120, 127);\n"
"    border: 2px solid #d0d0d0;  \n"
"    color: black;  \n"
"    box-shadow: 0px 0px 10px rgba(58, 120, 127, 0.7); /* Glow effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d6d6d6;\n"
"    border: 2px solid #b0b0b0;  \n"
"    color: black;  \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;  \n"
"    font-size: 16px;  \n"
"    font-weight: bold;  \n"
"    text-align: center;  \n"
"}\n"
"")
        self.refreshButtonBluetooth = QPushButton(self.bluetoothPage)
        self.refreshButtonBluetooth.setObjectName(u"refreshButtonBluetooth")
        self.refreshButtonBluetooth.setGeometry(QRect(150, 540, 181, 41))
        self.refreshButtonBluetooth.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.1);  /* Slightly visible background */\n"
"    border: 2px solid transparent;  \n"
"    color: white;  \n"
"    padding: 8px;  /* Increased padding for better look */\n"
"    border-radius: 8px;  \n"
"    font-size: 18px;  \n"
"    font-weight: bold;  /* Make text stand out */\n"
"    text-align: center;\n"
"    letter-spacing: 1px; /* Improve readability */\n"
"    transition: all 0.3s ease-in-out; /* Smooth transitions */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(58, 120, 127);\n"
"    border: 2px solid #d0d0d0;  \n"
"    color: black;  \n"
"    box-shadow: 0px 0px 10px rgba(58, 120, 127, 0.7); /* Glow effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d6d6d6;\n"
"    border: 2px solid #b0b0b0;  \n"
"    color: black;  \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;  \n"
"    font-size: 16px;  \n"
"    font-weight: bold;  \n"
"    text-align: center;  \n"
"}\n"
"")
        self.pairButton = QPushButton(self.bluetoothPage)
        self.pairButton.setObjectName(u"pairButton")
        self.pairButton.setGeometry(QRect(640, 540, 181, 41))
        self.pairButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.1);  /* Slightly visible background */\n"
"    border: 2px solid transparent;  \n"
"    color: white;  \n"
"    padding: 8px;  /* Increased padding for better look */\n"
"    border-radius: 8px;  \n"
"    font-size: 18px;  \n"
"    font-weight: bold;  /* Make text stand out */\n"
"    text-align: center;\n"
"    letter-spacing: 1px; /* Improve readability */\n"
"    transition: all 0.3s ease-in-out; /* Smooth transitions */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(58, 120, 127);\n"
"    border: 2px solid #d0d0d0;  \n"
"    color: black;  \n"
"    box-shadow: 0px 0px 10px rgba(58, 120, 127, 0.7); /* Glow effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d6d6d6;\n"
"    border: 2px solid #b0b0b0;  \n"
"    color: black;  \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;  \n"
"    font-size: 16px;  \n"
"    font-weight: bold;  \n"
"    text-align: center;  \n"
"}\n"
"")
        self.widget = QWidget(self.bluetoothPage)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(150, 50, 851, 101))
        self.widget.setStyleSheet(u"QWidget {\n"
"    background-color: #2b2b2b;\n"
"    color: #ffffff;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"    border-radius: 8px;\n"
"    border: 2px solid #555;\n"
"  /*  text-align: center;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"QLabel\n"
"{\n"
" border: 0px solid #555;\n"
"}")
        self.deviceInfoLabel = QLabel(self.widget)
        self.deviceInfoLabel.setObjectName(u"deviceInfoLabel")
        self.deviceInfoLabel.setGeometry(QRect(130, 50, 231, 41))
        font = QFont()
        font.setBold(True)
        self.deviceInfoLabel.setFont(font)
        self.deviceInfoLabel.setStyleSheet(u"QLabel {\n"
"    color: #ffffff;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"   /* text-align: center;\n"
"    qproperty-alignment: AlignCenter;*/\n"
"}\n"
"")
        self.deviceInfoLabel_2 = QLabel(self.widget)
        self.deviceInfoLabel_2.setObjectName(u"deviceInfoLabel_2")
        self.deviceInfoLabel_2.setGeometry(QRect(120, 10, 251, 41))
        self.deviceInfoLabel_2.setFont(font)
        self.deviceInfoLabel_2.setStyleSheet(u"QLabel {\n"
"    color: #ffffff;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"   /* text-align: center;\n"
"    qproperty-alignment: AlignCenter;*/\n"
"}\n"
"")
        self.deviceInfoLabel_3 = QLabel(self.widget)
        self.deviceInfoLabel_3.setObjectName(u"deviceInfoLabel_3")
        self.deviceInfoLabel_3.setGeometry(QRect(540, 10, 151, 41))
        self.deviceInfoLabel_3.setFont(font)
        self.deviceInfoLabel_3.setStyleSheet(u"QLabel {\n"
"    color: #ffffff;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"   /* text-align: center;\n"
"    qproperty-alignment: AlignCenter;*/\n"
"}\n"
"")
        self.deviceInfoLabel_4 = QLabel(self.widget)
        self.deviceInfoLabel_4.setObjectName(u"deviceInfoLabel_4")
        self.deviceInfoLabel_4.setGeometry(QRect(490, 50, 251, 41))
        self.deviceInfoLabel_4.setFont(font)
        self.deviceInfoLabel_4.setStyleSheet(u"QLabel {\n"
"    color: #ffffff;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"   /* text-align: center;\n"
"    qproperty-alignment: AlignCenter;*/\n"
"}\n"
"")
        self.bluetoothLabel_2 = QLabel(self.bluetoothPage)
        self.bluetoothLabel_2.setObjectName(u"bluetoothLabel_2")
        self.bluetoothLabel_2.setGeometry(QRect(150, -10, 851, 61))
        self.bluetoothLabel_2.setStyleSheet(u"QLabel {\n"
"    background-color: #2b2b2b;\n"
"    color: #ffffff;\n"
"    font-size: 30px;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"    border-radius: 8px;\n"
"border: 2px solid #555;\n"
"    text-align: center;\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.bluetoothPage)
        self.musicPlayerPage = QWidget()
        self.musicPlayerPage.setObjectName(u"musicPlayerPage")
        self.widget_2 = QWidget(self.musicPlayerPage)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(160, 0, 851, 591))
        self.widget_2.setFont(font)
        self.widget_2.setStyleSheet(u"QWidget {\n"
"    background-color: #2b2b2b;\n"
"    color: #ffffff;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
" /*     border-radius: 8px;\n"
"    border: 2px solid #555;\n"
"  text-align: center;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"QLabel\n"
"{\n"
" border: 0px solid #555;\n"
"\n"
"}\n"
"\n"
"    QSlider::groove:horizontal {\n"
"        border: none;\n"
"        height: 6px;\n"
"        background: rgba(255, 255, 255, 0.2); /* Transparent when not loaded */\n"
"        margin: 2px 0;\n"
"        border-radius: 3px;\n"
"    }\n"
"    QSlider::handle:horizontal {\n"
"        background: white;\n"
"        border: 2px solid #B0B0B0;\n"
"        width: 14px;\n"
"        height: 14px;\n"
"        margin: -5px 0;\n"
"        border-radius: 7px;\n"
"    }\n"
"    QSlider::handle:horizontal:hover {\n"
"        background: #F5F5F5;\n"
"        border: 2px solid #909090;\n"
"    }\n"
"    QSlider::sub-page:horizontal {\n"
"        background: white;  /* Progress bar"
                        " is white when loaded */\n"
"        border-radius: 3px;\n"
"    }\n"
"    QSlider::add-page:horizontal {\n"
"        background: rgba(255, 255, 255, 0.2); /* Transparent when not loaded */\n"
"        border-radius: 3px;\n"
"    }\n"
"")
        self.horizontalSlider = QSlider(self.widget_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(100, 450, 671, 31))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 150, 250, 250))
        self.label.setStyleSheet(u"QLabel {\n"
"    background-color: #2b2b2b;\n"
"    color: #ffffff;\n"
"    font-size: 30px;\n"
"    font-weight: bold;\n"
"\n"
"}\n"
"")
        self.label.setPixmap(QPixmap(u"C:/Users/OMEN/Desktop/Screenshot 2025-02-23 061041.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 350, 181, 41))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel {\n"
"    background-color: #2b2b2b;\n"
"font-weight: regular;\n"
"    color: rgba(255, 255, 255, 150);\n"
"    font-size: 20px;\n"
"    padding: 8px;\n"
"}\n"
"")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 300, 141, 61))
        self.label_3.setStyleSheet(u"QLabel {\n"
"    background-color: #2b2b2b;\n"
"    color: #ffffff;\n"
"    font-size: 35px;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"}\n"
"")
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 450, 51, 31))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"QLabel {\n"
"    background-color: #2b2b2b;\n"
"    color: #ffffff;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"")
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(770, 450, 51, 31))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"QLabel {\n"
"    background-color: #2b2b2b;\n"
"    color: #ffffff;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"")
        self.horizontalSlider_2 = QSlider(self.widget_2)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setGeometry(QRect(649, 510, 121, 22))
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(416, 484, 48, 79))
        self.pushButton.setStyleSheet(u"border: 0px solid #555;")
        icon = QIcon()
        icon.addFile(u"C:/Users/OMEN/Downloads/3669295_ic_white_filled_play_circle_icon (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(96, 96))
        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(471, 500, 48, 46))
        self.pushButton_2.setStyleSheet(u"border: 0px solid #555;")
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/OMEN/Downloads/6908877_forward_music_next_play_rounded_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(30, 30))
        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(360, 500, 49, 46))
        self.pushButton_3.setStyleSheet(u"border: 0px solid #555;")
        icon2 = QIcon()
        icon2.addFile(u"../../6908877_forward_music_next_play_rounded_icon - Copy.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(30, 30))
        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(280, 500, 49, 46))
        self.pushButton_4.setStyleSheet(u"border: 0px solid #555;")
        icon3 = QIcon()
        icon3.addFile(u"C:/Users/OMEN/Downloads/9022734_shuffle_duotone_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(30, 30))
        self.pushButton_5 = QPushButton(self.widget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(600, 500, 48, 46))
        self.pushButton_5.setStyleSheet(u"border: 0px solid #555;")
        icon4 = QIcon()
        icon4.addFile(u"C:/Users/OMEN/Downloads/speaker-xxl.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QSize(25, 25))
        self.stackedWidget.addWidget(self.musicPlayerPage)
        self.wifiPage = QWidget()
        self.wifiPage.setObjectName(u"wifiPage")
        self.wifiLabel = QLabel(self.wifiPage)
        self.wifiLabel.setObjectName(u"wifiLabel")
        self.wifiLabel.setGeometry(QRect(150, 10, 851, 61))
        self.wifiLabel.setStyleSheet(u"QLabel {\n"
"    background-color: #2b2b2b;\n"
"    color: #ffffff;\n"
"    font-size: 30px;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"    border-radius: 8px;\n"
"border: 2px solid #555;\n"
"    text-align: center;\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"")
        self.wifiListWidget = QListWidget(self.wifiPage)
        self.wifiListWidget.setObjectName(u"wifiListWidget")
        self.wifiListWidget.setGeometry(QRect(150, 70, 851, 511))
        self.wifiListWidget.setStyleSheet(u"QListWidget {\n"
"    background-color: #2b2b2b;\n"
"    border: 2px solid #555;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    color: #ddd;\n"
"    font-size: 20px;\n"
"    selection-background-color: #0078D7;\n"
"    selection-color: white;\n"
"}\n"
"QListWidget::item {\n"
"    padding: 10px;\n"
"    border-bottom: 1px solid #444;\n"
"}\n"
"QListWidget::item:selected {\n"
"    background-color: #0078D7;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.refreshButton = QPushButton(self.wifiPage)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(150, 540, 181, 41))
        self.refreshButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.1);  /* Slightly visible background */\n"
"    border: 2px solid transparent;  \n"
"    color: white;  \n"
"    padding: 8px;  /* Increased padding for better look */\n"
"    border-radius: 8px;  \n"
"    font-size: 18px;  \n"
"    font-weight: bold;  /* Make text stand out */\n"
"    text-align: center;\n"
"    letter-spacing: 1px; /* Improve readability */\n"
"    transition: all 0.3s ease-in-out; /* Smooth transitions */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(58, 120, 127);\n"
"    border: 2px solid #d0d0d0;  \n"
"    color: black;  \n"
"    box-shadow: 0px 0px 10px rgba(58, 120, 127, 0.7); /* Glow effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d6d6d6;\n"
"    border: 2px solid #b0b0b0;  \n"
"    color: black;  \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;  \n"
"    font-size: 16px;  \n"
"    font-weight: bold;  \n"
"    text-align: center;  \n"
"}\n"
"")
        self.connectButton = QPushButton(self.wifiPage)
        self.connectButton.setObjectName(u"connectButton")
        self.connectButton.setGeometry(QRect(820, 540, 181, 41))
        self.connectButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.1);  /* Slightly visible background */\n"
"    border: 2px solid transparent;  \n"
"    color: white;  \n"
"    padding: 8px;  /* Increased padding for better look */\n"
"    border-radius: 8px;  \n"
"    font-size: 18px;  \n"
"    font-weight: bold;  /* Make text stand out */\n"
"    text-align: center;\n"
"    letter-spacing: 1px; /* Improve readability */\n"
"    transition: all 0.3s ease-in-out; /* Smooth transitions */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(58, 120, 127);\n"
"    border: 2px solid #d0d0d0;  \n"
"    color: black;  \n"
"    box-shadow: 0px 0px 10px rgba(58, 120, 127, 0.7); /* Glow effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d6d6d6;\n"
"    border: 2px solid #b0b0b0;  \n"
"    color: black;  \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;  \n"
"    font-size: 16px;  \n"
"    font-weight: bold;  \n"
"    text-align: center;  \n"
"}\n"
"")
        self.stackedWidget.addWidget(self.wifiPage)
        self.mapPage = QWidget()
        self.mapPage.setObjectName(u"mapPage")
        self.horizontalLayout_7 = QHBoxLayout(self.mapPage)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.stackedWidget.addWidget(self.mapPage)
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.homePage.setStyleSheet(u"")
        self.dateTimeLabel = QLabel(self.homePage)
        self.dateTimeLabel.setObjectName(u"dateTimeLabel")
        self.dateTimeLabel.setGeometry(QRect(420, -40, 351, 141))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(11)
        sizePolicy1.setVerticalStretch(11)
        sizePolicy1.setHeightForWidth(self.dateTimeLabel.sizePolicy().hasHeightForWidth())
        self.dateTimeLabel.setSizePolicy(sizePolicy1)
        self.dateTimeLabel.setLayoutDirection(Qt.LeftToRight)
        self.dateTimeLabel.setStyleSheet(u"QLabel {\n"
"        background: linear-gradient(to bottom, #4CAF50, #76c7c0); /* Green gradient */\n"
"        border-radius: 10px;\n"
"        padding: 15px;\n"
"    }")
        self.lockBtn = QPushButton(self.homePage)
        self.lockBtn.setObjectName(u"lockBtn")
        self.lockBtn.setGeometry(QRect(1050, 10, 48, 44))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lockBtn.sizePolicy().hasHeightForWidth())
        self.lockBtn.setSizePolicy(sizePolicy2)
        self.lockBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;  /* Transparent background by default */\n"
"    border: 2px solid transparent;  /* Transparent border to maintain layout */\n"
"    color: black;                   /* Text color */\n"
"    padding: 5px;                   /* Add padding for a better click area */\n"
"    border-radius: 5px;             /* Rounded corners for a modern look */\n"
"    font-size: 14px;                /* Adjust font size for readability */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"	background-color: rgb(58, 120, 127);\n"
"    border-radius: 5px;             /* Maintain rounded corners */\n"
"    border: 1px solid #d0d0d0;      /* Subtle border for hover indication */\n"
"    color: black;                   /* Ensure the text color stays consistent */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d6d6d6;      /* Slightly darker gray for pressed effect */\n"
"    border-radius: 5px;             /* Maintain rounded corners */\n"
"    border: 1px solid #b0b0b0;  "
                        "    /* Darker border for pressed state */\n"
"    color: black;                   /* Keep text color consistent */\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"assets/icons/lock.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.lockBtn.setIcon(icon5)
        self.lockBtn.setIconSize(QSize(30, 30))
        self.seatbeltBtn = QPushButton(self.homePage)
        self.seatbeltBtn.setObjectName(u"seatbeltBtn")
        self.seatbeltBtn.setGeometry(QRect(1000, 10, 48, 44))
        self.seatbeltBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;  /* Transparent background by default */\n"
"    border: 2px solid transparent;  /* Transparent border to maintain layout */\n"
"    color: black;                   /* Text color */\n"
"    padding: 5px;                   /* Add padding for a better click area */\n"
"    border-radius: 5px;             /* Rounded corners for a modern look */\n"
"    font-size: 14px;                /* Adjust font size for readability */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"	background-color: rgb(58, 120, 127);\n"
"    border-radius: 5px;             /* Maintain rounded corners */\n"
"    border: 1px solid #d0d0d0;      /* Subtle border for hover indication */\n"
"    color: black;                   /* Ensure the text color stays consistent */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d6d6d6;      /* Slightly darker gray for pressed effect */\n"
"    border-radius: 5px;             /* Maintain rounded corners */\n"
"    border: 1px solid #b0b0b0;  "
                        "    /* Darker border for pressed state */\n"
"    color: black;                   /* Keep text color consistent */\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"assets/icons/safebelt.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.seatbeltBtn.setIcon(icon6)
        self.seatbeltBtn.setIconSize(QSize(30, 30))
        self.progressBar = QProgressBar(self.homePage)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(900, 70, 211, 31))
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(24)
        self.horizontalWidget = QWidget(self.homePage)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setGeometry(QRect(390, 90, 411, 301))
        self.horizontalWidget.setStyleSheet(u"background: transparent")
        self.homePageLayout = QHBoxLayout(self.horizontalWidget)
        self.homePageLayout.setSpacing(0)
        self.homePageLayout.setObjectName(u"homePageLayout")
        self.car = QPushButton(self.homePage)
        self.car.setObjectName(u"car")
        self.car.setGeometry(QRect(950, 330, 111, 141))
        self.car.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;  /* Transparent background by default */\n"
"    border: 2px solid transparent;  /* Transparent border to maintain layout */\n"
"    color: black;                   /* Text color */\n"
"    padding: 2px 5px;               /* Reduced padding for better fit */\n"
"    border-radius: 5px;             /* Rounded corners for a modern look */\n"
"    font-size: 14px;                /* Adjust font size for readability */\n"
"    min-width: 40px;                /* Ensure button has a minimal width */\n"
"    min-height: 30px;               /* Ensure button has a minimal height */\n"
"}\n"
"\n"
"\n"
"\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"assets/icons/car_closed.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.car.setIcon(icon7)
        self.car.setIconSize(QSize(100, 100))
        self.LF = QPushButton(self.homePage)
        self.LF.setObjectName(u"LF")
        self.LF.setGeometry(QRect(900, 350, 41, 41))
        self.LF.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.1);  /* Slightly visible background */\n"
"    border: 2px solid transparent;  \n"
"    color: white;  \n"
"    padding: 8px;  /* Increased padding for better look */\n"
"    border-radius: 8px;  \n"
"    font-size: 15px;  \n"
"    font-weight: bold;  /* Make text stand out */\n"
"    text-align: center;\n"
"    letter-spacing: 1px; /* Improve readability */\n"
"    transition: all 0.3s ease-in-out; /* Smooth transitions */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(58, 120, 127);\n"
"    border: 2px solid #d0d0d0;  \n"
"    color: black;  \n"
"    box-shadow: 0px 0px 10px rgba(58, 120, 127, 0.7); /* Glow effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d6d6d6;\n"
"    border: 2px solid #b0b0b0;  \n"
"    color: black;  \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;  \n"
"    font-size: 16px;  \n"
"    font-weight: bold;  \n"
"    text-align: center;  \n"
"}\n"
"")
        self.LF.setIconSize(QSize(20, 20))
        self.RF = QPushButton(self.homePage)
        self.RF.setObjectName(u"RF")
        self.RF.setGeometry(QRect(1070, 350, 41, 41))
        self.RF.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.1);  /* Slightly visible background */\n"
"    border: 2px solid transparent;  \n"
"    color: white;  \n"
"    padding: 8px;  /* Increased padding for better look */\n"
"    border-radius: 8px;  \n"
"    font-size: 15px;  \n"
"    font-weight: bold;  /* Make text stand out */\n"
"    text-align: center;\n"
"    letter-spacing: 1px; /* Improve readability */\n"
"    transition: all 0.3s ease-in-out; /* Smooth transitions */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(58, 120, 127);\n"
"    border: 2px solid #d0d0d0;  \n"
"    color: black;  \n"
"    box-shadow: 0px 0px 10px rgba(58, 120, 127, 0.7); /* Glow effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d6d6d6;\n"
"    border: 2px solid #b0b0b0;  \n"
"    color: black;  \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;  \n"
"    font-size: 16px;  \n"
"    font-weight: bold;  \n"
"    text-align: center;  \n"
"}\n"
"")
        self.RF.setIconSize(QSize(20, 20))
        self.LB = QPushButton(self.homePage)
        self.LB.setObjectName(u"LB")
        self.LB.setGeometry(QRect(900, 410, 41, 41))
        self.LB.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.1);  /* Slightly visible background */\n"
"    border: 2px solid transparent;  \n"
"    color: white;  \n"
"    padding: 8px;  /* Increased padding for better look */\n"
"    border-radius: 8px;  \n"
"    font-size: 15px;  \n"
"    font-weight: bold;  /* Make text stand out */\n"
"    text-align: center;\n"
"    letter-spacing: 1px; /* Improve readability */\n"
"    transition: all 0.3s ease-in-out; /* Smooth transitions */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(58, 120, 127);\n"
"    border: 2px solid #d0d0d0;  \n"
"    color: black;  \n"
"    box-shadow: 0px 0px 10px rgba(58, 120, 127, 0.7); /* Glow effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d6d6d6;\n"
"    border: 2px solid #b0b0b0;  \n"
"    color: black;  \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;  \n"
"    font-size: 16px;  \n"
"    font-weight: bold;  \n"
"    text-align: center;  \n"
"}\n"
"")
        self.LB.setIconSize(QSize(20, 20))
        self.RB = QPushButton(self.homePage)
        self.RB.setObjectName(u"RB")
        self.RB.setGeometry(QRect(1070, 410, 41, 41))
        self.RB.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.1);  /* Slightly visible background */\n"
"    border: 2px solid transparent;  \n"
"    color: white;  \n"
"    padding: 8px;  /* Increased padding for better look */\n"
"    border-radius: 8px;  \n"
"    font-size: 15px;  \n"
"    font-weight: bold;  /* Make text stand out */\n"
"    text-align: center;\n"
"    letter-spacing: 1px; /* Improve readability */\n"
"    transition: all 0.3s ease-in-out; /* Smooth transitions */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(58, 120, 127);\n"
"    border: 2px solid #d0d0d0;  \n"
"    color: black;  \n"
"    box-shadow: 0px 0px 10px rgba(58, 120, 127, 0.7); /* Glow effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d6d6d6;\n"
"    border: 2px solid #b0b0b0;  \n"
"    color: black;  \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;  \n"
"    font-size: 16px;  \n"
"    font-weight: bold;  \n"
"    text-align: center;  \n"
"}\n"
"")
        self.RB.setIconSize(QSize(20, 20))
        self.power = QPushButton(self.homePage)
        self.power.setObjectName(u"power")
        self.power.setGeometry(QRect(20, 510, 61, 51))
        self.power.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;  /* Transparent background by default */\n"
"    border: none;                   /* Remove border for a cleaner icon-only look */\n"
"    color: white;                   /* Change to white for better contrast on dark backgrounds */\n"
"    padding: 10px;                  /* Increase padding for better click area */\n"
"    border-radius: 10px;            /* Slightly more rounded corners for consistency */\n"
"    font-size: 20px;                /* Make the icons larger and more prominent */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(58, 120, 127, 0.6);  /* Subtle teal hover effect */\n"
"    border-radius: 10px;                        /* Ensure rounded corners remain */\n"
"    border: 1px solid #3A787F;                  /* Add a faint hover border */\n"
"    color: white;                               /* Ensure the icon stays visible */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(58, 120, 127, 1);    /* Darker "
                        "teal for pressed effect */\n"
"    border-radius: 10px;                        /* Maintain rounded corners */\n"
"    border: 1px solid #2A5A5F;                  /* Slightly darker border on press */\n"
"    color: white;                               /* Keep the text/icon white */\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u"assets/icons/car_shut.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.power.setIcon(icon8)
        self.power.setIconSize(QSize(50, 50))
        self.textEdit = QTextEdit(self.homePage)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 50, 301, 131))
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"    background-color: rgba(0, 0, 0, 150);  /* Semi-transparent black */\n"
"    border: none;  /* Remove border */\n"
"    border-radius: 15px;  /* Smooth rounded corners */\n"
"    color: white;  /* Text color */\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    padding: 10px;  /* Better spacing */\n"
"}\n"
"")
        self.textEdit_2 = QTextEdit(self.homePage)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(20, 360, 301, 101))
        self.textEdit_2.setStyleSheet(u"QTextEdit {\n"
"    background-color: rgba(0, 0, 0, 150);  /* Semi-transparent black */\n"
"    border: none;  /* Remove border */\n"
"    border-radius: 15px;  /* Smooth rounded corners */\n"
"    color: white;  /* Text color */\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    padding: 10px;  /* Better spacing */\n"
"}\n"
"")
        self.P = QPushButton(self.homePage)
        self.P.setObjectName(u"P")
        self.P.setGeometry(QRect(900, 480, 41, 41))
        self.P.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.1);  /* Slightly visible background */\n"
"    border: 2px solid transparent;  \n"
"    color: white;  \n"
"    padding: 8px;  /* Increased padding for better look */\n"
"    border-radius: 8px;  \n"
"    font-size: 15px;  \n"
"    font-weight: bold;  /* Make text stand out */\n"
"    text-align: center;\n"
"    letter-spacing: 1px; /* Improve readability */\n"
"    transition: all 0.3s ease-in-out; /* Smooth transitions */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(58, 120, 127);\n"
"    border: 2px solid #d0d0d0;  \n"
"    color: black;  \n"
"    box-shadow: 0px 0px 10px rgba(58, 120, 127, 0.7); /* Glow effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d6d6d6;\n"
"    border: 2px solid #b0b0b0;  \n"
"    color: black;  \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;  \n"
"    font-size: 16px;  \n"
"    font-weight: bold;  \n"
"    text-align: center;  \n"
"}\n"
"")
        self.P.setIconSize(QSize(20, 20))
        self.R = QPushButton(self.homePage)
        self.R.setObjectName(u"R")
        self.R.setGeometry(QRect(960, 480, 41, 41))
        self.R.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.1);  /* Slightly visible background */\n"
"    border: 2px solid transparent;  \n"
"    color: white;  \n"
"    padding: 8px;  /* Increased padding for better look */\n"
"    border-radius: 8px;  \n"
"    font-size: 15px;  \n"
"    font-weight: bold;  /* Make text stand out */\n"
"    text-align: center;\n"
"    letter-spacing: 1px; /* Improve readability */\n"
"    transition: all 0.3s ease-in-out; /* Smooth transitions */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(58, 120, 127);\n"
"    border: 2px solid #d0d0d0;  \n"
"    color: black;  \n"
"    box-shadow: 0px 0px 10px rgba(58, 120, 127, 0.7); /* Glow effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d6d6d6;\n"
"    border: 2px solid #b0b0b0;  \n"
"    color: black;  \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;  \n"
"    font-size: 16px;  \n"
"    font-weight: bold;  \n"
"    text-align: center;  \n"
"}\n"
"")
        self.R.setIconSize(QSize(20, 20))
        self.N = QPushButton(self.homePage)
        self.N.setObjectName(u"N")
        self.N.setGeometry(QRect(1020, 480, 41, 41))
        self.N.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.1);  /* Slightly visible background */\n"
"    border: 2px solid transparent;  \n"
"    color: white;  \n"
"    padding: 8px;  /* Increased padding for better look */\n"
"    border-radius: 8px;  \n"
"    font-size: 15px;  \n"
"    font-weight: bold;  /* Make text stand out */\n"
"    text-align: center;\n"
"    letter-spacing: 1px; /* Improve readability */\n"
"    transition: all 0.3s ease-in-out; /* Smooth transitions */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(58, 120, 127);\n"
"    border: 2px solid #d0d0d0;  \n"
"    color: black;  \n"
"    box-shadow: 0px 0px 10px rgba(58, 120, 127, 0.7); /* Glow effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d6d6d6;\n"
"    border: 2px solid #b0b0b0;  \n"
"    color: black;  \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;  \n"
"    font-size: 16px;  \n"
"    font-weight: bold;  \n"
"    text-align: center;  \n"
"}\n"
"")
        self.N.setIconSize(QSize(20, 20))
        self.D = QPushButton(self.homePage)
        self.D.setObjectName(u"D")
        self.D.setGeometry(QRect(1070, 480, 41, 41))
        self.D.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.1);  /* Slightly visible background */\n"
"    border: 2px solid transparent;  \n"
"    color: white;  \n"
"    padding: 8px;  /* Increased padding for better look */\n"
"    border-radius: 8px;  \n"
"    font-size: 15px;  \n"
"    font-weight: bold;  /* Make text stand out */\n"
"    text-align: center;\n"
"    letter-spacing: 1px; /* Improve readability */\n"
"    transition: all 0.3s ease-in-out; /* Smooth transitions */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(58, 120, 127);\n"
"    border: 2px solid #d0d0d0;  \n"
"    color: black;  \n"
"    box-shadow: 0px 0px 10px rgba(58, 120, 127, 0.7); /* Glow effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d6d6d6;\n"
"    border: 2px solid #b0b0b0;  \n"
"    color: black;  \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;  \n"
"    font-size: 16px;  \n"
"    font-weight: bold;  \n"
"    text-align: center;  \n"
"}\n"
"")
        self.D.setIconSize(QSize(20, 20))
        self.trunk = QPushButton(self.homePage)
        self.trunk.setObjectName(u"trunk")
        self.trunk.setGeometry(QRect(1070, 260, 41, 41))
        self.trunk.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.1);  /* Slightly visible background */\n"
"    border: 2px solid transparent;  \n"
"    color: white;  \n"
"    padding: 8px;  /* Increased padding for better look */\n"
"    border-radius: 8px;  \n"
"    font-size: 15px;  \n"
"    font-weight: bold;  /* Make text stand out */\n"
"    text-align: center;\n"
"    letter-spacing: 1px; /* Improve readability */\n"
"    transition: all 0.3s ease-in-out; /* Smooth transitions */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(58, 120, 127);\n"
"    border: 2px solid #d0d0d0;  \n"
"    color: black;  \n"
"    box-shadow: 0px 0px 10px rgba(58, 120, 127, 0.7); /* Glow effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d6d6d6;\n"
"    border: 2px solid #b0b0b0;  \n"
"    color: black;  \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;  \n"
"    font-size: 16px;  \n"
"    font-weight: bold;  \n"
"    text-align: center;  \n"
"}\n"
"")
        self.trunk.setIconSize(QSize(20, 20))
        self.back = QPushButton(self.homePage)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(900, 260, 41, 41))
        self.back.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.1);  /* Slightly visible background */\n"
"    border: 2px solid transparent;  \n"
"    color: white;  \n"
"    padding: 8px;  /* Increased padding for better look */\n"
"    border-radius: 8px;  \n"
"    font-size: 15px;  \n"
"    font-weight: bold;  /* Make text stand out */\n"
"    text-align: center;\n"
"    letter-spacing: 1px; /* Improve readability */\n"
"    transition: all 0.3s ease-in-out; /* Smooth transitions */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(58, 120, 127);\n"
"    border: 2px solid #d0d0d0;  \n"
"    color: black;  \n"
"    box-shadow: 0px 0px 10px rgba(58, 120, 127, 0.7); /* Glow effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d6d6d6;\n"
"    border: 2px solid #b0b0b0;  \n"
"    color: black;  \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;  \n"
"    font-size: 16px;  \n"
"    font-weight: bold;  \n"
"    text-align: center;  \n"
"}\n"
"")
        self.back.setIconSize(QSize(20, 20))
        self.light = QPushButton(self.homePage)
        self.light.setObjectName(u"light")
        self.light.setGeometry(QRect(1020, 260, 41, 41))
        self.light.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.1);  /* Slightly visible background */\n"
"    border: 2px solid transparent;  \n"
"    color: white;  \n"
"    padding: 8px;  /* Increased padding for better look */\n"
"    border-radius: 8px;  \n"
"    font-size: 15px;  \n"
"    font-weight: bold;  /* Make text stand out */\n"
"    text-align: center;\n"
"    letter-spacing: 1px; /* Improve readability */\n"
"    transition: all 0.3s ease-in-out; /* Smooth transitions */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(58, 120, 127);\n"
"    border: 2px solid #d0d0d0;  \n"
"    color: black;  \n"
"    box-shadow: 0px 0px 10px rgba(58, 120, 127, 0.7); /* Glow effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d6d6d6;\n"
"    border: 2px solid #b0b0b0;  \n"
"    color: black;  \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;  \n"
"    font-size: 16px;  \n"
"    font-weight: bold;  \n"
"    text-align: center;  \n"
"}\n"
"")
        self.light.setIconSize(QSize(20, 20))
        self.wiper = QPushButton(self.homePage)
        self.wiper.setObjectName(u"wiper")
        self.wiper.setGeometry(QRect(960, 260, 41, 41))
        self.wiper.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.1);  /* Slightly visible background */\n"
"    border: 2px solid transparent;  \n"
"    color: white;  \n"
"    padding: 8px;  /* Increased padding for better look */\n"
"    border-radius: 8px;  \n"
"    font-size: 15px;  \n"
"    font-weight: bold;  /* Make text stand out */\n"
"    text-align: center;\n"
"    letter-spacing: 1px; /* Improve readability */\n"
"    transition: all 0.3s ease-in-out; /* Smooth transitions */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(58, 120, 127);\n"
"    border: 2px solid #d0d0d0;  \n"
"    color: black;  \n"
"    box-shadow: 0px 0px 10px rgba(58, 120, 127, 0.7); /* Glow effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d6d6d6;\n"
"    border: 2px solid #b0b0b0;  \n"
"    color: black;  \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;  \n"
"    font-size: 16px;  \n"
"    font-weight: bold;  \n"
"    text-align: center;  \n"
"}\n"
"")
        self.wiper.setIconSize(QSize(20, 20))
        self.LF_2 = QPushButton(self.homePage)
        self.LF_2.setObjectName(u"LF_2")
        self.LF_2.setGeometry(QRect(900, 160, 211, 51))
        self.LF_2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.1);  /* Slightly visible background */\n"
"    border: 2px solid transparent;  \n"
"    color: white;  \n"
"    padding: 8px;  /* Increased padding for better look */\n"
"    border-radius: 8px;  \n"
"    font-size: 15px;  \n"
"    font-weight: bold;  /* Make text stand out */\n"
"    text-align: center;\n"
"    letter-spacing: 1px; /* Improve readability */\n"
"    transition: all 0.3s ease-in-out; /* Smooth transitions */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(58, 120, 127);\n"
"    border: 2px solid #d0d0d0;  \n"
"    color: black;  \n"
"    box-shadow: 0px 0px 10px rgba(58, 120, 127, 0.7); /* Glow effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d6d6d6;\n"
"    border: 2px solid #b0b0b0;  \n"
"    color: black;  \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;  \n"
"    font-size: 16px;  \n"
"    font-weight: bold;  \n"
"    text-align: center;  \n"
"}\n"
"")
        self.LF_2.setIconSize(QSize(20, 20))
        self.textEdit_3 = QTextEdit(self.homePage)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(430, 430, 331, 71))
        self.textEdit_3.setStyleSheet(u"QTextEdit {\n"
"    background-color: rgba(0, 0, 0, 150);  /* Semi-transparent black */\n"
"    border: none;  /* Remove border */\n"
"    border-radius: 15px;  /* Smooth rounded corners */\n"
"    color: white;  /* Text color */\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    padding: 10px;  /* Better spacing */\n"
"}\n"
"")
        self.LF_3 = QPushButton(self.homePage)
        self.LF_3.setObjectName(u"LF_3")
        self.LF_3.setGeometry(QRect(430, 520, 121, 41))
        self.LF_3.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.1);  /* Slightly visible background */\n"
"    border: 2px solid transparent;  \n"
"    color: white;  \n"
"    padding: 8px;  /* Increased padding for better look */\n"
"    border-radius: 8px;  \n"
"    font-size: 14px;  \n"
"    font-weight: bold;  /* Make text stand out */\n"
"    text-align: center;\n"
"    letter-spacing: 1px; /* Improve readability */\n"
"    transition: all 0.3s ease-in-out; /* Smooth transitions */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(58, 120, 127);\n"
"    border: 2px solid #d0d0d0;  \n"
"    color: black;  \n"
"    box-shadow: 0px 0px 10px rgba(58, 120, 127, 0.7); /* Glow effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d6d6d6;\n"
"    border: 2px solid #b0b0b0;  \n"
"    color: black;  \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;  \n"
"    font-size: 16px;  \n"
"    font-weight: bold;  \n"
"    text-align: center;  \n"
"}\n"
"")
        self.LF_3.setIconSize(QSize(20, 20))
        self.textEdit_4 = QTextEdit(self.homePage)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(20, 220, 301, 101))
        self.textEdit_4.setStyleSheet(u"QTextEdit {\n"
"    background-color: rgba(0, 0, 0, 150);  /* Semi-transparent black */\n"
"    border: none;  /* Remove border */\n"
"    border-radius: 15px;  /* Smooth rounded corners */\n"
"    color: white;  /* Text color */\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    padding: 10px;  /* Better spacing */\n"
"}\n"
"")
        self.LF_4 = QPushButton(self.homePage)
        self.LF_4.setObjectName(u"LF_4")
        self.LF_4.setGeometry(QRect(560, 520, 201, 41))
        self.LF_4.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0.1);  /* Slightly visible background */\n"
"    border: 2px solid transparent;  \n"
"    color: white;  \n"
"    padding: 8px;  /* Increased padding for better look */\n"
"    border-radius: 8px;  \n"
"    font-size: 14px;  \n"
"    font-weight: bold;  /* Make text stand out */\n"
"    text-align: center;\n"
"    letter-spacing: 1px; /* Improve readability */\n"
"    transition: all 0.3s ease-in-out; /* Smooth transitions */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(58, 120, 127);\n"
"    border: 2px solid #d0d0d0;  \n"
"    color: black;  \n"
"    box-shadow: 0px 0px 10px rgba(58, 120, 127, 0.7); /* Glow effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d6d6d6;\n"
"    border: 2px solid #b0b0b0;  \n"
"    color: black;  \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;  \n"
"    font-size: 16px;  \n"
"    font-weight: bold;  \n"
"    text-align: center;  \n"
"}\n"
"")
        self.LF_4.setIconSize(QSize(20, 20))
        self.stackedWidget.addWidget(self.homePage)

        self.horizontalLayout_4.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.mainContainer)

        self.bottomMenuContainer = QWidget(Widget)
        self.bottomMenuContainer.setObjectName(u"bottomMenuContainer")
        self.horizontalLayout = QHBoxLayout(self.bottomMenuContainer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bottomMenuSubContainer = QWidget(self.bottomMenuContainer)
        self.bottomMenuSubContainer.setObjectName(u"bottomMenuSubContainer")
        self.bottomMenuSubContainer.setStyleSheet(u"background-color: rgb(31, 35, 42);")
        self.horizontalLayout_2 = QHBoxLayout(self.bottomMenuSubContainer)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.bottomMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.homeBtn = QPushButton(self.frame)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setAutoFillBackground(False)
        self.homeBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;   /* Transparent background */\n"
"    border: none;                    /* Remove unnecessary border */\n"
"    padding: 8px;                    /* Padding for clickable area */\n"
"    border-radius: 10px;             /* Smooth rounded corners for icons */\n"
"    color: white;                    /* Icon color, use white for contrast */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(58, 120, 127, 0.3); /* Semi-transparent hover color */\n"
"    border-radius: 10px;            /* Maintain smooth corners */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(58, 120, 127, 0.6); /* Darker pressed effect */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: transparent;  /* No background when disabled */\n"
"    color: #808080;                 /* Greyed-out color for disabled icons */\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u"assets/icons/home_2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeBtn.setIcon(icon9)
        self.homeBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.homeBtn)

        self.wifiBtn = QPushButton(self.frame)
        self.wifiBtn.setObjectName(u"wifiBtn")
        self.wifiBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;   /* Transparent background */\n"
"    border: none;                    /* Remove unnecessary border */\n"
"    padding: 8px;                    /* Padding for clickable area */\n"
"    border-radius: 10px;             /* Smooth rounded corners for icons */\n"
"    color: white;                    /* Icon color, use white for contrast */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(58, 120, 127, 0.3); /* Semi-transparent hover color */\n"
"    border-radius: 10px;            /* Maintain smooth corners */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(58, 120, 127, 0.6); /* Darker pressed effect */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: transparent;  /* No background when disabled */\n"
"    color: #808080;                 /* Greyed-out color for disabled icons */\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u"assets/icons/wifi-signal.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.wifiBtn.setIcon(icon10)
        self.wifiBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.wifiBtn)

        self.musicBtn = QPushButton(self.frame)
        self.musicBtn.setObjectName(u"musicBtn")
        self.musicBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;   /* Transparent background */\n"
"    border: none;                    /* Remove unnecessary border */\n"
"    padding: 8px;                    /* Padding for clickable area */\n"
"    border-radius: 10px;             /* Smooth rounded corners for icons */\n"
"    color: white;                    /* Icon color, use white for contrast */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(58, 120, 127, 0.3); /* Semi-transparent hover color */\n"
"    border-radius: 10px;            /* Maintain smooth corners */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(58, 120, 127, 0.6); /* Darker pressed effect */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: transparent;  /* No background when disabled */\n"
"    color: #808080;                 /* Greyed-out color for disabled icons */\n"
"}\n"
"")
        icon11 = QIcon()
        icon11.addFile(u"assets/icons/spotify_2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.musicBtn.setIcon(icon11)
        self.musicBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.musicBtn)

        self.acBtn = QPushButton(self.frame)
        self.acBtn.setObjectName(u"acBtn")
        self.acBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;   /* Transparent background */\n"
"    border: none;                    /* Remove unnecessary border */\n"
"    padding: 8px;                    /* Padding for clickable area */\n"
"    border-radius: 10px;             /* Smooth rounded corners for icons */\n"
"    color: white;                    /* Icon color, use white for contrast */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(58, 120, 127, 0.3); /* Semi-transparent hover color */\n"
"    border-radius: 10px;            /* Maintain smooth corners */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(58, 120, 127, 0.6); /* Darker pressed effect */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: transparent;  /* No background when disabled */\n"
"    color: #808080;                 /* Greyed-out color for disabled icons */\n"
"}\n"
"")
        icon12 = QIcon()
        icon12.addFile(u"assets/icons/air-conditioning.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.acBtn.setIcon(icon12)
        self.acBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.acBtn)

        self.bluetoothBtn = QPushButton(self.frame)
        self.bluetoothBtn.setObjectName(u"bluetoothBtn")
        self.bluetoothBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;   /* Transparent background */\n"
"    border: none;                    /* Remove unnecessary border */\n"
"    padding: 8px;                    /* Padding for clickable area */\n"
"    border-radius: 10px;             /* Smooth rounded corners for icons */\n"
"    color: white;                    /* Icon color, use white for contrast */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(58, 120, 127, 0.3); /* Semi-transparent hover color */\n"
"    border-radius: 10px;            /* Maintain smooth corners */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(58, 120, 127, 0.6); /* Darker pressed effect */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: transparent;  /* No background when disabled */\n"
"    color: #808080;                 /* Greyed-out color for disabled icons */\n"
"}\n"
"")
        icon13 = QIcon()
        icon13.addFile(u"assets/icons/bluetooth.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bluetoothBtn.setIcon(icon13)
        self.bluetoothBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.bluetoothBtn)

        self.mapBtn = QPushButton(self.frame)
        self.mapBtn.setObjectName(u"mapBtn")
        self.mapBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;   /* Transparent background */\n"
"    border: none;                    /* Remove unnecessary border */\n"
"    padding: 8px;                    /* Padding for clickable area */\n"
"    border-radius: 10px;             /* Smooth rounded corners for icons */\n"
"    color: white;                    /* Icon color, use white for contrast */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(58, 120, 127, 0.3); /* Semi-transparent hover color */\n"
"    border-radius: 10px;            /* Maintain smooth corners */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(58, 120, 127, 0.6); /* Darker pressed effect */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: transparent;  /* No background when disabled */\n"
"    color: #808080;                 /* Greyed-out color for disabled icons */\n"
"}\n"
"")
        icon14 = QIcon()
        icon14.addFile(u"assets/icons/google-maps.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.mapBtn.setIcon(icon14)
        self.mapBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.mapBtn)

        self.youtubeBtn = QPushButton(self.frame)
        self.youtubeBtn.setObjectName(u"youtubeBtn")
        self.youtubeBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;   /* Transparent background */\n"
"    border: none;                    /* Remove unnecessary border */\n"
"    padding: 8px;                    /* Padding for clickable area */\n"
"    border-radius: 10px;             /* Smooth rounded corners for icons */\n"
"    color: white;                    /* Icon color, use white for contrast */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(58, 120, 127, 0.3); /* Semi-transparent hover color */\n"
"    border-radius: 10px;            /* Maintain smooth corners */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(58, 120, 127, 0.6); /* Darker pressed effect */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: transparent;  /* No background when disabled */\n"
"    color: #808080;                 /* Greyed-out color for disabled icons */\n"
"}\n"
"")
        icon15 = QIcon()
        icon15.addFile(u"assets/icons/youtube.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.youtubeBtn.setIcon(icon15)
        self.youtubeBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.youtubeBtn)

        self.callBtn = QPushButton(self.frame)
        self.callBtn.setObjectName(u"callBtn")
        self.callBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;   /* Transparent background */\n"
"    border: none;                    /* Remove unnecessary border */\n"
"    padding: 8px;                    /* Padding for clickable area */\n"
"    border-radius: 10px;             /* Smooth rounded corners for icons */\n"
"    color: white;                    /* Icon color, use white for contrast */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(58, 120, 127, 0.3); /* Semi-transparent hover color */\n"
"    border-radius: 10px;            /* Maintain smooth corners */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(58, 120, 127, 0.6); /* Darker pressed effect */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: transparent;  /* No background when disabled */\n"
"    color: #808080;                 /* Greyed-out color for disabled icons */\n"
"}\n"
"")
        icon16 = QIcon()
        icon16.addFile(u"assets/icons/phone-call.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.callBtn.setIcon(icon16)
        self.callBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.callBtn)

        self.calendarBtn = QPushButton(self.frame)
        self.calendarBtn.setObjectName(u"calendarBtn")
        self.calendarBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;   /* Transparent background */\n"
"    border: none;                    /* Remove unnecessary border */\n"
"    padding: 8px;                    /* Padding for clickable area */\n"
"    border-radius: 10px;             /* Smooth rounded corners for icons */\n"
"    color: white;                    /* Icon color, use white for contrast */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(58, 120, 127, 0.3); /* Semi-transparent hover color */\n"
"    border-radius: 10px;            /* Maintain smooth corners */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(58, 120, 127, 0.6); /* Darker pressed effect */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: transparent;  /* No background when disabled */\n"
"    color: #808080;                 /* Greyed-out color for disabled icons */\n"
"}\n"
"")
        icon17 = QIcon()
        icon17.addFile(u"assets/icons/calendar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.calendarBtn.setIcon(icon17)
        self.calendarBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.calendarBtn)

        self.updateBtn = QPushButton(self.frame)
        self.updateBtn.setObjectName(u"updateBtn")
        self.updateBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;   /* Transparent background */\n"
"    border: none;                    /* Remove unnecessary border */\n"
"    padding: 8px;                    /* Padding for clickable area */\n"
"    border-radius: 10px;             /* Smooth rounded corners for icons */\n"
"    color: white;                    /* Icon color, use white for contrast */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(58, 120, 127, 0.3); /* Semi-transparent hover color */\n"
"    border-radius: 10px;            /* Maintain smooth corners */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(58, 120, 127, 0.6); /* Darker pressed effect */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: transparent;  /* No background when disabled */\n"
"    color: #808080;                 /* Greyed-out color for disabled icons */\n"
"}\n"
"")
        icon18 = QIcon()
        icon18.addFile(u"assets/icons/update.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.updateBtn.setIcon(icon18)
        self.updateBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.updateBtn)

        self.settings_Btn = QPushButton(self.frame)
        self.settings_Btn.setObjectName(u"settings_Btn")
        self.settings_Btn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;   /* Transparent background */\n"
"    border: none;                    /* Remove unnecessary border */\n"
"    padding: 8px;                    /* Padding for clickable area */\n"
"    border-radius: 10px;             /* Smooth rounded corners for icons */\n"
"    color: white;                    /* Icon color, use white for contrast */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(58, 120, 127, 0.3); /* Semi-transparent hover color */\n"
"    border-radius: 10px;            /* Maintain smooth corners */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(58, 120, 127, 0.6); /* Darker pressed effect */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: transparent;  /* No background when disabled */\n"
"    color: #808080;                 /* Greyed-out color for disabled icons */\n"
"}\n"
"")
        icon19 = QIcon()
        icon19.addFile(u"assets/icons/Apple_Settings-512.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_Btn.setIcon(icon19)
        self.settings_Btn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.settings_Btn)


        self.horizontalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.bottomMenuSubContainer)


        self.verticalLayout.addWidget(self.bottomMenuContainer)


        self.retranslateUi(Widget)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.bluetoothLabel.setText(QCoreApplication.translate("Widget", u"Available Devices", None))
        self.connectButtonBluetooth.setText(QCoreApplication.translate("Widget", u"Connect", None))
        self.refreshButtonBluetooth.setText(QCoreApplication.translate("Widget", u"Refresh", None))
        self.pairButton.setText(QCoreApplication.translate("Widget", u"Pair", None))
        self.deviceInfoLabel.setText(QCoreApplication.translate("Widget", u"Status: Connected", None))
        self.deviceInfoLabel_2.setText(QCoreApplication.translate("Widget", u"Device Name: Car-Bt", None))
        self.deviceInfoLabel_3.setText(QCoreApplication.translate("Widget", u"PIN: 0000", None))
        self.deviceInfoLabel_4.setText(QCoreApplication.translate("Widget", u"Device: Hamo", None))
        self.bluetoothLabel_2.setText(QCoreApplication.translate("Widget", u"Device Info", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Widget", u"Kendrick Lamar", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Alright", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"1:00", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"3:15", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.wifiLabel.setText(QCoreApplication.translate("Widget", u"Available Wifi Networks", None))
        self.refreshButton.setText(QCoreApplication.translate("Widget", u"Refresh", None))
        self.connectButton.setText(QCoreApplication.translate("Widget", u"Connect", None))
        self.dateTimeLabel.setText(QCoreApplication.translate("Widget", u"text", None))
        self.lockBtn.setText("")
        self.seatbeltBtn.setText("")
        self.car.setText("")
        self.LF.setText(QCoreApplication.translate("Widget", u"LF", None))
        self.RF.setText(QCoreApplication.translate("Widget", u"RF", None))
        self.LB.setText(QCoreApplication.translate("Widget", u"LB", None))
        self.RB.setText(QCoreApplication.translate("Widget", u"RB", None))
        self.power.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:18px; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:400; color:#ffffff;\">Notification Alert !!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:400; color:#ffffff;\"><br />Ambulance coming on the right clear the way</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:16px; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:400;\">Send Message: No walahy ya 8aly shof elbnzena ely gya</span></p></body></html>", None))
        self.P.setText(QCoreApplication.translate("Widget", u"P", None))
        self.R.setText(QCoreApplication.translate("Widget", u"R", None))
        self.N.setText(QCoreApplication.translate("Widget", u"N", None))
        self.D.setText(QCoreApplication.translate("Widget", u"D", None))
        self.trunk.setText("")
        self.back.setText("")
        self.light.setText("")
        self.wiper.setText("")
        self.LF_2.setText(QCoreApplication.translate("Widget", u"Self Parking", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:16px; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:400;\">Drowsiness Detected !!!</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:400;\">Calling Emergency services after 5 seconds</span></p></body></html>", None))
        self.LF_3.setText(QCoreApplication.translate("Widget", u"I'm Fine", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:18px; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:400;\">Incoming Message:<br />M3aksh 5 gneh fka yzmely</span></p></body></html>", None))
        self.LF_4.setText(QCoreApplication.translate("Widget", u"Call Emergency Contact", None))
        self.homeBtn.setText("")
        self.wifiBtn.setText("")
        self.musicBtn.setText("")
        self.acBtn.setText("")
        self.bluetoothBtn.setText("")
        self.mapBtn.setText("")
        self.youtubeBtn.setText("")
        self.callBtn.setText("")
        self.calendarBtn.setText("")
        self.updateBtn.setText("")
        self.settings_Btn.setText("")
    # retranslateUi

