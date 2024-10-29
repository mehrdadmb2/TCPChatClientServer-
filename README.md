<!-- بخش مرکزی توضیحات و مشخصات پروژه -->
<div align="center">
  
  <!-- عنوان پروژه -->
  <h1> Simple Network Chat Program </h1>
  <p> A Basic Tool for Sending and Receiving Text Messages Between Devices Over a Network </p>

  <!-- بخش باج‌ها (Badges) -->
  <a href="https://github.com/mehrdadmb2/TCPChatClientServer" title="Go to GitHub repo">
    <img src="https://img.shields.io/static/v1?label=Mehrdad&message=Network-Chat&color=blue&logo=github" alt="Mehrdad - Network Chat">
  </a>
  <a href="https://github.com/mehrdadmb2/TCPChatClientServer">
    <img src="https://img.shields.io/github/stars/mehrdadmb2/TCPChatClientServer?style=social" alt="stars - Network Chat">
  </a>
  <a href="https://github.com/mehrdadmb2/TCPChatClientServer">
    <img src="https://img.shields.io/github/forks/mehrdadmb2/TCPChatClientServer?style=social" alt="forks - Network Chat">
  </a>

  <!-- لینک‌های سریع -->
<!--  <h4>
    <a href="https://github.com/mehrdadmb2/TCPChatClientServer/wiki">Documentation</a>
    <span> · </span>
    <a href="https://github.com/mehrdadmb2/TCPChatClientServer/issues">Report Bug</a>
    <span> · </span>
    <a href="https://github.com/mehrdadmb2/TCPChatClientServer/issues">Request Feature</a>
  </h4> -->
</div> 

<br />

<!-- معرفی پروژه -->
## :star2: About the Project

This project is a simple network chat program that allows users to send and receive messages over a local network. It includes automated library installation for required dependencies and offers an interactive console-based chat interface.

<div>&nbsp;</div>

<!-- بخش راه‌اندازی پروژه -->
## 🛠️ Installation and Setup

1. **Clone the Repository**  
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/mehrdadmb2/TCPChatClientServer.git
   cd TCPChatClientServer
   ```
   
    Then, run the following command:
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Dependencies**  
   The program includes an automatic library downloader. If any libraries are missing, the downloader will attempt to install them for you.

   Required Libraries:
   - `socket`
   - `threading`
   - `colorama`

3. **Run the Program**  
   Start the chat server and client:
   ```bash
   python Send_MSG(A).py
   ```
```bash
   python Send_MSG(B).py
   ```
<div>&nbsp;</div>

<!-- توضیحات پیکربندی -->
## ⚙️ Configuration
To customize the program, you may need to modify the following settings in the code:

- **SERVER_HOST**: The IP address to listen on. Defaults to `0.0.0.0`.
- **SERVER_PORT**: The port the server will use to listen for incoming connections. Default is `8080`.
- **CLIENT_PORT**: The port the client will use to connect. Default is `8082`.
- **TARGET_IP**: Set the IP address of the target device you wish to connect to. (Adjust this to match the network configuration)

Example:
```python
# Configuration (Adjust according to your setup)
SERVER_HOST = "0.0.0.0"       # Replace with your desired IP for server listening
SERVER_PORT = 8080            # Replace with your desired port for server listening
CLIENT_PORT = 8082            # Replace with your desired port for client connection
TARGET_IP = "192.168.1.102"   # Replace with the target IP address for sending messages
```

<div>&nbsp;</div>

<!-- دستورالعمل‌های استفاده -->
## 🚀 Usage

### Server Setup
Run the script on the device you wish to set up as the server. The server will listen for incoming connections on the specified `SERVER_HOST` and `SERVER_PORT`.

### Client Setup
Run the script on a different device, specifying the `TARGET_IP` and `CLIENT_PORT` for the connection. Enter messages in the console to communicate with the server.

### Stopping the Program
Type `exit` in the client console to terminate the connection.

<div>&nbsp;</div>

<!-- ویژگی‌های برنامه -->
## 🎯 Features
- **Automatic Library Downloader**: The program will check for required libraries and install them automatically if they are not already installed.
- **Clear Console**: Cross-platform command to clear the console screen (compatible with Windows and Linux).
- **Message Log**: Displays incoming and outgoing messages in different colors for easier readability.

<div>&nbsp;</div>

<!-- لایسنس پروژه -->
## 📜 License
Distributed under the MIT License. See `NOPEEEE` for more information.
NOOOOOO  Licensessss XD
<div>&nbsp;</div>

<!-- اطلاعات تماس -->
## 📬 Contact
Mehrdad - [game.developer.mb@gmail.com](mailto:game.developer.mb@gmail.com)

Project Link: [https://github.com/mehrdadmb2/TCPChatClientServer](https://github.com/mehrdadmb2/TCPChatClientServer)

<div>&nbsp;</div>

<!-- قدردانی‌ها -->
## 🤝 Acknowledgements
Special thanks to the open-source contributors for Colorama and other essential Python libraries.
```
### توضیحات:
- بخش مربوط به `Install Dependencies` به‌روز شده و اطلاعات مربوط به `requirements.txt` اضافه شده است.
- حالا کاربران می‌توانند به راحتی کتابخانه‌های مورد نیاز را نصب کنند.
