import json
from pathlib import Path
import pandas as pd

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup


APP_TITLE = "Paski Future"


class Home(Screen):
    pass


class Table(Screen):
    pass


class PaskiApp(App):

    def build(self):

        self.data = None
        self.filtered = None
        self.export_folder = None

        self.sm = ScreenManager()

        self.home = Home(name="home")
        self.table = Table(name="table")

        self.sm.add_widget(self.home)
        self.sm.add_widget(self.table)

        self.build_home()
        self.build_table()

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

        btn_excel = Button(text="Wybierz plik Excel")
        btn_load = Button(text="Wczytaj dane")
        btn_table = Button(text="Pokaż tabelę")

        btn_excel.bind(on_press=self.select_excel)
        btn_load.bind(on_press=self.load_excel)
        btn_table.bind(on_press=lambda x: self.show_table())

        self.preview = Label(text="Brak danych")

        layout.add_widget(title)
        layout.add_widget(btn_excel)
        layout.add_widget(btn_load)
        layout.add_widget(btn_table)
        layout.add_widget(self.preview)

        self.home.add_widget(layout)

# ---------------- TABLE ----------------

    def build_table(self):

        root = BoxLayout(orientation="vertical")

        self.search = TextInput(
            hint_text="Filtruj...",
            size_hint_y=None,
            height=dp(50)
        )

        self.search.bind(text=self.filter_data)

        back = Button(
            text="Powrót",
            size_hint_y=None,
            height=dp(50)
        )

        back.bind(on_press=lambda x: self.go_home())

        export = Button(
            text="Eksport CSV",
            size_hint_y=None,
            height=dp(50)
        )

        export.bind(on_press=self.export_csv)

        self.grid = GridLayout(
            cols=5,
            spacing=dp(5),
            size_hint_y=None
        )

        self.grid.bind(minimum_height=self.grid.setter("height"))

        scroll = ScrollView()
        scroll.add_widget(self.grid)

        root.add_widget(self.search)
        root.add_widget(export)
        root.add_widget(back)
        root.add_widget(scroll)

        self.table.add_widget(root)

# ---------------- DATA ----------------

    def select_excel(self, instance):

        popup = Popup(
            title="Info",
            content=Label(text="Picker pliku do dodania później"),
            size_hint=(0.8,0.4)
        )

        popup.open()

    def load_excel(self, instance):

        try:

            path = "data/test.xlsx"

            self.data = pd.read_excel(path)

            self.filtered = self.data.copy()

            self.preview.text = f"Wczytano {len(self.data)} rekordów"

        except Exception as e:

            self.preview.text = str(e)

# ---------------- FILTER ----------------

    def filter_data(self, instance, text):

        if self.data is None:
            return

        df = self.data

        mask = df.apply(
            lambda row: row.astype(str).str.contains(text, case=False).any(),
            axis=1
        )

        self.filtered = df[mask]

        self.display_table()

# ---------------- TABLE VIEW ----------------

    def show_table(self):

        if self.filtered is None:
            return

        self.display_table()

        self.sm.current = "table"


    def display_table(self):

        self.grid.clear_widgets()

        df = self.filtered

        if df is None:
            return

        self.grid.cols = len(df.columns)

        for c in df.columns:

            self.grid.add_widget(Label(
                text=str(c),
                size_hint_y=None,
                height=dp(40)
            ))

        for row in df.values:

            for cell in row:

                self.grid.add_widget(Label(
                    text=str(cell),
                    size_hint_y=None,
                    height=dp(35)
                ))

# ---------------- EXPORT ----------------

    def export_csv(self, instance):

        if self.filtered is None:
            return

        try:

            path = "export.csv"

            self.filtered.to_csv(path,index=False)

            self.popup("Eksport", "Zapisano export.csv")

        except Exception as e:

            self.popup("Błąd", str(e))


# ---------------- NAV ----------------

    def go_home(self):

        self.sm.current = "home"


# ---------------- POPUP ----------------

    def popup(self,title,text):

        p = Popup(
            title=title,
            content=Label(text=text),
            size_hint=(0.8,0.4)
        )

        p.open()


if __name__ == "__main__":
    PaskiApp().run()
