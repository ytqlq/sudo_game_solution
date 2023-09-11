from tkinter import *


def gui_show(quiz,root):
    
    root.title("SudoGame")
    lf00 = LabelFrame(root,padx=20,pady=20)
    lf01 = LabelFrame(root,padx=20,pady=20,bd=5)
    lf02 = LabelFrame(root,padx=20,pady=20,bd=5)
    lf10 = LabelFrame(root,padx=20,pady=20,bd=5)
    lf11 = LabelFrame(root,padx=20,pady=20,bd=5)
    lf12 = LabelFrame(root,padx=20,pady=20,bd=5)
    lf20 = LabelFrame(root,padx=20,pady=20,bd=5)
    lf21 = LabelFrame(root,padx=20,pady=20,bd=5)
    lf22 = LabelFrame(root,padx=20,pady=20,bd=5)
    lfs = [lf00,lf01,lf02,lf10,lf11,lf12,lf20,lf21,lf22]
    
    for row in range(len(quiz)):
        for col in range(len(quiz[0])):            
            tx = str(quiz[row][col])
            if tx == '0':
                tx = ''
            ind = row//3*3+col//3
            Label(lfs[ind],text=tx,bd=10,relief=SUNKEN).grid(row=row%3,column=col%3)
    bn = Button(root,text="Solve the quiz")
    bn.grid(row=3,column=0,columnspan=3)
    lf00.grid(row=0,column=0,padx=20,pady=20)
    lf01.grid(row=0,column=1,padx=20,pady=20)
    lf02.grid(row=0,column=2,padx=20,pady=20)
    lf10.grid(row=1,column=0,padx=20,pady=20)
    lf11.grid(row=1,column=1,padx=20,pady=20)
    lf12.grid(row=1,column=2,padx=20,pady=20)
    lf20.grid(row=2,column=0,padx=20,pady=20)
    lf21.grid(row=2,column=1,padx=20,pady=20)
    lf22.grid(row=2,column=2,padx=20,pady=20)


if __name__ == '__main__':
    quiz = [ [i for i in range(1,10)] for j in range(9)]
    # print(quiz)
    root = Tk()
    gui_show(quiz,root)
    root.mainloop()













