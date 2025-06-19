from pyminitel.interface import Interface
from config.settings import exec_path
import os

class MainInterface(Interface):
    def __init__(self):
        super().__init__(background_path=os.path.join(exec_path,"faas_interface","asset","main_background.vdt"))