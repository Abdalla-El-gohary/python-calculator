import tkinter as tk
from tkinter import messagebox, ttk
from base_series import LnSeries, ExpSeries, SinSeries, CosSeries, TanSeries, SinhSeries, CoshSeries, TanhSeries, LognSeries
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
        self.root.resizable(False, False)

        self.shift_active = False
        self.equal_pressed = False
        self.history_enabled = False

        self.history = []
        self.history_result = []
        self.history_index = 0


        self.mapping_dict = {
            'π': math.pi,
            'Ans': self.history_result[-1] if self.history_result else 0,
            'e': 'e'
        }
        
        self.buttons = [
        ('SHIFT', 'ALPHA','↑','MODE', 'ON'),
        ( '←', '→' , 'e^'),
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
        self.input_text.focus_set()  # Ensures the cursor is visible


        self.result_text = tk.Text(self.display_frame, height=1, width=25, font=DISPLAY_FONT)
        self.result_text.pack(expand=True, fill="both")
    

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
                elif button_text == 'e^':
                    btn.grid(row=i, column=4, padx=2, pady=2, sticky="nsew")
                else:
                    btn.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
            
        # Make rows and columns expand to fill space
        for i in range(len(self.buttons)):
            self.buttons_frame.rowconfigure(i, weight=1)
        for j in range(len(self.buttons[0])):  
            self.buttons_frame.columnconfigure(j, weight=1)

    def on_button_click(self, value):
        if not value in ["↑", "↓"]:
            self.history_enabled = False  # Disable history navigation if a new input is made or use right/left arrow keys

        # Arrows:
        if value in ["↑", "↓", "←", "→"]:
            self.handle_arrow_keys(value)
        
        # buttons with special functions
        elif value == "SHIFT":
            self.shift_active = not self.shift_active
        elif value == "AC":
            self.input_text.delete("1.0", tk.END)
            self.result_text.delete("1.0", tk.END)
            self.history_enabled = True
        elif value == "DEL":
            # Delete the character before the cursor
            self.input_text.delete("insert -1 chars")
            self.result_text.delete("1.0", tk.END)
        elif value == "=":
            self.equal_pressed = True
            self.calculate_result()

        else:
            if self.equal_pressed:  # Clear the input field if a new input is made after pressing '='
                self.input_text.delete("1.0", tk.END)
                self.result_text.delete("1.0", tk.END)
                self.equal_pressed = False
            if value == "Ans":
                if self.history_result:
                    self.input_text.insert(tk.INSERT, str("Ans"))
                else:
                    messagebox.showerror("Error", "No previous result to use as 'Ans'")

            elif value in ["sin", "cos", "tan"]:
                if self.shift_active:
                    self.input_text.insert(tk.INSERT, f"a{value}(")
                else:
                    self.input_text.insert(tk.INSERT, f"{value}(")

            # buttons with special characters
            elif value == "x²":
                self.input_text.insert(tk.INSERT, "^2")
            elif value == "log":
                self.input_text.insert(tk.INSERT, "log(")
            elif value == "ln":
                self.input_text.insert(tk.INSERT, "ln(")
            elif value == "Hyp":
                self.show_hyp_menu()
            elif value == "√":
                self.input_text.insert(tk.INSERT, " ")
                self.input_text.mark_set(tk.INSERT, "insert -1 chars") 
                self.input_text.insert(tk.INSERT, "√")
            elif value == "x⁻¹":
                self.input_text.insert(tk.INSERT, "^-1")
            elif value == "logₙ":
                self.input_text.insert(tk.INSERT, "logₙ(")
                self.input_text.mark_set(tk.INSERT, "insert -1 chars") 
            elif value == "(-)":
                self.input_text.insert(tk.INSERT, "-")


            # Not implemented buttons
            elif value in ["∫dx", "RCL", "ENG", "S⇔D", "MODE", "ON", "calc"]:
                pass # not implemented
            else:
                self.input_text.insert(tk.INSERT, value)

    def handle_arrow_keys(self, value):
        if value == "↑":
            if (self.history_index > 0) and self.history_enabled:
                print(self.history_index)
                self.history_index -= 1
                self.input_text.delete("1.0", tk.END)
                self.input_text.insert(tk.END, self.history[self.history_index])
                self.result_text.delete("1.0", tk.END)
                self.result_text.insert(tk.END, self.history_result[self.history_index])
                self.input_text.mark_set(tk.INSERT, "insert -1 chars")
            else:
                pass
        elif value == "↓":
            if (self.history_index < len(self.history) - 1) and self.history_enabled:
                print(self.history_index)
                self.history_index += 1
                self.input_text.delete("1.0", tk.END)
                self.input_text.insert(tk.END, self.history[self.history_index]) 
                self.result_text.delete("1.0", tk.END)
                self.result_text.insert(tk.END, self.history_result[self.history_index])
                self.input_text.mark_set(tk.INSERT, "insert -1 chars")
        elif value == "←":
            self.equal_pressed = False
            self.input_text.mark_set(tk.INSERT, "insert -1 chars")
            self.result_text.delete("1.0", tk.END)
        elif value == "→":
            self.equal_pressed = False
            self.input_text.mark_set(tk.INSERT, "insert +1 chars")
            self.result_text.delete("1.0", tk.END)

    def calculate_result(self):
        
        
        input_text = self.get_input_text()
        postfix = self.infix_to_postfix(input_text)

        try:
            result = self.evaluate_postfix(postfix)

            self.history.append(self.input_text.get("1.0", tk.END))
            self.history_result.append(result)
            self.history_index = len(self.history) -1
            self.history_enabled = True

            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, result)
            
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def get_input_text(self):  # Convert the input text to a format that can be evaluated
        input_text = self.input_text.get("1.0", tk.END)
        input_text = input_text.replace("×", "*").replace("÷", "/").replace("--", "+")

        if "Ans" in input_text:
            ans = str(self.history_result[-1] if self.history_result else 0)
            input_text = input_text.replace("Ans", ans)

        if "√" in input_text:
            # find whitespace after √
            index = input_text.find("√")
            whitespace = input_text.find(" ", index)
            if whitespace == -1:
                print("no whitespace")
            else:
                # replace √ with ()^0.5
                input_text = input_text[:index] + "(" + input_text[index+1:whitespace] + ")" + "^0.5" +   input_text[whitespace+1:]
        
        if "-" in input_text:
            i = 1
            while i < len(input_text):
                if input_text[i] == "-" and input_text[i-1]  not in ["+", "-", "*", "/", "(", "^"] and  input_text[i+1].isnumeric():  # Check if the '-' is a negative sign
                    input_text = input_text[:i] + "+" + input_text[i:]
                    i += 1
                i += 1
        
        match = re.search(r"log(\d+)\(", input_text)
        if match:
            self.base_log = match.group(1)
            input_text = input_text.replace(f"log{self.base_log}(", "lon(")

        # input_text = re.sub(r"log(\d+)\((\d+)\)", r"ln(\2)/ln(\1)", input_text) # Convert logₙ(x) to ln(x)/ln(ₙ)
        # input_text = re.sub(r"log\((\d+)\)", r"ln(\1)/ln(10)", input_text) # Convert log(x) to ln(x)/ln(10)

        return input_text

    def infix_to_postfix(self, expression):
        precedence = {
            'lon': 3, # log with base n
            'log': 3,
            'ln': 3,
            'sin': 3,
            'cos': 3,
            'tan': 3,
            'asin': 3,
            'acos': 3,
            'atan': 3,
            'sinh': 3,
            'cosh': 3,
            'tanh': 3,
            'asinh': 3,
            'acosh': 3,
            'atanh': 3,
            '^': 3,
            '*': 2,
            '/': 2,
            '+': 1,
            '-': 1,
            '(': 0,
            ')': 0
        }
        stack = []
        postfix = []
        

        tokens = re.findall(r"[\d.]+|[-\d.]+|[A-Za-z]+|\S", expression) # Tokenize the expression
        
        print(tokens)
        for token in tokens:
            if token.replace("-", "", 1).replace(".", "", 1).isnumeric():
                postfix.append(token)
            elif  token in ['π', 'e']:  # numerical constants
                postfix.append(self.mapping_dict[token])
                print(self.mapping_dict[token])
            elif token in precedence:
                if token == '(':
                    stack.append(token)
                elif token == ')':
                    while stack and stack[-1] != '(':
                        postfix.append(stack.pop())
                    stack.pop()
                else:
                    while stack and precedence[stack[-1]] >= precedence[token]:
                        print(precedence[stack[-1]], precedence[token])
                        postfix.append(stack.pop())
                    stack.append(token)
            else:
                postfix.append(token)
        while stack:
            postfix.append(stack.pop())
        print(postfix)
        return postfix

    def evaluate_postfix(self, postfix):
        stack = []
        for token in postfix:
            if token.replace("-", "", 1).replace(".", "", 1).isnumeric():
                stack.append(float(token))
            elif token == 'e':
                stack.append('e')
            elif token in ['sin', 'cos', 'tan', 'log', 'ln', 'lon', 'sinh', 'cosh', 'tanh', 'asin', 'acos', 'atan', 'asinh', 'acosh', 'atanh']:
                arg = stack.pop()
                if token == 'sin':
                    sin_series = SinSeries()
                    stack.append(sin_series.calculate(math.radians(arg)))
                elif token == 'cos':
                    cos_series = CosSeries()
                    stack.append(cos_series.calculate(math.radians(arg)))
                elif token == 'tan':
                    tan_series = TanSeries()
                    stack.append(tan_series.calculate(math.radians(arg)))
                
                elif token == 'sinh':
                    sinh_series = SinhSeries()
                    stack.append(sinh_series.calculate(arg))
                elif token == 'cosh':
                    cosh_series = CoshSeries()
                    stack.append(cosh_series.calculate(arg))
                elif token == 'tanh':
                    tanh_series = TanhSeries()
                    stack.append(tanh_series.calculate(arg))
                elif token == 'asin':
                    stack.append(math.asin(arg))
                elif token == 'acos':
                    stack.append(math.acos(arg))
                elif token == 'atan':
                    stack.append(math.atan(arg))
                elif token == 'asinh':
                    stack.append(math.asinh(arg))
                elif token == 'acosh':
                    stack.append(math.acosh(arg))
                elif token == 'atanh':
                    stack.append(math.atanh(arg))

                elif token == 'ln':
                    ln_series = LnSeries()
                    stack.append(ln_series.calculate(arg))
                
                elif token == 'log':
                    log_series = LognSeries()
                    stack.append(log_series.calculate(arg, 10))
                elif token == 'lon':
                    print(self.base_log)
                    logn_series = LognSeries()
                    stack.append(logn_series.calculate(arg, float(self.base_log)))

                

                
            
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(a / b)
                elif token == '^':
                    if a == 'e':
                        myex = ExpSeries()
                        stack.append(myex.calculate(x=b))
                    else:
                        stack.append(a ** b)
        return stack[0]

        
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()