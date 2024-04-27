from tkinter import *

class MyShop:
    root = Tk()
    font_family ='JetBrains Mono'
    login_geometry = '500x250'
    app_geometry = '700x300'

    def __init__(self):
        self.draw_window()

    def draw_window(self):
        self.root.title('MyShop')
        self.root.geometry(self.login_geometry)

        self.draw_login()

        self.root.mainloop()



  

    def draw_login(self):
    # Clear any existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
    
        main_text = Label(self.root, text='Login to MyShop', font=('',16))
        main_text.pack(pady=10)

        # Create login form components
        username_label = Label(self.root, text='Username:')
        username_label.pack()
        self.username_entry = Entry(self.root)
        self.username_entry.pack()

        password_label = Label(self.root, text='Password:')
        password_label.pack()
        self.password_entry = Entry(self.root, show='*')
        self.password_entry.pack()

        login_button = Button(self.root, text='Login', command=self.login)
        login_button.pack(pady=10)

        switch_button = Button(self.root, text='Switch to Register', command=self.draw_register)
        switch_button.pack(pady=5)

    def draw_register(self):
        # Clear any existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        main_text = Label(self.root, text='Register to MyShop', font=('',16))
        main_text.pack(pady=10)

        # Create register form components
        username_label = Label(self.root, text='Username:')
        username_label.pack()
        self.username_entry = Entry(self.root)
        self.username_entry.pack()


        email_label = Label(self.root, text='Email:')
        email_label.pack()
        self.email_entry = Entry(self.root)
        self.email_entry.pack()


        password_label = Label(self.root, text='Password:')
        password_label.pack()
        self.password_entry = Entry(self.root, show='*')
        self.password_entry.pack()

        register_button = Button(self.root, text='Register', command=self.register)
        register_button.pack(pady=10)

        switch_button = Button(self.root, text='Switch to Login', command=self.draw_login)
        switch_button.pack(pady=5)


    def login(self):
        # Placeholder for login functionality
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(f"Login: Username={username}, Password={password}")

    def register(self):
        # Placeholder for register functionality
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(f"Register: Username={username}, Password={password}")




myshop = MyShop()