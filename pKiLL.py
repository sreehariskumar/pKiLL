from tkinter import * 
import subprocess


#window frame
main = Tk()
main.geometry("400x200")
main.title("pKiLL v1.1")
main.configure(bg='#343434')
main.resizable(0,0)
p1 = PhotoImage(file='icon.png')
main.iconphoto(False, p1)



def end():
   process = process_var.get()
   file = open("process.txt","w")
   file.write(process)
   file.close()   
   subprocess.call(["./end.sh"])
   


def start():   
   process = process_var.get()
   file = open("process.txt","w")
   file.write(process)
   file.close()   
   subprocess.call(["./start.sh"])



def clear():
   process_entry.delete(0, END)



#label and entry field
process_var = StringVar()
process_label = Label(main, text='Enter the process', font=('calibre',10, 'bold'))
process_entry = Entry(main, textvariable = process_var, font=('calibre',10,'normal'))
process_label.place(x=30, y=50)
process_entry.place(x=190, y=50)



#buttons
Button(main, text="Start", command=lambda:[start(), clear()]).place(x=100, y=125)   #250
Button(main, text="End", command=lambda:[end(), clear()]).place(x=230, y=125)        #80



#quit
main.mainloop()
