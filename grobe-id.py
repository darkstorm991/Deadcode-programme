from tkinter import *
programme = Tk()
programme.title("Deadcode")
programme.geometry("600x500+500+250")
programme.config(background="dodgerblue4")
lbl  =Label(text="we are agroub of hackers join \n\n connect with me" , bg="dodgerblue4", fg="gray")
lbl.configure(font=('Arial', 25))
lbl.pack()
def facebook():
    import webbrowser
    webbrowser.open_new_tab(" https://www.facebook.com/maro.melad.714/")

def instagram():
    import webbrowser
    webbrowser.open_new_tab(" https://www.instagram.com/maromelad_/")

fb = Button(text="Facebook" , bg="dodgerblue4", fg="gold4" , command=facebook)
ib = Button(text="Instagram" , bg="dodgerblue4", fg="gold4" , command=instagram)
fb.configure(font=('Arial', 25))
ib.configure(font=('Arial', 25))
ib.pack(pady=25)
fb.pack(pady=5)
programme.mainloop()