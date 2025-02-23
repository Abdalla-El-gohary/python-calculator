import tkinter as tk
from tkinter import messagebox, ttk
from base_series import LnSeries, ExpSeries, SinSeries, CosSeries
import math
import re

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
LIGHT_GREEN = '#d8ead8'
BLACK = '#20272b'
DISPLAY_FONT = ("Arial", 30)
BUTTONS_FONT = ("Arial", 14)

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("570x700")
        
        self.buttons = [
        ('SHIFT', 'ALPHA','↑','MODE', 'ON'),
        ( '←', '→' ),
        ( 'calc','∫dx', '↓', 'x⁻¹', 'logₙ'),
        ( '√', 'x²', '^', 'log', 'ln'), 
        ('(-)', 'Hyp', 'sin', 'cos', 'tan'),
        ('RCL', 'ENG', '(', ')', 'S⇔D'),
        ('7', '8', '9', 'DEL', 'AC'),
        ('4', '5', '6', '×', '÷'),
        ('1', '2', '3', '+', '-'),
        ('0', '.', '×10^x', 'Ans', '=')
        ]

        self.display_frame =self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        self.add_display_widgets()
        self.add_buttons_widgets()

        self.shift_active = False
        


    def create_display_frame(self):
        frame = tk.Frame(self.root, height=100, bg=LIGHT_GREEN)
        frame.pack(expand=False, fill="both")
        return frame
    def create_buttons_frame(self):
        frame = tk.Frame(self.root, bg=BLACK)
        frame.pack(expand=True, fill="both")
        return frame

    def add_display_widgets(self):
        self.input_text = tk.Text(self.display_frame, height=3, width=25, font=DISPLAY_FONT)
        self.input_text.pack(expand=True, fill="both")
    

    def show_hyp_menu(self):
        """Display a pop-up menu for selecting a hyperbolic function."""
        hyp_functions = ["sinh", "cosh", "tanh", "asinh", "acosh", "atanh"]

        def insert_hyp_function(hyp_func):
            """Insert the selected hyperbolic function into the input field."""
            self.input_text.insert(tk.END, f"{hyp_func}(")

        # Create a new window for selection
        hyp_window = tk.Toplevel(self.root)
        hyp_window.title("Select Hyperbolic Function")
        hyp_window.geometry("250x250")

        # Add buttons for each hyperbolic function
        for func in hyp_functions:
            btn = tk.Button(hyp_window, text=func, font=BUTTONS_FONT, command=lambda f=func: [insert_hyp_function(f), hyp_window.destroy()])
            btn.pack(fill="both", expand=True, padx=5, pady=5)


    def add_buttons_widgets(self):
    # Define button sizes dynamically based on the layout
        button_width = 6
        button_height = 2
        for i, row in enumerate(self.buttons):
            for j, button_text in enumerate(row):

                # Create button
                btn = tk.Button(
                    self.buttons_frame, text=button_text, font=BUTTONS_FONT,
                    height=button_height, width=button_width,
                    command=lambda b=button_text: self.on_button_click(b)
                )

                if button_text == '←':
                    btn.grid(row=i, column=1, padx=2, pady=2, sticky="nsew")  # Below '↑'
                elif button_text == '→':
                    btn.grid(row=i, column=3, padx=2, pady=2, sticky="nsew")  # Next to '←'
                else:
                    btn.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
            
        # Make rows and columns expand to fill space
        for i in range(len(self.buttons)):
            self.buttons_frame.rowconfigure(i, weight=1)
        for j in range(len(self.buttons[0])):  
            self.buttons_frame.columnconfigure(j, weight=1)

    def on_button_click(self, value):
        if value == "SHIFT":
            self.shift_active = not self.shift_active
        elif value == "AC":
            self.input_text.delete("1.0", tk.END)
        elif value == "DEL":
            current_text = self.input_text.get("1.0", tk.END)[:-2]
            self.input_text.delete("1.0", tk.END)
            self.input_text.insert("1.0", current_text)
        elif value in ["sin", "cos", "tan"]:
            if self.shift_active:
                self.input_text.insert(tk.END, f"a{value}(")
            else:
                self.input_text.insert(tk.END, f"{value}(")
        
        elif value == "x²":
            self.input_text.insert(tk.END, "^2")
        
        elif value == "log":
            self.input_text.insert(tk.END, "log(")
        elif value == "ln":
            self.input_text.insert(tk.END, "ln(")
        elif value == "Hyp":
            self.show_hyp_menu()
        elif value == "calc":
            pass # not implemented
        elif value == "=":
            self.calculate_result()
        elif value == "x⁻¹":
            self.input_text.insert(tk.END, "**-1")
        elif value == "∫dx":
            pass # not implemented
        elif value == "logₙ":
            self.input_text.insert(tk.END, "logₙ(")
        elif value == "RCL":
            pass # not implemented
        elif value == "ENG":
            pass # not implemented
        elif value == "S⇔D":
            pass # not implemented
        elif value == "Ans":
            pass # not implemented
        elif value == "×10^x":
            self.input_text.insert(tk.END, "*10**")
        else:
            self.input_text.insert(tk.END, value)

    def calculate_result(self):
        expression = self.input_text.get("1.0", tk.END)
        expression = expression.replace("×", "*").replace("÷", "/").replace("^", "**")
        expression = expression.replace("logₙ", "logn")
        expression = expression.replace("a", "math.")
        expression = expression.replace("sinh", "math.sinh").replace("cosh", "math.cosh").replace("tanh", "math.tanh")
        expression = expression.replace("asinh", "math.asinh").replace("acosh", "math.acosh").replace("atanh", "math.atanh")
        expression = expression.replace("logn", "math.log").replace("ln", "math.log")
        expression = expression.replace("sqrt", "math.sqrt")
        expression = expression.replace("π", "math.pi")
        expression = expression.replace("e", "math.e")
        try:
            result = eval(expression)
            self.input_text.delete("1.0", tk.END)
            self.input_text.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid expression: {e}")



if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()