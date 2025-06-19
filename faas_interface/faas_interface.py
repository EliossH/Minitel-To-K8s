from pyminitel.minitelinterface import MinitelInterfaces
from pyminitel.interface import Interface
from pyminitel.menu import Menu
from faas_interface.function_menu import FunctionMenu
from config.settings import exec_path
import os

FaaSInterface = MinitelInterfaces()

mainInterface = Interface(background_path=os.path.join(exec_path,"faas_interface","asset","main_background.vdt"))
functionListInterface = Interface(background_path=os.path.join(exec_path,"faas_interface","asset","function_list.vdt"))

FaaSInterface.add_interface(mainInterface, main=True)
FaaSInterface.add_interface(functionListInterface)

mainInterfaceMenu = Menu(
    options=[
        {"text":"Liste des fonctions","callback":lambda:FaaSInterface.set_active(functionListInterface)},
        {"text":"test1","callback":lambda:print("test1")},
        {"text":"test2","callback":lambda:print("test2")},
        {"text":"test3","callback":lambda:print("test3")}
    ],
    x=2,
    y=8,
    length=10,
    selected_index=0,
    bg_color=3,
    font_color=4
)
mainInterface.add_widget(mainInterfaceMenu)

functionMenu = FunctionMenu()
functionListInterface.add_widget(functionMenu)

"""
class FaaSInterface(MinitelInterfaces):
    def __init__(self, connector):
        super().__init__(connector)
        self.debug = True
        self.interfaces = [
            testInterface
        ]"""