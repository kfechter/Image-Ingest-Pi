import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class DisplayApp():
    def __init__(self):
        self.root = ttk.Window(themename="superhero")
        self.root.attributes('-fullscreen', True)

        self.root.mainloop()