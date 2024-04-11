import pygame
import sudosolution as ss
from sudopreprocess import preprocess


sc_width = 800
sc_height = 600
b_width = 60

def getquiz():
    quiz = []
    ss.inputquiz(quiz)
    return quiz

def solvesodu(quiz):
    preprocess(quiz)
    starttuple = (0,0)
    if quiz[0][0] !=0:
        starttuple = ss.findnextblanktuple((0,0),quiz)

    ss.trueNum(starttuple,quiz)
    # 3.输出结果
    
    ss.showQuiz(quiz)




def main():
    quiz = getquiz()
    solvesodu(quiz)

    pygame.init()
    screen = pygame.display.set_mode((sc_width,sc_height))
    pygame.display.set_caption('Sudo Game')

    startpoint = ((sc_width-9*b_width)//2, (sc_height-9*b_width)//2)
    
    

    for i in range(10):
        if i % 3 == 0:
            line_w = 2
        else:
            line_w = 1
        pygame.draw.line(screen, 'green', (startpoint[0]+i*b_width, startpoint[1]), (startpoint[0]+i*b_width, startpoint[1]+9*b_width),width=line_w)
        pygame.draw.line(screen, 'green', (startpoint[0], startpoint[1]+b_width*i), (startpoint[0]+ 9*b_width, startpoint[1]+b_width*i),width=line_w)
    
    

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
        pygame.display.update()





if __name__ == "__main__":
    main()
    pygame.quit()