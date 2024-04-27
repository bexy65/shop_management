from tkinter import *
from database_utils import Database_client as db


class MyShop:
    root = Tk()
    font_family ='JetBrains Mono'
    login_geometry = '450x250'
    app_geometry = '700x400'
    window_minsize_geometry =[250, 200]

    def __init__(self):
        self.draw_window()

    def draw_window(self):
        self.root.title('MyShop')
        self.root.geometry(self.login_geometry)
        self.root.minsize(self.window_minsize_geometry[0], self.window_minsize_geometry[1])

        self.draw_login_form()

        self.root.mainloop()


    def draw_login_form(self):
    # Clear any existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
    
        main_text = Label(self.root, text='Login to MyShop', font=('',16))
        main_text.pack(pady=10)

        username_label = Label(self.root, text='Username:')
        username_label.pack()
        self.username_entry = Entry(self.root)
        self.username_entry.pack()

        password_label = Label(self.root, text='Password:')
        password_label.pack()
        self.password_entry = Entry(self.root, show='*')
        self.password_entry.pack()

        login_button = Button(self.root, text='Login', command=self.login, background='lightblue')
        login_button.pack(side='right', padx=25)

        switch_button = Button(self.root, text='Register', command=self.draw_register_form)
        switch_button.pack(side='left', padx=25)

    def draw_register_form(self):
        # Clear any existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        main_text = Label(self.root, text='Register to MyShop', font=('',16))
        main_text.pack(pady=10)

        username_label = Label(self.root, text='Username:')
        username_label.pack()
        self.username_entry = Entry(self.root)
        self.username_entry.pack()


        password_label = Label(self.root, text='Password:')
        password_label.pack()
        self.password_entry = Entry(self.root, show='*')
        self.password_entry.pack()

        register_button = Button(self.root, text='Register', command=self.register, background='lightblue')
        register_button.pack(side='right', padx=25)

        switch_button = Button(self.root, text='Back', command=self.draw_login_form)
        switch_button.pack(side='left', padx=25)


    def login(self):
        # Placeholder for login functionality
        username = self.username_entry.get()
        password = self.password_entry.get()

        if db.authenticate_user(db, username, password):
            print('authenticated')
            self.root.geometry(self.app_geometry)

        print(f"Login: Username={username}, Password={password}")


    def register(self):
        # Placeholder for register functionality
        username = self.username_entry.get()
        password = self.password_entry.get()
        db.create_user(db,username , password)
        print(f"Register: Username={username}, Password={password}")





myshop = MyShop()