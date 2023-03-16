import tkinter
from tkinter import *
root = Tk()
root.title('18_MY CUTEY CALCULATOR')
root.geometry("518x570+125+150")
root.resizable(False, True)
root.configure(bg='#000000')

operasi = []

def btn_calc(dobel):
    global operasi
    if operasi and operasi[-1] == "Error":
        return
    if operasi and operasi[-1] in ["+", "-", "*", "/", "."]:
        operasi[-1] = dobel
    else:
        operasi.append(dobel)
    show("".join(operasi))

def btn_num(number):
    global operasi
    if operasi and operasi[-1] == "Error":
        return
    if len(operasi) == 1 and operasi[0] == "0":
        operasi = []
    operasi.append(str(number))
    show("".join(operasi))

def delete_each():
    global operasi
    if operasi:
        operasi.pop()
        if operasi:
            show("".join(operasi))
        else:
            show("0")
        # global operasi
        # list = []
        # list.extend(operasi)
        # list.pop(len(list) -1)
        # result = ''.join(list)
        # operasi = result
        # label_tampil.config(text=operasi)

def calc():
    global operasi
    if operasi and operasi[-1] == "Error":
        return
    calc = "".join(operasi)
    try:
        result = eval(calc)
        result = round(result, 10)
         
        if float(result).is_integer():
            result = int(result)
        show(str(result))
        operasi = [str(result)]
        
    except ZeroDivisionError:
        show("Can't divide by zero")
        operasi = []
    except SyntaxError:
        show("Syntax Error")
        operasi = []
    

def show(value):
    # global operasi
    # operasi+=value
    label_tampil.config(text=value)
    
def clear():
    global operasi
    operasi = []
    label_tampil.config(text=operasi)

label_tampil = Label(root,width=20, bg="#ff94e0", height=2, text="", font=('Poppins ',25))
label_tampil.pack()

# Top-btn
Button(root, text="Del", width=4, height=1, font=("Poppins", 25, "bold"),  border=5, bg="#FDAED8", fg="#ffffff", command= delete_each).place(x=125, y=110)
Button(root, text="C", width=4, height=1, font=("Poppins", 25, "bold"),  border=5, bg="#FDAED8", fg="#ffffff", command=lambda: clear()).place(x=20, y=110)
Button(root, text="=", width=12, height=1, font=("Poppins", 25, "bold"),  border=5, bg="#FE83C6", fg="#ffffff", command=lambda: calc()).place(x=230, y=110)

# right-side
Button(root, text="x", width=6, height=1, font=("Poppins", 25, "bold"), border=5, bg="#ff59c7", fg="#ffffff", command=lambda: btn_calc('*')).place(x=353, y=200)
Button(root, text="÷", width=6, height=1, font=("Poppins", 25, "bold"), border=5, bg="#ff59c7", fg="#ffffff", command=lambda: btn_calc('/')).place(x=353, y=290)
Button(root, text="+", width=6, height=1, font=("Poppins", 25, "bold"), border=5, bg="#ff59c7", fg="#ffffff", command=lambda: btn_calc('+')).place(x=353, y=380)
Button(root, text="-", width=6, height=1, font=("Poppins", 25, "bold"), border=5, bg="#ff59c7", fg="#ffffff", command=lambda: btn_calc('-')).place(x=353, y=470)

# Top-number
Button(root, text="7", width=4, height=1, font=("Poppins", 25, "bold"), border=5,  fg="#ffffff", bg="#ffa6fc", command=lambda: btn_num('7')).place(x=20, y=200)
Button(root, text="8", width=4, height=1, font=("Poppins", 25, "bold"), border=5,  fg="#ffffff", bg="#ffa6fc", command=lambda: btn_num('8')).place(x=125, y=200)
Button(root, text="9", width=4, height=1, font=("Poppins", 25, "bold"), border=5,  fg="#ffffff", bg="#ffa6fc", command=lambda: btn_num('9')).place(x=230, y=200)

# Middle-number
Button(root, text="4", width=4, height=1, font=("Poppins", 25, "bold"), border=5, fg="#ffffff", bg="#ffa6fc",  command=lambda: btn_num('4')).place(x=20, y=290)
Button(root, text="5", width=4, height=1, font=("Poppins", 25, "bold"), border=5, fg="#ffffff", bg="#ffa6fc",  command=lambda: btn_num('5')).place(x=125, y=290)
Button(root, text="6", width=4, height=1, font=("Poppins", 25, "bold"), border=5, fg="#ffffff", bg="#ffa6fc",  command=lambda: btn_num('6')).place(x=230, y=290)

# decimal
Button(root, text=".", width=4, height=1, font=("Poppins", 25, "bold"), border=5, bg="#ff59c7", fg="#ffffff", command=lambda: btn_calc('.')).place(x=230, y=470)

# Bottom-number
Button(root, text="1", width=4, height=1, font=("Poppins", 25, "bold"), border=5, fg="#ffffff", bg="#ffa6fc",   command=lambda: btn_num('1')).place(x=20, y=380)
Button(root, text="2", width=4, height=1, font=("Poppins", 25, "bold"), border=5, fg="#ffffff", bg="#ffa6fc",   command=lambda: btn_num('2')).place(x=125, y=380)
Button(root, text="3", width=4, height=1, font=("Poppins", 25, "bold"), border=5, fg="#ffffff", bg="#ffa6fc",   command=lambda: btn_num('3')).place(x=230, y=380)
Button(root, text="0", width=9, height=1, font=("Poppins", 25, "bold"), border=5, fg="#ffffff", bg="#ffa6fc",   command=lambda: btn_num('0')).place(x=22, y=470)



root.mainloop()