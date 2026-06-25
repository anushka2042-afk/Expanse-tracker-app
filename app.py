import tkinter as tk


# list to store expenses
expenses = []


# loading old expenses from file
try:
    with open("expenses.txt", "r") as file:

        for line in file:

            name, amount, category = line.strip().split(",")

            expenses.append({
                "name": name,
                "amount": float(amount),
                "category": category
            })


except FileNotFoundError:
    pass



# function to save expense
def add_expense():

    name = name_entry.get()
    amount = float(amount_entry.get())
    category = category_entry.get()


    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }


    expenses.append(expense)


    # saving into file
    with open("expenses.txt", "a") as file:

        file.write(
            name + "," +
            str(amount) + "," +
            category + "\n"
        )


    result_label.config(text="Expense Added!")


    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)



# function to show expenses
def view_expenses():

    display.delete("1.0", tk.END)


    for expense in expenses:

        display.insert(
            tk.END,
            "Name: " + expense["name"] +
            "\nAmount: ₹" + str(expense["amount"]) +
            "\nCategory: " + expense["category"] +
            "\n-------------------\n"
        )



# function to calculate total
def total_expense():

    total = 0


    for expense in expenses:

        total += expense["amount"]


    result_label.config(
        text="Total Expense: ₹" + str(total)
    )



# creating app window

window = tk.Tk()

window.title("Expense Tracker")

window.geometry("400x550")



# labels and entry boxes

tk.Label(window, text="Expense Name").pack()

name_entry = tk.Entry(window)

name_entry.pack()



tk.Label(window, text="Amount").pack()

amount_entry = tk.Entry(window)

amount_entry.pack()



tk.Label(window, text="Category").pack()

category_entry = tk.Entry(window)

category_entry.pack()



# buttons

tk.Button(
    window,
    text="Add Expense",
    command=add_expense
).pack(pady=5)



tk.Button(
    window,
    text="View Expenses",
    command=view_expenses
).pack(pady=5)



tk.Button(
    window,
    text="Show Total",
    command=total_expense
).pack(pady=5)



# display area

display = tk.Text(
    window,
    height=12,
    width=40
)

display.pack()



result_label = tk.Label(window, text="")

result_label.pack()



# keep app running

window.mainloop()