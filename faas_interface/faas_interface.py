from pyminitel.minitelinterface import MinitelInterfaces
from faas_interface.test_interface import TestInterface
from pyminitel.menu import Menu

testInterface = TestInterface()
TestInterfaceMenu = Menu(["test1", "test2", "test3"], x=2, y=8, length=10, selected_index=0, bg_color=3, font_color=4)
testInterface.add_widget(TestInterfaceMenu)

class FaaSInterface(MinitelInterfaces):
    def __init__(self, connector):
        super().__init__(connector)
        self.debug = True
        self.interfaces = [
            testInterface
        ]