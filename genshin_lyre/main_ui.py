import tkinter


root = tkinter.Tk()
root.title("Genshin Lyre")
root.configure(background="#171717")

width, height = 600, 400

root.geometry(f"{width}x{height}+0+0")

button = tkinter.Button(root, anchor="nw")

root.mainloop()