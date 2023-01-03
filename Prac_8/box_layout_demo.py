from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        self.root.ids.output_label.text = f"Hello {self.root.ids.output_label.text}"
        return self.root

    def handle_greet(self):
        print('greet')



BoxLayoutDemo().run(