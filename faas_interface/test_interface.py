from pyminitel.interface import Interface

class TestInterface(Interface):
    def __init__(self):
        super().__init__(background_path=r"C:\Users\cohel\Downloads\Minitel-To-K8s\faas_interface\asset\test.vdt")