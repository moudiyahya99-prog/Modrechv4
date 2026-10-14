from kivy.app import App
from kivy.uix.label import Label

class ModrechApp(App):
    def build(self):
        return Label(text="MODRECH V4 IKO TAYARI!", font_size=24)

ModrechApp().run()
