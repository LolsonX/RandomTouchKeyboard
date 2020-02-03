from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class Screen(GridLayout):
    def __init__(self):
        super().__init__(cols=4, size_hint=(1.0, 3.0))
        self.output = Label(text="", font_size='30sp')
        self.difficulty = Label(text="", font_size='30sp')
        self.input = Label(text="", font_size='30sp')
        self.time = Label(text="", font_size='30sp')
        self.add_widget(Label(text="Word:", font_size='30sp'))
        self.add_widget(self.input)
        self.add_widget(Label(text="Difficulty", font_size='30sp'))
        self.add_widget(self.difficulty)
        self.add_widget(Label(text="Answer:", font_size='30sp'))
        self.add_widget(self.output)
        self.add_widget(Label(text="Time:", font_size='30sp'))
        self.add_widget(self.time)
