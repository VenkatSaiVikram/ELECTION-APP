import time
from tkinter import *
from tkinter import messagebox

main=Tk()
main.title("Election")
main.geometry("800x600")
main.resizable(height=False,width=False)
main.configure(bg="#000000")

candidate1_votes=0
candidate2_votes=0
candidate3_votes=0

no_of_votes=0

def cast1():
	global candidate1_votes
	global candidate2_votes
	global candidate3_votes
	global no_of_votes
	candidate1_votes+=1
	no_of_votes+=1
	votes.configure(text="Number of votes casted : "+str(no_of_votes))
	time.sleep(10)

def cast2():
	global candidate1_votes
	global candidate2_votes
	global candidate3_votes
	global no_of_votes
	candidate2_votes+=1
	no_of_votes+=1
	votes.configure(text="Number of votes casted : "+str(no_of_votes))
	time.sleep(10)

def cast3():
	global candidate1_votes
	global candidate2_votes
	global candidate3_votes
	global no_of_votes
	candidate3_votes+=1
	no_of_votes+=1
	votes.configure(text="Number of votes casted : "+str(no_of_votes))
	time.sleep(10)

title=Label(main,text="ELECTION",bg="#000000",fg="#FFFFFF",font=("Consolas",32))
title.pack(pady=30)

msg=Label(main,text="Cast your Vote below",bg="#000000",fg="#FFFFFF",font=("Consolas",16))
msg.pack(pady=10)

candidate1=Button(main,text="Candidate-1",height=10,width=25,font=("Consolas",10),command=cast1)
candidate1.place(x=60,y=225)

candidate2=Button(main,text="Candidate-2",height=10,width=25,font=("Consolas",10),command=cast2)
candidate2.place(x=300,y=225)

candidate2=Button(main,text="Candidate-3",height=10,width=25,font=("Consolas",10),command=cast3)
candidate2.place(x=550,y=225)

votes=Label(main,text="Number of votes casted : "+str(no_of_votes),bg="#000000",fg="#FFFFFF",font=("Consolas",16))
votes.place(x=225,y=425)

def result():
	if candidate1_votes>candidate2_votes and candidate1_votes>candidate3_votes:
		messagebox.showinfo("RESULT","ELECTION ENDED!\n--------------------------\nCANDIDATE-1 - "+str(candidate1_votes)+"\nCANDIDATE-2 - "+str(candidate2_votes)+"\nCANDIDATE-3 - "+str(candidate3_votes)+"\n--------------------------\nCANDIDATE-1 IS THE WINNER!")

	elif candidate2_votes>candidate1_votes and candidate2_votes>candidate3_votes:
		messagebox.showinfo("RESULT","ELECTION ENDED!\n--------------------------\nCANDIDATE-1 - "+str(candidate1_votes)+"\nCANDIDATE-2 - "+str(candidate2_votes)+"\nCANDIDATE-3 - "+str(candidate3_votes)+"\n--------------------------\nCANDIDATE-2 IS THE WINNER!")

	elif candidate3_votes>candidate1_votes and candidate3_votes>candidate2_votes:
		messagebox.showinfo("RESULT","ELECTION ENDED!\n--------------------------\nCANDIDATE-1 - "+str(candidate1_votes)+"\nCANDIDATE-2 - "+str(candidate2_votes)+"\nCANDIDATE-3 - "+str(candidate3_votes)+"\n--------------------------\nCANDIDATE-3 IS THE WINNER!")

end=Button(main,text="END ELECTION",height=3,width=20,font=("Consolas",10),command=result)
end.place(x=325,y=500)

main.mainloop()