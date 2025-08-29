# simple-network-scanner
A simple Python network scanner to detect open ports on a given CIDR network.

# 📌 Features
- Scans a target host (IP address or domain).
- Checks for open ports within a given range.
- Displays results in a clean format.
- Lightweight and easy to understand.

---

# 📂 Technologies Used
Python

socket → for network communication

ipaddress → for handling IP ranges

---

# 🛠️ Installation & Setup
   1. Clone the repository:

   ```bash
   git clone https://github.com/ahinsa2/simple-network-scanner.git
   cd simple-network-scanner
   ```
   
   2.Install Python (if not already installed).
   Check version:
   ```bash
   python --version
   ```
   3.Run the scanner:
   ```bash
   python scanner.py
   ```
   ***📘 Inputs You Provide***
   
   IP Range (CIDR format) → Example: 192.168.1.0/24
   
   👉 You can find your local network IP range using:
   
   On Windows: ipconfig
   
   On Linux/Mac: ifconfig or ip a
   
   4.Test case
   ```bash
       network_scanner("192.168.1.0/24", [22, 80, 443])
   ```


---
# 🎯 Use Cases
Learn how network scanning works

Understand IP addressing & subnets

## 📄 License

This project is open-source and free to use under the [MIT License](./LICENSE).

---

by ***Ahinsa Mohanty***
