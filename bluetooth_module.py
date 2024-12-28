from PyQt5.QtWidgets import QApplication , QStackedWidget ,QPushButton, QWidget, QSizePolicy, QLabel
import subprocess

class bluetoothModule():
    def __init__(self,widgets: list[QWidget]):
        self.widgets = widgets
        self.devices = []
        # self.list_paired_devices()
    
    def update_paired_devices(self):
        try:
            print("Fetching paired devices...")
            result = subprocess.run(
                ["bluetoothctl", "paired-devices"],
                capture_output=True,
                text=True
            )
            print(result.stdout)
            if result.stdout.strip():
                print("Paired devices found:")
                lines = result.stdout.splitlines()
                self.devices = []
                for line in lines:
                    if line.startswith("Device"):
                        parts = line.split(" ", 2)
                        if len(parts) == 3:
                            address, name = parts[1], parts[2]
                            self.devices.append((address, name))
                self.update_devices_names()
                    
            else:
                print("No paired devices found.")
                return []
        except Exception as e:
            print(f"Error fetching paired devices: {e}")
            return []
    
    def update_devices_names(self):
        for i in range(min(4,len(self.devices))):
            self.widgets[i].findChild(QLabel,f"deviceName{i+1}").setText("text",self.devices[i][1])
            