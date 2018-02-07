from Tkinter import *
import ttk
import random

master = Tk()
master.title('Lucky Draw')

cn = 1

#frame1
frame1 = Frame(master)
frame1.pack()

label_award = Label(frame1,text="Award")
label_award.grid(row=0)


number = StringVar()
numberChosen = ttk.Combobox(frame1,textvariable=number)
numberChosen['values']=("First Prize","Second Prize","Third Prize")
numberChosen.grid(row=0,column=1)
numberChosen.current(0)


#e = Entry(frame1)
#e.grid(row=0, column=1)

label_winner = Label(frame1,text="List of Winners")
label_winner.grid(row=1)

#separtor
#ttk.Separator(master,orient=HORIZONTAL).grid(row=2)
#separator = Frame(master,height=1,bg="yellow")
#separator.pack(fill=X)


#entry
#d = Entry(master)
#d.pack(fill=X)

listbox = Listbox(master)
listbox.pack()



def update_status():
    global cn

    if cn==0:
        print "end"
        cn = 1
        return 1
    else:
        listbox.delete(0,END)
        slice = random.sample(range(1,100),5)
        #cn += 1
        #print cn
        for i in slice:
            listbox.insert(END,i)
        #const += 1
        master.after(30,update_status)

def end_status():
    global cn
    cn = 0
    return


#frame3
frame3 = Frame(master)
frame3.pack()

Start_button = Button(frame3, text="Start",command=update_status)
Start_button.pack(side=LEFT)
#Start_button.bind('<Button-1>',update_status)
#Start_button.bind('<Double-1>',test)


End_button = Button(frame3, text="End",command=end_status)
End_button.pack(side=LEFT)

#master.after(1,update_status)
mainloop()
