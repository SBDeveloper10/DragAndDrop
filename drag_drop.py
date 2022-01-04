from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivy.core.window import Window


kv = """
MDLabel:
    text: app.l
    halign: "center"
    font_style: "H4"
"""


class DragAndDropApp(MDApp):
    l = StringProperty()

    def build(self):
        Window.bind(on_dropfile=self.on_file_drop)
        return Builder.load_string(kv)

    def on_file_drop(self, window, file_path):
        l = file_path
        self.l = str(l)


if __name__ == '__main__':
    app = DragAndDropApp()
    app.run()
