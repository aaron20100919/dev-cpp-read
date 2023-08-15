from tkinter import *

root = Tk()
root.overrideredirect(True)

root.geometry("700x20")
root.geometry("+%d+%d" % (900, 840))
root.attributes("-topmost", True)

text_list = [
    "Welcome to Aaron's small dev c++ readers!!",
    "<;> or button Exit to exit;",
    "<,> or button Back to page up;",
    "<.> or button Forward to page down;",
    "</> or button Hid to say fuck to XC;",
    "You can change the current_index to turn that page;",
    "You can change the path.",
    "Enjoy reading",
]
with open("./xiaoshuo.txt", encoding="utf-8") as f:
    while True:
        txt = f.read(40)
        if not txt:
            break
        text_list.append(txt.split())

current_index = 0


def forward_text(event=None):
    global current_index
    current_index = (current_index - 1 + len(text_list)) % len(text_list)
    label.config(text=text_list[current_index])


def back_text(event=None):
    global current_index
    current_index = (current_index + 1) % len(text_list)
    label.config(text=text_list[current_index])


def exit_app(event=None):
    root.destroy()


def hid(event=None):
    if root.attributes("-alpha") == 1:
        root.attributes("-alpha", 0.05)
    else:
        root.attributes("-alpha", 1)


exit_button = Button(root, text="Exit", command=exit_app)
exit_button.pack(side=LEFT)

forward_button = Button(root, text="Forward", command=forward_text)
forward_button.pack(side=LEFT)

back_button = Button(root, text="Back", command=back_text)
back_button.pack(side=LEFT)

clear_button = Button(root, text="Hid", command=hid)
clear_button.pack(side=LEFT)

root.bind("<KeyPress-;>", exit_app)
root.bind("<KeyPress-,>", forward_text)
root.bind("<KeyPress-.>", back_text)
root.bind("<KeyPress-/>", hid)

label = Label(root, text=text_list[current_index])
label.pack(side=LEFT)

root.mainloop()
print(f"current_index = {current_index}")
