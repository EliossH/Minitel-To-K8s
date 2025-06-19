from pyminitel.widget import Widget
from pyminitel.menu import Menu
from pyminitel.text import Text
from config.settings import exec_path
from pyminitel.utils import format_string
from api.api import get_functions_list, get_function_detail, get_function_status
import os

class InternalFunctionMenu(Menu):
    def change_selection(self, dx):
        super().change_selection(dx)
        self.parent.update_text()

class FunctionMenu(Widget):
    def render(self):
        self.widgets =[]
        self.function_data = self.get_functions_data()
        print(self.function_data)

        self.menu = InternalFunctionMenu(
            options=[
                {
                    "text":data['name'],
                    "callback":lambda:print("No callback")
                }
                for data in self.function_data
            ],
            x=2,
            y=12,
            length=10,
            selected_index=0,
            bg_color=3,
            font_color=4
        )
        self.add_widget(self.menu)

        self.text_status = Text(format_string(self.function_data[self.widgets[0].selected_index]["status"], 30, fill=True), x=10, y=9, font_color=3, bg_color=4)
        self.text_url = Text(format_string(self.function_data[self.widgets[0].selected_index]["url"], 33, fill=True), x=7, y=10, font_color=3, bg_color=4)
        self.add_widget(self.text_status)
        self.add_widget(self.text_url)

        return super().render()
    
    def get_functions_data(self):
        function_list=get_functions_list()
        function_data = [
            {
                "name":name,
                "url":get_function_detail(name)["url"],
                "status":get_function_status(name)["etat"]
            }
            for name in function_list
        ]
        return function_data

    def update_text(self):
        self.text_status.text=format_string(self.function_data[self.menu.selected_index]["status"], 30, fill=True)
        self.text_url.text=format_string(self.function_data[self.menu.selected_index]["url"], 33, fill=True)
        self.update(self.text_status.render()+self.text_url.render())