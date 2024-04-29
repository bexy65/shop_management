from tkinter import *
from tkinter import ttk
from database_utils import DatabaseClient



class Dashboard:
    db = DatabaseClient()
    
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('My Shop')
        self.root.minsize(700, 400)
        self.draw_header()
        self.add_product_button()
        self.get_product_button()
        self.selected_cat = None
        
        self.root.mainloop()
    
    def add_product_button(self):
        add_product_button = Button(self.root, text='Add product', command=self.open_add_product_window)
        add_product_button.pack()
    
    def get_product_button(self):
        get_products_button = Button(self.root, text='Products', command=self.open_products_windows)
        get_products_button.pack()
    
    def draw_header(self):
        header_text = Label(self.root, text='My Shop v0.1', font=24)
        header_text.pack(pady=1)
    
    
    def save_changes(self, entries, data):
        for i, (name_entry, price_entry, count_entry) in enumerate(entries):
            name = name_entry.get()
            price = price_entry.get()
            count = count_entry.get()
            # Update data list in DB with edited values
            print(name, price, count)

    def cancel_changes(self, window, editable_entries, data):
        # Clear Entry widgets and re-insert original data
        for i, (name_entry, price_entry, count_entry) in enumerate(editable_entries):
            name_entry.delete(0, END)
            name_entry.insert(0, data[i][0])
            price_entry.delete(0, END)
            price_entry.insert(0, data[i][1])
            count_entry.delete(0, END)
            count_entry.insert(0, data[i][2] if data[i][2] is not None else '')
        
        window.destroy()
            
    def open_products_windows(self):
        products_window = Tk()
        products_window.minsize(600, 350)
        
        products = self.db.get_products()
        
        canvas_frame = Frame(products_window)
        canvas_frame.pack(fill="both", expand=True)
        
        canvas = Canvas(canvas_frame)
        canvas.pack(side="left", fill="both", expand=True)
        
        scrollbar = Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        
        canvas.configure(yscrollcommand=scrollbar.set)
        
        entries_frame = Frame(canvas)
        canvas.create_window((0, 0), window=entries_frame, anchor="nw")
            
        Label(entries_frame, text='Name').grid(row=0, column=0)
        Label(entries_frame, text='Price').grid(row=0, column=1)
        Label(entries_frame, text='Quantity').grid(row=0, column=2)
        Label(entries_frame, text='Category').grid(row=0, column=3)

        entries = []
        for i, (name, price, count, category) in enumerate(products, start=1):
            
            name_entry = Entry(entries_frame)
            name_entry.insert(0, name)
            name_entry.grid(row=i, column=0)

            price_entry = Entry(entries_frame)
            price_entry.insert(0, price)
            price_entry.grid(row=i, column=1)

            count_entry = Entry(entries_frame)
            count_entry.insert(0, count if count is not None else '')
            count_entry.grid(row=i, column=2)

            Label(entries_frame, text=f'{category}').grid(row=i, column=3)
            
            entries.append((name_entry, price_entry, count_entry))

        save_button = Button(products_window, text="Save Changes", command=lambda: self.save_changes(entries, products))
        save_button.pack(side='left', padx=5, pady=5)

        cancel_button = Button(products_window, text="Cancel Changes", command=lambda: self.cancel_changes(products_window, entries, products))
        cancel_button.pack(side='right',padx=5, pady=5)
        
        entries_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
    
       
        
    def open_add_product_window(self):
        product_window = Tk()
        product_window.minsize(250, 300)
        
        #later on we will get catogeries predefined from DB
        categories = self.db.get_categories()
        
        category_label = Label(product_window, text='Category')
        category_label.pack(pady=5)
        
        dropdown = ttk.Combobox(product_window, values=categories)
        dropdown.set('Select category')
        dropdown.pack()
        
        product_label = Label(product_window, text='Product name:')
        product_label.pack()
        name_entry = Entry(product_window)
        name_entry.pack(pady=5)
        
        count_label = Label(product_window, text='Product count:')
        count_label.pack()
        count_entry = Entry(product_window)
        count_entry.pack(pady=5)
        
        product_price_label = Label(product_window, text='Product price:')
        product_price_label.pack()
        price_entry = Entry(product_window)
        price_entry.pack(pady=5)
        
        
        def add_product():
            product = {
                'name':name_entry.get(),
                'price':price_entry.get(),
                'category':dropdown.get(),
                'count':count_entry.get()
            }
           
           
            self.db.add_product(product)
            product_window.destroy()
        
        button = Button(product_window, text='ADD', command=add_product)
        button.pack()
    
    

app = Dashboard()
