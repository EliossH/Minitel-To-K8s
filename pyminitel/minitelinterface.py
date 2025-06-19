class MinitelInterfaces:
    def __init__(self):
        self.connector = None
        self.send_data = None
        self.interfaces = []
        self.current_interface = None
        self.main_interface = None

    def add_interface(self, interface, main=False):
        interface.root = self
        self.interfaces.append(interface)
        if self.current_interface is None:
            self.current_interface = interface
        if main :
            self.main_interface = interface
            self.current_interface = interface
    
    def set_connector(self, connector):
        self.connector=connector
        self.send_data = connector.send_data
        self.connector.set_receive_callback(self.handle_input)

    def set_active(self, interface):
        self.current_interface = interface
        self.send_data(self.current_interface.render())
    
    def set_main(self):
        if self.current_interface != self.main_interface:
            self.set_active(self.main_interface)

    def handle_input(self, char):
        if char == "*":
            self.set_main()
        elif self.current_interface:
            self.current_interface.handle_input(char)

    def start(self):
        if self.current_interface:
            self.send_data(self.current_interface.render())
        elif self.interfaces:
            self.set_active(self.interfaces[0])

    def send_update(self, bits):
        self.send_data(bits)