import tkinter as tk
def calculate():
    num1= float(entry_num1.get())
    num2=float(entry_num2.get())
    operator=operator_var.get()
    if operator=="Add":
        result= num1+num2
    elif operator=="Subtract":
        result=num1-num2
    elif operator=="Multiply":
        result=num1*num2
    elif operator=="Divide":
        result=num1/num2

    label_result.config(text="Result:%.2f"%result)
root=tk.Tk()
root.title("Lino Calculator ")
operators=["Add","Subtract","Multiply","Divide"]
label_num1=tk.Label(root,text="First number:")
label_num1.pack()

entry_num1=tk.Entry(root)
entry_num1.pack()
label_num2=tk.Label(root,text="Second number:")
label_num2.pack()
entry_num2=tk.Entry(root)
entry_num2.pack()
operator_var=tk.StringVar(root)
operator_var.set(operators[0])# default operator
label_operator=tk.Label(root, text="Select operator:")
label_operator.pack()
dropdown_operator=tk.OptionMenu(root, operator_var,*operators)
dropdown_operator.pack()
button_calc=tk.Button(root, text="Calculate",command=calculate)
button_calc.pack()
label_result=tk.Label(root,text="Result:", font=("consolas",20))
label_result.pack()

root.mainloop()
