from pyminitel.widget import Widget
from pyminitel.text import Text

class Menu(Widget):
    def __init__(self, options, x=0, y=0, length=10, selected_index=0, font_color=7, bg_color=0):
        super().__init__()
        self.x = x
        self.y = y
        self.bg_color=bg_color
        self.font_color=font_color
        self.selected_index=selected_index

        for i, option in enumerate(options):
            string_widget = Text(option["text"],callback=option["callback"], x=self.x, y=self.y + i, font_color=self.font_color, bg_color=self.bg_color)
            self.add_widget(string_widget)
        self.set_focus(self.widgets[self.selected_index])

    def set_focus(self, widget):
        if self.focused_widget:
            self.focused_widget.inverted=False
        super().set_focus(widget)
        self.focused_widget.inverted=True

    def handle_input(self, char):
        if char == "A":
            self.change_selection(-1)
        elif char == "Q":
            self.change_selection(1)
        elif char == "E":
            self.focused_widget.execute()
        else :
            super().handle_input(char)
    
    def change_selection(self, dx):
        old_index = self.selected_index
        new_index = (self.selected_index+dx)%len(self.widgets)
        self.set_focus(self.widgets[new_index])
        self.selected_index = new_index
        to_render = self.widgets[new_index].render() + self.widgets[old_index].render()
        self.update(to_render)

    def get_selected(self):
        return self.focused_widget.text if self.focused_widget else None
