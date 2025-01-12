import pygame
import random
pygame.font.init()
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("SUDOKU")
img = pygame.image.load('C:\\Users\HP\Downloads\icon.jpg')
pygame.display.set_icon(img)
x = 0
y = 0
dif = 500 / 9
val = 0
a=[4,8,6,5,3,7,2,9,1]
b=[1,9,7,8,2,6,3,5,4]
c=[5,3,2,9,4,1,8,6,7]
d=[3,1,9,6,7,5,4,2,8]
e=[2,6,8,4,1,3,5,7,9]
f=[7,5,4,2,8,9,6,1,3]
g=[9,4,5,1,6,8,7,3,2]
h=[6,2,3,7,9,4,1,8,5]
i=[8,7,1,3,5,2,9,4,6]
q=[]
for j in range(random.randint(0,20)):
    a1=random.randint(1,9)
    b1=random.randint(1,9)
    if a1!=b1 and a1 not in q and b1 not in q:
        for k in [a,b,c,d,e,f,g,h,i]:
            for l in range(9):
                if k[l]==a1:
                    k[l]=b1
                elif k[l]==b1:
                    k[l]=a1
                else:
                    pass
    q.append(a1)
    q.append(b1)
for j in range(random.randint(0,4)):
    a1=random.randint(1,3)
    if a1==1:
        a,b,c,d,e,f=d,e,f,a,b,c
    elif a1==2:
        a,b,c,g,h,i=g,h,i,a,b,c
    else:
        d,e,f,g,h,i=g,h,i,d,e,f
for j in range(random.randint(0,4)):
    a1=random.randint(1,3)
    if a1==1:
        for k in range(9):
            a[k],d[k]=d[k],a[k]
            b[k],e[k]=e[k],b[k]
            c[k],f[k]=f[k],c[k]
    elif a1==2:
        for k in range(9):
            g[k],d[k]=d[k],g[k]
            h[k],e[k]=e[k],h[k]
            i[k],f[k]=f[k],i[k]
    else:
        for k in range(9):
            a[k],g[k]=g[k],a[k]
            b[k],h[k]=h[k],b[k]
            c[k],i[k]=i[k],c[k]
m=[a,b,c,d,e,f,g,h,i]
print('Level:')
print('1 for easy')
print('2 for medium')
print('3 for hard')
print('4 for blank')
r=int(input(':'))
if r==1:
    for j in range(1,21):
        x=[random.randint(0,8),random.randint(0,8)]
        y=0
        m[x[0]][x[1]]=y
elif r==2:
    for j in range(1,37):
        x=[random.randint(0,8),random.randint(0,8)]
        y=0
        m[x[0]][x[1]]=y
elif r==3:
    for j in range(1,51):
        x=[random.randint(0,8),random.randint(0,8)]
        y=0
        m[x[0]][x[1]]=y
elif r==4:
    for j in m:
        for k in range(9):
            j[k]=0
grid=[a,b,c,d,e,f,g,h,i]
font1 = pygame.font.SysFont("comicsans", 32)
font2 = pygame.font.SysFont("comicsans", 18)
def get_cord(pos):
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif
def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)        
def draw():
    for i in range (9):
        for j in range (9):
            if grid[i][j]!= 0:
                pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))
                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))          
    for i in range(10):
        if i % 3 == 0 :
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)        
def draw_val(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * dif + 15, y * dif + 15))   
def raise_error1():
    text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
    screen.blit(text1, (20, 570)) 
def raise_error2():
    text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
    screen.blit(text1, (20, 570)) 
def valid(m, i, j, val):
    for it in range(9):
        if m[i][it]== val:
            return False
        if m[it][j]== val:
            return False
    it = i//3
    jt = j//3
    for i in range(it * 3, it * 3 + 3):
        for j in range (jt * 3, jt * 3 + 3):
            if m[i][j]== val:
                return False
    return True
def solve(grid, i, j):
    while grid[i][j]!= 0:
        if i<8:
            i+= 1
        elif i == 8 and j<8:
            i = 0
            j+= 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()
    for it in range(1, 10):
        if valid(grid, i, j, it)== True:
            grid[i][j]= it
            global x, y
            x = i
            y = j
            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(grid, i, j)== 1:
                return True
            else:
                grid[i][j]= 0
            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(50)   
    return False 
def instruction():
    text1 = font2.render("PRESS D TO RESET TO DEFAULT / R TO EMPTY", 1, (0, 0, 0))
    text2 = font2.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, (0, 0, 0))
    screen.blit(text1, (20, 520))       
    screen.blit(text2, (20, 540))
def result():
    text1 = font1.render("FINISHED PRESS R or D", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))   
run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0
while run:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False   
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x+= 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y-= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y+= 1
                flag1 = 1   
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2   
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9 
            if event.key == pygame.K_RETURN:
                flag2 = 1  
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag2 = 0
                grid =[
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            if event.key == pygame.K_d:
                rs = 0
                error = 0
                flag2 = 0
                grid =[a,b,c,d,e,f,g,h,i]
    if flag2 == 1:
        if solve(grid, 0, 0)== False:
            error = 1
        else:
            rs = 1
        flag2 = 0   
    if val != 0:           
        draw_val(val)
        if valid(grid, int(x), int(y), val)== True:
            grid[int(x)][int(y)]= val
            flag1 = 0
        else:
            grid[int(x)][int(y)]= 0
            raise_error2()  
        val = 0   
       
    if error == 1:
        raise_error1() 
    if rs == 1:
        result()       
    draw() 
    if flag1 == 1:
        draw_box()      
    instruction()   
    pygame.display.update() 
