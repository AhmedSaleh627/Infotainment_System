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
    QPushButton, QSizePolicy, QStackedWidget, QTextEdit,
    QVBoxLayout, QWidget)

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
        self.dateTimeLabel.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.dateTimeLabel.setStyleSheet(u"QLabel {\n"
"        background: linear-gradient(to bottom, #4CAF50, #76c7c0); /* Green gradient */\n"
"        border-radius: 10px;\n"
"        padding: 15px;\n"
"    }")
        self.dateTimeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        icon = QIcon()
        icon.addFile(u"assets/icons/lock.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.lockBtn.setIcon(icon)
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
        icon1 = QIcon()
        icon1.addFile(u"assets/icons/safebelt.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.seatbeltBtn.setIcon(icon1)
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
        icon2 = QIcon()
        icon2.addFile(u"assets/icons/car_shut.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.power.setIcon(icon2)
        self.power.setIconSize(QSize(50, 50))
        self.textEdit = QTextEdit(self.homePage)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 80, 351, 131))
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
        self.LF_2 = QPushButton(self.homePage)
        self.LF_2.setObjectName(u"LF_2")
        self.LF_2.setGeometry(QRect(830, 160, 281, 51))
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
        self.dms_Updates = QTextEdit(self.homePage)
        self.dms_Updates.setObjectName(u"dms_Updates")
        self.dms_Updates.setGeometry(QRect(380, 420, 421, 101))
        self.dms_Updates.setStyleSheet(u"QTextEdit {\n"
"    background-color: rgba(0, 0, 0, 150);  /* Semi-transparent black */\n"
"    border: none;  /* Remove border */\n"
"    border-radius: 15px;  /* Smooth rounded corners */\n"
"    color: white;  /* Text color */\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    padding: 10px;  /* Better spacing */\n"
"}\n"
"")
        self.textEdit_4 = QTextEdit(self.homePage)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(10, 260, 351, 211))
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
        self.LF_4.setGeometry(QRect(490, 530, 201, 41))
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
        self.dms_CameraFeed = QLabel(self.homePage)
        self.dms_CameraFeed.setObjectName(u"dms_CameraFeed")
        self.dms_CameraFeed.setGeometry(QRect(830, 240, 281, 311))
        self.dms_CameraFeed.setStyleSheet(u"QLabel {\n"
"        border: 2px solid #00FF00;  /* Subtle green border matching other UI elements */\n"
"        border-radius: 10px; /* Smooth edges */\n"
"        background-color: black; /* Black background */\n"
"    }")
        self.stackedWidget.addWidget(self.homePage)
        self.mapPage = QWidget()
        self.mapPage.setObjectName(u"mapPage")
        self.horizontalLayout_7 = QHBoxLayout(self.mapPage)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.stackedWidget.addWidget(self.mapPage)
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
        self.fotaPage = QWidget()
        self.fotaPage.setObjectName(u"fotaPage")
        self.label = QLabel(self.fotaPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 361, 81))
        self.label.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-size: 26px;\n"
"    font-weight: bold;\n"
"    background-color: transparent;\n"
"    padding: 5px;\n"
"    border: none;\n"
"    letter-spacing: 0.5px;\n"
"}\n"
"")
        self.label_2 = QLabel(self.fotaPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 60, 361, 81))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    background-color: transparent;\n"
"    padding: 5px;\n"
"    border: none;\n"
"    letter-spacing: 0.5px;\n"
"}\n"
"")
        self.check_updates_btn = QPushButton(self.fotaPage)
        self.check_updates_btn.setObjectName(u"check_updates_btn")
        self.check_updates_btn.setGeometry(QRect(40, 490, 281, 61))
        self.check_updates_btn.setStyleSheet(u"QPushButton {\n"
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
        self.release_notes_text = QTextEdit(self.fotaPage)
        self.release_notes_text.setObjectName(u"release_notes_text")
        self.release_notes_text.setGeometry(QRect(570, 70, 471, 251))
        self.release_notes_text.setStyleSheet(u"\n"
"    QTextEdit {\n"
"        background-color: #1a1a1a;  /* Darker background for better contrast */\n"
"        border: 2px solid #333;  /* Subtle border */\n"
"        border-radius: 12px;  /* Rounded corners */\n"
"        padding: 10px;  /* Inner spacing */\n"
"        color: #f0f0f0;  /* Light text for readability */\n"
"        font-size: 14px;\n"
"        font-weight: bold;\n"
"    }\n"
"\n"
"    QTextEdit:focus {\n"
"        border: 2px solid #0078D7;  /* Highlight when focused */\n"
"    }\n"
"\n"
"")
        self.update_now_btn = QPushButton(self.fotaPage)
        self.update_now_btn.setObjectName(u"update_now_btn")
        self.update_now_btn.setGeometry(QRect(820, 490, 281, 61))
        self.update_now_btn.setStyleSheet(u"QPushButton {\n"
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
        self.status_text = QTextEdit(self.fotaPage)
        self.status_text.setObjectName(u"status_text")
        self.status_text.setGeometry(QRect(20, 220, 361, 181))
        self.status_text.setStyleSheet(u"\n"
"    QTextEdit {\n"
"        background-color: #1a1a1a;  /* Darker background for better contrast */\n"
"        border: 2px solid #333;  /* Subtle border */\n"
"        border-radius: 12px;  /* Rounded corners */\n"
"        padding: 10px;  /* Inner spacing */\n"
"        color: #f0f0f0;  /* Light text for readability */\n"
"        font-size: 14px;\n"
"        font-weight: bold;\n"
"    }\n"
"\n"
"    QTextEdit:focus {\n"
"        border: 2px solid #0078D7;  /* Highlight when focused */\n"
"    }\n"
"\n"
"")
        self.stackedWidget.addWidget(self.fotaPage)

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
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
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
        icon3 = QIcon()
        icon3.addFile(u"assets/icons/home_2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeBtn.setIcon(icon3)
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
        icon4 = QIcon()
        icon4.addFile(u"assets/icons/wifi-signal.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.wifiBtn.setIcon(icon4)
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
        icon5 = QIcon()
        icon5.addFile(u"assets/icons/spotify_2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.musicBtn.setIcon(icon5)
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
        icon6 = QIcon()
        icon6.addFile(u"assets/icons/air-conditioning.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.acBtn.setIcon(icon6)
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
        icon7 = QIcon()
        icon7.addFile(u"assets/icons/bluetooth.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bluetoothBtn.setIcon(icon7)
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
        icon8 = QIcon()
        icon8.addFile(u"assets/icons/google-maps.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.mapBtn.setIcon(icon8)
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
        icon9 = QIcon()
        icon9.addFile(u"assets/icons/youtube.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.youtubeBtn.setIcon(icon9)
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
        icon10 = QIcon()
        icon10.addFile(u"assets/icons/phone-call.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.callBtn.setIcon(icon10)
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
        icon11 = QIcon()
        icon11.addFile(u"assets/icons/calendar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.calendarBtn.setIcon(icon11)
        self.calendarBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.calendarBtn)

        self.fotaBtn = QPushButton(self.frame)
        self.fotaBtn.setObjectName(u"fotaBtn")
        self.fotaBtn.setStyleSheet(u"QPushButton {\n"
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
        icon12.addFile(u"assets/icons/update.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.fotaBtn.setIcon(icon12)
        self.fotaBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.fotaBtn)

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
        icon13 = QIcon()
        icon13.addFile(u"assets/icons/Apple_Settings-512.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_Btn.setIcon(icon13)
        self.settings_Btn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.settings_Btn)


        self.horizontalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.bottomMenuSubContainer)


        self.verticalLayout.addWidget(self.bottomMenuContainer)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.wifiLabel.setText(QCoreApplication.translate("Widget", u"Available Wifi Networks", None))
        self.refreshButton.setText(QCoreApplication.translate("Widget", u"Refresh", None))
        self.connectButton.setText(QCoreApplication.translate("Widget", u"Connect", None))
        self.dateTimeLabel.setText(QCoreApplication.translate("Widget", u"text", None))
        self.lockBtn.setText("")
        self.seatbeltBtn.setText("")
        self.power.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:18px; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ffffff;\">Notification Alert !!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ffffff;\"><br />Ambulance coming on the right clear the way</span></p></body></html>", None))
        self.LF_2.setText(QCoreApplication.translate("Widget", u"Self Parking", None))
        self.dms_Updates.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:16px; font-weight:700; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:18px; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Caution: A vehicle is approaching from your left. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-si"
                        "ze:10pt;\">Distance: 20 meters<br />Speed: 60 MPH<br />Direction: Left Side</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Auto Dismiss in 5 seconds</span></p></body></html>", None))
        self.LF_4.setText(QCoreApplication.translate("Widget", u"Call Emergency Contact", None))
        self.dms_CameraFeed.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Starting DMS</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Infotainment Software", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Current Software Version: \"v1.0.0\"", None))
        self.check_updates_btn.setText(QCoreApplication.translate("Widget", u"Check For Updates", None))
        self.release_notes_text.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14px; font-weight:700; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">Update Information</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px"
                        ";\"><br /></p></body></html>", None))
        self.update_now_btn.setText(QCoreApplication.translate("Widget", u"Update Now", None))
        self.status_text.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14px; font-weight:700; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Update Status</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span sty"
                        "le=\" font-size:11pt;\">- Last update: 20/02/2025</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">- Check for updates every two weeks to be updated</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p></body></html>", None))
        self.homeBtn.setText("")
        self.wifiBtn.setText("")
        self.musicBtn.setText("")
        self.acBtn.setText("")
        self.bluetoothBtn.setText("")
        self.mapBtn.setText("")
        self.youtubeBtn.setText("")
        self.callBtn.setText("")
        self.calendarBtn.setText("")
        self.fotaBtn.setText("")
        self.settings_Btn.setText("")
    # retranslateUi

