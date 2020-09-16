import pyperclip
from tkinter import *


# , sys,os

def array_to_string(array, printed_string=""):
    for thing in array:
        printed_string += thing
    return printed_string


def make_array(message, width=12, height=19, spaces=2):
    def array_to_string_add_spaces_make_all_equal_length(array, printed_string="", spaces=2, width=12):
        # VVVV makes a string with a certain amount of spaces based on the value of space
        spaces = "".join(" " for x in range(spaces))

        # VVVV  turns each string in the array into a list
        array_with_strings_to_arrays = [list(string) for string in array if len(string) > 0]

        # VVVV  adds a space to each of the letters, the amount of spaces is determined my space
        array_with_strings_to_arrays_and_spaces = \
            [[letter + spaces for letter in mini_array] for mini_array in array_with_strings_to_arrays]

        # VVVV turns the message into a consistant width
        for line in array_with_strings_to_arrays_and_spaces:
            while len(line) < width:
                line += [spaces + " "]
            line += ["\n"]

        array_with_strings_to_arrays_and_spaces=[array_to_string(line) for line in array_with_strings_to_arrays_and_spaces if len(line)>0]

        global copied_message
        copied_message=""
        for line in array_with_strings_to_arrays_and_spaces:
            copied_message+=array_to_string(line)

        return array_with_strings_to_arrays_and_spaces

    if height < 0 or width < 0 or spaces < 0 or message == None:
        return

    message = list(message)
    return_array = ["" for x in range(height)]
    increment = 0

    # vvv while the last array index is not filled and words in the message sill haven't been added
    while len(return_array[height - 1]) < width and len(message) > 0:
        current = increment  # the current array index
        # VVVV while the index is bigger than -1, the current index isn't bigger than the width, and theres
        # still letters to add
        while current >= 0 and len(return_array[current]) < width and len(message) > 0:
            return_array[current] += message[0]
            message.pop(0)
            current -= 1  # everytime a letter is added, the index gets lower to move to the one below
        increment += increment < (height - 1)  # insures that the array index isn't more than the length of

    return_array = array_to_string_add_spaces_make_all_equal_length(return_array, spaces=spaces, width=width)

    return return_array


def make_message_and_print(message,spaces,width,height):
    if message==None or len(message)==0:
        return

    try:
        spaces=int(spaces)
    except ValueError:
        spaces=0
    try:
        width=int(width)
    except ValueError:
        width=12
    try:
        height=int(height)
    except ValueError:
        height=19


    if spaces==None or spaces<0:
        spaces=0
    if width==None or isinstance(width,str) or width<0:
        width=12
    if height==None or isinstance(height,str) or width<0:
        height=19

    if isinstance(width,float):
        width=round(width)
    if isinstance(height,float):
        height=round(height)

    text = Text(root, width=57, bg=black, fg=white, font="Serif")
    message_array=make_array(message,width=width,height=height,spaces=spaces)

    for line in message_array:
        text.insert(END, line)

    text.grid(column=0, row=4, columnspan=3)

def copy_message_to_clip():
    global copied_message
    pyperclip.copy(copied_message)

def draw_everything():
    message_label.grid(column=0, row=0, sticky=W)
    spaces_label.grid(column=0, row=1, sticky=W)
    width_label.grid(column=0, row=2, sticky=W)
    height_label.grid(column=0, row=3, sticky=W)

    message_entry.grid(column=1, row=0)
    spaces_entry.grid(column=1, row=1)
    width_entry.grid(column=1, row=2)
    height_entry.grid(column=1, row=3)

    make_message.grid(column=2, row=0,rowspan=2)
    copy_message.grid(column=2, row=2,rowspan=2)

copied_message=""
black = "#1a1a1a"
white = "#F1F1F1"

root = Tk()
# changes the title of the program
root.title("Write Diagonally")
root.configure(bg=black)

message_label = Label(root, text="Message: ", bg=black, fg=white)
spaces_label = Label(root, text="# of Spaces: ", bg=black, fg=white)
width_label = Label(root, text="Width:", bg=black, fg=white)
height_label = Label(root, text="Height: ", bg=black, fg=white)

message_entry = Entry(root, width=50, bg=black, fg=white, insertbackground=white)
spaces_entry = Entry(root, width=50, bg=black, fg=white, insertbackground=white)
width_entry = Entry(root, width=50, bg=black, fg=white, insertbackground=white)
height_entry = Entry(root, width=50, bg=black, fg=white, insertbackground=white)

make_message=Button(root,text="Make Message",padx=30,pady=10,activebackground=black,
                    activeforeground=white, bg=black, fg=white, command=lambda :
    make_message_and_print(message_entry.get(),spaces_entry.get(),width_entry.get(),height_entry.get()))
copy_message=Button(root,text="Copy Message",padx=30,pady=10,activebackground=black,
                    activeforeground=white, bg=black, fg=white,command=lambda : copy_message_to_clip())

draw_everything()

root.mainloop()
