'''from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.button import MDFloatingActionButton,MDFloatingActionButtonSpeedDial
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
import mysql.connector
from kivymd.uix.datatables import MDDataTable
import re
from kivy.uix.anchorlayout import AnchorLayout
from kivy.metrics import dp
from kivy.properties import ListProperty, StringProperty , BooleanProperty
from kivy.uix.screenmanager import (ScreenManager, Screen, NoTransition,
SlideTransition, CardTransition, SwapTransition,
FadeTransition, WipeTransition, FallOutTransition, RiseInTransition)


class ShowexpenseScreen(Screen):
    con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pas"
        )
    d = con.cursor()
    def load_table(self):
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            pos_hint={'center_y': 0.5, 'center_x': 0.5},
            size_hint=(0.8, 0.9),
            padding=50,
            use_pagination=True,
            check=True,
            rows_num=8,
            elevation=20,
            background_color_header="#65275d",
            background_color_selected_cell="e4514f",
            column_data=[
                ("expense id", dp(30)),
                ("source", dp(30)),
                ("date", dp(30)),
                ("amount", dp(30)),
                 ],
             )
        for x in r:
            self.data_tables.add_row(x)
        self.add_widget(self.data_tables)
        self.add_widget(self.button_box)
        return layout
        self.d.close()
        self.con.close()

    def on_enter(self):
        query = "select * from expenseinfo"
        self.d.execute(query)
        self.r = self.d.fetchall()
        self.load_table()
       '''
         