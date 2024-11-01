import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Initialize display
        self.display_text = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Display
        display_frame = tk.Frame(self.root)
        display_frame.pack(expand=True, fill="both")
        
        display = tk.Entry(display_frame, textvariable=self.display_text, font=("Arial", 24), bd=10, relief="ridge", justify="right")
        display.pack(expand=True, fill="both")

        # Button layout
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        for row in buttons:
            button_frame = tk.Frame(self.root)
            button_frame.pack(expand=True, fill="both")
            for btn_text in row:
                button = tk.Button(button_frame, text=btn_text, font=("Arial", 18), bd=5, command=lambda x=btn_text: self.on_button_click(x))
                button.pack(side="left", expand=True, fill="both")

    def on_button_click(self, character):
        if character == "C":
            self.display_text.set("")
        elif character == "=":
            try:
                expression = self.display_text.get()
                result = str(eval(expression))
                self.display_text.set(result)
            except:
                self.display_text.set("Error")
        else:
            self.display_text.set(self.display_text.get() + character)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
