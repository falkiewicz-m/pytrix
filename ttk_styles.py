import tkinter.ttk as ttk

style = ttk.Style()

class StylesDef(object):
	def button_style():
		style.configure("Custom.TButton",
                    	foreground="black",
                    	background="white",
                    	padding=[10, 10, 10, 10],
                    	font="Verdana 12 underline")
		return style

	def label_style():
		style.configure("Custom.TLabel",
        				foreground="magenta",
        				background="yellow",
        				padding=[10, 10, 10,10],
        				font="Helvetica 15")
		return style