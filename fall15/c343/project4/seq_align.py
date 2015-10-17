#! /usr/bin/env python

import sys, time, random
import pygame

# string of unique letters in the english alphabet
e_aplh = "abcdefghijklmnopqrstuvwxyz"
# string of unique possible chars in a DNA sequence
dna_alph = "ACGT"

# generate random string drawn from the given alphabet and of a given length
def gen_random_string(alphabet, length):
    # find the length of the given alphabet
    a_len = len(alphabet)
    # initialize a return string
    ret = ""
    # at each index of length given:
    for n in range(length):
        # add a random element from the given alphabet to the return string
        ret += alphabet[random.randint(0, a_len-1)]
    # return the string
    return ret

# print gen_random_string(e_aplh, 5)

SPACE_CHAR = '_'
SPACE_PENALTY = -1

# the scoring function (takes a pair of chars)
def s(x, y):
    # if either is a blank, return -1
    if x == SPACE_CHAR or y == SPACE_CHAR:
        return SPACE_PENALTY
    # if they're a match, return +2
    elif x == y:
        return 2
    # if they're a mismatch, return -2
    else:
        return -2

TILE_SIZE = 40
tile_color = (255, 255, 255)
highlight_color = (120, 129, 250)

def init_board(m, n):
    screen = pygame.display.set_mode(((m+2)*TILE_SIZE, (n+2)*TILE_SIZE))
    screen.fill((0, 0, 0))
    pygame.display.set_caption('Dot Board')
    pygame.font.init()
    font = pygame.font.Font(None, 15)
    return screen, font

def create_tile(font, text, color):
    tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
    tile.fill(color)
    b1 = font.render(text, 1, (0, 0, 0))
    tile.blit(b1, (TILE_SIZE/2, TILE_SIZE/2))
    return tile

# takes a board (screen), font, sequence1, sequence2, 
# and F, a dictionary which has the (coordinate, pairs) as keys and a score as the value.
def render_board(board, font, s1, s2, F):
    for i in range(len(s1)):
        tile = create_tile(font, s1[i], tile_color)
        board.blit(tile, ((i+2)*TILE_SIZE, 0))
    tile = create_tile(font, '', tile_color); board.blit(tile, (0, 0))
    tile = create_tile(font, '', tile_color); board.blit(tile, (TILE_SIZE, 0))
    for j in range(len(s2)):
        tile = create_tile(font, s2[j], tile_color)
        board.blit(tile, (0, (j+2)*TILE_SIZE))
    tile = create_tile(font, '', tile_color); board.blit(tile, (0, TILE_SIZE))
    for (x,y) in sorted(F.keys()):
        tile = create_tile(font, str(F[(x,y)]), tile_color)
        board.blit(tile, ((x+1)*TILE_SIZE, (y+1)*TILE_SIZE))
    

def seq_align(s1, s2, enable_graphics=True):
    # final dictionary of key: (coordinate pair) and value: (best score)
    F = {(0,0):0}
    # dictionary to track how to reverse engineer the optimal alignments
    R = {(0,0):None}
    # initialize two lists for return values:
    t1,t2 = "",""

    # for every (x,y) coordinate on the board
    for x in range(len(s1)+1):
        for y in range(len(s2)+1):
            # fill out the (0,y) row and (x,0) column with correct SPACE_PENALTY
            if x == 0:
                F[(0,y)]=y*SPACE_PENALTY
                assert F[(0,y)]==y*SPACE_PENALTY
                # record the direction we came from (above = seq2 blank)
                R[(0,y)]='above'
                assert R[(0,y)]=='above'
            elif y == 0:
                F[(x,0)]=x*SPACE_PENALTY
                assert F[(x,0)]==x*SPACE_PENALTY
                #  record the direction we came from
                R[(x,0)]='left'
                assert R[(x,0)]=='left'

            elif x>0 and y>0:
                # result of scoring function
                M = s(s1[x-1],s2[y-1])
                # match/mismatch case
                A = F[(x-1, y-1)] + M
                # Insert (blank in sequence 2)
                B = F[(x,y-1)] + SPACE_PENALTY
                # Delete (blank in sequence 1)
                C = F[(x-1, y)] + SPACE_PENALTY
                # Use the maximum score as key value
                score = max(A,B,C)
                F[(x,y)] = score
                # coming from left (s2 stays the same, s1 gets a blank)
                if score == A:
                    R[(x,y)]='diagonal'
                elif score == B:
                    R[(x,y)]= 'above'
                # coming from above (s1 stays the same, s2 gets a blank)
                elif score == C:
                    R[(x,y)] = 'left'
                else:
                    print 'this shouldnt happen'
                    exit(-1)
            else:
                print 'you shouldnt be here'
                exit(-1)
   
    i,j = len(s1),len(s2)
    while i>-1 and j>-1:
        if i==0 and j==0:
            break
        # came from diagonal
        if R[(i,j)]=='diagonal':
            t1 += s1[i-1]
            t2 += s2[j-1]
            i,j = i-1,j-1
        # came from the left (blank in sequence 2)
        elif R[(i,j)] == 'left':
            t1 += s1[j-1]
            t2 += SPACE_CHAR
            i,j = i-1, j
        # came from above (blank in sequence 1)
        elif R[(i,j)]=='above':
            t1 += SPACE_CHAR
            t2 += s2[j-1]
            i,j = i, j-1
        else:
            print "you shouldnt be here"
            exit(-1)

    if enable_graphics:
        screen,font = init_board(len(s1),len(s2))
        render_board(screen, font, s1, s2, F)
        pygame.display.flip()
        time.sleep(2)

    #r1,r2 = str(t1[::-1]),str(t2[::-1])
    # show the sequences aligned:
    #print r1+'\n'+r2
    
    # return the reverse of strings derived from retracing process
    return (t1[::-1],t2[::-1])

def bestSoln(orig_a1, orig_a2, ret_a1, ret_a2, a1, a2):
    if len(ret_a1) != len(ret_a2):
        return False
    ansScore = 0
    for ctr in range(len(a1)):
        ansScore += s(a1[ctr], a2[ctr])
    retScore = 0
    for ctr in range(len(ret_a1)):
        retScore += s(ret_a1[ctr], ret_a2[ctr])
    if retScore > ansScore:
        return False
    orig_ctr = 0
    for ctr in range(len(ret_a1)):
        if ret_a1[ctr] != "_":
            if ret_a1[ctr] != orig_a1[orig_ctr]:
                return False
            orig_ctr += 1
    orig_ctr = 0
    for ctr in range(len(ret_a2)):
        if ret_a2[ctr] != "_":
            if ret_a2[ctr] != orig_a2[orig_ctr]:
                return False
            orig_ctr += 1
    return True

# if the file is run with argument 'test'
if len(sys.argv) == 2 and sys.argv[1] == 'test':
    # assign a txt file to variable f with read permissions; assign the result of reading the txt file to variable tests; close the file 
    f=open('tests.txt', 'r');tests= eval(f.read());f.close()
    cnt = 0; passed = True
    # print tests
    for ((s1, s2), (a1, a2)) in tests:
        (ret_a1, ret_a2) = seq_align(s1, s2, False)
        #if (ret_a1 != a1) or (ret_a2 != a2):
        if( not bestSoln(s1, s2, ret_a1, ret_a2, a1, a2) ):
            print s1, s2 
            print a1, a2
            print ret_a1, ret_a2
            print("test#" + str(cnt) + " failed...")
            passed = False
        cnt += 1
    if passed: print("All tests passed!")
elif len(sys.argv) == 2 and sys.argv[1] == 'gentests':
    tests = []
    for n in range(25):
        m = random.randint(8, 70); n = random.randint(8, 70)
        (s1, s2) = (gen_random_string(dna_alph, m), gen_random_string(dna_alph, n))
        (a1, a2) = seq_align(s1, s2, False)
        tests.append(((s1, s2), (a1, a2)))
    f=open('tests.txt', 'w');f.write(str(tests));f.close()
else:
    if __name__ == "__main__":
        assert __name__ == "__main__"
        assert s('A','C') == -2

        # l = [('AC','CA')]
        # l = [('ACAC','AGCA')]
        l = [('ACACACTA', 'AGCACACA'), ('IMISSMISSISSIPI', 'MYMISSISAHIPPIE')]
        enable_graphics = True
        if enable_graphics: pygame.init()
        for (s1, s2) in l:
            print 'sequences:'
            print (s1, s2)
            m = len(s1)
            n = len(s2)
            print 'alignment: '
            print seq_align(s1, s2, enable_graphics)   
        
        if enable_graphics: pygame.quit()