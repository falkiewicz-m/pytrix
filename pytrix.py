import tkinter as tk
import tkinter.ttk as ttk

class Window:
    def __init__(self, master):
        self.master = master

        frame = ttk.Frame(self.master)

        style = ttk.Style()
        style.configure("Custom.TButton",
                         foreground="black",
                         background="white",
                         padding=[10, 10, 10, 10],
                         font="Verdana 12 underline")

        bttn = ttk.Button(frame, text="test", style="Custom.TButton", state="disabled")
        bttn.pack()

        frame.pack(padx = 5, pady = 5)

        style.configure("Custom.TLabel",
        				foreground="magenta",
        				background="yellow",
        				padding=[10, 10, 10,10],
        				font="Helvetica 15")
        label1 = ttk.Label(frame, text="text on label", style="Custom.TLabel")
        label1.pack()
        frame.pack(padx = 200, pady = 10)

        bttn2 = tk.Button(text="second button with another style", fg="red", bg="white")
        bttn2.pack()

        notebook1 = ttk.Notebook(root, width="500", height="400")
        ntbframe1 = ttk.Frame(notebook1)
        ntbframe2 = ttk.Frame(notebook1)
        label2 = ttk.Label(ntbframe1, text="Label in notebook", style="Custom.TLabel")
        label2.pack()
        ntbframe1.pack(expand="True")
        ntbframe2.pack(expand="True")

        notebook1.add(ntbframe1, text="First notebook tab")
        notebook1.add(ntbframe2, text="There is another")
        notebook1.pack(side = "right")



root = tk.Tk()
root.title("Tkinter experiments")
window = Window(root)
root.mainloop()
