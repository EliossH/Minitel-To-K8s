import serial
import threading
import time

class SerialConnector:
    def __init__(self, port, baudrate=4800, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None
        self.running = False
        self.external_receive_callback = None
        self.lock = threading.Lock()

    def start(self):
        """Open the serial port and start the reading thread."""
        try:
            self.serial_connection = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            self.running = True
            threading.Thread(target=self.read_data, daemon=True).start()
        except serial.SerialException as e:
            print(f"[ERROR] Could not open serial port {self.port}: {e}")

    def stop(self):
        """Stop the reading thread and close the serial connection."""
        with self.lock:
            self.running = False
        if self.serial_connection and self.serial_connection.is_open:
            try:
                self.serial_connection.close()
            except serial.SerialException as e:
                print(f"[ERROR] Could not close serial port: {e}")

    def read_data(self):
        """Continuously read from the serial port and invoke the callback."""
        while self.running:
            try:
                if self.serial_connection.in_waiting > 0:
                    data = self.serial_connection.read(
                        self.serial_connection.in_waiting
                    ).decode('utf-8', errors='ignore')
                    if self.external_receive_callback:
                        self.external_receive_callback(data)
            except serial.SerialException as e:
                print(f"[ERROR] Error reading from serial port: {e}")
                self.stop()
            time.sleep(0.1)

    def send_data(self, data):
        """Send bytes data over the serial port."""
        try:
            if self.serial_connection and self.serial_connection.is_open:
                print(data.hex())
                self.serial_connection.write(data)
            else:
                print("[WARN] Serial port is not open.")
        except serial.SerialException as e:
            print(f"[ERROR] Error sending data: {e}")

    def set_receive_callback(self, callback):
        """Register a function to handle received data."""
        self.external_receive_callback = callback
