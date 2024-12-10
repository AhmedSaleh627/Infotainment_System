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
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1084, 552)
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
        self.mainContainer.setStyleSheet(u"background-color: rgb(111, 111, 111);")
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
        self.horizontalLayout_5 = QHBoxLayout(self.homePage)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget = QWidget(self.homePage)
        self.widget.setObjectName(u"widget")

        self.horizontalLayout_5.addWidget(self.widget)

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
        icon.addFile(u"assets/icons/home_2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeBtn.setIcon(icon)
        self.homeBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.homeBtn)

        self.wifiBtn = QPushButton(self.frame)
        self.wifiBtn.setObjectName(u"wifiBtn")
        self.wifiBtn.setStyleSheet(u"QPushButton {\n"
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
        icon1.addFile(u"assets/icons/wifi-signal.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.wifiBtn.setIcon(icon1)
        self.wifiBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.wifiBtn)

        self.musicBtn = QPushButton(self.frame)
        self.musicBtn.setObjectName(u"musicBtn")
        self.musicBtn.setStyleSheet(u"QPushButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(u"assets/icons/spotify_2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.musicBtn.setIcon(icon2)
        self.musicBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.musicBtn)

        self.acBtn = QPushButton(self.frame)
        self.acBtn.setObjectName(u"acBtn")
        self.acBtn.setStyleSheet(u"QPushButton {\n"
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
        icon3 = QIcon()
        icon3.addFile(u"assets/icons/air-conditioning.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.acBtn.setIcon(icon3)
        self.acBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.acBtn)

        self.bluetoothBtn = QPushButton(self.frame)
        self.bluetoothBtn.setObjectName(u"bluetoothBtn")
        self.bluetoothBtn.setStyleSheet(u"QPushButton {\n"
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
        icon4 = QIcon()
        icon4.addFile(u"assets/icons/bluetooth.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bluetoothBtn.setIcon(icon4)
        self.bluetoothBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.bluetoothBtn)

        self.mapBtn = QPushButton(self.frame)
        self.mapBtn.setObjectName(u"mapBtn")
        self.mapBtn.setStyleSheet(u"QPushButton {\n"
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
        icon5.addFile(u"assets/icons/google-maps.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.mapBtn.setIcon(icon5)
        self.mapBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.mapBtn)

        self.youtubeBtn = QPushButton(self.frame)
        self.youtubeBtn.setObjectName(u"youtubeBtn")
        self.youtubeBtn.setStyleSheet(u"QPushButton {\n"
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
        icon6.addFile(u"assets/icons/youtube.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.youtubeBtn.setIcon(icon6)
        self.youtubeBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.youtubeBtn)

        self.callBtn = QPushButton(self.frame)
        self.callBtn.setObjectName(u"callBtn")
        self.callBtn.setStyleSheet(u"QPushButton {\n"
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
        icon7 = QIcon()
        icon7.addFile(u"assets/icons/phone-call.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.callBtn.setIcon(icon7)
        self.callBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.callBtn)

        self.calendarBtn = QPushButton(self.frame)
        self.calendarBtn.setObjectName(u"calendarBtn")
        self.calendarBtn.setStyleSheet(u"QPushButton {\n"
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
        icon8 = QIcon()
        icon8.addFile(u"assets/icons/calendar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.calendarBtn.setIcon(icon8)
        self.calendarBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.calendarBtn)

        self.updateBtn = QPushButton(self.frame)
        self.updateBtn.setObjectName(u"updateBtn")
        self.updateBtn.setStyleSheet(u"QPushButton {\n"
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
        icon9 = QIcon()
        icon9.addFile(u"assets/icons/update.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.updateBtn.setIcon(icon9)
        self.updateBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.updateBtn)

        self.settings_Btn = QPushButton(self.frame)
        self.settings_Btn.setObjectName(u"settings_Btn")
        self.settings_Btn.setStyleSheet(u"QPushButton {\n"
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
        icon10 = QIcon()
        icon10.addFile(u"assets/icons/Apple_Settings-512.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_Btn.setIcon(icon10)
        self.settings_Btn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.settings_Btn)


        self.horizontalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.bottomMenuSubContainer, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.bottomMenuContainer, 0, Qt.AlignBottom)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
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

