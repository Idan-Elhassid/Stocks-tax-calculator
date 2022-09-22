from tkinter import *
import sv_ttk


def calculate_tax():
    commission = 2.5
    number_of_stocks = float(stocks_entry.get())
    commission_fee = commission / number_of_stocks
    sell_price = float(sell_entry.get())
    buy_price = float(buy_entry.get())
    gross_revenue = (number_of_stocks*(sell_price - buy_price)) - commission_fee
    tax_cut = gross_revenue / 4
    after_tax_profit = (gross_revenue - tax_cut)
    commission_fee_label["text"] = round(commission_fee, 2)
    taxes_owed_label["text"] = round(tax_cut, 3)
    net_profit_label["text"] = round(after_tax_profit, 3)
    your_money_amount["text"] = round(after_tax_profit + (buy_price*number_of_stocks), 3)


# this section is the Tkinter GUI
window = Tk()
sv_ttk.set_theme("dark")
window.title("Tax Calculator")
window.config(padx=100, pady=50)

canvas = Canvas(width=400, height=300, highlightthickness=0)
money_img = PhotoImage(file="money.PNG.")
canvas.create_image(200, 100, image=money_img)
canvas.grid(column=1, row=0)

buy_price_label = Label(text="Buy Price:", font=("david", 20))
buy_price_label.grid(column=0, row=1)

sell_price_label = Label(text="Sell Price:", font=("david", 20))
sell_price_label.grid(column=0, row=2)

stocks_label = Label(text="number of stocks sold:", font=("david", 20))
stocks_label.grid(column=0, row=3)


buy_entry = Entry(width=50)
buy_entry.insert(END, string="0")
buy_entry.grid(column=1, row=1)

sell_entry = Entry(width=50)
sell_entry.insert(END, string="0")
sell_entry.grid(column=1, row=2)

stocks_entry = Entry(width=50)
stocks_entry.insert(END, string="1")
stocks_entry.grid(column=1, row=3)

calculate_button = Button(text="Calculate taxes", width=43, command=calculate_tax)
calculate_button.grid(column=1, row=4)

commission_label = Label(text="commission per share is: ", font=("david", 20))
commission_label.grid(column=0, row=5)

taxes_label = Label(text="taxes owed:", font=("david", 20))
taxes_label.grid(column=0, row=6)

profit_label = Label(text="your net profit is:", font=("david", 20))
profit_label.grid(column=0, row=7)

commission_fee_label = Label(text="0", font=("david", 20))
commission_fee_label.grid(column=1, row=5)

taxes_owed_label = Label(text="0", font=("david", 20))
taxes_owed_label.grid(column=1, row=6)

net_profit_label = Label(text="0", font=("david", 20))
net_profit_label.grid(column=1, row=7)

your_money_label = Label(text="initial investment + profits:", font=("david", 20))
your_money_label.grid(column=0, row=8)

your_money_amount = Label(text="0", font=("david", 20))
your_money_amount.grid(column=1, row=8)

window.mainloop()
