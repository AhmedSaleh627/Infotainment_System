# Infotainment System + V2X Integration

## Overview
This infotainment system is designed for smart vehicles, integrating V2X communication, real-time driver monitoring, and various connectivity features. Built using PySide6 and deployed on a Raspberry Pi, the system offers a user-friendly interface with essential functionalities to enhance driver awareness and convenience.

## Features
### User Interface
- **Home Page**: Displays V2X notifications, vehicle alerts, a speedometer, driver monitoring system and allows control of car functions.
- **WiFi Page**: Scans and connects to available WiFi networks on the Raspberry Pi.
- **Map Page**: Provides navigation using OpenStreetMap tiles for accurate global location tracking.
- **Calendar Page**: A built-in calendar using QtCalendarWidget for scheduling and reminders.
- **Bluetooth Page**: Enables Bluetooth connectivity on the Raspberry Pi for device pairing and data transfer.
- **Media Player Page**: A multimedia interface for playing audio and video files.
- **Settings Page**: Customizable user preferences and system configurations.
- **Software Updates Page**: Provides updates for system enhancements and bug fixes.
### Home Page
![drowsy_3](https://github.com/user-attachments/assets/c6273f75-00dc-402c-a6e2-dac3801f9fbe)

### WiFi Page
![{9594D14E-37FC-49E6-9C46-0809208CE814}](https://github.com/user-attachments/assets/99901ecb-18b8-4ab4-8ded-2550b2617e52)

### Map Page
![WhatsApp Image 2025-06-24 at 05 51 44_f1369829](https://github.com/user-attachments/assets/73a60a24-c0e5-4e82-b29c-9b288aac0d26)

### Frimware Updates over the Air Page
![fota_update_available](https://github.com/user-attachments/assets/023855db-f4a1-4947-8590-d915335defa1)

### Bluetooth Page
![WhatsApp Image 2025-06-24 at 18 12 21_4f97307b](https://github.com/user-attachments/assets/1625ba10-14b4-49a8-b88a-87ac272dc66e)

### Songs Page
![WhatsApp Image 2025-06-24 at 15 13 53_b972d20d](https://github.com/user-attachments/assets/ca8b7907-1b0c-46f0-a7b9-4c216a2ebd8d)

### Media Page
![WhatsApp Image 2025-06-24 at 15 24 49_8749c773](https://github.com/user-attachments/assets/522a923d-58fc-452c-9867-d1148bd66a22)

### Calendar Page
![{732A26EF-9B48-4CC3-927E-7F27EDA3B7FE}](https://github.com/user-attachments/assets/1216b5bf-b06a-46b3-8fbe-b6e99dcfd988)

## Implementation Details
### Technologies Used
- **Programming Language**: Python (PySide6 for UI)
- **Hardware**: Raspberry Pi, Raspberry Pi Camera, LCD Touch Screen, GPS
- **Networking**: MQTT, ESP-NOW, WI-FI and Bluetooth modules
- **Mapping Service**: OpenStreetMap

### Challenges & Solutions
- **Hardware Limitations**: Optimized system performance for smooth operation on Raspberry Pi 5.
- **V2X Integration**: Ensured real-time communication and alert processing.
- **UI Responsiveness**: Designed an intuitive interface with minimal latency.

## Testing and Validation
- **Module Testing**: Individual component validation for correct functionality.
- **System Performance**: Evaluated UI responsiveness, connectivity stability, and processing speed.
- **Integration Testing**: Verified seamless interaction between infotainment features and V2X communication.

## Installation
To set up the system on Raspberry Pi 5:
1. Clone the repository:
   ```bash
   git clone https://github.com/AhmedSaleh627/Infotainment_System
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```
