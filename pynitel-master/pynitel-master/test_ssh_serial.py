import serial
import threading
import time
import winpty

# ====== CONFIGURATION ======
SERIAL_PORT = 'COM5'
BAUDRATE = 4800
ENCODING = 'latin1'
SSH_COMMAND = "damien@172.16.50.102"
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

# ====== SSH via PTY SETUP ======
pty = winpty.PTY(cols=MINITEL_COLS, rows=MINITEL_ROWS)
success = pty.spawn(appname="ssh", cmdline=SSH_COMMAND)

if not success:
    print("Failed to start SSH process")
    exit(1)

# ====== THREAD: SSH --> Serial ======
def ssh_to_serial():
    while True:
        try:
            data = pty.read(READ_SIZE)  # str
            if data:
                ser.write(data.encode(ENCODING, errors='ignore'))  # to bytes
            else:
                time.sleep(SLEEP_IDLE)
        except Exception as e:
            print("Error reading from PTY:", e)
            break

# ====== THREAD: Serial --> SSH ======
def serial_to_ssh():
    while True:
        try:
            data = ser.read(READ_SIZE)  # bytes
            if data:
                pty.write(data.decode(ENCODING, errors='ignore'))  # to str
            else:
                time.sleep(SLEEP_IDLE)
        except Exception as e:
            print("Error writing to PTY:", e)
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
