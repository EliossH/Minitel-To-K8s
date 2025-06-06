from pyminitel.widget import Widget

class Text(Widget):
    def __init__(self, text, x=0, y=0, inverted=False, color=None):
        super().__init__()
        self.text = text
        self.inverted = inverted
        self.color = color
        self.x = x
        self.y = y

    def render(self):
        output = bytes([0x1F, 0x28 + self.x, 0x28 + self.y])  # Positionne le curseur
        print(output.hex())
        if self.inverted:
            output += bytes([0x0F])  # Inversion des couleurs
        if self.color is not None:
            output += bytes([0x1B, 0x40 + self.color])  # Code couleur (à adapter)
        output += self.text.encode("latin-1")
        if self.inverted:
            output += bytes([0x0E])  # Fin inversion
        print(output.hex())
        return output.decode('latin-1')
