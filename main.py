from tkinter import *


class Dashboard:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('My Shop')
        self.root.geometry('700x400')
        self.root.minsize(700, 400)
        self.draw_header()
        self.add_product_draw()
        
        self.root.mainloop()
    
    def add_product_draw(self):
        add_product_button = Button(self.root, text='Add product', command=self.add_product)
        add_product_button.pack()
        
    def draw_header(self):
        header_text = Label(self.root, text='My Shop v0.1', font=24)
        header_text.pack(pady=1)
        
    def add_product(self):
        product_window = Tk()
        product_window.geometry('250x200')
        
        #later on we will get catogeries predefined from DB
        category_label = Label(product_window, text='Category:')
        category_label.pack()
        category_entry = Entry(product_window)
        category_entry.pack(pady=5)
        
        product_label = Label(product_window, text='Product name:')
        product_label.pack()
        name_entry = Entry(product_window)
        name_entry.pack(pady=5)
           
        product_price_label = Label(product_window, text='Product price:')
        product_price_label.pack()
        price_entry = Entry(product_window)
        price_entry.pack(pady=5)
        
        button = Button(product_window, text='ADD', command=self.some_func)
        button.pack()
    def some_func(self):
        print('sup')
        

# app = Dashboard()