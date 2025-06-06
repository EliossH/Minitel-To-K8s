from pyminitel.widget import Widget
from pyminitel.text import Text

class Menu(Widget):
    def __init__(self, labels, x=0, y=0, length=10, selected_index=0):
        super().__init__()
        self.x = x
        self.y = y

        for i, label in enumerate(labels):
            string_widget = Text(label, x=self.x, y=self.y + i)
            self.add_widget(string_widget)
        self.set_focus(self.widgets[selected_index])

    def update_display(self):
        for widget in self.widgets:
            widget.inverted = (widget == self.focused_widget)

    def handle_input(self, char):
        if char == "B":  # UP arrow
            idx = self.widgets.index(self.focused_widget)
            idx = (idx - 1) % len(self.widgets)
            self.set_focus(self.widgets[idx])
            self.update_display()
            self.update(self.render())
        elif char == "H":  # DOWN arrow
            idx = self.widgets.index(self.focused_widget)
            idx = (idx + 1) % len(self.widgets)
            self.set_focus(self.widgets[idx])
            self.update_display()
            self.update(self.render())
        elif char == "\n":  # ENTER
            self.on_select(self.widgets.index(self.focused_widget))

    def on_select(self, index):
        print(index)

    def get_selected(self):
        return self.focused_widget.text if self.focused_widget else None
