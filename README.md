# 🔍 Simple Port Scanner

This is a basic Python script to scan a specific port on a given IP address. It's intended for educational purposes and quick port testing.

## 📜 Features

- Prompts the user to enter an IP address and port number.
- Checks if the specified port is open or closed.
- Uses Python’s built-in `socket` module.

## 🧠 How It Works

The script attempts to establish a TCP connection to the target IP and port using `socket.connect_ex`. If the connection is successful, the port is considered open. Otherwise, it's closed.

## 🛠️ Requirements

- Python 3.x

No external libraries are needed.

## 🚀 How to Run

1. Clone this repository or download the script.

2. Open your terminal and run the script:

```bash
python networkscanner.py
