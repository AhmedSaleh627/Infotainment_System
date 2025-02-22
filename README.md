# Infotainment System + V2X Integration

## Overview
This infotainment system is designed for smart vehicles, integrating V2X communication, real-time driver monitoring, and various connectivity features. Built using PySide6 and deployed on a Raspberry Pi 5, the system offers a user-friendly interface with essential functionalities to enhance driver awareness and convenience.

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
![{70458762-4835-4C00-910A-FD70D5B8E3BD}](https://github.com/user-attachments/assets/55769358-c12a-491f-823a-733b4a03edf8)

### WiFi Page
![{9594D14E-37FC-49E6-9C46-0809208CE814}](https://github.com/user-attachments/assets/99901ecb-18b8-4ab4-8ded-2550b2617e52)

### Map Page
![{3D329B47-E29B-4400-9A83-5FD1A6E6B9CA}](https://github.com/user-attachments/assets/4edf6b45-f673-4f9a-9fa1-dc6c88d36552)

### Calendar Page
![{732A26EF-9B48-4CC3-927E-7F27EDA3B7FE}](https://github.com/user-attachments/assets/1216b5bf-b06a-46b3-8fbe-b6e99dcfd988)

### Bluetooth Page
![{F7A2BB6D-445A-47AC-8635-4285706F0F73}](https://github.com/user-attachments/assets/34ffb4bc-5bf2-4211-b75a-6d11d74f9a07)

## Implementation Details
### Technologies Used
- **Programming Language**: Python (PySide6 for UI)
- **Hardware**: Raspberry Pi 5, Raspberry Pi Camera, LCD Touch Screen, GPS
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
   git clone https://github.com/your-repo/infotainment-system.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```
