import json
from pathlib import Path

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen


APP_TITLE = "Paski Future Stable"


class PaskiApp(App):

    def build(self):

        self.full_data = []

        self.sm = ScreenManager()

        self.home_screen = Screen(name="home")
        self.table_screen = Screen(name="table")

        self.build_home()
        self.build_table()

        self.sm.add_widget(self.home_screen)
        self.sm.add_widget(self.table_screen)

        self.sm.current = "home"

        return self.sm


# ---------------- HOME ----------------

    def build_home(self):

        layout = BoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(10)
        )

        title = Label(
            text=APP_TITLE,
            size_hint_y=None,
            height=dp(50)
        )

        btn = Button(
            text="Test danych",
            size_hint_y=None,
            height=dp(60)
        )

        btn.bind(on_press=self.load_test_data)

        self.info = Label(
            text="Aplikacja uruchomiona",
            halign="center"
        )

        layout.add_widget(title)
        layout.add_widget(btn)
        layout.add_widget(self.info)

        self.home_screen.add_widget(layout)


# ---------------- TABLE ----------------

    def build_table(self):

        root = BoxLayout(orientation="vertical")

        back = Button(
            text="Powrót",
            size_hint_y=None,
            height=dp(60)
        )

        back.bind(on_press=self.go_home)

        self.grid = GridLayout(
            cols=5,
            spacing=dp(5),
            size_hint_y=None
        )

        self.grid.bind(minimum_height=self.grid.setter("height"))

        scroll = ScrollView()
        scroll.add_widget(self.grid)

        root.add_widget(back)
        root.add_widget(scroll)

        self.table_screen.add_widget(root)


# ---------------- DATA ----------------

    def load_test_data(self, instance):

        self.full_data = []

        for i in range(30):

            row = [
                f"ID{i}",
                f"Produkt{i}",
                f"{i*3}",
                f"{i*2}",
                f"{i*10}"
            ]

            self.full_data.append(row)

        self.info.text = f"Wczytano {len(self.full_data)} rekordów"

        self.display_table()

        self.sm.current = "table"


# ---------------- TABLE VIEW ----------------

    def display_table(self):

        self.grid.clear_widgets()

        headers = ["ID", "Produkt", "Stan", "Sprzedaż", "Cena"]

        for h in headers:

            self.grid.add_widget(Label(
                text=h,
                size_hint_y=None,
                height=dp(40)
            ))

        for row in self.full_data:

            for cell in row:

                self.grid.add_widget(Label(
                    text=str(cell),
                    size_hint_y=None,
                    height=dp(35)
                ))


# ---------------- NAV ----------------

    def go_home(self, instance):

        self.sm.current = "home"


if __name__ == "__main__":
    PaskiApp().run()
