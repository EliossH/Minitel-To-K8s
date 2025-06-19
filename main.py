from connector.serial_connector import SerialConnector
from faas_interface.faas_interface import FaaSInterface


def main():

    connector = SerialConnector(port="/dev/ttyS0")
    connector.start()
    
    minitel = FaaSInterface(connector)
    input("Press Enter to start the Minitel interface...")

    minitel.start()

    try:
        while True:
            pass  # Keep the main thread alive
    except KeyboardInterrupt:
        connector.stop()  # Stop the connector on exit

if __name__ == "__main__":
    main()