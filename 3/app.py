from tkinter import *

#------------------------------
window = Tk()
window.minsize(400,300)
window.maxsize(600,500)
window.geometry('400x300')

#------------------------------
#      --functions--
def sayhello():
    print('hello God')

count = 0
def counter():
    global count
    count += 1
    l_cnt.config(text=f"count: {count}")

def change_color():
    l1.config(text='active',bg="green")

#------------------------------
window.title("hello app")
Label(window , text="\"hello world\"",bg='black',fg='white',font='Tahoma').pack()

l1 = Label(window,text='unactive',bg='red',font=('Tahoma',20))
l1.pack()
Button(window,text="activate",fg="blue",bg='yellow',command=change_color).pack()

# l_cnt = Label(window,text="count: ")
# l_cnt.pack()
# Button(window,text="click",fg="blue",bg='yellow',command=counter).pack()


#------------------------------
window.mainloop()