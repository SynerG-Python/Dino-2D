import pygame
from random import randint
import time
import os

#Параметры экрана
w = 1400
h = 700
FPS = 144
color_dino = (0,128,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,128,0)
OrangeRed = (255, 119, 0)
YELLOW = (255,148,0)
DarkMagenta = (139, 0, 139)
Cyan = (0, 204, 204)
Lime = (0, 210, 0)
Gray = (105, 105, 105)
idSkin = 0
idMusic=0
idFPS = 0 
#Музыка
music1 = r'SoundsDino\Roy Knox - Lost In Sound.mp3'
music2 = r'SoundsDino\RUDE - Eternal Youth.mp3'

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

# Создание функции
def print_text(message, x, y, font_color = (0,0,0), font_type = 'Avenir Heavy', font_size = 65):
    font_type = pygame.font.SysFont(font_type, font_size)
    text = font_type.render(message, True, font_color)
    sc.blit(text,(x,y))

#Создание окна
sc = pygame.display.set_mode((w,h))
pygame.display.set_caption('Dino')

#Саунд
sound_jump = pygame.mixer.Sound(r'SoundsDino\Jump_sound.wav')
sound_points = pygame.mixer.Sound(r'SoundsDino\Points_sound.wav')
sound_select = pygame.mixer.Sound(r'SoundsDino\Sound_select.wav')
sound_forward = pygame.mixer.Sound(r'SoundsDino\Sound_forward.wav')
sound_quit = pygame.mixer.Sound(r'SoundsDino\Sound_quit.wav')
sound_dead = pygame.mixer.Sound(r'SoundsDino\Sound_GO.wav')

#Картинка загрузки
Load0 = pygame.image.load(r'SpritesDino\Load\Load0.jpg')
Load1 = pygame.image.load(r'SpritesDino\Load\Dino2D.jpg')
#Позиция фона
xload = -50
yload = -10
#Загрузка в спиксок
Load = [Load0,Load1]
#Загрузка изображения фона
fon1 = pygame.image.load(r'SpritesDino\Fon\Fon.png')
fon2 = fon1
fonNight1 = pygame.image.load(r'SpritesDino\Fon\NightFon.png')
fonNight2 = fonNight1
#Позиция фона
xfon1 = 0
yfon1 = 0

xfon2 = 700
yfon2 = 0

# Месяц
Month = pygame.image.load(r'SpritesDino\Fon\Month.png')
# Позиция месяца
xmonth = 1450
ymonth = 70

# Луна
Moon = pygame.image.load(r'SpritesDino\Fon\Moon.png')
# Позиция луны
xmoon = 3000
ymoon = 70

# Звёзды
# Маленькие звёзды
# №1
Small_Star1 = pygame.image.load(r'SpritesDino\Fon\Star_small1.png')
small_star1 = pygame.image.load(r'SpritesDino\Fon\Star_small2.png')
xss1 = 200
yss1 = randint(0,400)
Small_Star_One = [Small_Star1,small_star1]
# №2
Small_Star2 = pygame.image.load(r'SpritesDino\Fon\Star_small1.png')
small_star2 = pygame.image.load(r'SpritesDino\Fon\Star_small2.png')
xss2 = 1200
yss2 = randint(0,400)
Small_Star_Two = [Small_Star2,small_star2]
# Большие звёзды
# №1
Big_Star1 = pygame.image.load(r'SpritesDino\Fon\Star_big1.png')
big_star1 = pygame.image.load(r'SpritesDino\Fon\Star_big2.png')
xbs1 = 500
ybs1 = randint(0,400)
Big_Star_One = [Big_Star1,big_star1]
# №2
Big_Star2 = pygame.image.load(r'SpritesDino\Fon\Star_big1.png')
big_star2 = pygame.image.load(r'SpritesDino\Fon\Star_big2.png')
xbs2 = 760
ybs2 = randint(0,400)
Big_Star_Two = [Big_Star2,big_star2]

#Загрузка дороги №1
road1 = pygame.image.load(r'SpritesDino\Road\Road_1.png')
#Позиция дороги №1
xroad1=0
yroad1=300

#Загрузка дороги №2
road2 = pygame.image.load(r'SpritesDino\Road\Road5.png')
#Позиция дороги №2
xroad2=600
yroad2=300

#Загрузка дороги №3
road3 = pygame.image.load(r'SpritesDino\Road\Road_2.png')
#Позиция дороги №3
xroad3=1200
yroad3=300

#Загрузка дороги №4
road4 = road2
#Позиция дороги №4
xroad4=1800
yroad4=300

#Загрузка дороги №5
road5 = pygame.image.load(r'SpritesDino\Road\Road_3.png')
#Позиция дороги №5
xroad5=2400
yroad5=300

#Загрузка дороги №6
road6 = road2
#Позиция дороги №6
xroad6=3000
yroad6=300

#Загрузка дороги №7
road7 = pygame.image.load(r'SpritesDino\Road\Road_4.png')
#Позиция дороги №7
xroad7=3600
yroad7=300

#Загрузка дороги №8
road8 = road2
#Позиция дороги №8
xroad8=4200
yroad8=300

#Дино
dino1 = pygame.image.load(r'SpritesDino\Dino\Dino\DINO.png')
dino2 = pygame.image.load(r'SpritesDino\Dino\Dino\DINO2.png')
dino3 = pygame.image.load(r'SpritesDino\Dino\Dino\DINO3.png')
#Загрузка прыгающего Дино
dino_jump= pygame.image.load(r'SpritesDino\Dino\Dino\Dino_jump.png')
#Мёртвый Дино
dino_dead = pygame.image.load(r'SpritesDino\Dino\Dino\DINO_dead.png')
#Мёртвый Дино в прыжке
dead_jump = pygame.image.load(r'SpritesDino\Dino\Dino\dead_jump.png')
#Загрузка Дино вприсяди 
dino_down1= pygame.image.load(r'SpritesDino\Dino\Dino\Dino_down1.png')
dino_down2= pygame.image.load(r'SpritesDino\Dino\Dino\Dino_down2.png')
#Загрузка в список
Dino = [dino1,dino2,dino3,dino_jump]
#Загрузка в список Дино вприсяди
Dino_down = [dino_down1,dino_down2]

#Дино (Фараон)
Pharaoh = pygame.image.load(r'SpritesDino\Dino\Dino_Pharaoh\Pharaoh.png')
Pharaoh2 = pygame.image.load(r'SpritesDino\Dino\Dino_Pharaoh\Pharaoh2.png')
Pharaoh3 = pygame.image.load(r'SpritesDino\Dino\Dino_Pharaoh\Pharaoh3.png')
#Загрузка прыгающего Дино
Pharaoh_Jump= pygame.image.load(r'SpritesDino\Dino\Dino_Pharaoh\Pharaoh_Jump.png')
#Мёртвый Дино
Pharaoh_Dead = pygame.image.load(r'SpritesDino\Dino\Dino_Pharaoh\Pharaoh_Dead.png')
#Мёртвый Дино в прыжке
PharaohJump_Dead = pygame.image.load(r'SpritesDino\Dino\Dino_Pharaoh\Pharaoh (Jump-Dead).png')
#Загрузка Дино вприсяди 
Pharaoh_Down1= pygame.image.load(r'SpritesDino\Dino\Dino_Pharaoh\Pharaoh_Down1.png')
Pharaoh_Down2= pygame.image.load(r'SpritesDino\Dino\Dino_Pharaoh\Pharaoh_Down2.png')
#Загрузка в список
Dino_Pharaoh = [Pharaoh,Pharaoh2,Pharaoh3,Pharaoh_Jump]
#Загрузка в список Дино вприсяди
Dino_down_Pharaoh = [Pharaoh_Down1,Pharaoh_Down2]

#Дино СидиДома
Covid19_dino1 = pygame.image.load(r'SpritesDino\Dino\Dino#SitAtHome\Dino1#SitAtHome.png')
Covid19_dino2 = pygame.image.load(r'SpritesDino\Dino\Dino#SitAtHome\Dino2#SitAtHome.png')
Covid19_dino3 = pygame.image.load(r'SpritesDino\Dino\Dino#SitAtHome\Dino3#SitAtHome.png')
#Загрузка прыгающего Дино
Covid19_dino_jump= pygame.image.load(r'SpritesDino\Dino\Dino#SitAtHome\Dino_jump#SitAtHome.png')
#Мёртвый Дино
Covid19_dino_dead = pygame.image.load(r'SpritesDino\Dino\Dino#SitAtHome\Dino_dead#SitAtHome.png')
#Мёртвый Дино в прыжке
Covid19_dead_jump = pygame.image.load(r'SpritesDino\Dino\Dino#SitAtHome\dead_jump#SitAtHome.png')
#Загрузка Дино вприсяди 
Covid19_dino_down1= pygame.image.load(r'SpritesDino\Dino\Dino#SitAtHome\Dino_down1#SitAtHome.png')
Covid19_dino_down2= pygame.image.load(r'SpritesDino\Dino\Dino#SitAtHome\Dino_down2#SitAtHome.png')
#Загрузка в список
Covid19 = [Covid19_dino1,Covid19_dino2,Covid19_dino3,Covid19_dino_jump]
#Загрузка в список Дино вприсяди
Covid19_down = [Covid19_dino_down1,Covid19_dino_down2]

#Дино Демон
Demon1 = pygame.image.load(r'SpritesDino\Dino\Demon\Demon1.png')
Demon2 = pygame.image.load(r'SpritesDino\Dino\Demon\Demon2.png')
Demon3 = pygame.image.load(r'SpritesDino\Dino\Demon\Demon3.png')
#Загрузка прыгающего Дино
Demon_Jump= pygame.image.load(r'SpritesDino\Dino\Demon\Demon Jump.png')
#Мёртвый Дино
Demon_dead = pygame.image.load(r'SpritesDino\Dino\Demon\Demon_dead.png')
#Мёртвый Дино в прыжке
Demon_JumpDead = pygame.image.load(r'SpritesDino\Dino\Demon\Demon_JumpDead.png')
#Загрузка Дино вприсяди 
Demon_down1= pygame.image.load(r'SpritesDino\Dino\Demon\Demon_down1.png')
Demon_down2= pygame.image.load(r'SpritesDino\Dino\Demon\Demon_down2.png')
#Загрузка в список
Demon = [Demon1,Demon2,Demon3,Demon_Jump]
#Загрузка в список Дино вприсяди
Demon_down = [Demon_down1,Demon_down2]

#Позиция Дино
xpos=15
ypos=570

#Птерадактиль
Pteradactyl_one = pygame.image.load(r'SpritesDino\Pteradactyl\Pteradactyl1.png')
Pteradactyl_two = pygame.image.load(r'SpritesDino\Pteradactyl\Pteradactyl2.png')
Pteradactyl = [Pteradactyl_one,Pteradactyl_two]
#Позиция Птерадактиля
xpos_enemy=1400
ypos_enemy=0
#Рандомная позиция по оси y
yrandom = randint(1,2)
if yrandom == 1:
    ypos_enemy = 590
if yrandom == 2:
    ypos_enemy = 550

#Кактус №1
cactus1 = pygame.image.load(r'SpritesDino\Cactus\Cactus_one.png')
#Позиция кактуса №1
xcactus1 = 1000
ycactus1 = 570

#Кактус2.0
cactus2 = pygame.image.load(r'SpritesDino\Cactus\Cactus_two.png')
#Позиция кактуса №2
xcactus2 = 1500
ycactus2 = 615

#Кактус3.0
cactus3 = pygame.image.load(r'SpritesDino\Cactus\Cactus_three.png')
#Позиция кактуса №3
xcactus3 = 2000
ycactus3 = 570

#Кактус4.0
cactus4 = pygame.image.load(r'SpritesDino\Cactus\Cactus_four.png')
#Позиция кактуса №4
xcactus4 = 2500
ycactus4 = 570

#Облако №1
cloud1 = pygame.image.load(r'SpritesDino\Cloud\Cloud_final.png')
cloud_night1 = pygame.image.load(r'SpritesDino\Cloud\Cloud_Night.png')
#Позиция облака №1
xcloud1 = 1400
ycloud1 = randint(200,400)

#Облако №2
cloud2 = cloud1
cloud_night2 = cloud_night1
#Позиция облака №2
xcloud2 = 1850
ycloud2 = randint(0,200)

#Параметры цикла
clock = pygame.time.Clock()
run = False
menu = False

menu_gear = False
management = False
menumusic = False
description = False

menu_skin = False

# Переменные для поля ввода
need_input = False
input_text = '|'
input_tick = 10
save_texttime = ''
save_textskin = ''

#Шрифты
f = pygame.font.SysFont('Avenir Heavy', 25, True)
f1 = pygame.font.SysFont('comic sans ms', 50, True)
f2 = pygame.font.SysFont('comic sans ms', 35, True)
fm = pygame.font.SysFont('comic sans ms', 40, True)
Fmenu = pygame.font.SysFont('comic sans ms', 70, True)

#Параметры прыжка
isJump = False
jumpCount = 10

#Переменная клавиатуры
keyboard = True

#Параметры скорости для цикла
speed = 15
speed_down = 0
speed_enemy = 22.5
speed_cloud1 = 2.5
speed_cloud2 = 3
speed_month = 0.5
speed_moon = 0.5
speed_star = 0.3

#Переменные очков
record_points = 0
points = 0

#Переменные спауна кактусов(рандом)
crmini1=650
crmax1=1000

crmini2=650
crmax2=1000

crmini3=650
crmax3=1000

crmini4=650
crmax4=1000
cr1= randint(crmini1 , crmax1)
cr2= randint(crmini2 , crmax2)
cr3= randint(crmini3 , crmax3)
cr4= randint(crmini4 , crmax4)
#Переменная анимации
animCount = 0
animCountDown = 0
animCount2 = 0
animLoad1 = 0
animCountStar = 0

# Motion
motion = 'STOP'

#Цикл загрузки
Loading = True
lg = 0
while  Loading:
    if animLoad1 +1 >= 150:
        animLoad1 = 0
    if lg < 150:
        sc.blit(Load[animLoad1 // 75],(xload,yload))
        animLoad1 += 1
    #Закрытие окна
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            run = False
            menu = False
            Loading = False 
            pygame.quit()
            
    if Loading == True:
        lg+=1
    if lg >= 150:
        Loading = False
        menu = True

    #Конец цикла        
    pygame.display.update()
    clock.tick(FPS)
# Переменные консоли
Collision_cactus = 1
Collision_enemy = 0
Field = pygame.image.load(r'SpritesDino\Menu\Field.png')
#Фон меню настроек
idGear = 0
fon_gear = pygame.image.load(r'SpritesDino\Menu\menu_gear.png')
fon_gear1 = pygame.image.load(r'SpritesDino\Menu\menu_gear1.png')
fon_gear2 = pygame.image.load(r'SpritesDino\Menu\menu_gear2.png')
xfon_gear = 350
yfon_gear = 100
#Фон меню скинов
fon_skin = pygame.image.load(r'SpritesDino\Menu\Menu_Skin.png')
fon_skinCovid19 = pygame.image.load(r'SpritesDino\Menu\Menu_Skin#СидиДома.png')
fon_skinPharaon = pygame.image.load(r'SpritesDino\Menu\Menu_Skin Pharaon.png')
fon_skinDemon = pygame.image.load(r'SpritesDino\Menu\Menu_Skin Demon.png')

xfon_skin = 350
yfon_skin = 100
# Кнопки в меню
gear = pygame.image.load(r'SpritesDino\Menu\Gear.png')
xgear = 10
ygear = 10
skins_menu = pygame.image.load(r'SpritesDino\Menu\Skins.png')
xskins = 80
yskins = 10
# Спрайт замка
Lock = pygame.image.load(r'SpritesDino\Menu\Lock.png')
# Без звука
Grimmest = pygame.image.load(r'SpritesDino\Menu\Grimmest.png')
#Меню
while  menu:
    #Загрузка фона
    if save_texttime != 'Night' or save_texttime == 'Return':
        sc.blit(fon1,(xfon1,yfon1))
        sc.blit(fon2,(xfon2,yfon2))
    if save_texttime == 'Night':
        sc.blit(fonNight1,(xfon1,yfon1))
        sc.blit(fonNight2,(xfon2,yfon2))
    #Загрузка дороги
    sc.blit(road1,(xroad1,yroad1))
    sc.blit(road2,(xroad2,yroad2))
    sc.blit(road3,(xroad3,yroad3))
    sc.blit(road4,(xroad4,yroad4))
    
    sc.blit(road5,(xroad5,yroad5))
    sc.blit(road6,(xroad6,yroad6))
    sc.blit(road7,(xroad7,yroad7))
    sc.blit(road8,(xroad8,yroad8))
    #Dino
    if idSkin == 0:
        sc.blit(Dino[0],(xpos,ypos))
    elif idSkin == 1:
        sc.blit(Covid19[0],(xpos,ypos))
    elif idSkin == 2 or idSkin == 3 and save_textskin != 'Demon':
        sc.blit(Dino_Pharaoh[0],(xpos,ypos))
    elif idSkin == 3 and save_textskin == 'Demon':
        sc.blit(Demon[0],(xpos,ypos))
    #Загрузка кактусов
    sc.blit(cactus1,(xcactus1,ycactus1))
    sc.blit(cactus2,(xcactus2,ycactus2))
    sc.blit(cactus3,(xcactus3,ycactus3))
    sc.blit(cactus4,(xcactus4,ycactus4))
    #Загрузка звёзд
    if save_texttime == 'Night':
    	if animCountStar +1 >=12:
    		animCountStar = 0
    	if menu == True:
	        sc.blit(Small_Star_One[animCountStar // 6],(xss1,yss1))
	        sc.blit(Small_Star_Two[animCountStar // 6],(xbs2,ybs2))
	        sc.blit(Big_Star_One[animCountStar // 6],(xbs1,ybs1))
	        sc.blit(Big_Star_Two[animCountStar // 6],(xss2,yss2))
	        animCountStar += 1
    #Загрузка месяца
    if save_texttime == 'Night':
    	sc.blit(Month,(xmonth,ymonth))
    #Загрузка луны
    if save_texttime == 'Night':
    	sc.blit(Moon,(xmoon,ymoon))
    #Загрузка облаков
    if save_texttime != 'Night' or save_texttime == 'Return':
	    sc.blit(cloud1,(xcloud1,ycloud1))
	    sc.blit(cloud2,(xcloud2,ycloud2))
    if save_texttime == 'Night':
	    sc.blit(cloud_night1,(xcloud1,ycloud1))
	    sc.blit(cloud_night2,(xcloud2,ycloud2))

    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            run = False
            menu = False 
            pygame.quit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE and need_input != True:
                run = True 
                menu = False
                menu_skin = False
                management = False
                isJump = True
                pygame.mixer.Sound.play(sound_jump)
        # Обработка открытие меню настроек      
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                if 10<i.pos[0]<60:
                    if 10<i.pos[1]<60:
                        menu_gear = True
                        pygame.mixer.Sound.play(sound_select)
        # Переключение окон меню настроек 
        if i.type == pygame.MOUSEBUTTONDOWN and menu_gear == True and menumusic!=True  and description!=True and management!=True:
            if i.button == 1 and idGear>0:
                if 350<=i.pos[0]<=370:
                    if 340<=i.pos[1]<=360:
                        idGear-=1
                        pygame.mixer.Sound.play(sound_forward)
            if i.button == 1 and idGear<1:
                if 1030<=i.pos[0]<=1050:
                    if 340<=i.pos[1]<=360:
                        idGear+=1
                        pygame.mixer.Sound.play(sound_forward)
        # Управление коллизией кактусов
        if i.type == pygame.MOUSEBUTTONDOWN and menu_gear and idGear==1:
            if i.button == 1:
                if 400<=i.pos[0]<=420:
                    if 272<=i.pos[1]<=299:
                        if Collision_cactus ==1:
                            Collision_cactus = 0
                        elif Collision_cactus ==0:
                            Collision_cactus = 1
                        pygame.mixer.Sound.play(sound_forward) 
        # Управление коллизией птерадактелей
        if i.type == pygame.MOUSEBUTTONDOWN and menu_gear and idGear==1:
            if i.button == 1:
                if 400<=i.pos[0]<=420:
                    if 370<=i.pos[1]<=390:
                        if Collision_enemy ==1:
                            Collision_enemy = 0
                        elif Collision_enemy ==0:
                            Collision_enemy = 1
                        pygame.mixer.Sound.play(sound_forward) 
        # Поле ввода 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                if 475<i.pos[0]<925:
                    if 450<i.pos[1]<525:
                        need_input = True
        if need_input and i.type == pygame.KEYDOWN:
            input_text = input_text.replace('|','')
            input_tick = 30
            if i.key == pygame.K_RETURN:
                if input_text == 'Night':
                    need_input = False
                    save_texttime = input_text
                    input_text = ''
                if input_text == 'Return':
                    need_input = False
                    save_texttime = input_text
                    input_text = ''
                if input_text == 'Demon':
                    need_input = False
                    save_textskin = input_text
                    input_text = ''
            elif i.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                if len (input_text) < 10:
                    input_text += i.unicode
            input_text += '|'                 
        # Включение ФПС   
        if i.type == pygame.MOUSEBUTTONDOWN and idFPS==0 and idGear==0:
            if i.button == 1:
                if 402<i.pos[0]<417:
                    if 432<i.pos[1]<448:
                        idFPS=1
                        pygame.mixer.Sound.play(sound_forward) 
        # Выключение ФПС   
        elif i.type == pygame.MOUSEBUTTONDOWN and idFPS==1 and idGear==0:
            if i.button == 1:
                if 402<i.pos[0]<417:
                    if 432<i.pos[1]<448:
                        idFPS-=1
                        pygame.mixer.Sound.play(sound_forward)              
        # Обработка закрытие меню настроек   
        if i.type == pygame.MOUSEBUTTONDOWN and menu_gear == True:
            if i.button == 1:
                if 1010<=i.pos[0]<=1050:
                    if 100<=i.pos[1]<=120:
                        menu_gear = False
                        management = False
                        menumusic = False
                        description = False
                        idGear=0
                        input_text = ''
                        pygame.mixer.Sound.play(sound_quit)
        # Обработка открытие меню настроек управления  
        if i.type == pygame.MOUSEBUTTONDOWN and menu_gear == True and menumusic!=True  and description!=True and idGear==0:
            if i.button == 1:
                if 400<=i.pos[0]<=690:
                    if 260<=i.pos[1]<=325:
                        management = True
                        pygame.mixer.Sound.play(sound_forward)
        # Обработка открытие меню настроек Музыки 
        if i.type == pygame.MOUSEBUTTONDOWN and menu_gear == True and management!=True and description!=True and idGear==0:
            if i.button == 1:
                if 770<=i.pos[0]<=960:
                    if 260<=i.pos[1]<=321:
                        menumusic = True
                        pygame.mixer.Sound.play(sound_forward)
        #Об игре
        if i.type == pygame.MOUSEBUTTONDOWN and menu_gear == True and management!=True and menumusic!=True and idGear==0:
            if i.button == 1:
                if 770<=i.pos[0]<=970:
                    if 410<=i.pos[1]<=471:
                        description = True
                        pygame.mixer.Sound.play(sound_forward)
        #Выбор музыки 1
        if i.type == pygame.MOUSEBUTTONDOWN and menumusic == True and idGear==0:
            if i.button == 1:
                if 400<=i.pos[0]<=420:
                    if 272<=i.pos[1]<=299:
                        idMusic = 0
                        pygame.mixer.Sound.play(sound_forward)
        #Выбор музыки 2
        if i.type == pygame.MOUSEBUTTONDOWN and menumusic == True and idGear==0:
            if i.button == 1:
                if 400<=i.pos[0]<=420:
                    if 370<=i.pos[1]<=390:
                        idMusic = 1
                        pygame.mixer.Sound.play(sound_forward) 
        #Выбор музыки 3
        if i.type == pygame.MOUSEBUTTONDOWN and menumusic == True and idGear==0:
            if i.button == 1:
                if 400<=i.pos[0]<=420:
                    if 468<=i.pos[1]<=488:
                        idMusic = 2
                        pygame.mixer.Sound.play(sound_forward)       
    #Открытие настроек №1
    if menu_gear == True and idFPS==0 and idGear==0:
        sc.blit(fon_gear1,(xfon_gear,yfon_gear))
        Menu = Fmenu.render('Настройки', 1 , BLUE)
        sc.blit(Menu, (515,120))
        Managemet = f1.render('Управление', 1 , RED)
        sc.blit(Managemet, (400,250))
        Music_menu = f1.render('Музыка', 1 , DarkMagenta)
        sc.blit(Music_menu, (770,250))
        pygame.draw.circle(sc,Gray,(410,440),15)
        fps = f1.render('FPS', 1 , OrangeRed)
        sc.blit(fps, (450,400))
        AboutTheGame = f1.render('Об игре', 1 , YELLOW)
        sc.blit(AboutTheGame, (770,400))
    if menu_gear == True and idFPS==1 and idGear==0:
        sc.blit(fon_gear1,(xfon_gear,yfon_gear))
        Menu = Fmenu.render('Настройки', 1 , BLUE)
        sc.blit(Menu, (515,120))
        Managemet = f1.render('Управление', 1 , RED)
        sc.blit(Managemet, (400,250))
        Music_menu = f1.render('Музыка', 1 , DarkMagenta)
        sc.blit(Music_menu, (770,250))
        pygame.draw.circle(sc,Gray,(410,440),15)
        pygame.draw.circle(sc,Lime,(410,440),10)
        fps = f1.render('FPS', 1 , OrangeRed)
        sc.blit(fps, (450,400))
        AboutTheGame = f1.render('Об игре', 1 , YELLOW)
        sc.blit(AboutTheGame, (770,400))
    #Открытие настроек управления
    if menu_gear == True and management == True and idGear==0:
        sc.blit(fon_gear,(xfon_gear,yfon_gear))
        Managemet = Fmenu.render('Управление', 1 , RED)
        sc.blit(Managemet, (500,120))
        jump_management = f1.render('Прыжок:  Пробел', 1 , YELLOW)
        sc.blit(jump_management, (400,250))
        ctrl_management = f1.render('Пригнуться:  Lctrl', 1 , OrangeRed)
        sc.blit(ctrl_management, (400,350))
    #Открытие настроек музыки 1
    if menu_gear == True and menumusic == True and idMusic==0 and idGear==0:
        sc.blit(fon_gear,(xfon_gear,yfon_gear))
        sc.blit(Grimmest,(450,435))
        Music_menu = Fmenu.render('Музыка', 1 , DarkMagenta)
        sc.blit(Music_menu, (560,120))
        Music1 = fm.render('Roy Knox - Lost In Sound', 1 , Cyan)
        sc.blit(Music1, (450,250))
        Music2 = fm.render('RUDE - Eternal Youth', 1 , Lime)
        sc.blit(Music2, (450,350))
        pygame.draw.circle(sc,Gray,(410,282),15)
        pygame.draw.circle(sc,RED,(410,282),10)
        pygame.draw.circle(sc,Gray,(410,380),15)
        pygame.draw.circle(sc,Gray,(410,478),15)
    #Открытие настроек музыки 2
    if menu_gear == True and menumusic == True and idMusic==1 and idGear==0:
        sc.blit(fon_gear,(xfon_gear,yfon_gear))
        sc.blit(Grimmest,(450,435))
        Music_menu = Fmenu.render('Музыка', 1 , DarkMagenta)
        sc.blit(Music_menu, (560,120))
        Music1 = fm.render('Roy Knox - Lost In Sound', 1 , Cyan)
        sc.blit(Music1, (450,250))
        Music2 = fm.render('RUDE - Eternal Youth', 1 , Lime)
        sc.blit(Music2, (450,350))
        pygame.draw.circle(sc,Gray,(410,282),15)
        pygame.draw.circle(sc,Gray,(410,380),15)
        pygame.draw.circle(sc,RED,(410,380),10)
        pygame.draw.circle(sc,Gray,(410,478),15)
    #Открытие настроек музыки 3
    if menu_gear == True and menumusic == True and idMusic==2 and idGear==0:
        sc.blit(fon_gear,(xfon_gear,yfon_gear))
        sc.blit(Grimmest,(450,435))
        Music_menu = Fmenu.render('Музыка', 1 , DarkMagenta)
        sc.blit(Music_menu, (560,120))
        Music1 = fm.render('Roy Knox - Lost In Sound', 1 , Cyan)
        sc.blit(Music1, (450,250))
        Music2 = fm.render('RUDE - Eternal Youth', 1 , Lime)
        sc.blit(Music2, (450,350))
        pygame.draw.circle(sc,Gray,(410,282),15)
        pygame.draw.circle(sc,Gray,(410,380),15)
        pygame.draw.circle(sc,Gray,(410,478),15)
        pygame.draw.circle(sc,RED,(410,478),10)
    # Открытие описания игры
    if menu_gear == True and description == True and idGear==0:
        sc.blit(fon_gear,(xfon_gear,yfon_gear))
        AboutTheGame = Fmenu.render('Об игре', 1 , YELLOW)
        sc.blit(AboutTheGame, (560,120))
        Text1 = fm.render("Ремастер легендарной игры",1,BLUE)
        sc.blit(Text1, (410,250))
        Text2 = fm.render("        Google 'Dino2D'",1,BLUE)
        sc.blit(Text2, (400,300))
        Text3 = fm.render("Создатель: SynerG",1,BLUE)
        sc.blit(Text3, (410,450))
    #Открытие настроек №2
    #1
    if menu_gear == True and idGear==1 and Collision_cactus == 1 and Collision_enemy == 0:
        sc.blit(fon_gear2,(xfon_gear,yfon_gear))
        sc.blit(Field,(475,450))
        Consol = f1.render('Консоль разработчика', 1 , BLACK)
        sc.blit(Consol, (420,120))
        pygame.draw.circle(sc,Gray,(410,282),15)
        pygame.draw.circle(sc,GREEN,(410,282),10)
        pygame.draw.circle(sc,Gray,(410,380),15)
        pygame.draw.circle(sc,RED,(410,380),10)
        Collision1 = fm.render('Коллизия кактусов', 1 , BLACK)
        sc.blit(Collision1, (450,250))
        Collision2 = fm.render('Коллизия птерадактелей', 1 , BLACK)
        sc.blit(Collision2, (450,350))
        print_text(input_text,500,460)
        # Мегающая чёрточка
        input_tick-=1
        if input_tick == 0:
            input_text = input_text[:-1]
        if input_tick == -10:
        	input_text += '|'
        	input_tick = 10 
    #2
    if menu_gear == True and idGear==1 and Collision_cactus == 0 and Collision_enemy == 1:
        sc.blit(fon_gear2,(xfon_gear,yfon_gear))
        sc.blit(Field,(475,450))
        Consol = f1.render('Консоль разработчика', 1 , BLACK)
        sc.blit(Consol, (420,120))
        pygame.draw.circle(sc,Gray,(410,282),15)
        pygame.draw.circle(sc,RED,(410,282),10)
        pygame.draw.circle(sc,Gray,(410,380),15)
        pygame.draw.circle(sc,GREEN,(410,380),10)
        Collision1 = fm.render('Коллизия кактусов', 1 , BLACK)
        sc.blit(Collision1, (450,250))
        Collision2 = fm.render('Коллизия птерадактелей', 1 , BLACK)
        sc.blit(Collision2, (450,350))
        print_text(input_text,500,460)
        # Мегающая чёрточка
        input_tick-=1
        if input_tick == 0:
        	input_text = input_text[:-1]
        if input_tick == -10:
        	input_text += '|'
        	input_tick = 10 
    #3
    if menu_gear == True and idGear==1 and Collision_cactus == 0 and Collision_enemy == 0:
        sc.blit(fon_gear2,(xfon_gear,yfon_gear))
        sc.blit(Field,(475,450))
        Consol = f1.render('Консоль разработчика', 1 , BLACK)
        sc.blit(Consol, (420,120))
        pygame.draw.circle(sc,Gray,(410,282),15)
        pygame.draw.circle(sc,RED,(410,282),10)
        pygame.draw.circle(sc,Gray,(410,380),15)
        pygame.draw.circle(sc,RED,(410,380),10)
        Collision1 = fm.render('Коллизия кактусов', 1 , BLACK)
        sc.blit(Collision1, (450,250))
        Collision2 = fm.render('Коллизия птерадактелей', 1 , BLACK)
        sc.blit(Collision2, (450,350))
        print_text(input_text,500,460)
        # Мегающая чёрточка
        input_tick-=1
        if input_tick == 0:
        	input_text = input_text[:-1]
        if input_tick == -10:
        	input_text += '|'
        	input_tick = 10 
    #4
    if menu_gear == True and idGear==1 and Collision_cactus == 1 and Collision_enemy == 1:
        sc.blit(fon_gear2,(xfon_gear,yfon_gear))
        sc.blit(Field,(475,450))
        Consol = f1.render('Консоль разработчика', 1 , BLACK)
        sc.blit(Consol, (420,120))
        pygame.draw.circle(sc,Gray,(410,282),15)
        pygame.draw.circle(sc,GREEN,(410,282),10)
        pygame.draw.circle(sc,Gray,(410,380),15)
        pygame.draw.circle(sc,GREEN,(410,380),10)
        Collision1 = fm.render('Коллизия кактусов', 1 , BLACK)
        sc.blit(Collision1, (450,250))
        Collision2 = fm.render('Коллизия птерадактелей', 1 , BLACK)
        sc.blit(Collision2, (450,350))
        print_text(input_text,500,460)
        # Мегающая чёрточка
        input_tick-=1
        if input_tick == 0:
        	input_text = input_text[:-1]
        if input_tick == -10:
        	input_text += '|'
        	input_tick = 10 
    #Закрытие настроек 
    if menu_gear == False:
        #Загрузка фона
        if save_texttime != 'Night' or save_texttime == 'Return':
            sc.blit(fon1,(xfon1,yfon1))
            sc.blit(fon2,(xfon2,yfon2))
        if save_texttime == 'Night':
            sc.blit(fonNight1,(xfon1,yfon1))
            sc.blit(fonNight2,(xfon2,yfon2))
        #Загрузка дороги
        sc.blit(road1,(xroad1,yroad1))
        sc.blit(road2,(xroad2,yroad2))
        sc.blit(road3,(xroad3,yroad3))
        sc.blit(road4,(xroad4,yroad4))
    
        sc.blit(road5,(xroad5,yroad5))
        sc.blit(road6,(xroad6,yroad6))
        sc.blit(road7,(xroad7,yroad7))
        sc.blit(road8,(xroad8,yroad8))
        #Dino
        if idSkin == 0:
            sc.blit(Dino[0],(xpos,ypos))
        elif idSkin == 1:
            sc.blit(Covid19[0],(xpos,ypos))
        elif idSkin == 2  or idSkin == 3 and save_textskin != 'Demon':
            sc.blit(Dino_Pharaoh[0],(xpos,ypos))
        elif idSkin == 3 and save_textskin == 'Demon':
            sc.blit(Demon[0],(xpos,ypos))
        #Загрузка кактусов
        sc.blit(cactus1,(xcactus1,ycactus1))
        sc.blit(cactus2,(xcactus2,ycactus2))
        sc.blit(cactus3,(xcactus3,ycactus3))
        sc.blit(cactus4,(xcactus4,ycactus4))
        #Загрузка звёзд
        if save_texttime == 'Night':
            if animCountStar +1 >=12:
            	animCountStar = 0
            if menu == True:
            	sc.blit(Small_Star_One[animCountStar // 6],(xss1,yss1))
            	sc.blit(Small_Star_Two[animCountStar // 6],(xbs2,ybs2))
            	sc.blit(Big_Star_One[animCountStar // 6],(xbs1,ybs1))
            	sc.blit(Big_Star_Two[animCountStar // 6],(xss2,yss2))
            	animCountStar += 1
        #Загрузка месяца
        if save_texttime == 'Night':
            sc.blit(Month,(xmonth,ymonth))
        #Загрузка луны
        if save_texttime == 'Night':
    	    sc.blit(Moon,(xmoon,ymoon))
    	# Загрузка облаков
        if save_texttime != 'Night' or save_texttime == 'Return':
    	    sc.blit(cloud1,(xcloud1,ycloud1))
    	    sc.blit(cloud2,(xcloud2,ycloud2))
        if save_texttime == 'Night':
    	    sc.blit(cloud_night1,(xcloud1,ycloud1))
    	    sc.blit(cloud_night2,(xcloud2,ycloud2))
        # Обработка открытие меню скинов
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                if 80<i.pos[0]<130:
                    if 10<i.pos[1]<60:
                        menu_skin = True
                        pygame.mixer.Sound.play(sound_select)
        # Обработка закрытия меню настроек   
        if i.type == pygame.MOUSEBUTTONDOWN and menu_skin == True:
            if i.button == 1:
                if 1010<=i.pos[0]<=1050:
                    if 100<=i.pos[1]<=120:
                        menu_skin = False
                        pygame.mixer.Sound.play(sound_quit)
        #Обработка выбора скинов
        if i.type == pygame.MOUSEBUTTONDOWN and menu_skin == True:
            if i.button == 1 and idSkin>0:
                if 350<=i.pos[0]<=370:
                    if 340<=i.pos[1]<=360:
                        idSkin-=1
                        pygame.mixer.Sound.play(sound_forward)
            if i.button == 1 and idSkin<3:
                if 1030<=i.pos[0]<=1050:
                    if 340<=i.pos[1]<=360:
                        idSkin+=1
                        pygame.mixer.Sound.play(sound_forward)
        if i.type == pygame.KEYDOWN and menu_skin == True:
            if i.key == pygame.K_RIGHT and idSkin<3:
                idSkin+=1
                pygame.mixer.Sound.play(sound_forward)
            elif i.key == pygame.K_LEFT and idSkin>0:
                idSkin-=1
                pygame.mixer.Sound.play(sound_forward)

    #Открытие меню скинов
    if menu_skin == True and idSkin == 0:
        sc.blit(fon_skin,(xfon_skin,yfon_skin))
        sc.blit(Dino[0],(xpos,ypos))
    if menu_skin == True and idSkin == 1:
        sc.blit(fon_skinCovid19,(xfon_gear,yfon_gear))
        sc.blit(Covid19[0],(xpos,ypos))
    if menu_skin == True and idSkin == 2:
        sc.blit(fon_skinPharaon,(xfon_gear,yfon_gear))
        sc.blit(Dino_Pharaoh[0],(xpos,ypos))
    if menu_skin == True and idSkin == 3:
        sc.blit(fon_skinDemon,(xfon_gear,yfon_gear))
        sc.blit(Demon[0],(xpos,ypos))
    if menu_skin == True:
        Skins = Fmenu.render('Скины', 1 , BLUE)
        sc.blit(Skins, (580,110))
        if idSkin == 0:
            Dino_Skin = Fmenu.render('Дино', 1 , GREEN)
            sc.blit(Dino_Skin, (595,485))
        if idSkin == 1:
            Covid19_Skin = Fmenu.render('#СидиДома', 1 , BLACK)
            sc.blit(Covid19_Skin, (495,485))
        if idSkin == 2:
            Pharaoh_Skin = Fmenu.render('Фараон', 1 , YELLOW)
            sc.blit(Pharaoh_Skin, (580,485))
        if idSkin == 3 and save_textskin != 'Demon':
            Demon_Skin = Fmenu.render('Демон', 1 , RED)
            sc.blit(Demon_Skin, (580,485))
            sc.blit(Lock,(655,296))
        if idSkin == 3 and save_textskin == 'Demon':
            Demon_Skin = Fmenu.render('Демон', 1 , RED)
            sc.blit(Demon_Skin, (580,485))

    if menu ==True:
        score_counter=f.render("HI:   "+ str(int(record_points)) + "    " +str(int(points))+"", 1 , WHITE)
        sc.blit(score_counter, (1220,0))
        sc.blit(gear,(xgear,ygear))
        sc.blit(skins_menu,(xskins,yskins))
    if idFPS==0:
        pygame.display.set_caption('Dino')
    elif idFPS==1:
        pygame.display.set_caption(str('Dino                                                                                                                                                             FPS:' + str(int(clock.get_fps()))))

    if menu ==True and menu_gear == True and idGear == 1 and need_input != True:
    	sc.blit(Field,(475,450))
    	need_text = f1.render('Введите код', 1 , WHITE)
    	sc.blit(need_text, (500,445))

    #Конец цикла        
    pygame.display.update()
    clock.tick(FPS)
    
#Загрузка музыки
if idMusic==0 and idMusic != 2:
    pygame.mixer.music.load(music1)
    pygame.mixer.music.set_volume(0.25)
if idMusic==1 and idMusic != 2:
    pygame.mixer.music.load(music2)
    pygame.mixer.music.set_volume(1)

#Музыка
if menu == False and idMusic != 2:
    pygame.mixer.music.play(-1)
        
#Цикл игры
Points100=100
GameOver = False
GO = 1
while run:
    #Загрузка фона
    if save_texttime != 'Night' or save_texttime == 'Return':
        sc.blit(fon1,(xfon1,yfon1))
        sc.blit(fon2,(xfon2,yfon2))
    if save_texttime == 'Night':
        sc.blit(fonNight1,(xfon1,yfon1))
        sc.blit(fonNight2,(xfon2,yfon2))
    #Загрузка дороги
    sc.blit(road1,(xroad1,yroad1))
    sc.blit(road2,(xroad2,yroad2))
    sc.blit(road3,(xroad3,yroad3))
    sc.blit(road4,(xroad4,yroad4))
    
    sc.blit(road5,(xroad5,yroad5))
    sc.blit(road6,(xroad6,yroad6))
    sc.blit(road7,(xroad7,yroad7))
    sc.blit(road8,(xroad8,yroad8))
    #Загрузка Дино с анимацией
    if idSkin == 0:
        if animCount +1 >= 9:
            animCount = 0
        if speed >= 15 and ypos==570  and motion == 'STOP':
            sc.blit(Dino[animCount // 3],(xpos,ypos))
            animCount += 1
        elif ypos<570:
            sc.blit(Dino[3],(xpos,ypos))
        #Загрузка Дино с анимацией вприсяди
        if animCountDown +1 >=12:
            animCountDown = 0
        if speed >= 15 and ypos == 570 and motion == 'ctrl':
            sc.blit(Dino_down[animCountDown // 6],(xpos,ypos))
            animCountDown += 1

    #Дино СидиДома
    if idSkin == 1:
        if animCount +1 >= 9:
            animCount = 0
        if speed >= 15 and ypos==570  and motion == 'STOP':
            sc.blit(Covid19[animCount // 3],(xpos,ypos))
            animCount += 1
        elif ypos<570:
            sc.blit(Covid19[3],(xpos,ypos))
        #Загрузка Дино с анимацией вприсяди
        if animCountDown +1 >=12:
            animCountDown = 0
        if speed >= 15 and ypos == 570 and motion == 'ctrl':
            sc.blit(Covid19_down[animCountDown // 6],(xpos,ypos))
            animCountDown += 1

    #Дино Фараон
    if idSkin == 2 or idSkin == 3 and save_textskin != 'Demon':
        if animCount +1 >= 9:
            animCount = 0
        if speed >= 15 and ypos==570  and motion == 'STOP':
            sc.blit(Dino_Pharaoh[animCount // 3],(xpos,ypos))
            animCount += 1
        elif ypos<570:
            sc.blit(Dino_Pharaoh[3],(xpos,ypos))
        #Загрузка Дино с анимацией вприсяди
        if animCountDown +1 >=12:
            animCountDown = 0
        if speed >= 15 and ypos == 570 and motion == 'ctrl':
            sc.blit(Dino_down_Pharaoh[animCountDown // 6],(xpos,ypos))
            animCountDown += 1

    #Дино Демон
    if idSkin == 3 and save_textskin == 'Demon':
        if animCount +1 >= 9:
            animCount = 0
        if speed >= 15 and ypos==570  and motion == 'STOP':
            sc.blit(Demon[animCount // 3],(xpos,ypos))
            animCount += 1
        elif ypos<570:
            sc.blit(Demon[3],(xpos,ypos))
        #Загрузка Дино с анимацией вприсяди
        if animCountDown +1 >=12:
            animCountDown = 0
        if speed >= 15 and ypos == 570 and motion == 'ctrl':
            sc.blit(Demon_down[animCountDown // 6],(xpos,ypos))
            animCountDown += 1

    #Загрузка птерадактиля с анимацией
    if points >=500:
        if animCount2 +1 >= 12:
            animCount2 = 0
        if speed>=0:
            sc.blit(Pteradactyl[animCount2 // 6],(xpos_enemy,ypos_enemy))
            animCount2 += 1

    #Загрузка кактусов
    sc.blit(cactus1,(xcactus1,ycactus1))
    sc.blit(cactus2,(xcactus2,ycactus2))
    sc.blit(cactus3,(xcactus3,ycactus3))
    sc.blit(cactus4,(xcactus4,ycactus4))
    #Загрузка звёзд
    if save_texttime == 'Night':
    	if animCountStar +1 >=12:
    		animCountStar = 0
    	if run == True:
	        sc.blit(Small_Star_One[animCountStar // 6],(xss1,yss1))
	        sc.blit(Small_Star_Two[animCountStar // 6],(xbs2,ybs2))
	        sc.blit(Big_Star_One[animCountStar // 6],(xbs1,ybs1))
	        sc.blit(Big_Star_Two[animCountStar // 6],(xss2,yss2))
	        animCountStar += 1
    #Загрузка месяца
    if save_texttime == 'Night':
    	sc.blit(Month,(xmonth,ymonth))
    #Загрузка луны
    if save_texttime == 'Night':
    	sc.blit(Moon,(xmoon,ymoon))
    #Загрузка облаков
    if save_texttime != 'Night' or save_texttime == 'Return':
	    sc.blit(cloud1,(xcloud1,ycloud1))
	    sc.blit(cloud2,(xcloud2,ycloud2))
    if save_texttime == 'Night':
	    sc.blit(cloud_night1,(xcloud1,ycloud1))
	    sc.blit(cloud_night2,(xcloud2,ycloud2))

    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            run = False
            pygame.quit()
        if keyboard == True:
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_SPACE:
                    isJump = True
                    if ypos==570 and speed!=0:
                        pygame.mixer.Sound.play(sound_jump)
                if i.key == pygame.K_LCTRL:
                    if ypos == 570:
                        motion = 'ctrl'
            elif i.type == pygame.KEYUP:
                if i.key == pygame.K_LCTRL:
                    motion = 'STOP'
    #Прыжок 
    if isJump == True and speed!=0:
        if jumpCount>=-10:
            if jumpCount<0:
                ypos+=(jumpCount ** 2) / 2.75
            else:
                ypos-=(jumpCount ** 2) / 2.75
            jumpCount-=1
        else:
            isJump = False
            jumpCount = 10
                    
    #Движение кактусов ,дороги
    if speed>0:
        xcactus1 -= speed
        xcactus2 -= speed
        xcactus3 -= speed
        xcactus4 -= speed
        xroad1 -= speed
        xroad2 -= speed
        xroad3 -= speed
        xroad4 -= speed
        xroad5 -= speed
        xroad6 -= speed
        xroad7 -= speed
        xroad8 -= speed
        if points >=500:
            xpos_enemy-=speed_enemy
        #Движение облаков
        if run == True:
            xcloud1 -= speed_cloud1
            if run == True:
                xcloud2 -= speed_cloud2
        #Движение месяца и звёзд
        if run == True and save_texttime == 'Night':
            xmonth -= speed_month
            xmoon -= speed_moon
            xss1 -= speed_star
            xss2 -= speed_star
            xbs1 -= speed_star
            xbs2 -= speed_star
        #Перемещение дороги с одного края на другой       
        if run==True:
            if xroad1<=-600:
                xroad1=xroad8+600
            elif xroad2<=-600:
                xroad2=xroad1+600

            elif xroad3<=-600:
                xroad3=xroad2+600
            elif xroad4<=-600:
                xroad4=xroad3+600

            elif xroad5<=-600:
                xroad5=xroad4+600
            elif xroad6<=-600:
                xroad6=xroad5+600

            elif xroad7<=-600:
                xroad7=xroad6+600
            elif xroad8<=-600:
                xroad8=xroad7+600
                
        #Перемещение облаков с одного края на другой    
        if xcloud1<=-100:
            xcloud1=1500
            ycloud1 = randint(200,400)
        if xcloud2<=-100:
            xcloud2=1500
            ycloud2 = randint(0,200)
        #Перемещение звёзд с одного края на другой
        if save_texttime == 'Night' and xss1<=-20:
            xss1=1420
            yss1 = randint(0,400)
        if save_texttime == 'Night' and xss2<=-20:
            xss2=1420
            yss2 = randint(0,400)
        if save_texttime == 'Night' and xbs1<=-20:
            xbs1=1420
            ybs1 = randint(0,400)
        if save_texttime == 'Night' and xbs2<=-20:
            xbs2=1420
            ybs2 = randint(0,400)
        #Перемещение месяца с одного края на другой
        if save_texttime == 'Night' and xmonth<=-100:
            xmonth=3000
        #Перемещение луны с одного края на другой
        if save_texttime == 'Night' and xmoon<=-100:
            xmoon=3000

        #Перемещение Птера с одного края на другой + по оси y
        if points >=500:
            if xpos_enemy<=-100:
                xpos_enemy= randint(1500,4000)
            if xpos_enemy>=1500:
                yrandom = randint(1,2)
                if yrandom == 1:
                    ypos_enemy = 590
                elif yrandom == 2:
                    ypos_enemy = 550
        
        #Перемещение кактусов и прибавление расстояния кактусам
        if xcactus1<=-100:
            crmini1+=30
            crmax1+=30
            xcactus1=xcactus4+cr1
            cr1= randint(crmini1 , crmax1)
        if xcactus2<=-100:
            crmini2+=30
            crmax2+=30
            xcactus2=xcactus1+cr2
            cr2= randint(crmini2 , crmax2)
        if xcactus3<=-100:
            crmini3+=30
            crmax3+=30
            xcactus3=xcactus2+cr3
            cr3= randint(crmini3 , crmax3)
        if xcactus4<=-100:
            crmini4+=30
            crmax4+=30
            xcactus4=xcactus3+cr4
            cr4= randint(crmini4 , crmax4)
            
    #Начисление очков и скорости
    if speed>0:
        points+=0.5
        speed+=0.015
        speed_enemy+=0.015
        speed_down = speed
    #Звук начисления очков
    if points == Points100:
        pygame.mixer.Sound.play(sound_points)
        Points100+=100
    # Счётчик очков 
    if speed!=0:
        score_counter=f.render("HI:   "+ str(int(record_points)) + "    " +str(int(points))+"", 1 , WHITE)
        sc.blit(score_counter, (1220,0))
        pygame.display.update()
    #Коллизия кактусов
    if Collision_cactus == 1:
        if ypos>=485 and -30<=xcactus1<=60 or ypos>=550 and -60<=xcactus2<=75 or ypos>=485 and -30<=xcactus3<=60 or ypos>=485 and -40<=xcactus4<=80:
            speed = 0
    #Коллизия Птера
    if Collision_enemy == 1:
        if points >=500:
            #Коллизия Птера по (координата-1)
            if ypos_enemy==590 and -50<=xpos_enemy<=100 and ypos>=540:
                speed = 0
            #Коллизия Птера по (координата-2)
            if ypos_enemy<=550 and -50<=xpos_enemy<=110 and 490<=ypos<=570:
                speed = 0
            #Коллизия Птера по (координата-2) когда Дино вприсяди 
            if ypos_enemy==550 and -50<=xpos_enemy<=110 and 490<=ypos<=570 and motion == 'ctrl':
                speed = speed_down
    #Экран Game Over    
    if speed == 0:
        keyboard = False
        motion = 'STOP'
        GameOver = True
        record_points=points
        sc.blit(road1,(xroad1,yroad1))
        sc.blit(road2,(xroad2,yroad2))
        sc.blit(road3,(xroad3,yroad3))
        sc.blit(road4,(xroad4,yroad4))
        sc.blit(road5,(xroad5,yroad5))
        sc.blit(road6,(xroad6,yroad6))
        sc.blit(road7,(xroad7,yroad7))
        sc.blit(road8,(xroad8,yroad8))
        sc.blit(cactus1,(xcactus1,ycactus1))
        sc.blit(cactus2,(xcactus2,ycactus2))
        sc.blit(cactus3,(xcactus3,ycactus3))
        sc.blit(cactus4,(xcactus4,ycactus4))
        if save_texttime != 'Night' or save_texttime == 'Return':
            sc.blit(cloud1,(xcloud1,ycloud1))
            sc.blit(cloud2,(xcloud2,ycloud2))
        if save_texttime == 'Night':
            sc.blit(cloud_night1,(xcloud1,ycloud1))
            sc.blit(cloud_night2,(xcloud2,ycloud2))

        if points>=500:
            sc.blit(Pteradactyl[animCount2 // 6],(xpos_enemy,ypos_enemy))
            animCount2 += 1
        if idSkin == 0:
            if ypos<570:
                sc.blit(dead_jump,(xpos,ypos))
            if ypos==570:
                sc.blit(dino_dead,(xpos,ypos))
        if idSkin == 1:
            if ypos<570:
                sc.blit(Covid19_dead_jump,(xpos,ypos))
            if ypos==570:
                sc.blit(Covid19_dino_dead,(xpos,ypos))       
        if idSkin == 2:
            if ypos<570:
                sc.blit(PharaohJump_Dead,(xpos,ypos))
            if ypos==570:
                sc.blit(Pharaoh_Dead,(xpos,ypos))
        if idSkin == 3:
            if ypos<570:
                sc.blit(Demon_JumpDead,(xpos,ypos))
            if ypos==570:
                sc.blit(Demon_dead,(xpos,ypos))
        
        score_counter=f.render("HI:   "+ str(int(record_points)) + "    " +str(int(points))+"", 1 , WHITE)
        sc.blit(score_counter, (1220,0))
        gameOver=f1.render('Game Over', 1 , RED)
        sc.blit(gameOver, (565,300))
        pygame.mixer.music.pause()
        pygame.display.update()
        
    if GameOver == True and GO == 1:
        pygame.mixer.Sound.play(sound_dead)
        GO = 0
    if idFPS==0:
        pygame.display.set_caption('Dino')
    elif idFPS==1:
        pygame.display.set_caption(str('Dino                                                                                                                                                             FPS:' + str(int(clock.get_fps()))))

    #Конец цикла        
    pygame.display.update()
    clock.tick(FPS)
