'''
数独游戏的前期正常处理
'''

from sudosettings import LENGTH


def preprocess(quiz):
    '''
    思路1：按顺序查询空格，或存在行、列、九宫只有唯一值的，则确定该格的值。循环，直至没有新的解产生，则结束。
    思路2：空格全填上1-9，考察有值的格子，消除行、列、九宫所在的空格的数字，若最后消的只有唯一值了，则该值为空格的值。
    
    '''
    
    # 思路2：
    # 所有空格变集合1-9
    for row in range(LENGTH):
        for col in range(LENGTH):
            if  quiz[row][col] == 0:
                quiz[row][col] = set(range(1,10))
    # 清洗，按现有值进行集合消减。
  
    while True:
        flag = 0
        for row in range(LENGTH):
            for col in range(LENGTH):
                if isinstance(quiz[row][col],set):
                    if len(quiz[row][col]) == 1:
                        quiz[row][col] = quiz[row][col].pop()
                        clean((row,col),quiz)
                        flag = 1
                else:
                    clean((row,col),quiz)
                    # flag = 1
        if flag == 0:
            break
    for row in range(LENGTH):
        for col in range(LENGTH):
            if  isinstance(quiz[row][col],set):
                quiz[row][col] = 0
                
                    
                
def clean(tuple,quiz):
    row,col = tuple
    for j  in range(LENGTH):
        if j == col:
            continue
        if isinstance(quiz[row][j],set):
            # quiz[row][j].remove(quiz[row][col])
            quiz[row][j] = quiz[row][j] - {quiz[row][col]}
    
    for i in range(LENGTH):
        if i == row:
            continue
        if isinstance(quiz[i][col],set):
            # quiz[i][col].remove(quiz[row][col])
            quiz[i][col] = quiz[i][col] - {quiz[row][col]}
    
    for i in range(row//3*3, row//3*3+3):
        for j in range(col//3*3,col//3*3+3):
            if i == row and j == col:
                continue
            if isinstance(quiz[i][j],set):
                # quiz[i][j].remove(quiz[row][col])
                quiz[i][j] = quiz[i][j] - {quiz[row][col]}
 
                
if __name__ == '__main__':
    quiz = []
    # LENGTH = 9
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
    # quiz = [
    #     [0,2,0,0,0,7,3,6,0],
    #     [3,0,0,0,4,0,0,0,0],
    #     [0,0,5,9,0,0,0,2,0],
    #     [0,0,0,0,0,9,0,0,0],
    #     [0,8,0,0,0,0,0,7,2],
    #     [2,6,0,5,0,4,0,0,0],
    #     [0,1,2,0,0,0,0,0,0],
    #     [7,0,6,2,3,0,1,0,8],
    #     [0,0,0,0,0,0,0,0,5]
    # ]
    preprocess(quiz)
    for item in quiz:
        print(item)
    

    
                 