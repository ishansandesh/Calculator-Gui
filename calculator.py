from tkinter import *

root = Tk()
root.title("CALCULATOR")
root.geometry("300x300")
root.configure(bg="#93A8AC")
root.resizable(False, False)

value = 0
operator = ""

def number(num):
    current = main_entry.get()
    main_entry.delete(0, END)
    main_entry.insert(0, str(current) + str(num))

def clear():
    global value, operator
    main_entry.delete(0, END)
    value = 0
    operator = ""

def back():
    current = main_entry.get()
    main_entry.delete(0, END)
    main_entry.insert(0, current[:-1])

def cal(sign):
    global value, operator
    if sign == "=":
        if operator:
            try:
                value = eval(f"{value}{operator}{main_entry.get()}")
                main_entry.delete(0, END)
                main_entry.insert(0, value)
                operator = ""
            except Exception as e:
                main_entry.delete(0, END)
                main_entry.insert(0, "Error")
                value = 0
                operator = ""
    else:
        if main_entry.get() != "":
            if operator:
                try:
                    value = eval(f"{value}{operator}{main_entry.get()}")
                except:
                    value = 0
            else:
                value = float(main_entry.get())
            operator = sign
            main_entry.delete(0, END)


# main entry 
main_entry = Entry(root, width=25, font=("helvetica", 15, "bold"))
main_entry.grid(padx=10, pady=10, row=0, columnspan=4)

# Row 1
button_clear = Button(root, text="AC", width=7, height=2, font=("helvetica", 8, "bold"), bg="#424B54", fg="white", command=clear)
button_clear.grid(row=1, column=0, pady=5)
button_back = Button(root, text="⌫", width=7, height=2, font=("helvetica", 8, "bold"), bg="#424B54", fg="white", command=back)
button_back.grid(row=1, column=1, pady=5)
button_divide = Button(root, text="/", width=7, height=2, font=("helvetica", 8, "bold"), bg="#424B54", fg="white", command=lambda: cal("/"))
button_divide.grid(row=1, column=2, pady=5)
button_multiply = Button(root, text="*", width=7, height=2, font=("helvetica", 8, "bold"), bg="#424B54", fg="white", command=lambda: cal("*"))
button_multiply.grid(row=1, column=3, pady=5)

# Row 2
button_7 = Button(root, text="7", width=7, height=2, font=("helvetica", 8, "bold"), bg="#424B54", fg="white", command=lambda: number(7))
button_7.grid(row=2, column=0)
button_8 = Button(root, text="8", width=7, height=2, font=("helvetica", 8, "bold"), bg="#424B54", fg="white", command=lambda: number(8))
button_8.grid(row=2, column=1)
button_9 = Button(root, text="9", width=7, height=2, font=("helvetica", 8, "bold"), bg="#424B54", fg="white", command=lambda: number(9))
button_9.grid(row=2, column=2)
button_minus = Button(root, text="-", width=7, height=2, font=("helvetica", 8, "bold"), bg="#424B54", fg="white", command=lambda: cal("-"))
button_minus.grid(row=2, column=3)

# Row 3
button_4 = Button(root, text="4", width=7, height=2, font=("helvetica", 8, "bold"), bg="#424B54", fg="white", command=lambda: number(4))
button_4.grid(row=3, column=0, pady=5)
button_5 = Button(root, text="5", width=7, height=2, font=("helvetica", 8, "bold"), bg="#424B54", fg="white", command=lambda: number(5))
button_5.grid(row=3, column=1, pady=5)
button_6 = Button(root, text="6", width=7, height=2, font=("helvetica", 8, "bold"), bg="#424B54", fg="white", command=lambda: number(6))
button_6.grid(row=3, column=2, pady=5)
button_plus = Button(root, text="+", width=7, height=2, font=("helvetica", 8, "bold"), bg="#424B54", fg="white", command=lambda: cal("+"))
button_plus.grid(row=3, column=3, pady=5)

# Row 4
button_1 = Button(root, text="1", width=7, height=2, font=("helvetica", 8, "bold"), bg="#424B54", fg="white", command=lambda: number(1))
button_1.grid(row=4, column=0)
button_2 = Button(root, text="2", width=7, height=2, font=("helvetica", 8, "bold"), bg="#424B54", fg="white", command=lambda: number(2))
button_2.grid(row=4, column=1)
button_3 = Button(root, text="3", width=7, height=2, font=("helvetica", 8, "bold"), bg="#424B54", fg="white", command=lambda: number(3))
button_3.grid(row=4, column=2)
button_equal = Button(root, text="=", width=7, height=4, font=("helvetica", 8, "bold"), bg="#424B54", fg="white", command=lambda: cal("="))
button_equal.grid(row=4, column=3, rowspan=2, sticky=N+S)

# Row 5
button_0 = Button(root, text="0", width=18, height=3, font=("helvetica", 8, "bold"), bg="#424B54", fg="white", command=lambda: number(0))
button_0.grid(row=5, column=0, columnspan=2, pady=5)
button_dot = Button(root, text=".", width=7, height=3, font=("helvetica", 8, "bold"), bg="#424B54", fg="white", command=lambda: number("."))
button_dot.grid(row=5, column=2, pady=5)

root.mainloop()
