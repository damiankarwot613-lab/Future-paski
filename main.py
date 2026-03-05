import json
import threading
from pathlib import Path

from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView

APP_TITLE = "Paski Future Stable"
PREVIEW_ROWS = 5


class Home(Screen):
    pass


class Table(Screen):
    pass


class PaskiApp(App):

    def build(self):

        self.full_data = []
        self.filtered_data = []
        self.current_file = None
        self.export_tree_uri = None

        self.config_path = Path(self.user_data_dir) / "config.json"

        self.sm = ScreenManager()

        self.home = Home(name="home")
        self.table = Table(name="table")

        self.sm.add_widget(self.home)
        self.sm.add_widget(self.table)

        # opóźnienie startu (ważne dla Androida)
        Clock.schedule_once(self.finish_init, 1)

        return self.sm

    def finish_init(self, dt):

        self.load_config()
        self.build_home()
        self.build_table()

        self.sm.current = "home"

    # ---------------- CONFIG ----------------

    def load_config(self):

        if self.config_path.exists():

            try:
                with open(self.config_path, "r") as f:
                    data = json.load(f)
                    self.export_tree_uri = data.get("export_tree_uri")
            except:
                pass

    def save_config(self):

        try:
            with open(self.config_path, "w") as f:
                json.dump({"export_tree_uri": self.export_tree_uri}, f)
        except:
            pass

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
            height=dp(40)
        )

        btn_preview = Button(
            text="Test danych"
        )

        btn_preview.bind(on_press=self.fake_load)

        self.preview_label = Label(
            text="Brak danych",
            halign="left",
            valign="top"
        )

        layout.add_widget(title)
        layout.add_widget(btn_preview)
        layout.add_widget(self.preview_label)

        self.home.add_widget(layout)

    # ---------------- TABLE ----------------

    def build_table(self):

        layout = BoxLayout(orientation="vertical")

        btn_back = Button(
            text="Powrót",
            size_hint_y=None,
            height=dp(50)
        )

        btn_back.bind(on_press=lambda x: self.go_home())

        self.table_grid = GridLayout(
            cols=5,
            spacing=dp(5),
            size_hint_y=None
        )

        self.table_grid.bind(
            minimum_height=self.table_grid.setter('height')
        )

        scroll = ScrollView()
        scroll.add_widget(self.table_grid)

        layout.add_widget(btn_back)
        layout.add_widget(scroll)

        self.table.add_widget(layout)

    # ---------------- NAVIGATION ----------------

    def go_home(self):

        self.sm.current = "home"

    def go_table(self):

        self.sm.current = "table"

    # ---------------- TEST DATA ----------------

    def fake_load(self, instance):

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

        self.preview_label.text = f"Wczytano {len(self.full_data)} rekordów"

        self.display_table()

        self.go_table()

    # ---------------- TABLE DISPLAY ----------------

    def display_table(self):

        self.table_grid.clear_widgets()

        headers = ["ID", "Produkt", "Stan", "Sprzedaż", "Cena"]

        for h in headers:

            self.table_grid.add_widget(Label(
                text=h,
                size_hint_y=None,
                height=dp(40)
            ))

        for row in self.full_data:

            for cell in row:

                self.table_grid.add_widget(Label(
                    text=str(cell),
                    size_hint_y=None,
                    height=dp(35)
                ))

    # ---------------- POPUP ----------------

    def popup(self, title, text):

        box = BoxLayout(orientation="vertical")

        label = Label(text=text)

        btn = Button(text="OK", size_hint_y=None, height=dp(40))

        box.add_widget(label)
        box.add_widget(btn)

        popup = Popup(
            title=title,
            content=box,
            size_hint=(0.8, 0.4)
        )

        btn.bind(on_press=popup.dismiss)

        popup.open()


if __name__ == "__main__":
    PaskiApp().run()
