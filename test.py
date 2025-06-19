import serial

connector = serial.Serial(
    port="/dev/ttyS0",
    baudrate=1200,
    bytesize=serial.SEVENBITS,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE
)

path = '/home/user/Downloads/Minitel-To-K8s/faas_interface/asset/test.vdt'

with open(path, 'rb') as file:
    to_send = file.read()
    print(to_send.hex())
    connector.write(to_send)