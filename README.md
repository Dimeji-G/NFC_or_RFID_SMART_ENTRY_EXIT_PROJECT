# NFC Smart Entry-Exit System

A comprehensive smart access control system combining RFID simulation, Arduino microcontroller programming, and web-based monitoring. This project demonstrates embedded systems design, circuit simulation, and full-stack development for ICT 215 - Robotics and Embedded Systems.

![Project Status](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Arduino](https://img.shields.io/badge/Arduino-C%2B%2B-00979D.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey.svg)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Hardware Components](#hardware-components)
- [Software Components](#software-components)
- [Installation](#installation)
- [Usage](#usage)
- [Project Files](#project-files)
- [Simulation Platforms](#simulation-platforms)
- [Web Interface](#web-interface)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview

The NFC Smart Entry-Exit System is an educational project that demonstrates:

- **RFID-based access control** with entry/exit tracking
- **Arduino microcontroller programming** for real-time control
- **Analog circuit design** for power regulation
- **Web-based monitoring** using Flask
- **Circuit simulation** in Proteus and Tinkercad
- **PCB design** using EasyEDA

### Project Objectives

1. Design and simulate a complete access control system
2. Develop analog circuits for stable microcontroller operation
3. Implement entry/exit logic with occupancy tracking
4. Create a web interface for remote monitoring
5. Design a professional PCB layout
6. Document the entire development process

---

## Features

### Hardware Features
- RFID authentication (simulated via Virtual Terminal)
- Dual LED indicators (Red: Denied, Green: Granted)
- Entry/exit tracking with time logging
- Occupancy detection (prevents multiple simultaneous entries)
- Voltage regulation (7805) for stable 5V supply

### Software Features
- Real-time access control logic
- Multiple authorized users (ADMIN, STAFF, GUEST)
- Web-based activation interface
- Countdown timer display
- Serial monitoring and debugging
- Status API endpoint for ESP integration

---

## System Architecture

```
┌─────────────────┐
│  RFID Scanner   │ (Simulated via Virtual Terminal)
│  (Input)        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Arduino Nano   │ ◄─── Power Supply (7805 Regulator)
│  (Processor)    │
└────────┬────────┘
         │
         ├──────► LED Indicators (Digital Pins 5, 6)
         │
         └──────► Serial Output (Logging)
                  
┌─────────────────┐
│  Flask Server   │ ◄─── Web Interface (Port 8002)
│  (Monitoring)   │
└─────────────────┘
```

---

## Hardware Components

### Required Components

| Component | Quantity | Specification |
|-----------|----------|---------------|
| Arduino Nano | 1 | ATmega328P |
| 7805 Voltage Regulator | 1 | 5V, 1A |
| LED (Red) | 1 | 5mm, 20mA |
| LED (Green) | 1 | 5mm, 20mA |
| Resistor | 2 | 220Ω, 1/4W |
| Capacitor | 2 | 100µF, 25V |
| RFID Module | 1 | RC522 (for physical implementation) |

### Pin Mapping

```cpp
// Arduino Nano Pin Configuration
Pin D5  → Red LED (Access Denied)
Pin D6  → Green LED (Access Granted)
Pin RX  → RFID Input (Virtual Terminal)
Pin TX  → Serial Output (Debugging)
VIN     → 7805 Output (5V)
GND     → Common Ground
```

---

## Software Components

### 1. Arduino Code (Embedded System)

#### Proteus Version ([`Proteus_Code.txt`](Proteus_Code.txt))
- Full entry/exit tracking
- Multiple authorized users
- Time logging
- Occupancy detection
- Status feedback via Serial

#### Tinkercad Version ([`Tinker_Card_Code.txt`](Tinker_Card_Code.txt))
- Simplified version for educational purposes
- Single RFID validation
- Basic LED control
- Serial debugging

### 2. Flask Web Server ([`app.py`](app.py))
- Real-time status monitoring
- Web-based activation interface
- RESTful API endpoints
- Countdown timer

### 3. Web Interface ([`templates/activate.html`](templates/activate.html))
- Modern, responsive design
- Real-time countdown display
- Visual status indicators
- Particle.js animations

---

## Installation

### Prerequisites

```bash
# Python 3.8 or higher
python --version

# Arduino IDE 1.8.x or higher
arduino --version
```

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/nfc-smart-entry-exit.git
cd nfc-smart-entry-exit
```

### Step 2: Install Python Dependencies

```bash
pip install flask
```

### Step 3: Arduino Setup

1. Open Arduino IDE
2. Copy code from [`Tinker_Card_Code.txt`](Tinker_Card_Code.txt) or [`Proteus_Code.txt`](Proteus_Code.txt)
3. Select board: **Tools → Board → Arduino Nano**
4. Select processor: **Tools → Processor → ATmega328P**
5. Upload to Arduino

### Step 4: Proteus Simulation

1. Open Proteus Design Suite
2. Create new project
3. Add components:
   - Arduino Nano
   - Virtual Terminal (for RFID simulation)
   - LEDs (Red and Green)
   - Resistors (220Ω)
   - 7805 Regulator
4. Connect according to schematic
5. Load HEX file from Arduino compilation
6. Run simulation

### Step 5: Tinkercad Simulation

1. Visit [Tinkercad Circuits](https://www.tinkercad.com/circuits)
2. Create new circuit
3. Add Arduino Uno (compatible with Nano code)
4. Add LEDs and resistors
5. Paste code from [`Tinker_Card_Code.txt`](Tinker_Card_Code.txt)
6. Start simulation
7. Open Serial Monitor

---

## Usage

### Running the Web Server

```bash
python app.py
```

The server will start on `http://localhost:8002`

### Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Server status check |
| `/activate` | GET | Activate system (10-second timer) |
| `/status` | GET | Check if system is ON/OFF |

### Testing RFID in Proteus

1. Open Virtual Terminal in Proteus
2. Type authorized RFID codes:
   - `010D429BBF6A` (ADMIN)
   - `020A5B8CD3E7` (STAFF)
   - `030F9E4A1C2B` (GUEST)
3. Press Enter
4. Observe LED indicators and Serial output

### Testing RFID in Tinkercad

1. Open Serial Monitor
2. Set baud rate to 9600
3. Type RFID: `010D429BBF6A`
4. Press Send
5. Observe LED behavior

### Web Activation Flow

1. Navigate to `http://localhost:8002/activate`
2. System activates for 10 seconds
3. Countdown timer displays remaining time
4. ESP can poll `/status` endpoint
5. Returns "ON" during active period, "OFF" afterward

---

## Project Files

```
NFC_Smart_Entry_Exit_Project/
│
├── app.py                          # Flask web server
├── Proteus_Code.txt                # Arduino code for Proteus
├── Tinker_Card_Code.txt            # Arduino code for Tinkercad
├── deepseek_python_20260116_25684f.py  # Report generation script
├── README.md                       # This file
│
└── templates/
    └── activate.html               # Web interface template
```

---

## Simulation Platforms

### Proteus Design Suite

**Features:**
- Professional circuit simulation
- Virtual Terminal for RFID input
- Real-time serial monitoring
- PCB layout capabilities

**Advantages:**
- Industry-standard tool
- Advanced debugging
- Export to PCB

### Tinkercad Circuits

**Features:**
- Browser-based simulation
- User-friendly interface
- Educational focus
- Free access

**Advantages:**
- No installation required
- Great for learning
- Community support

---

## Web Interface

### Features

- **Modern UI**: Clean, professional design with Dimroid branding
- **Real-time Updates**: JavaScript-based countdown
- **Responsive**: Works on all devices
- **Visual Feedback**: Status indicators and animations
- **Particle.js**: Interactive animated background

### Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Flask (Python)
- **Styling**: Custom CSS with Google Fonts (Inter, Outfit)
- **Effects**: Particles.js for dynamic background
- **Fonts**: Font Awesome for icons

---

## Testing

### Unit Tests

```cpp
// Test 1: Valid RFID Entry
Input: "010D429BBF6A"
Expected: Green LED ON for 5 seconds

// Test 2: Invalid RFID
Input: "000000000000"
Expected: Red LED blinks 3 times

// Test 3: Exit (Same User)
Input: "010D429BBF6A" (after entry)
Expected: Green LED ON, time logged

// Test 4: Occupancy Check
Input: "020A5B8CD3E7" (while ADMIN inside)
Expected: Red LED blinks 5 times
```

### Integration Tests

1. **Power Supply Test**: Verify 5V regulation
2. **LED Response Test**: Confirm correct indicator behavior
3. **Serial Communication Test**: Validate output format
4. **Web Server Test**: Check endpoint responses

---

## Future Enhancements

### Hardware
- [ ] Physical RFID RC522 module integration
- [ ] LCD display for status messages
- [ ] Buzzer for audio feedback
- [ ] Relay module for door lock control
- [ ] Battery backup system

### Software
- [ ] Database logging (SQLite/MySQL)
- [ ] User management dashboard
- [ ] Email/SMS notifications
- [ ] Biometric authentication
- [ ] Mobile app integration
- [ ] Real-time analytics

### Features
- [ ] Multi-room support
- [ ] Time-based access control
- [ ] Visitor management
- [ ] Emergency override
- [ ] Cloud synchronization

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Coding Standards

- Follow Arduino style guide for embedded code
- Use PEP 8 for Python code
- Comment complex logic
- Update documentation

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Acknowledgments
# Course Information
- **Course**: ICT 215 - Robotics and Embedded Systems.
- **Institution**: Bells University of Technology.
- **Instructor**: Lecturer Ayuba Mohammed.

### Group Members
- Adewoye Rachel Kikelomo 2024/13384- Group Leader
- Adebimpe Elisha Eriogo 2024/13659
- Adebiyi Azeem Adebayo 2024/13791
- Abbah Martins Oche 2024/13324
- Abdulhammed Sufyan Ademola 2024/13228

### Tools Used
- **Proteus Design Suite** - Circuit simulation
- **Tinkercad** - Educational prototyping
- **EasyEDA** - PCB design
- **Arduino IDE** - Code development
- **Flask** - Web framework
- **Visual Studio Code** - Code editor

## Project Status

### Completed
- [x] Arduino code development
- [x] Proteus simulation
- [x] Tinkercad simulation
- [x] Flask web server
- [x] Web interface design
- [x] Particle.js integration
- [x] Documentation

### In Progress
- [ ] PCB fabrication
- [ ] Physical prototype assembly
- [ ] Comprehensive testing

### Planned
- [ ] Physical RFID integration
- [ ] Database implementation
- [ ] Mobile app development

---

## Quick Links

- [Arduino Documentation](https://www.arduino.cc/reference/en/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Proteus Tutorials](https://www.labcenter.com/)
- [Tinkercad Learn](https://www.tinkercad.com/learn)
- [RFID RC522 Datasheet](https://www.nxp.com/docs/en/data-sheet/MF1S50YYX_V1.pdf)
- [Particles.js](https://particles.js.org/)
