# here we go
import tkinter


# root = tk.Tk()
#
# label = tk.Label(root, text="Hello World", padx=15, pady=20)
# label.pack()
#
# root.mainloop()

class Root(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.label = tkinter.Label(self, text="hello github", padx=25, pady=35)
        self.label.pack()  # called as a way of placing the label into the root


# root = Root()  # create obj
# root.mainloop()

# create a TODO list
# allow user to inter text/ bind func to key press/ widgets/ scroll/ storing data


class TODO(tkinter.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            tasks = []
        else:
            self.tasks = tasks

        self.title('TO-DO')
        self.geometry(500, 600)

        todolist = tkinter.Label(self, text='--add your text--', bg='dark blue', fg='light blue', pady=15)

        self.tasks.append(todolist)
        for task in tasks:
            task.pack(side=tkinter.TOP, fill=tkinter.X)

        self.create_task = tkinter.Text(self, height=5, bg='white', fg='dark gray')
        self.create_task.pack(tkinter.BOTTOM, fill=tkinter.X)
        self.create_task.focus_set()  # so that the cursor is inside the box when the window is opened
        self.bind('<Return>', self.add_task)

        self.colour_schemes = [{'bg': 'dark gray', 'fg': 'light gray'}, {'bg': 'light gray', 'fg': 'white'}]

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tkinter.END).strip()
        # 1.0 tells it to begin at the first character and the END constant tells it to look until the end of the box
        # strip() to remove the newline character which is entered when the user presses Return to submit the text

        if len(task_text) > 0:
            new_task = tkinter.Label(self, text=task_text, pady=10)

            _, task_style_choice = divmod(len(self.tasks), 2)
            my_scheme_choice = self.colour_schemes[task_style_choice]

            new_task.configure(my_scheme_choice['bg'])
            new_task.configure(my_scheme_choice['fg'])
            # is used to set a property of a widget,
            new_task.pack(side=tkinter.TOP, fill=tkinter.X)

            self.tasks.append(new_task)
        self.task_create.delete(1.0, tkinter.END)


todo = TODO()
todo.mainloop()
