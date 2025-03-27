# here we go
import tkinter
import tkinter.messagebox as msg

# create a TODO list
# allow user to inter text/ bind func to key press/ widgets/ scroll/ storing data


class TODO(tkinter.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks
        # canvas
        self.tasks_canvas = tkinter.Canvas(self)

        self.tasks_frame = tkinter.Frame(self.tasks_canvas)
        self.text_frame = tkinter.Frame(self)

        self.scrollbar = tkinter.Scrollbar(self.tasks_canvas, orient='vertical', command=self.tasks_canvas.yview)

        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.title('TO-DO')
        self.geometry("600x400+100+50")

        self.create_task = tkinter.Text(self, height=5, bg='white', fg='dark gray')

        self.tasks_canvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor='n')

        self.create_task.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        self.text_frame.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        self.create_task.focus_set()  # so that the cursor is inside the box when the window is opened

        todolist = tkinter.Label(self.tasks_frame, text='--add your text--', bg='dark blue', fg='light blue', pady=15)
        todolist.bind('<Button-1>', self.add_task)
        remove = tkinter.Label(self.tasks_frame, text='del', bg='red', fg='black')
        remove.bind('<Button-1>', self.remove_task)
        remove.pack(side=tkinter.RIGHT)
        self.tasks.append(todolist)

        for task in self.tasks:
            task.pack(side=tkinter.TOP, fill=tkinter.X)

        self.bind('<Return>', self.add_task)
        self.bind('<Configure>', self.on_frame_configure)
        self.bind_all('<MouseWheel>', self.mouse_scroll)
        self.bind_all('<Button-4>', self.mouse_scroll)
        self.bind_all('<Button-5>', self.mouse_scroll)
        self.tasks_canvas.bind('<Configure>', self.task_width)

        self.colour_schemes = [{"bg": "light grey", "fg": "black"}, {"bg": "grey", "fg": "white"}]

    def add_task(self, event=None):
        task_text = self.create_task.get(1.0, tkinter.END).strip()
        # 1.0 tells it to begin at the first character and the END constant tells it to look until the end of the box
        # strip() to remove the newline character which is entered when the user presses Return to submit the text

        if len(task_text) > 0:
            new_task = tkinter.Label(self, text=task_text, pady=10)
            new_task.pack(side=tkinter.TOP, fill=tkinter.X)
            self.tasks.append(new_task)

        self.create_task.delete(1.0, tkinter.END)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno('Delete?', f'Delete {task.cget("text")}?'):
            self.tasks.remove(task)
            self.recolor_tasks()
            event.widget.destroy()

    def recolor_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_color(index, task)

    def set_task_color(self, position, task):
        _, task_style_choice = divmod(len(self.tasks), 2)
        my_scheme_choice = self.colour_schemes[task_style_choice]

        task.configure(my_scheme_choice['bg'])
        task.configure(my_scheme_choice['fg'])
        # is used to set a property of a widget

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox('all'))
        # sets the scrollable region for our canvas

    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)
        # responsible for ensuring the task Labels stay at the full width of the canvas

    def mouse_scroll(self, event):
        # how we bind scrolling to the mouse wheel as well as the scrollbar
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1*(event.delta/120)), 'units')
            # call the Canvas’ yview_scroll method based upon whether receive a delta or a num within the event
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1

            self.tasks_canvas.yview_scroll(move, 'units')


todo = TODO()
todo.mainloop()
# apparently, structure is ok but UX is a disaster!! gonna delete it
