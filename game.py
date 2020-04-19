import pygame
import point_n_rect as pnr
import poker_hands as pkhand

pygame.init()

TABLE     = (  0,128,  0)
BLACK     = (  0,  0,  0)
WHITE     = (255,255,255)
RED       = (255,  0,  0)
BROWN     = (150, 75,  0)
LIGHTBLUE = ( 75,137,220)
win_size  = [1280,960]
screen = pygame.display.set_mode(win_size)
screen.fill(WHITE)
pygame.display.set_caption("Poker Game")

run = True
clock = pygame.time.Clock()

class Button():
    def __init__(self, color, position, width, height, text = ''):
        self.color = color
        self.posn = position
        self.width = width
        self.height = height
        self.text = text
    def draw(self, window, outline=None):
        if outline:
            pygame.draw.rect(window, outline, (self.posn.x-2,self.posn.y-2,self.width+4,self.height+4), 0)
        pygame.draw.rect(window, self.color, (self.posn.x, self.posn.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            window.blit(text, (self.posn.x + (self.width/2 - text.get_width()/2), self.posn.y + (self.height/2 - text.get_height()/2)))
    
    def isOver(self, pos):
        if self.posn.x < pos[0] and pos[0] <self.posn.x +self.width:
            if self.posn.y < pos[1] <self.posn.y + self.height:
                return True
        return False
class Table():
    def __init__(self, color, win_size):
        self.color = color
        self.x = 0
        self.y = win_size[1]/2 - win_size[1]/15
        self.width = win_size[0]
        self.height = win_size[1]-self.y
    
    def draw(self, window, boarder = BROWN):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), 0)
        pygame.draw.rect(window, boarder, (self.x, self.y, self.width, self.height/10), 0)
    def put_on_card(self):
        pass
startButton = Button(LIGHTBLUE, pnr.Point(515, 630), 250, 100, 'Start!')
pokertable = Table(TABLE, win_size)
ready = True
click_pos=()
while run:
    # This limits the while loop to a max of 30 time per second
    # 30fps
    clock.tick(30)

    # Main Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            if startButton.isOver(pos):
                print("pressed")
                ready = False
    screen.fill(WHITE)
    pokertable.draw(screen)
    if ready:
        startButton.draw(screen, BROWN)
    # This MUST happen after all the other drawing commands
    pygame.display.update()
pygame.quit()

