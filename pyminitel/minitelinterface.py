class MinitelInterfaces:
    def __init__(self, connector):
        self.connector = connector
        self.send_data = self.connector.send_data
        self.connector.set_receive_callback(self.handle_input)
        self.debug = False
        self.interfaces = []
        self.current_interface = None

    def add_interface(self, interface):
        interface.root = self
        self.interfaces.append(interface)
        if self.current_interface is None:
            self.set_active(interface)

    def set_active(self, interface):
        self.current_interface = interface
        self.send_data(self.current_interface.render())

    def handle_input(self, char):
        if self.debug:
            print(f"Input received: {char}")

        if self.current_interface:
            self.current_interface.handle_input(char)

    def start(self):
        if self.current_interface:
            self.send_data(self.current_interface.render())
        elif self.interfaces:
            self.set_active(self.interfaces[0])

    def send_update(self, bits):
        self.send_data(bits)