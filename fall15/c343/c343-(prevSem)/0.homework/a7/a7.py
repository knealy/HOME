import pygame
from pygame import *
from random import *
import copy

#-----------------------------------------------------------------------------
# colors

class C : 
    def __init__ (self,name,rgb) :
        self.name = name
        self.rgb = rgb

    def __eq__ (self, other) :
        return self.name == other.name

    def __repr__ (self) :
        return self.name

PINK   = C("pink",   (255, 105, 180))
VIOLET = C("violet", (138, 43,  226))
YELLOW = C("yellow", (255, 255, 0))
RED    = C("red",    (255, 69,  0))
OLIVE  = C("olive",  (110, 139, 61))
BLUE   = C("blue",   (0,   191, 255))

class Colors : 
    def __init__ (self, colors=None) :
        if colors :
            self.colors = colors
        else :
            self.colors = \
                { 'pink'   : PINK, \
                  'violet' : VIOLET, \
                  'yellow' : YELLOW, \
                  'red'    : RED, \
                  'olive'  : OLIVE, \
                  'blue'   : BLUE }

    def random (self) : 
        ks = self.colors.keys()
        return self.colors[choice(ks)]

#-----------------------------------------------------------------------------
# tiles

class Tile :
    def __init__ (self,x,y,color,size=None) :
        self.x = x
        self.y = y
        self.color = color
        if size :
            self.size = size
        else :
            self.size = 32

    def updateColor (self, c) :
        self.color = c

    def draw (self, screen) :
        t = pygame.Surface((self.size,self.size))
        t.fill(self.color.rgb)
        screen.blit(t, (self.size*self.x,self.size*self.y))

    def __repr__ (self) :
        return repr(self.color)

#-----------------------------------------------------------------------------
# main class: the board

class Board : 
    def __init__ (self,n=None,colors=None,tiles=None) :
        if n and colors :
            self.n = n
            self.colors = colors
            self.tiles = [None]*n
            for x in range(n) :
                self.tiles[x] = [None]*n
                for y in range(n) :
                    self.tiles[x][y] = Tile(x,y,colors.random())
        elif tiles :
            self.n = len(tiles)
            self.tiles = tiles
            cs = {}
            for x in range(self.n) :
                for y in range(self.n) :
                    tile = self.tiles[x][y]
                    if tile.color.name not in cs :
                        cs[tile.color.name] = tile.color
            self.colors = Colors(cs)
        else :
            raise Exception
        self.flooded = set([self.tiles[0][0]])

    def draw (self, screen) :
        for x in range(self.n) :
            for y in range(self.n) :
                self.tiles[x][y].draw(screen)

    #----------------------- METHODS TO IMPLEMENT ----------------------------
    
    
    def floodFill(self, x, y, c):
        if x != 0:
            left = self.tiles[x-1][y]
            if left not in self.flooded:
                if left.color == c:
                    self.flooded.add(left)
                    self.floodFill(left.x,left.y,c)
        if y != 0:
            up = self.tiles[x][y-1]
            if up not in self.flooded:
                if up.color == c:
                    self.flooded.add(up)
                    self.floodFill(up.x,up.y,c)
        if x != len(self.tiles)-1:
            right = self.tiles[x+1][y]
            if right not in self.flooded:
                if right.color == c:
                    self.flooded.add(right)
                    self.floodFill(right.x,right.y,c)
        if y != len(self.tiles)-1:
            down = self.tiles[x][y+1]
            if down not in self.flooded:
                if down.color == c:
                    self.flooded.add(down)
                    self.floodFill(down.x,down.y,c)
        
            
    
    def move (self,c) :
        # to complete!
        # self.flooded = {start:[self.tiles[0][0]]}
        for tile in self.flooded.copy():
            tile.updateColor(c)
            self.floodFill(tile.x,tile.y,c)
            
    def neighbors (self,x,y):
        if x != 0:
            left = self.tiles[x-1][y]
            if left not in self.flooded:
                self.flooded.add(left)
                self.floodFill(left.x,left.y,c)
    
    def greedy1 (self) : 
        
        # to fix

    def greedy2 (self) : 
        
        # to fix

    def greedy3 (self) : 
        return YELLOW
        # to fix

    #-------------------- END OF METHODS TO IMPLEMENT ------------------------

    def __repr__ (self) :
        res = ""
        for x in range(self.n) :
            for y in range(self.n) :
                res += '{:<7}'.format(repr(self.tiles[x][y]))
            res += '\n'
        return res

#-----------------------------------------------------------------------------
# top-level wrapper class: game

class Game :
    def __init__ (self,n=None,colors=None,tiles=None) :
        pygame.init()
        self.screen = pygame.display.set_mode((608,448)) 
        # board
        self.board = Board(n,colors,tiles)
        self.board.draw(self.screen)
        # global parameters
        textfont = pygame.font.Font(None,18)
        textcolor = (187,187,187)
        # controls
        newgame_rect = pygame.Rect(540,32,32,25)
        newgame_text = textfont.render('New game',True,textcolor)
        self.screen.blit(newgame_text,newgame_rect)
        control_x,control_y = (576,72)
        for c in self.board.colors.colors.values() :
            pygame.draw.circle(self.screen,c.rgb,(control_x,control_y),16)
            control_y = control_y + 40
        control_x = 540
        hint_rect = pygame.Rect(control_x,control_y,32,25)
        hint_text = textfont.render('Hint I',True,textcolor)
        self.screen.blit(hint_text,hint_rect)
        control_y += 20
        hint_rect = pygame.Rect(control_x,control_y,32,25)
        hint_text = textfont.render('Hint II',True,textcolor)
        self.screen.blit(hint_text,hint_rect)
        control_y += 20
        hint_rect = pygame.Rect(control_x,control_y,32,25)
        hint_text = textfont.render('Hint III',True,textcolor)
        self.screen.blit(hint_text,hint_rect)
        # event loop
        quit = False
        while not quit :
            pygame.display.update()
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    quit = True
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN :
                    if newgame_rect.collidepoint(event.pos) :
                        self.board = Board(self.board.n,self.board.colors)
                        self.board.draw(self.screen)
                    else :
                        control_x,control_y = (576,72)
                        for c in self.board.colors.colors.values() :
                            r = pygame.Rect(control_x-16,control_y-16,32,32)
                            if r.collidepoint(event.pos) :
                                self.board.move(c)
                                self.board.draw(self.screen)
                                break
                            else :
                                control_y = control_y + 40
                        control_x = 540
                        r = pygame.Rect(control_x,control_y,32,25)
                        if r.collidepoint(event.pos) :
                            c = self.board.greedy1()
                            self.board.move(c)
                            self.board.draw(self.screen)
                            break                        
                        control_y += 20
                        r = pygame.Rect(control_x,control_y,32,25)
                        if r.collidepoint(event.pos) :
                            c = self.board.greedy2()
                            self.board.move(c)
                            self.board.draw(self.screen)
                            break                        
                        control_y += 20
                        r = pygame.Rect(control_x,control_y,32,25)
                        if r.collidepoint(event.pos) :
                            c = self.board.greedy3()
                            self.board.move(c)
                            self.board.draw(self.screen)
                            break                        
                        continue
                else :
                    continue
        pygame.quit()

#-----------------------------------------------------------------------------
# Test cases

if __name__ == "__main__" :

    def waitForQuit () : 
        quit = False
        while not quit :
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    quit = True
                    break
                else :
                    continue
        pygame.quit()

    def test_two_tiles () :
        pygame.init()
        screen = pygame.display.set_mode((608,448)) 
        colors = Colors()
        tile = Tile(5,2,BLUE)
        tile.draw(screen)
        tile = Tile(2,5,RED)
        tile.draw(screen)
        pygame.display.update()
        waitForQuit()

    sample_tiles = \
      [ [ Tile(0,0,PINK), Tile(1,0,VIOLET), Tile(2,0,YELLOW), Tile(3,0,RED), \
            Tile(4,0,VIOLET), Tile(5,0,YELLOW) ], \
        [ Tile(0,1,YELLOW), Tile(1,1,YELLOW), Tile(2,1,RED), Tile(3,1,OLIVE), \
            Tile(4,1,VIOLET), Tile(5,1,PINK) ], \
        [ Tile(0,2,RED), Tile(1,2,YELLOW), Tile(2,2,YELLOW), Tile(3,2,PINK), \
            Tile(4,2,VIOLET), Tile(5,2,YELLOW) ], \
        [ Tile(0,3,OLIVE), Tile(1,3,RED), Tile(2,3,YELLOW), Tile(3,3,BLUE), \
            Tile(4,3,VIOLET), Tile(5,3,PINK) ], \
        [ Tile(0,4,YELLOW), Tile(1,4,VIOLET), Tile(2,4,RED), Tile(3,4,YELLOW), \
            Tile(4,4,RED), Tile(5,4,YELLOW) ], \
        [ Tile(0,5,VIOLET), Tile(1,5,YELLOW), Tile(2,5,RED), Tile(3,5,PINK), \
            Tile(4,5,OLIVE), Tile(5,5,BLUE) ] ]

    def test_sample_board () :
        pygame.init()
        screen = pygame.display.set_mode((608,448)) 
        b = Board(tiles=sample_tiles)
        b.draw(screen)
        pygame.display.update()
        event = pygame.event.wait()
        waitForQuit()

    def test_random_board () :
        pygame.init()
        screen = pygame.display.set_mode((608,448)) 
        b = Board(14,Colors())
        b.draw(screen)
        pygame.display.update()
        event = pygame.event.wait()
        waitForQuit()

    def play_small () :
        Game(tiles=sample_tiles)

    def play () :
        Game(14,Colors())

#-----------------------------------------------------------------------------

play()
