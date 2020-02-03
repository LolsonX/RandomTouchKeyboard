from random import shuffle

from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class Keyboard(GridLayout):
    def __init__(self, output: Label, key_callback: callable):
        super().__init__(cols=10, size_hint_y=2)
        self.output_label = output
        self.key_callback = key_callback
        self.blocked = True
        self.button_functions = {
            'Caps Lock': self.caps_lock,
            'Shift': self.shift,
            'BackSpace': self.backspace,
            'Clear': self.clear
        }
        self.big_letters = False
        self.one_big = False
        self.generate_keyboard()

    def generate_keyboard(self):
        self.clear_widgets()
        button_symbols = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
                          '', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                          '', '', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '']
        special_buttons = ['Caps Lock', 'Clear', 'BackSpace', 'Shift']
        shuffle(button_symbols)
        shuffle(special_buttons)
        for letter in button_symbols:
            if letter != '':
                self.add_widget((Button(text=letter, on_press=self.print_button_text, font_size='30sp')))
            else:
                btn_name = special_buttons.pop()
                self.add_widget(self.generate_special_button(btn_name))

    def generate_special_button(self, btn_name: str) -> Button:
        return Button(text=btn_name, on_press=self.button_functions[btn_name], font_size='30sp')

    def print_button_text(self, instance):
        if self.big_letters and not self.one_big:
            self.output_label.text += instance.text.upper()
        elif self.one_big and not self.big_letters:
            self.output_label.text += instance.text.upper()
            self.one_big = False
        elif self.big_letters and self.one_big:
            self.output_label.text += instance.text
            self.one_big = False
        else:
            self.output_label.text += instance.text
        Clock.schedule_once(self.key_callback, -1)

    def caps_lock(self, instance: Button):
        self.big_letters = not self.big_letters

    def shift(self, instance: Button):
        self.one_big = not self.one_big

    def backspace(self, instance: Button):
        self.output_label.text = self.output_label.text[:-1]

    def clear(self, instance: Button):
        self.output_label.text = ''
