'''
解决数独游戏的程序
'''

from sudosettings import LENGTH
from sudopreprocess import preprocess
from sudoexcelinput import getquizfromexcel
from tkinter import *
import tkinter_performance as tp

def showQuiz():
    for item in quiz:
        print(item)

def checkrcb(num, tuple):
    # 测试num 在序号为tuple的位置在横竖九宫里是不是唯一值。
    row, col = tuple
    rowL = []
    colL = []
    blockL = []
    for j  in range(LENGTH):
        if j == col:
            continue
        rowL.append(quiz[row][j])
    
    for i in range(LENGTH):
        if i == row:
            continue
        colL.append(quiz[i][col])
    
    for i in range(row//3*3, row//3*3+3):
        for j in range(col//3*3,col//3*3+3):
            if i == row and j == col:
                continue
            blockL.append(quiz[i][j])       
    return num not in rowL and num not in colL and num not in blockL

def findnextblanktuple(tuple):
    row,col = tuple
    nextrow = row
    nextcol = col+1
    while True:        
        if nextcol >= LENGTH:
            nextcol = 0
            if nextrow +1 <LENGTH:
                nextrow = nextrow +1
            else:
                return None
        if quiz[nextrow][nextcol] != 0:
            nextrow = nextrow
            nextcol = nextcol +1
            # if (nextrow, nextcol) not in unsolvedtuple:
            #     unsolvedtuple.append(nextrow,nextcol)
        else:
            return nextrow,nextcol
      
def trueNum(tuple):
    row ,col  = tuple
    for n in range(1,LENGTH+1):
        if checkrcb(n,tuple): 
            quiz[row][col] = n
            nexttuple = findnextblanktuple(tuple)
            if nexttuple is None:
                # quiz[row][col] = n
                return True
            else:
                if trueNum(nexttuple):
                    # quiz[row][col] = n
                    return True                  
    quiz[row][col] = 0
    return False

def inputquiz(quiz):
    i = 0
    while i<LENGTH:
        tmp = []
        inputLine = input('Enter line{0} (0 stands for blank):\n'.format(i+1))
        for c  in inputLine:
            tmp.append(int(c))
        while len(tmp)<LENGTH:
            tmp.append(0)
        quiz.append(tmp)
        i += 1
    

# 1.输入谜题
if __name__ == '__main__':
    quiz = []
    # LENGTH = 9
    # 手动输入quiz。
    # inputquiz(quiz) 
    
    getquizfromexcel(quiz)# 从excel表格中导入
    # pre_solve_quiz = quiz[:]
    root = Tk()
    # 提前处理
    # tp.gui_show(pre_solve_quiz,root)
    preprocess(quiz)
    # 2.求解过程

    starttuple = (0,0)
    if quiz[0][0] !=0:
        starttuple = findnextblanktuple((0,0))

    trueNum(starttuple)
    # 3.输出结果
    tp.gui_show(quiz,root)
    showQuiz()
    root.mainloop()
    
