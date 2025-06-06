import serial
import threading
import time
import os
import pty
import subprocess

# ====== CONFIGURATION ======
SERIAL_PORT = '/dev/ttyUSB0'
BAUDRATE = 1200
ENCODING = 'latin1'
SSH_COMMAND = ["ssh", "damien@172.16.50.102"]
READ_SIZE = 64
SLEEP_IDLE = 0.005
MINITEL_COLS = 40
MINITEL_ROWS = 24

# ====== SERIAL SETUP ======
ser = serial.Serial(
    port=SERIAL_PORT,
    baudrate=BAUDRATE,
    bytesize=serial.SEVENBITS,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE,
    timeout=0,
    write_timeout=0,
    inter_byte_timeout=0.001,
    xonxoff=False,
    rtscts=False,
    dsrdtr=False
)

# ====== SSH via PTY ======
pid, fd = pty.fork()

if pid == 0:
    # Enfant : remplacer par le processus SSH
    os.execvp(SSH_COMMAND[0], SSH_COMMAND)
else:
    print("SSH process started in PTY")

# ====== THREAD: SSH → Serial ======
def ssh_to_serial():
    while True:
        try:
            data = os.read(fd, READ_SIZE)
            if data:
                # Convert UTF-8 → ASCII + translittération (minimal pour Minitel)
                clean_data = data.decode('utf-8', errors='ignore').encode(ENCODING, errors='ignore')
                ser.write(clean_data)
            else:
                time.sleep(SLEEP_IDLE)
        except Exception as e:
            print("Error reading from SSH:", e)
            break

# ====== THREAD: Serial → SSH ======
def serial_to_ssh():
    while True:
        try:
            data = ser.read(READ_SIZE)
            if data:
                # On envoie tel quel vers le PTY
                os.write(fd, data)
            else:
                time.sleep(SLEEP_IDLE)
        except Exception as e:
            print("Error writing to SSH:", e)
            break

# ====== START THREADS ======
threading.Thread(target=ssh_to_serial, daemon=True).start()
threading.Thread(target=serial_to_ssh, daemon=True).start()

# ====== KEEP SCRIPT ALIVE ======
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nSession terminated.")
