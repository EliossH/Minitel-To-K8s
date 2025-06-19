from pyminitel.widget import Widget

class Interface(Widget):
    def __init__(self, background_path=None):
        super().__init__()
        self.background_path = background_path

    def render(self):
        output = self.get_static_frame()
        output += super().render()
        return output

    def get_static_frame(self):
        if self.background_path:
            try:
                with open(self.background_path, "rb") as file:
                    return file.read()
            except Exception as e:
                print(f"[Erreur chargement fond: {e}]")
        return b"No background set"