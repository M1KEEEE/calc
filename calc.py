import tkinter as tk
from tkinter.ttk import Radiobutton 

euro = 86,79
dollar = 77,13

def user_choise():
   euro == "1"
   dollar == "2"
   if user_choise == "1":
      print(value)

value = ()

# создание окна
window = tk.Tk()

#создание ярлыка
label = tk.Label(text="Калькулятор валют")
label.pack()

#выбор валюты
def clicked():
   print(value)

rad1 = Radiobutton(window,text='Доллар', value=1, command=clicked)
rad2 = Radiobutton(window,text='Eвро', value=2, command=clicked)
rad1.pack()
rad2.pack()
rad1.place(x=650, y=35)
rad2.place(x=650, y=55)

#текст
label1 = tk.Label(text="Введите значение")
label1.pack()
label1.place(x=550, y=80)


#ввод значения
entry = tk.Entry()
entry.pack()
entry.place(x=540, y=100)
   
#кнопка
button = tk.Button(text="Посчитать", width=10)
button.pack()
button.place(x=700, y=95)

#цикл
window.mainloop()
