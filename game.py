import pygame
import point_n_rect as pnr
import poker_hands as pkhand
import random

TABLE     = (  0,128,  0)
BLACK     = (  0,  0,  0)
WHITE     = (255,255,255)
RED       = (255,  0,  0)
BROWN     = (150, 75,  0)
LIGHTBLUE = ( 75,137,220)
win_size  = [1280,960]

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

class Card():

    def __init__(self, card_tuple, *args):
        self.posn = pnr.Point(args[0], args[1])
        self.rect = pnr.Rectangle(self.posn, win_size[0]*(3/20), win_size[0]*(3/20)*(88/62))
        self.card = card_tuple
        self.upsidedown = True
    pass

class Table():

    def __init__(self, color, win_size):
        self.color = color
        self.x = 0
        self.y = win_size[1]/2 - win_size[1]/15
        self.width = win_size[0]
        self.height = win_size[1]-self.y
        self.card_width = self.width*(3/20)
        self.card_height = self.height*(72/100)
        self.card_on_table = []
    
    def draw(self, window, boarder = BROWN):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), 0)
        pygame.draw.rect(window, boarder, (self.x, self.y, self.width, self.height/10), 0)
    
    def put_on_card(self, card_tuple):
        idx = len(self.card_on_table)
        x_pos = self.x + (1 + idx)*self.width*(1/24) + len(self.card_on_table)*self.card_width
        y_pos = (self.y+self.height/10) + self.height*(9/100)
        self.card_on_table.append(Card(card_tuple, x_pos, y_pos))
        
    def draw_card(self, window, idx, upsidedown):
        if upsidedown:
            pygame.draw.rect(window, WHITE, (self.card_on_table[idx].posn.x, self.card_on_table[idx].posn.y, self.card_on_table[idx].rect.width, self.card_on_table[idx].rect.height), 0)
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render('back', 1, (0,0,0))
            window.blit(text, (self.card_on_table[idx].posn.x + (self.card_on_table[idx].rect.width/2 - text.get_width()/2), self.card_on_table[idx].posn.y + (self.card_on_table[idx].rect.height/2 - text.get_height()/2)))
        else:
            pygame.draw.rect(window, WHITE, (self.card_on_table[idx].posn.x, self.card_on_table[idx].posn.y, self.card_on_table[idx].rect.width, self.card_on_table[idx].rect.height), 0)
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(str(self.card_on_table[idx].card), 1, (0,0,0))
            window.blit(text, (self.card_on_table[idx].posn.x + (self.card_on_table[idx].rect.width/2 - text.get_width()/2), self.card_on_table[idx].posn.y + (self.card_on_table[idx].rect.height/2 - text.get_height()/2)))

pygame.init()

screen = pygame.display.set_mode(win_size)
screen.fill(WHITE)
pygame.display.set_caption("Poker Game")

run = True
clock = pygame.time.Clock()

startButton = Button(LIGHTBLUE, pnr.Point(515, 630), 250, 100, 'Start!')
pokertable = Table(TABLE, win_size)
ready = True
card_set = pkhand.card_set
random.shuffle(card_set)
on_table = 0

while run:
    # This limits the while loop to a max of 30 time per second
    # 30fps
    clock.tick(30)

    # Main Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:      #마우스 클릭시
            pos = pygame.mouse.get_pos()                #pos 에 마우스 좌표값 저장(tuple)
            print(pos)
            if startButton.isOver(pos):
                print("pressed")
                ready = False
            if ready == False:
                for card in pokertable.card_on_table:
                    if card.rect.contains(pnr.Point(pos[0],pos[1])):
                        card.upsidedown = False
    screen.fill(WHITE)
    pokertable.draw(screen)
    if ready:
        startButton.draw(screen, BROWN)
    else:
        if on_table < 5:
            pokertable.put_on_card(card_set.pop())
            on_table += 1
            pygame.time.wait(100)
        for i in range(len(pokertable.card_on_table)):
            pokertable.draw_card(screen, i, pokertable.card_on_table[i].upsidedown)

    # This MUST happen after all the other drawing commands
    pygame.display.update()
pygame.quit()

