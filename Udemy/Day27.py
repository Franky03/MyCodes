import tkinter

from numpy import True_
window= tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)

#LABEL
my_label= tkinter.Label(text='I Am a Label', font=('Arial', 24, 'italic'))
my_label.pack(expand=True)



window.mainloop()