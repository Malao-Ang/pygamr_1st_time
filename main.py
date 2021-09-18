
#main.py

#1. player
#2. enermy too ,O
#3. กระสุน
#setupเริ้มต้นให้pgameทำงาน
import pygame
import math
import random
pygame.init()
#ปรับขนาดหน้าจอ
WIDTH = 900
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('ฝึกยิงตู่') #set name game
icon = pygame.image.load('logo.png') #โหลดรูปเข้ามาในpygame
pygame.display.set_icon(icon)#set icon

background = pygame.image.load('bg.png')
########################################################################
# 1. player - finger.png
psize = 128 #ความกว้างของภาพman
pimg = pygame.image.load('ufo.png') 
px = 100 #จุดเริ่มต้นแกน x(แนวนอน)
py = HEIGHT - psize #จุดเริ่มต้นแกน y(แนวตั้ง)
pxchange = 0
def Player(x,y):
    screen.blit(pimg,(x,y))#blit วางภาพในจอ
########################################################################
#2. enermy - tooกับO
esize = 64
eimg = pygame.image.load('E_Too.png')
ex = 50
ey = 0
eychange = 3
def Enemy(x,y):
    screen.blit(eimg,(x,y))

################################################################
#3. กระสุน
bsize = 32
bimg = pygame.image.load('Bom.png')
bx = 100
by = HEIGHT-psize
bychange = 20
bstate = 'ready'
def fire_bom(x,y):
    global bstate
    bstate ='fire'
    screen.blit(bimg,(x,y))

#######################Null-enemy#########################

exlist = [] #เก็บตำแหน่งแกน x ของ enermy
eylist = []
ey_change_list = [] #สุ่มความเร็วของ enermy
allenemy = 3

for i in range(allenemy):
    exlist.append(random.randint(50,WIDTH - esize))
    eylist.append(random.randint(0,100))
    #ey_change_list.append(random.randint(1,5)) #สุ่มความเร็ว
    ey_change_list.append(5) #กำหนดความเร็วเป็น1แล้วค่อยเพิ่ม
#########collison############
def isCollision(ecx,ecy,bcx,bcy):
    distance = math.sqrt(math.pow(ecx - bcx,2)+math.pow(ecy - bcy,2))
    #ชนให้ขึ้นว่าtrue
    print(distance)
    if distance < 48:
        return True
    else:
        return False

#############score###########
allscore = 0
font = pygame.font.Font(None,30)

def showscore():
    score = font.render('Point : {} Point'.format(allscore),True,(255,255,255))
    screen.blit(score,(30,30))
#############sound###########
pygame.mixer.music.load('game.wav')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

sound = pygame.mixer.Sound('start.wav')
sound.set_volume(0.5)
sound.play()
#############game over############
fontover = pygame.font.Font(None,120)
fontover2 = pygame.font.Font(None,80)
playsound = False
gameover = False
def GameOver ():
    global playsound
    overtext = fontover.render("coup d'etat!!!",True,(255,0,0))
    screen.blit(overtext,(200,300))
    overtext2 = fontover2.render("Press [N] New Game",True,(255,255,255))
    screen.blit(overtext2,(190,250))
    if playsound == False:
        gsound = pygame.mixer.Sound('over.wav')
        gsound.play()
        playsound = True
    '''if gameover == False:
        gameover = True'''

###Game loop################################
running = True #บอกให้โปรแกรมทำงาน
clock = pygame.time.Clock()
FPS = 30 #framerate


while running:

    
    for event in pygame.event.get():
        #รัยเช็คว่ามีการกดปิดpygame[x]
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pxchange = -20
            if event.key == pygame.K_RIGHT:
                pxchange = 20

            if event.key == pygame.K_SPACE:
                if bstate == 'ready':
                    b1 = pygame.mixer.Sound('iba.mp3')
                    b1.play()
                    bx = px + 49 #ขยีบให้อยู่ตรงกลางจานบิน
                    fire_bom(bx,by)

            if event.key == pygame.K_n:
                #gameover = False
                playsound = False
                allscore = 0
                for i in range(allenemy):
                    eylist[i] = random.randint(0,100)
                    exlist[i] = random.randint(50,WIDTH - esize)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pxchange = 0



#############Run player#############    
    #px,py จุดเริ่มต้น
    Player(px,py)
    #mave right left
    if px <= 0:
        #สุดขอบจอให้ซ้ายให้ปรับค่า pxchange เป้น +1
        px = 0
        px += pxchange
    elif px >= WIDTH - psize:
    #width (ความกว้าง - ขนาดของรูป)
    #สุดขอบจอให้ซ้ายให้ปรับค่า pxchange เป้น -1
        px = WIDTH - psize
        px += pxchange 
    else:
        #ถ้าอยู่ระหว่างหน้าจอให้ + - ตามpxchange
        px += pxchange 


    #############Run Enermy##################
    '''for i in range(5):
        Enemy(ex,ey)
        ey += eychange'''
###runn eney singlr#############
#เช็คว่าชนมั้ย
    collision = isCollision(ex,ey,bx,by)
    if collision:
        by = HEIGHT - psize
        bstate = 'ready'
        ey = 0
        ex = random.randint(50,WIDTH - esize)
        allscore += 1
        #randomตำแหน่งความกว้างหน้าจอ - ขนาดของ หน้าลุงตู่

###### run multi enemy##############################
    for i in range(allenemy):
        #เพิ่มความเร็วของตัวที่จะยิง
        if eylist[i] > HEIGHT - esize and gameover == False:
            for i in range(allenemy):
                eylist[i] = 1000
            GameOver()
            break
        

        eylist[i] += ey_change_list[i]
        colissionmuti = isCollision(exlist[i],eylist[i],bx,by)
        if colissionmuti:
            by = HEIGHT - psize
            bstste = 'ready'
            eylist[i] = 0
            exlist[i] = random.randint(50,WIDTH - esize)
            allscore += 1
            ey_change_list[i] += 1
        Enemy(exlist[i],eylist[i])

######fire bom ############
    if bstate == 'fire':
        fire_bom(bx,by)
        by -= bychange

#เช็คว่าวื่งไปชนขอบยัง ถ้าชนให้ state เปลี่ยนเป้นพร้อมยิง
    if by <= 0:
        by = HEIGHT - psize
        bstate = 'ready'



    showscore()
    print(px)
    pygame.display.update()
    pygame.display.flip()
    pygame.event.pump()
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    clock.tick(FPS)