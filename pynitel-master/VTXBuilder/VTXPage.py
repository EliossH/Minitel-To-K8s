class VTXPage:
    def __init__(self, widget_list=[]):
        self.widget_list = widget_list
    
    def render(self):
        content = bytearray()
        content += bytes([0x1B, 0x40])
        content += bytes([0x1B, 0x45])
        for widget in self.widget_list:
            content += widget.render()
        return content