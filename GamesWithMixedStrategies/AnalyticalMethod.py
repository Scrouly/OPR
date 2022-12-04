from GamesWithMixedStrategies.Components.SaddlePoint import find_saddle_point
from GamesWithMixedStrategies.Components.ValueOfTheGame import value_of_the_game
from GamesWithMixedStrategies.Components.OptimalMixedStrategyForPlayers import optimal_mixed_strategy_for_players
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

Window.size = (500, 500)
Window.clearcolor = (128 / 255, 128 / 255, 128 / 255, 1)
Window.title = 'Games with Mixed Strategies'


class AnalyticalMethod(App):
    def __init__(self):
        super().__init__()
        self.array = []
        self.label = Label(text='Game Theory :\nGames with Mixed Strategies\nAnalytic method', font_size=18, )
        self.saddle_point = Label(text='', font_size=18)
        self.game_value = Label(text='', font_size=18)
        self.optimal_strategy = Label(text='', font_size=18)
        self.input_1 = TextInput(hint_text='a11', multiline=False, font_size=25, halign='center', )
        self.input_1.bind(text=self.on_text)
        self.input_2 = TextInput(hint_text='a12', multiline=False, font_size=25, halign='center', )
        self.input_2.bind(text=self.on_text)
        self.input_3 = TextInput(hint_text='a21', multiline=False, font_size=25, halign='center', )
        self.input_3.bind(text=self.on_text)
        self.input_4 = TextInput(hint_text='a22', multiline=False, font_size=25, halign='center', )
        self.input_4.bind(text=self.on_text)
        self.box_1 = BoxLayout()
        self.box_2 = BoxLayout()
        self.temp = Label(text='', font_size=18)

    def btn_pressed(self, *args):
        self.label.color = (185 / 255, 4 / 255, 4 / 255, 1)

    def is_number(self, number):
        try:
            float(number)
            return True
        except ValueError:
            return False

    def on_text(self, *args):
        data_1 = self.input_1.text
        data_2 = self.input_2.text
        data_3 = self.input_3.text
        data_4 = self.input_4.text
        if self.is_number(data_1) and self.is_number(data_2) and self.is_number(data_3) and self.is_number(data_4):
            self.array = [[float(data_1), float(data_2)], [float(data_3), float(data_4)]]
            print(self.array)
            if not find_saddle_point(self.array):
                self.saddle_point.text = 'No Saddle Point'
                self.game_value.text = 'Game Value : ' + str(value_of_the_game(self.array))
                print(optimal_mixed_strategy_for_players(self.array))
                self.optimal_strategy.text = f'The optimal strategy for player A = {str(optimal_mixed_strategy_for_players(self.array)[0])}\n' \
                                             f'The optimal strategy for player B = {str(optimal_mixed_strategy_for_players(self.array)[1])}'
            else:
                self.saddle_point.text = 'The game contains Saddle Point'
                self.game_value.text = ''
                self.optimal_strategy.text = ''
        else:
            self.saddle_point.text = ''
            self.game_value.text = ''
            self.optimal_strategy.text = ''

    def build(self):
        box = BoxLayout(orientation='vertical')
        btn = Button(text='Press me')
        btn.bind(on_press=self.btn_pressed)
        self.box_1.add_widget(self.input_1)
        self.box_1.add_widget(self.input_2)
        self.box_2.add_widget(self.input_3)
        self.box_2.add_widget(self.input_4)
        box.add_widget(self.label)
        box.add_widget(self.box_1)
        box.add_widget(self.box_2)
        box.add_widget(self.saddle_point)
        box.add_widget(self.game_value)
        box.add_widget(self.optimal_strategy)
        box.add_widget(self.temp)

        return box


AnalyticalMethod().run()
