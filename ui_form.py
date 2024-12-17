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
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1125, 610)
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
"    background-color: rgba(43, 43, 43, 240); /* Dark color with slight transparency */\n"
"    border-radius: 10px; /* Rounded corners for a sleek look */\n"
"}\n"
"\n"
"QLabel {\n"
"    background-color: rgba(0, 0, 0, 100); /* Translucent overlay for content areas */\n"
"    color: white; /* Ensures text is visible */\n"
"    padding: 10px;\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.horizontalLayout_4 = QHBoxLayout(self.mainContainer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, 0)
        self.stackedWidget = QStackedWidget(self.mainContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.calendarPage = QWidget()
        self.calendarPage.setObjectName(u"calendarPage")
        self.calendarPage.setStyleSheet(u"alternate-background-color: rgb(125, 125, 125);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI\";\n"
"border-color: rgb(0, 0, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(180, 180, 180);\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(self.calendarPage)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.calendarWidget = QCalendarWidget(self.calendarPage)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.horizontalLayout_6.addWidget(self.calendarWidget)

        self.stackedWidget.addWidget(self.calendarPage)
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
        self.dateTimeLabel.setGeometry(QRect(400, -40, 351, 141))
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
        self.progressBar.setGeometry(QRect(990, 70, 118, 23))
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(24)
        self.horizontalLayoutWidget = QWidget(self.homePage)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(220, 100, 661, 301))
        self.homePageLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.homePageLayout.setObjectName(u"homePageLayout")
        self.homePageLayout.setContentsMargins(0, 0, 0, 0)
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
        icon2 = QIcon()
        icon2.addFile(u"assets/icons/home_2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeBtn.setIcon(icon2)
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
        icon3 = QIcon()
        icon3.addFile(u"assets/icons/wifi-signal.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.wifiBtn.setIcon(icon3)
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
        icon4 = QIcon()
        icon4.addFile(u"assets/icons/spotify_2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.musicBtn.setIcon(icon4)
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
        icon5 = QIcon()
        icon5.addFile(u"assets/icons/air-conditioning.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.acBtn.setIcon(icon5)
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
        icon6 = QIcon()
        icon6.addFile(u"assets/icons/bluetooth.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bluetoothBtn.setIcon(icon6)
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
        icon7 = QIcon()
        icon7.addFile(u"assets/icons/google-maps.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.mapBtn.setIcon(icon7)
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
        icon8 = QIcon()
        icon8.addFile(u"assets/icons/youtube.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.youtubeBtn.setIcon(icon8)
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
        icon9 = QIcon()
        icon9.addFile(u"assets/icons/phone-call.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.callBtn.setIcon(icon9)
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
        icon10 = QIcon()
        icon10.addFile(u"assets/icons/calendar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.calendarBtn.setIcon(icon10)
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
        icon11 = QIcon()
        icon11.addFile(u"assets/icons/update.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.updateBtn.setIcon(icon11)
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
        icon12 = QIcon()
        icon12.addFile(u"assets/icons/Apple_Settings-512.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_Btn.setIcon(icon12)
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
        self.dateTimeLabel.setText(QCoreApplication.translate("Widget", u"text", None))
        self.lockBtn.setText("")
        self.seatbeltBtn.setText("")
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

