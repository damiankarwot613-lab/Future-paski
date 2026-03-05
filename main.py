import pandas as pd
from pathlib import Path

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout


class MainLayout(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.data = None
        self.filtered = None

        self.header = Label(
            text="Paski Future",
            size_hint=(1, 0.1),
            font_size=26
        )
        self.add_widget(self.header)

        self.load_button = Button(
            text="Wczytaj Excel",
            size_hint=(1, 0.1)
        )
        self.load_button.bind(on_press=self.load_excel)
        self.add_widget(self.load_button)

        self.search = TextInput(
            hint_text="Szukaj...",
            size_hint=(1, 0.1),
            multiline=False
        )
        self.search.bind(text=self.filter_data)
        self.add_widget(self.search)

        self.preview = Label(
            text="Brak danych",
            size_hint=(1, 0.1)
        )
        self.add_widget(self.preview)

        self.scroll = ScrollView(size_hint=(1, 0.6))

        self.grid = GridLayout(
            cols=1,
            size_hint_y=None
        )
        self.grid.bind(minimum_height=self.grid.setter("height"))

        self.scroll.add_widget(self.grid)
        self.add_widget(self.scroll)

    def load_excel(self, instance):

        try:

            path = Path("data/test.xlsx")

            if not path.exists():
                self.preview.text = "Brak pliku data/test.xlsx"
                return

            self.data = pd.read_excel(path)
            self.filtered = self.data.copy()

            self.preview.text = f"Wczytano {len(self.data)} rekordów"

            self.show_data()

        except Exception as e:
            self.preview.text = str(e)

    def filter_data(self, instance, text):

        if self.data is None:
            return

        if text == "":
            self.filtered = self.data.copy()
        else:
            mask = self.data.astype(str).apply(
                lambda row: row.str.contains(text, case=False).any(),
                axis=1
            )
            self.filtered = self.data[mask]

        self.show_data()

    def show_data(self):

        self.grid.clear_widgets()

        if self.filtered is None:
            return

        for _, row in self.filtered.head(100).iterrows():

            label = Label(
                text=str(row.to_dict()),
                size_hint_y=None,
                height=40
            )

            self.grid.add_widget(label)


class FutureApp(App):

    def build(self):
        return MainLayout()


if __name__ == "__main__":
    FutureApp().run()
