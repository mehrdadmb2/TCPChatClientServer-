import importlib
import subprocess
import platform
import sys
# If Any Error First Download Colorama (pip install colorama) :)
from colorama import Fore
import time

def auto_lib_downloader(libs):
    osnames = platform.system()
    python_executable = sys.executable  

    for lib in libs:
        try:
            importlib.import_module(lib)
            print(Fore.GREEN + f"[+] Library '{lib}' has been imported successfully.")
        except ImportError:
            print(Fore.YELLOW + f"[-] Library '{lib}' is not installed.")
            print(Fore.CYAN + f"[/] Downloading library '{lib}'...")

            result = subprocess.run(
                [python_executable, "-m", "pip", "install", lib],
                capture_output=True, text=True
            )

            if result.returncode == 0:
                print(Fore.GREEN + f"[++] Library '{lib}' has been successfully installed and imported.")
            else:
                print(Fore.RED + f"[!!] Failed to install '{lib}'. Error:\n{result.stderr}")

    print(Fore.GREEN + "[++] All libraries have been processed.")

def clear():
    osnames = platform.system()
    subprocess.run(['cls' if osnames == "Windows" else 'clear'], shell=True)

def Import_Lib():
    global socket , threading , colorama
    import socket
    import threading
    import colorama

auto_lib_downloader(['socket','threading','colorama'])

time.sleep(1)

clear()

Import_Lib()

# Server configuration
SERVER_HOST = "0.0.0.0"       # Server IP address (do not change for local server)
SERVER_PORT = 8080            # Server port
CLIENT_PORT = 8082            # Port to send messages to the other device
TARGET_IP = "192.168.1.102"   # Target IP address (change this to the IP of the other device)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

def receive_messages():
    while True:
        client_socket, client_address = server_socket.accept()
        print(Fore.BLUE + f"[Connected] with {client_address}")
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(Fore.CYAN + f"[Received] {message}")
        client_socket.close()

def send_messages():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = False

    while not connected:
        try:
            client_socket.connect((TARGET_IP, CLIENT_PORT))
            connected = True
            print(Fore.GREEN + f"[Connected] to {TARGET_IP}:{CLIENT_PORT} to send messages.")
        except ConnectionRefusedError:
            print(Fore.YELLOW + "[!] Connection failed. Retrying in 3 seconds...")
            time.sleep(3)

    while True:
        message = input("Enter message: ")
        if message.lower() == 'exit':
            break
        client_socket.send(message.encode('utf-8'))
    client_socket.close()

receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)

receive_thread.start()
send_thread.start()

receive_thread.join()
send_thread.join()
