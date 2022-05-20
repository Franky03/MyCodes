import tkinter


class NewWindow(tkinter.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title('E O NARGA?')
        self.minsize(width=512, height=512)
        self.bg= tkinter.PhotoImage(file='./Additional/narga.png')
        self.canvas1= tkinter.Canvas(self, width=500, height=300)
        self.canvas1.pack(fill='both', expand=True)
        self.canvas1.create_image(0,0, image= self.bg, anchor='nw')
        
        

window= tkinter.Tk() 
window.title('E O NARGA?')
window.minsize(width=500, height=300)
window.config(padx=200, pady=100)

#LABEL
my_label= tkinter.Label(text='I Am a Label', font=('Arial', 24, 'italic'))

def button_click():
    my_label.config(text= 'E O NARGA?')

#BUTTON
btn= tkinter.Button(window, text='E O NARGA?', bd= '5')
btn.bind('<Button>', lambda e: NewWindow(window), button_click())


my_label.pack(expand=True)
btn.pack(expand=True)
window.mainloop()

