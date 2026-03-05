import os
import csv
from openpyxl import load_workbook, Workbook

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from plyer import filechooser


class UltraLayout(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=15, spacing=10, **kwargs)

        self.file_path = None
        self.folder = None
        self.headers = []
        self.rows = []
        self.checkboxes = []

        self.status = Label(text="ULTRA Exporter - wybierz plik")
        self.add_widget(self.status)

        btn_file = Button(text="Wczytaj plik XLS/XLSX/CSV", size_hint_y=None, height=80)
        btn_file.bind(on_press=self.load_file)
        self.add_widget(btn_file)

        btn_folder = Button(text="Wybierz folder zapisu", size_hint_y=None, height=80)
        btn_folder.bind(on_press=self.choose_folder)
        self.add_widget(btn_folder)

        self.scroll = ScrollView(size_hint=(1, 1))
        self.column_layout = GridLayout(cols=1, size_hint_y=None)
        self.column_layout.bind(minimum_height=self.column_layout.setter('height'))
        self.scroll.add_widget(self.column_layout)

        self.add_widget(self.scroll)

        btn_export = Button(text="EXPORT ULTRA", size_hint_y=None, height=90)
        btn_export.bind(on_press=self.export_files)
        self.add_widget(btn_export)

    def load_file(self, instance):

        file = filechooser.open_file(filters=["*.xlsx","*.xls","*.csv"])

        if not file:
            return

        self.file_path = file[0]

        ext = self.file_path.split(".")[-1].lower()

        if ext == "csv":
            self.load_csv()
        else:
            self.load_excel()

        self.show_columns()

    def load_excel(self):

        wb = load_workbook(self.file_path)
        ws = wb.active

        data = list(ws.values)

        self.headers = list(data[0])
        self.rows = list(data[1:])

        self.status.text = f"Wczytano {len(self.rows)} rekordów"

    def load_csv(self):

        with open(self.file_path, newline="", encoding="utf-8") as f:

            reader = list(csv.reader(f))

            self.headers = reader[0]
            self.rows = reader[1:]

        self.status.text = f"Wczytano {len(self.rows)} rekordów"

    def show_columns(self):

        self.column_layout.clear_widgets()
        self.checkboxes = []

        for col in self.headers:

            btn = ToggleButton(text=col, size_hint_y=None, height=80)

            btn.state = "down"

            self.column_layout.add_widget(btn)
            self.checkboxes.append(btn)

    def choose_folder(self, instance):

        folder = filechooser.choose_dir()

        if folder:
            self.folder = folder[0]
            self.status.text = f"Folder: {self.folder}"

    def export_files(self, instance):

        if not self.folder:
            self.status.text = "Najpierw wybierz folder"
            return

        selected_indexes = []

        for i,btn in enumerate(self.checkboxes):

            if btn.state == "down":
                selected_indexes.append(i)

        if not selected_indexes:
            self.status.text = "Wybierz kolumny"
            return

        headers = [self.headers[i] for i in selected_indexes]

        count = 0

        for row in self.rows:

            imie = str(row[0])
            nazwisko = str(row[1])

            filename = f"{imie}_{nazwisko}.xlsx"

            path = os.path.join(self.folder, filename)

            wb = Workbook()
            ws = wb.active

            ws.append(headers)

            data = [row[i] for i in selected_indexes]

            ws.append(data)

            wb.save(path)

            count += 1

        self.status.text = f"Wyeksportowano {count} plików"


class UltraApp(App):
    def build(self):
        return UltraLayout()


UltraApp().run()
