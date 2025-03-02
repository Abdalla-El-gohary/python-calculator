#!/usr/bin/env python3

import tkinter as tk
from gui import CalculatorApp
from postifix_calculation import Postfix

if __name__ == "__main__":
    root = tk.Tk()
    postfix  = Postfix()
    app = CalculatorApp(root, postfix)
    root.mainloop()