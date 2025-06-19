from connector.serial_connector import SerialConnector
from faas_interface.faas_interface import FaaSInterface


def main():

    connector = SerialConnector(port="/dev/ttyS0")
    connector.start()
    
    FaaSInterface.set_connector(connector)
    input("Press Enter to start the Minitel interface...")

    FaaSInterface.start()

    try:
        while True:
            pass  # Keep the main thread alive
    except KeyboardInterrupt:
        connector.stop()  # Stop the connector on exit

if __name__ == "__main__":
    main()