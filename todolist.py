from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do-List')
        self.root.geometry('1200x410+300+150')

        self.label = Label(self.root, text='To-do-List-APP',
            font='TimesNewRoman, 25 bold', width=10, bd=2, relief='solid', bg='yellow', fg='red')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Text',
            font='TimesNewRoman, 18 bold', width=10, bd=2, relief='solid', bg='orange', fg='black')
        self.label2.place(x=150, y=75)

        self.label3 = Label(self.root, text='Tasks',
            font='TimesNewRoman, 18 bold', width=10, bd=2, relief='solid', bg='orange', fg='black')
        self.label3.place(x=900, y=75)

        self.main_text = Listbox(self.root, height=10, bd=10, width=23, font='TimesNewRoman, 23 bold')
        self.main_text.place(x=750, y=150)

        self.separator = ttk.Separator(self.root, orient='horizontal')
        self.separator.place(x=0, y=120, width=1300)

        self.separator = ttk.Separator(self.root, orient='vertical')
        self.separator.place(x=650, y=50, height=360)

        self.text = Text(self.root, bd=5, height=2, width=30, font='TimesNewRoman, 10 bold')
        self.text.place(x=120, y=150)

        self.button = Button(self.root, text="Add", font='sarif, 20 bold italic',
                             width=10, bd=5, bg='orange', fg='black', command=self.add)
        self.button.place(x=140, y=230)

        self.button2 = Button(self.root, text="Delete", font='sarif, 20 bold italic',
                              width=10, bd=5, bg='orange', fg='black', command=self.delete)
        self.button2.place(x=140, y=300)

        # Button to remove all tasks
        self.button3 = Button(self.root, text="Remove All", font='sarif, 20 bold italic',
                              width=10, bd=5, bg='orange', fg='black', command=self.remove_all)
        self.button3.place(x=140, y=370)

        self.load_tasks()

    def add(self):
        content = self.text.get(1.0, END).strip()
        if content:
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content + "\n")
            self.text.delete(1.0, END)

    def delete(self):
        try:
            index = self.main_text.curselection()[0]
            self.main_text.delete(index)
            self.update_file()
        except IndexError:
            pass

    def remove_all(self):
        self.main_text.delete(0, END)
        with open('data.txt', 'w') as file:
            file.truncate()

    def load_tasks(self):
        with open('data.txt', 'r') as file:
            tasks = file.readlines()
            for task in tasks:
                self.main_text.insert(END, task.strip())

    def update_file(self):
        with open('data.txt', 'w') as file:
            tasks = list(self.main_text.get(0, END))
            for task in tasks:
                file.write(task + "\n")

def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
