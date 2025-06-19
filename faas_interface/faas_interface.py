from pyminitel.minitelinterface import MinitelInterfaces
from faas_interface.main_interface import MainInterface
from pyminitel.menu import Menu

FaaSInterface = MinitelInterfaces()

mainInterface = MainInterface()

FaaSInterface.add_interface(mainInterface)

mainInterfaceMenu = Menu(
    options=[
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

"""
class FaaSInterface(MinitelInterfaces):
    def __init__(self, connector):
        super().__init__(connector)
        self.debug = True
        self.interfaces = [
            testInterface
        ]"""