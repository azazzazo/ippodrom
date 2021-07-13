from tkinter import *
from tkinter import messagebox
from pygameip import init
root = Tk()
root.title("Ипподром")
root.geometry("500x500")
root.resizable(False, False)
def getV(arg):
    a = scale1.get()
    b = scale2.get()
    if b>a:
        messagebox.showerror("Ошибка!", "Несуществующая лошадь...")
        return
    else:
        win=init(a)
        if b==win:
            messagebox.showinfo("Результат", "Вы победили!")
        else:
            messagebox.showinfo("Результат", "Вы програли... Первой пришла лошадь №{}".format(win))

scale1 = Scale(root,orient=HORIZONTAL,length=300,from_=2,to=10,tickinterval=1,
               resolution=1)
lab1=Label(root,text='Количество лошадей',width=25,height=5,fg='black',font='arial 14')
scale2 = Scale(root,orient=HORIZONTAL,length=300,from_=1,to=10,tickinterval=1,
               resolution=1)
lab2=Label(root,text='Ставка на лошадь:',width=25,height=5,fg='black',font='arial 14')
button1 = Button(root,text=u"Начать гонку!")
lab1.pack()
scale1.pack()
lab2.pack()
scale2.pack()
button1.pack()
button1.bind("<Button-1>",getV)
root.mainloop()