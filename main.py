import os
import pandas as pd

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox

from plyer import filechooser


class MainLayout(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.df = None
        self.selected_columns = []

        self.info = Label(text="Excel Exporter ULTRA PRO")
        self.add_widget(self.info)

        btn_load = Button(text="Load Excel")
        btn_load.bind(on_press=self.load_excel)
        self.add_widget(btn_load)

        self.columns_layout = GridLayout(cols=1, size_hint_y=None)
        self.columns_layout.bind(minimum_height=self.columns_layout.setter("height"))

        scroll = ScrollView(size_hint=(1, .4))
        scroll.add_widget(self.columns_layout)

        self.add_widget(scroll)

        btn_export = Button(text="Export")
        btn_export.bind(on_press=self.export_rows)
        self.add_widget(btn_export)

        self.progress = ProgressBar(max=100)
        self.add_widget(self.progress)

    def load_excel(self, instance):

        filechooser.open_file(
            on_selection=self.file_selected,
            filters=["*.xls", "*.xlsx"]
        )

    def file_selected(self, selection):

        if not selection:
            return

        path = selection[0]

        try:

            self.df = pd.read_excel(path)

            self.info.text = f"Loaded {len(self.df)} rows"

            self.build_column_selector()

        except Exception as e:
            self.info.text = str(e)

    def build_column_selector(self):

        self.columns_layout.clear_widgets()
        self.selected_columns.clear()

        for col in self.df.columns:

            row = BoxLayout(size_hint_y=None, height=40)

            cb = CheckBox()
            cb.bind(active=self.on_checkbox)

            label = Label(text=str(col))

            row.add_widget(cb)
            row.add_widget(label)

            self.columns_layout.add_widget(row)

    def on_checkbox(self, checkbox, value):

        label = checkbox.parent.children[0].text

        if value:
            self.selected_columns.append(label)
        else:
            if label in self.selected_columns:
                self.selected_columns.remove(label)

    def export_rows(self, instance):

        if self.df is None:
            self.info.text = "Load file first"
            return

        if not self.selected_columns:
            self.selected_columns = list(self.df.columns)

        Clock.schedule_once(lambda dt: self.run_export())

    def run_export(self):

        output_dir = os.path.expanduser("~/Documents")

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        total = len(self.df)

        for i, row in self.df.iterrows():

            data = row[self.selected_columns]

            df_row = pd.DataFrame([data])

            try:

                name = str(row.get("Imię", "row"))
                surname = str(row.get("Nazwisko", i))

                filename = f"{name}_{surname}.xlsx"

            except:
                filename = f"row_{i}.xlsx"

            path = os.path.join(output_dir, filename)

            df_row.to_excel(path, index=False)

            progress = int((i + 1) / total * 100)
            self.progress.value = progress

        self.info.text = f"Exported {total} files"


class ExcelApp(App):

    def build(self):

        layout = MainLayout()

        Clock.schedule_once(lambda dt: print("App started"), 1)

        return layout


ExcelApp().run()
