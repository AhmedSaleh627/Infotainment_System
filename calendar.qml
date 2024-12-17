import QtQuick 6.0
import QtQuick.Controls 6.0
import QtQuick.Layouts 1.1

ApplicationWindow {
    visible: true
    width: 600
    height: 400
    title: "Simple Calendar"

    GridView {
        id: calendar
        width: parent.width
        height: parent.height
        cellWidth: 50
        cellHeight: 50
        model: ListModel {
            ListElement { day: "1" }
            ListElement { day: "2" }
            ListElement { day: "3" }
            ListElement { day: "4" }
            ListElement { day: "5" }
            ListElement { day: "6" }
            ListElement { day: "7" }
            ListElement { day: "8" }
            ListElement { day: "9" }
            ListElement { day: "10" }
            ListElement { day: "11" }
            ListElement { day: "12" }
            ListElement { day: "13" }
            ListElement { day: "14" }
            ListElement { day: "15" }
            ListElement { day: "16" }
            ListElement { day: "17" }
            ListElement { day: "18" }
            ListElement { day: "19" }
            ListElement { day: "20" }
            ListElement { day: "21" }
            ListElement { day: "22" }
            ListElement { day: "23" }
            ListElement { day: "24" }
            ListElement { day: "25" }
            ListElement { day: "26" }
            ListElement { day: "27" }
            ListElement { day: "28" }
            ListElement { day: "29" }
            ListElement { day: "30" }
            ListElement { day: "31" }
        }

        delegate: Rectangle {
            width: calendar.cellWidth
            height: calendar.cellHeight
            border.color: "black"
            color: "lightgray"
            Text {
                anchors.centerIn: parent
                text: model.day
                font.pixelSize: 20
            }
        }
    }
}
