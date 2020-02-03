from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class ControlPanel(GridLayout):
    def __init__(self, start_event, reset_event, change_event):
        super().__init__(cols=4, size_hint=(1, 0.2))
        self.start_btn = Button(text="Start", on_press=start_event, font_size='30sp')
        self.add_widget(self.start_btn)
        self.reset_btn = Button(text="Reset", on_press=reset_event, font_size='30sp')
        self.add_widget(self.reset_btn)
        self.change_btn = Button(text="Change Difficulty", on_press=change_event, font_size='30sp')
        self.add_widget(self.change_btn)
        self.add_widget(Button(text="Exit", on_press=self.stop_app, font_size='30sp'))

    def stop_app(self, *largs):
        App.get_running_app().stop()

    def lock_controls(self):
        self.start_btn.disabled = True
        self.change_btn.disabled = True

    def unlock_controls(self):
        self.start_btn.disabled = False
        self.change_btn.disabled = False
