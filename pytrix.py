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

        bttn = ttk.Button(frame, text="test", style="Custom.TButton", state="focus")
        bttn.pack()

        frame.pack(padx = 5, pady = 5)

        bttn2 = tk.Button(text="second button with another style", fg="red", bg="white")
        bttn2.pack()

root = tk.Tk()
window = Window(root)
root.mainloop()
