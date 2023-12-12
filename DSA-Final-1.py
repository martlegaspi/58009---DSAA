from tkinter import *
from tkinter.ttk import *

class ShoppingCart:
    items = []

    @classmethod
    def add_item(cls, item, price):
        cls.items.append({"name": item, "price": price})

    @classmethod
    def remove_item(cls, index):
        if 0 <= index < len(cls.items):
            del cls.items[index]

    @classmethod
    def get_items(cls):
        return cls.items

    @classmethod
    def clear_items(cls):
        cls.items = []

    @classmethod
    def get_total_price(cls):
        return sum(item['price'] for item in cls.items)

class MyWindow:
    def __init__(self,window):

        self.window = window
        # Labels and items
        self.lbl1 = Label(window,text="Item List")
        self.lbl1.place(x = 70, y = 20)
        self.item1 = Label(window,text="Black Ballpen - P10.00")
        self.item1.place(x = 25, y = 52)
        self.item2 = Label(window,text="Red Ballpen - P10.00")
        self.item2.place(x = 25, y = 87)
        self.item3 = Label(window,text="Yellow Pad 80Leaves - P50.00")
        self.item3.place(x = 25, y = 122)
        self.item4 = Label(window,text="Pencil - P7.00")
        self.item4.place(x = 25, y = 157)
        self.item5 = Label(window,text="Calculator - P400.00")
        self.item5.place(x = 25, y = 192)
        self.item6 = Label(window,text="Notebook - P25.00")
        self.item6.place(x = 25, y = 227)

        # Buttons
        self.cart = Button(window, text="My Cart", command=self.MyCart)
        self.cart.place(x=210, y=10)
        self.ibut1 = Button(window, text = "Add to Cart", command=lambda: self.add_to_cart("Black Ballpen", 10.00))
        self.ibut1.place(x = 210, y = 50)
        self.ibut2 = Button(window, text = "Add to Cart", command=lambda: self.add_to_cart("Red Ballpen", 10.00))
        self.ibut2.place(x = 210, y = 85)
        self.ibut3 = Button(window, text = "Add to Cart", command=lambda: self.add_to_cart("Yellow Pad 80Leaves", 50.00))
        self.ibut3.place(x = 210, y = 120)
        self.ibut4 = Button(window, text="Add to Cart", command=lambda: self.add_to_cart("Pencil", 7.00))
        self.ibut4.place(x=210, y=155)
        self.ibut5 = Button(window, text="Add to Cart", command=lambda: self.add_to_cart("Calculator", 400.00))
        self.ibut5.place(x=210, y=190)
        self.ibut6 = Button(window, text="Add to Cart", command=lambda: self.add_to_cart("Notebook", 25.00))
        self.ibut6.place(x=210, y=225)


    #https://www.geeksforgeeks.org/open-a-new-window-with-a-button-in-python-tkinter/


    def MyCart(self):
        new_window = Toplevel(self.window)
        new_window.title("CpE Shop")
        new_window.geometry("300x300")
        new_window.resizable(width=0, height=0)
        NewWindow(new_window)

    def add_to_cart(self, item, price):
        ShoppingCart.add_item(item, price)


class NewWindow:
    def __init__(self, window):
        self.window = window

        # Label
        self.nlbl1 = Label(window, text="My Cart")
        self.nlbl1.place(x=120, y=20)

        # Listbox to display items in the cart
        self.cart_listbox = Listbox(window)
        self.cart_listbox.place(x=80, y=50)

        # Display items in the cart
        for cart_item in ShoppingCart.get_items():
            self.cart_listbox.insert(END, f"{cart_item['name']} - P{cart_item['price']:.2f}")

        # Delete Function
        delete_button = Button(window, text="Remove Selected", command=self.delete_selected)
        delete_button.place(x=90, y=220)

        # Checkout Function
        checkout_button = Button(window, text="Checkout", command=self.checkout)
        checkout_button.place(x=100, y=250)

        self.selected_item = -1

        self.cart_listbox.bind('<<ListboxSelect>>', self.on_select)

    def delete_selected(self):
        if self.selected_item != -1:
            ShoppingCart.remove_item(self.selected_item)
            self.cart_listbox.delete(self.selected_item)
            self.selected_item = -1

    def on_select(self, event):
        selected_item = self.cart_listbox.curselection()
        if selected_item:
            self.selected_item = int(selected_item[0])

    def checkout(self):
        CheckoutWindow(ShoppingCart.get_items(), ShoppingCart.get_total_price())

class CheckoutWindow:
    def __init__(self, items, total_price):
        checkout_window = Toplevel()
        checkout_window.title("Checkout")
        checkout_window.resizable(width=0, height=0)
        Label(checkout_window, text="Checkout Success, Total: ").pack(pady=20)
        Label(checkout_window, text="Items in Your Cart:").pack()
        for item in items:
            Label(checkout_window, text=f"{item['name']} - P{item['price']:.2f}").pack()

        Label(checkout_window, text=f"Total Price: P{total_price:.2f}").pack(pady=20)
        Button(checkout_window, text="OK", command=window.destroy).pack(pady=10)

        ShoppingCart.clear_items()


if __name__ == "__main__":
    window = Tk()
    window.geometry("300x300+20+10")
    window.resizable(width=0, height=0)
    window.title('CpE Shop')
    my_window = MyWindow(window)
    window.mainloop()