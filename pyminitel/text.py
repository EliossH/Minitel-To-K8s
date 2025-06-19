from pyminitel.widget import Widget

class Text(Widget):
    def __init__(self, text, callback=lambda: print("No callback set"), x=1, y=1, inverted=False, font_color=7, bg_color=0):
        super().__init__(callback=callback)
        self.text = text
        self.inverted = inverted
        self.bg_color=bg_color
        self.font_color=font_color
        self.x = x
        self.y = y

    def render(self):
        output = bytes([0x1F, 64 + self.y, 64 + self.x])  # Positionne le curseur
        output += bytes([0x1B, 80 + self.bg_color]) # Mets la bonne couleur de fond
        output += bytes([0x1B, 64 + self.font_color]) # Mets la bonne couleur de texte
        if self.inverted:
            output += bytes([0x1B, 0x5D])
        output += self.text.encode("latin-1")
        return output
