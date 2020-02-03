from kivy import Config
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from control_panel import ControlPanel
from keyboard import Keyboard
from screen import Screen
from timer import Timer
from word_generator import WordGenerator

MAX_TIME = 40
CHANGE_TIME = 5


class TouchKeyboard(App):

    def __init__(self):

        self.words_generator = WordGenerator('word.yml')
        self.layout = BoxLayout(orientation="vertical")
        self.keyboard = None
        self.control_panel = ControlPanel(self.start_timer, self.stop_ev, self.change_difficulty)
        self.timer = None
        self.stop_event = None
        self.tick_event = None
        self.ticks = MAX_TIME
        self.screen = Screen()
        self.difficulty = "Easy"
        super(TouchKeyboard, self).__init__()

    def build(self):
        self.layout.add_widget(self.control_panel)
        self.layout.add_widget(self.screen)
        self.screen.difficulty.text = self.difficulty
        self.keyboard = Keyboard(self.screen.output, self.key_callback)
        self.layout.add_widget(self.keyboard)
        return self.layout

    def reshuffle_keys(self, instance):
        self.keyboard.generate_keyboard()

    def start_timer(self, instance: Button):
        self.control_panel.lock_controls()
        self.screen.output.text = ""
        self.screen.input.text = self.words_generator.generate_word(self.difficulty)
        self.timer = Timer.start(self.reshuffle_keys, CHANGE_TIME)
        self.tick_event = Timer.start(self.decrease_tick, 1)
        self.stop_event = Clock.schedule_once(self.stop_ev, MAX_TIME)

    def stop_ev(self, *largs):
        Clock.unschedule(self.timer)
        Clock.unschedule(self.stop_event)
        Clock.unschedule(self.tick_event)
        self.ticks = MAX_TIME
        self.control_panel.unlock_controls()
        self.screen.output.text = ""
        self.screen.time.text = str(self.ticks)
        self.screen.input.text = ""

    def decrease_tick(self, *largs):
        self.ticks -= 1
        self.screen.time.text = str(self.ticks)

    def key_callback(self, *largs):
        if self.screen.output.text == self.screen.input.text:
            self.stop_ev()
            self.show_win()

    def show_win(self):
        popup = Popup(title='Winner',
                      content=Label(text='You won', font_size='40sp'),
                      size_hint=(None, None), size=(400, 400))
        popup.open()

    def change_difficulty(self, *largs):
        if self.difficulty == 'Easy':
            self.difficulty = 'Medium'
        elif self.difficulty == 'Medium':
            self.difficulty = 'Hard'
        else:
            self.difficulty = 'Easy'
        self.screen.difficulty.text = self.difficulty


if __name__ == '__main__':
    Config.set('graphics', 'borderless', 1)
    Config.set('graphics', 'window_state', 'maximized')
    TouchKeyboard().run()
