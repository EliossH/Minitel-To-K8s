from connector.serial_connector import SerialConnector
from faas_interface.faas_interface import FaaSInterface
from config.settings import serial_port


def main():

    connector = SerialConnector(port=serial_port)
    connector.start()
    
    FaaSInterface.set_connector(connector)

    FaaSInterface.start()

    try:
        while True:
            pass  # Keep the main thread alive
    except KeyboardInterrupt:
        connector.stop()  # Stop the connector on exit

if __name__ == "__main__":
    main()