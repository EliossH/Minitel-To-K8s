class Widget:
    def __init__(self):
        self.visible = True
        self.widgets = []
        self.parent = None
        self.focused_widget = None
        self.root = None

    def update(self, bits):
        if self.root:
            self.root.send_update(bits)

    def handle_input(self, char):
        if self.focused_widget:
            self.focused_widget.handle_input(char)

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False

    def set_focus(self, widget):
        if widget in self.widgets:
            self.focused_widget = widget

    def add_widget(self, widget):
        widget.parent = self
        widget.root = self.root
        self.widgets.append(widget)

    def render(self):
        result = bytes()
        for widget in self.widgets:
            if widget.visible:
                result += widget.render()
        return result