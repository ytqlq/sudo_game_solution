import pygame
import sudosolution as ss
from sudopreprocess import preprocess


sc_width = 800
sc_height = 600
b_width = 60
fontsize = 40
font_color = 'red'

class Shuzi():
    def __init__(self,num,screen,fontrect) -> None:
        self.c_font = pygame.font.SysFont("Arial",fontsize)
        
        self.num = num
        self.screen = screen
        self.fontrect = fontrect
        self.fontsurface = self.c_font.render(str(self.num),True,font_color)
    def writeshuzi(self):
        
        
        # print(fontsurface.get_size())
        self.screen.blit(self.fontsurface, self.fontrect)
    


def getquiz():
    quiz = []
    ss.inputquiz(quiz)
    return quiz

def pygameshowquiz(quiz,screen:pygame.Rect,sp):
    
    # print(quiz)
    for i in range(9):
        for j in range(9):
            num = quiz[i][j]
            fontrect = pygame.Rect((sp[0]+j*b_width, sp[1]+i*b_width),(b_width,b_width))            
            sz = Shuzi(num,screen,fontrect)
            fw, fh = sz.fontsurface.get_size()
            fontrect.move_ip((b_width-fw)//2, (b_width-fh)//2)
            sz.writeshuzi()

            

def solvesodu(quiz):
    preprocess(quiz)
    starttuple = (0,0)
    if quiz[0][0] !=0:
        starttuple = ss.findnextblanktuple((0,0),quiz)

    ss.trueNum(starttuple,quiz)
    # 3.输出结果
    
    # ss.showQuiz(quiz)
    




def main():
    quiz = getquiz()
    solvesodu(quiz)

    pygame.init()
    screen = pygame.display.set_mode((sc_width,sc_height))
    pygame.display.set_caption('Sudo Game')

    startpoint = ((sc_width-9*b_width)//2, (sc_height-9*b_width)//2)
    # screen.blit()
    

    for i in range(10):
        if i % 3 == 0:
            line_w = 2
        else:
            line_w = 1
        pygame.draw.line(screen, 'green', (startpoint[0]+i*b_width, startpoint[1]), (startpoint[0]+i*b_width, startpoint[1]+9*b_width),width=line_w)
        pygame.draw.line(screen, 'green', (startpoint[0], startpoint[1]+b_width*i), (startpoint[0]+ 9*b_width, startpoint[1]+b_width*i),width=line_w)
    pygameshowquiz(quiz,screen,startpoint)
    

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
        pygame.display.update()





if __name__ == "__main__":
    main()
    pygame.quit()