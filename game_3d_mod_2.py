import pygame
import math as m
import pygame.freetype
from pygame.draw import *
from random import randint
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
black = (0, 0, 0)
screen = pygame.display.set_mode((1200, 600))

GAME_FONT = pygame.freetype.Font(None, 20)
GAME_FONT_1 = pygame.freetype.Font(None, 36)
#def cube_start(size, cx, cy, cz): # making first object, cx, cy, cz - coordinates of the center
    #cube_0[0] = (size + cx, size + cy, size + cz)
    #cube_0[1] = (-size + cx, size + cy, size + cz)
    #cube_0[2] = (-size + cx, -size + cy, size + cz)
    #cube_0[3] = (size + cx, -size + cy, size + cz)
    #cube_0[4] = (size + cx, size + cy, -size + cz) 
    #cube_0[5] = (-size + cx, size + cy, -size + cz)
    #cube_0[6] = (-size + cx, -size + cy, -size + cz) 
    #cube_0[7] = (size + cx, -size + cy, -size + cz)
#def hero(hx, hy, hz, cx, cy, cz, lx, ly, lz):
#    0
#def screen(alpha):
    

    
#def alpha(hx, hy, hz, cx, cy, cz, lx, ly, lz):
#    a = m.acos(((cx-hx)*lx + (cy-hy)*ly + (cz-hz)*lz)/((((cx-hx)**2 + (cy-hy)**2 + (cz-hz)**2)**2)*(l)))
#    return a
r = 0
l = 600
rad = 100*(2**0.5)

x_0 = 0
y_0 = -100
z_0 = 1500#800*(3**0.5)
x_0 = 0#800
x_p = 0
y_p = 0
z_p = 0

global n_dot
n_dot = 16

al = 0
be = 0
#arr0 = [(r, m.pi/3, m.pi/4),(r, m.pi/3, -m.pi/4),(r, -m.pi/3, -m.pi/4),(r, -m.pi/3, m.pi/4)]
def out_scr(r, alpha, beta):
    alpha += al #= turn_alpha(alpha, al)
    beta += be #= turn_beta(beta, be)
    
    x = l*(m.sin(beta)*m.cos(alpha))/(m.sin(beta)*m.sin(alpha)) + 600
    y = l*(m.cos(beta))/(m.sin(beta)*m.sin(alpha)) + 300
    disp = (x, y)
    return disp

k = 0
finished = False

def turn_alpha(alpha_0, alpha_t):
    alpha_0 += alpha_t
    return alpha_0
def turn_beta(beta_0, beta_t):
    beta_0 += beta_t
    return beta_0
"""
def rotate_a(alpha, b):
    for numb in range(8):
        b[numb][0] = b[numb][0]*m.sin(al) 
        b[numb][2] = b[numb][2]*m.cos(al) 

def rotate_b():
    for numb in range(8):
        b[numb][1] = b[numb][1]*m.sin(be) 
        b[numb][2] = b[numb][2]*m.cos(be) 
"""


def pol_cor_r(x, y, z): # y - alpha, z - beta
    r = (x**2 + y**2 + z**2)**0.5
    return r

def pol_cor_alpha(x, y, z): # y - alpha, z - beta
    if x == 0:
        alpha = m.pi/2
        pass
    else:
        alpha = m.atan(z/x)
        if alpha < 0:
            alpha += m.pi
    return alpha

def pol_cor_beta(x, y, z): # y - alpha, z - beta
    beta = m.acos(y/((x**2 + y**2 + z**2)**0.5))
    return beta

def make_x(t):
    x = rad*m.sin(t)
    return x
def make_z(t):
    z = rad*m.cos(t)
    return z
rot = 0
t = m.pi/4
ang = 0
while not finished:
    clock.tick(30)
    pygame.mouse.set_visible(False)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                finished = True
            if event.key == pygame.K_w:
                z_p -= 100
            if event.key == pygame.K_s:
                z_p += 100
            if event.key == pygame.K_d:
                x_p -= 100
            if event.key == pygame.K_a:
                x_p += 100
            if event.key == pygame.K_r:
                y_p -= 100
            if event.key == pygame.K_f:
                y_p += 100 
            
                
            if event.key == pygame.K_m:   
                pygame.mouse.set_pos(600,300)
                


            
        if event.type == pygame.MOUSEMOTION:
            global pos
            pos = event.pos 
            k = 0.002
            al += k*(pos[0] - 600)
            be += k*(pos[1] - 300) 
            pygame.mouse.set_pos(600,300)








    global b, alpha_arr, beta_arr
    b = [0]*8
    b_3 = [0]*8
    
    r = [0]*32
    c = [0]*8
    c_2 = [0]*8
    c_3 = [0]*8
    alpha_arr = [0]*32
    beta_arr = [0]*32
    
    b[0] = (make_x(t) + x_0 + x_p, y_0 + 100 + y_p, make_z(t) + z_0 + z_p)
    b[1] = (make_x(t + m.pi/2) + x_0 + x_p, y_0 + 100 + y_p, make_z(t + m.pi/2) + z_0 + z_p)
    b[2] = (make_x(t + m.pi) + x_0 + x_p, y_0 + 100 + y_p, make_z(t + m.pi) + z_0 + z_p)
    b[3] = (make_x(t + 3*m.pi/2) + x_0 + x_p, y_0 + 100 + y_p, make_z(t + 3*m.pi/2) + z_0 + z_p)
    
    b[4] = (make_x(t) + x_0 + x_p, y_0 - 100 + y_p, make_z(t) + z_0 + z_p)
    b[5] = (make_x(t + m.pi/2) + x_0 + x_p, y_0 - 100 + y_p, make_z(t + m.pi/2) + z_0 + z_p)
    b[6] = (make_x(t + m.pi) + x_0 + x_p, y_0 - 100 + y_p, make_z(t + m.pi) + z_0 + z_p)
    b[7] = (make_x(t + 3*m.pi/2) + x_0 + x_p, y_0 - 100 + y_p, make_z(t + 3*m.pi/2) + z_0 + z_p)
    #b[8] = (1000, -100, 0)
    
    b_2 = [0]*8
    b_2[0] = (-1000 + x_p,  0 + y_p, 1000 + z_p)
    b_2[1] = (1000  + x_p,  0 + y_p, 1000 + z_p)
    b_2[2] = (-1000 + x_p,  0 + y_p, 2000 + z_p)
    b_2[3] = (1000  + x_p,  0 + y_p, 2000 + z_p)
    b_2[4] = (-1000 + x_p, -400 + y_p, 1000 + z_p)
    b_2[5] = (1000  + x_p, -400 + y_p, 1000 + z_p)
    b_2[6] = (-1000 + x_p, -400 + y_p, 2000 + z_p)
    b_2[7] = (1000  + x_p, -400 + y_p, 2000 + z_p)

    b_3[0] = (100  + x_p, 0 + y_p, 1000 + z_p)
    b_3[1] = (-100 + x_p, 0 + y_p, 1000 + z_p)
    b_3[2] = (100  + x_p, 0 + y_p, 2000 + z_p)
    b_3[3] = (-100 + x_p, 0 + y_p, 2000 + z_p)
    b_3[4] = (1000 + x_p, 0 + y_p, 1400 + z_p)
    b_3[5] = (-1000 + x_p, 0 + y_p, 1400 + z_p)
    b_3[6] = (1000 + x_p, 0 + y_p, 1600 + z_p)
    b_3[7] = (-1000 + x_p, 0 + y_p, 1600 + z_p)

    b_4 = [0]*24
    c_4 = [0]*24


    b_4[0] =  (700  + x_p, 0 + y_p, 1000 + z_p)
    b_4[1] =  (500 + x_p, 0 + y_p, 1000 + z_p)
    b_4[2] =  (700  + x_p, 0 + y_p, 2000 + z_p)
    b_4[3] =  (500 + x_p, 0 + y_p, 2000 + z_p)
    b_4[4] =  (300  + x_p, 0 + y_p, 1000 + z_p)
    b_4[5] =  (100 + x_p, 0 + y_p, 1000 + z_p)
    b_4[6] =  (300  + x_p, 0 + y_p, 2000 + z_p)
    b_4[7] =  (100 + x_p, 0 + y_p, 2000 + z_p)
    b_4[8] =  (-300  + x_p, 0 + y_p, 1000 + z_p)
    b_4[9] =  (-100 + x_p, 0 + y_p, 1000 + z_p)
    b_4[10] = (-300  + x_p, 0 + y_p, 2000 + z_p)
    b_4[11] = (-100 + x_p, 0 + y_p, 2000 + z_p)
    b_4[12] = (500 + x_p, 0 + y_p, 2000 + z_p)
    b_4[13] = (300  + x_p, 0 + y_p, 1000 + z_p)
    b_4[14] = (500 + x_p, 0 + y_p, 1000 + z_p)
    b_4[15] = (300  + x_p, 0 + y_p, 2000 + z_p)
    b_4[16] = (-500 + x_p, 0 + y_p, 2000 + z_p)
    b_4[17] = (-300  + x_p, 0 + y_p, 1000 + z_p)
    b_4[18] = (-500 + x_p, 0 + y_p, 1000 + z_p)
    b_4[19] = (-300  + x_p, 0 + y_p, 2000 + z_p)
    b_4[20] = (-700 + x_p, 0 + y_p, 2000 + z_p)
    b_4[21] = (-500  + x_p, 0 + y_p, 1000 + z_p)
    b_4[22] = (-700 + x_p, 0 + y_p, 1000 + z_p)
    b_4[23] = (-500  + x_p, 0 + y_p, 2000 + z_p)
    


    
    main_arr = [b,]

    i = 0
    while i < 8:
        d = b[i]
        r[i] = pol_cor_r(d[0], d[1], d[2])
        alpha_arr[i] = pol_cor_alpha(d[0], d[1], d[2])
        beta_arr[i] = pol_cor_beta(d[0], d[1], d[2])
        c[i] = out_scr(r[i], turn_alpha(alpha_arr[i], al), turn_beta(beta_arr[i], be))
        i += 1
    
    i = 0
    while i < 8:
        d = b_2[i]
        r[i] = pol_cor_r(d[0], d[1], d[2])
        alpha_arr[i] = pol_cor_alpha(d[0], d[1], d[2])
        beta_arr[i] = pol_cor_beta(d[0], d[1], d[2])
        c_2[i] = out_scr(r[i], turn_alpha(alpha_arr[i], al), turn_beta(beta_arr[i], be))
        i += 1
    
    i = 0
    while i < 8:
        d = b_3[i]
        r[i] = pol_cor_r(d[0], d[1], d[2])
        alpha_arr[i] = pol_cor_alpha(d[0], d[1], d[2])
        beta_arr[i] = pol_cor_beta(d[0], d[1], d[2])
        c_3[i] = out_scr(r[i], turn_alpha(alpha_arr[i], al), turn_beta(beta_arr[i], be))
        i += 1
    i = 0
    while i < 24:
        d = b_4[i]
        r[i] = pol_cor_r(d[0], d[1], d[2])
        alpha_arr[i] = pol_cor_alpha(d[0], d[1], d[2])
        beta_arr[i] = pol_cor_beta(d[0], d[1], d[2])
        c_4[i] = out_scr(r[i], turn_alpha(alpha_arr[i], al), turn_beta(beta_arr[i], be))
        i += 1




    #field:

    polygon(screen, (100, 255, 100), [c_2[0], c_2[1], c_2[3], c_2[2]])
    
    polygon(screen, (255, 255, 255), [c_2[0], c_2[2], c_2[6], c_2[4]], 2)
    polygon(screen, (255, 255, 255), [c_2[1], c_2[3], c_2[7], c_2[5]], 2)
    polygon(screen, (255, 255, 255), [c_2[3], c_2[2], c_2[6], c_2[7]], 2)

    
    polygon(screen, (255, 255, 255), [c_3[0], c_3[1], c_3[3], c_3[2]], 2)
    polygon(screen, (255, 255, 255), [c_3[4], c_3[5], c_3[7], c_3[6]], 2)
    
    polygon(screen, (255, 255, 255), [c_4[0],  c_4[1],  c_4[3],  c_4[2]], 2)
    polygon(screen, (255, 255, 255), [c_4[4],  c_4[5],  c_4[7],  c_4[6]], 2)
    polygon(screen, (255, 255, 255), [c_4[8],  c_4[9],  c_4[10], c_4[11]], 2)
    polygon(screen, (255, 255, 255), [c_4[12], c_4[13], c_4[15], c_4[14]], 2)
    polygon(screen, (255, 255, 255), [c_4[16], c_4[17], c_4[19], c_4[18]], 2)
    polygon(screen, (255, 255, 255), [c_4[20], c_4[21], c_4[23], c_4[22]], 2)


    
    #First cube
    polygon(screen, (255, 0, 0), [(100,100), (200,100), (200,200), (100,200)], 2)
    #polygon(screen, (255, 0, 0), [c[0], c[1], (0,0), (0,200)], 2)
    #polygon(screen, (255, 0, 0), [(1200,0), (1200,200), c[2], c[3]], 2)
    
    polygon(screen, (255, 255, 255), [c[0], c[1], c[2], c[3]], 2)
    polygon(screen, (255, 255, 255), [c[4], c[5], c[6], c[7]], 2)
    
    polygon(screen, (255, 255, 255), [c[0], c[1], c[5], c[4]], 2)
    polygon(screen, (255, 255, 255), [c[2], c[3], c[7], c[6]], 2)

    polygon(screen, (255, 0, 0), [c[0], c[3], c[7], c[4]], 2)
    polygon(screen, (255, 255, 255), [c[1], c[2], c[6], c[5]], 2)

    

    #FIXME:
    q = [0]*8
    for sln in range(8):

        q[sln] = [0]*2
    for sln in range(8):
        q[sln][0] = (c[sln][0] + 10)//1
        q[sln][1] = (c[sln][1] + 10)//1
        a_0 = b[sln][0]//1
        a_1 = b[sln][1]//1
        a_2 = b[sln][2]//1
        GAME_FONT.render_to(screen, (1000, 10 + 30 * sln ), f"{alpha_arr[sln]*180/m.pi//1}, {beta_arr[sln]*180/m.pi//1}", (255, 255, 255))
        GAME_FONT.render_to(screen, (10, 10 + 30 * sln ), f"{c[sln][0]//1}, {c[sln][1]//1}", (255, 255, 255))
    p0 = pos[0]
    p1 = pos[1]
    GAME_FONT_1.render_to(screen, (10,550), f"{p0}, {p1}", (255, 255, 255))
    GAME_FONT_1.render_to(screen, (400, 550), "Print P to exit", (255, 255, 255))






    white = (255,255,255)
    aaline(screen, white, [0, 400], [1200, 400])


    
    
    pygame.display.update()
    black = (0,0,0)
    screen.fill(black)

    t += 0#0.05

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
"""
import pygame
import math as m
import pygame.freetype
from pygame.draw import *
from random import randint
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
black = (0, 0, 0)
screen = pygame.display.set_mode((1200, 600))

GAME_FONT = pygame.freetype.Font(None, 20)
GAME_FONT_1 = pygame.freetype.Font(None, 36)
"""