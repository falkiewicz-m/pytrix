import tkinter as tk
import tkinter.ttk as ttk
from commands_pytrix import *
from ttk_styles import StylesDef

class Window:
    def __init__(self, master):
        self.master = master

        frame = ttk.Frame(self.master)
        style = ttk.Style()

        style = StylesDef.button_style()
        style = StylesDef.label_style()

        bttn = ttk.Button(frame, text="test", style="Custom.TButton", state="disabled")
        bttn.pack()

        label1 = ttk.Label(frame, text="text on label", style="Custom.TLabel")
        label1.pack()

        bttn2 = tk.Button(frame, text="second button with another style", fg="red", bg="white")
        bttn2.pack()
        frame.pack(padx = 200, pady = 10)

        notebook1 = ttk.Notebook(root, width="500", height="400")
        ntbframe1 = ttk.Frame(notebook1)
        ntbframe2 = ttk.Frame(notebook1)
        label2 = ttk.Label(ntbframe1, text="Label in notebook", style="Custom.TLabel")
        label2.pack()
        bttn3 = ttk.Button(ntbframe2, text="Print command", style="Custom.TButton", command=bttn3_click)
        bttn3.pack()
        ntbframe1.pack(expand="True")
        ntbframe2.pack(expand="True")

        notebook1.add(ntbframe1, text="First notebook tab")
        notebook1.add(ntbframe2, text="There is another")
        notebook1.pack(side = "right")



root = tk.Tk()
root.title("Tkinter experiments")
window = Window(root)
root.mainloop()


