from tkinter import *
user = "X"


root = Tk()
root.title("TIC TAC TOE")
title= Label(root,text="Tic Tac Toe",fg="red")
title.grid(row=0,column=1)

winner = Label(root,text="")
winner.grid(row=2,column=1)





#create click function 
def click(button):
    global user
    button.config(text=user)
    if user == "X":
        user = "O"
    else:
        user = "X"
    #call the function whether the condition were already met   
    check_win()


#check the Winner
def check_win():
    win = "X"
    if b1.cget("text") == b2.cget("text") == b3.cget("text") == win:
        winner.config(text="Player 1 Wins")
    elif b1.cget("text") == b4.cget("text") == b7.cget("text") == win:
        winner.config(text="Player 1 Wins")
    elif b1.cget("text") == b5.cget("text") == b9.cget("text") == win:
        winner.config(text="Player 1 Wins")
    elif b2.cget("text") == b5.cget("text") == b8.cget("text") == win:
        winner.config(text="Player 1 Wins")
    elif b3.cget("text") == b6.cget("text") == b9.cget("text") == win:
        winner.config(text="Player 1 Wins")
    elif b3.cget("text") == b5.cget("text") == b7.cget("text") == win:
        winner.config(text="Player 1 Wins")
    elif b4.cget("text") == b5.cget("text") == b6.cget("text") == win:
        winner.config(text="Player 1 Wins")
    elif b7.cget("text") == b8.cget("text") == b9.cget("text") == win:
        winner.config(text="Player 1 Wins")
    else:
        win = "O"
        if b1.cget("text") == b2.cget("text") == b3.cget("text") == win:
            winner.config(text="Player 2 Wins")
        elif b1.cget("text") == b4.cget("text") == b7.cget("text") == win:
            winner.config(text="Player 2 Wins")
        elif b1.cget("text") == b5.cget("text") == b9.cget("text") == win:
            winner.config(text="Player 2 Wins")
        elif b2.cget("text") == b5.cget("text") == b8.cget("text") == win:
            winner.config(text="Player 2 Wins")
        elif b3.cget("text") == b6.cget("text") == b9.cget("text") == win:
            winner.config(text="Player 2 Wins")
        elif b3.cget("text") == b5.cget("text") == b7.cget("text") == win:
            winner.config(text="Player 2 Wins")
        elif b4.cget("text") == b5.cget("text") == b6.cget("text") == win:
            winner.config(text="Player 2 Wins")
        elif b7.cget("text") == b8.cget("text") == b9.cget("text") == win:
            winner.config(text="Player 2 Wins")

	


b1 = Button(root,text="",bg="white",width=10,height=5,command=lambda:click(b1))

b2 = Button(root,text="",bg="white",width=10,height=5,command=lambda:click(b2))

b3 = Button(root,text="",bg="white",width=10,height=5,command=lambda:click(b3))


b4 = Button(root,text="",bg="white",width=10,height=5,command=lambda:click(b4))


b5 = Button(root,text="",bg="white",width=10,height=5,command=lambda:click(b5))


b6 = Button(root,text="",bg="white",width=10,height=5,command=lambda:click(b6))


b7 = Button(root,text="",bg="white",width=10,height=5,command=lambda:click(b7))


b8 = Button(root,text="",bg="white",width=10,height=5,command=lambda:click(b8))


b9 = Button(root,text="",bg="white",width=10,height=5,command=lambda:click(b9))



b1.grid(row=5,column=0)
b2.grid(row=5,column=1)
b3.grid(row=5,column=2)
b4.grid(row=6,column=0)
b5.grid(row=6,column=1)
b6.grid(row=6,column=2)
b7.grid(row=7,column=0)
b8.grid(row=7,column=1)
b9.grid(row=7,column=2)

if check_win():
	reset()

def reset():
	global user
	user = "X"
	winner.config(text="")
	for Button in buttons:
		Button.config(text="")

buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9]


reset= Button(root,text="RESET",command=reset)
reset.grid(row=1,column=0)




root.mainloop()