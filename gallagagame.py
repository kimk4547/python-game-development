import pgzrun
import random

width= 1200
height= 600

#-- colors --
white = (255, 255, 255)
black = (0,0,0)

#-- actors
ship = Actor('galaga')
ship.pos = (width//2, height - 60)

speed = 5
score = 0
#bullets and enemies
bullets = []
enemies = []
life = 3
#start with a few enemies
for _ in range(5):
    e = Actor("bug")
    e.x = random.randint(50 , width -50)
    e.y = random.randint(-300,-100)
    enemies.append(e)
#-- UI ---
def displayScore():
    screendraw.text(str(score),(50,30),color = white, fontsize = 42)
def lives():
    screen.draw.text("Lives Remaining: {}".format(str(life)), (800,30),color = white, fontsize = 42)


#--- input shooting bullets
def on_key_down(key):
    if key == keys.SPACE:
        b = Actor('bullet')
        b.x = ship.x
        b.y - ship.y - 50
        bullets.append(b)
#Game loop
game_over = False
def update():
    global score, life, game_over
#ship movement
    if keyboard.left():
        ship.x -= speed
    if keyboard.right():
        ship.y += speed
    ship.x = max(0,min(width, ship.x)) #<--- stops ship from going offscreen

#bullet movement
    for bullet in bullets[:]:
        if bullet.y <= 0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10
#enemy movement and collision
    for enemy in enemies[:]:
        enemy.y += 5 #<---- enemies will fall down
        #enemy reaches the bottom
        if enemy.y >= height:
            enemy.y = -100
            enemy.x = random.randint(50,width -50)
        for bullet in bullets[:]:
            if enemy.collidirect(bullet):
                score += 100
                bullets.remove(bullet)
                enemies.remove(enemy)
#respawn the bug 
                new_e = Actor('bug')
                new_e.x = random.randint(50 , width -50)
                new_e.y = random.randint(-300,-100)
                enemies.append(new_e)
                break
#check if bug hit the ship
        if enemy.collidirect(ship):
            life = life -1
            enemies.remove(enemy)
            new_e = Actor("bug")
            new_e.x = random.randint(50 , width -50)
            new_e.y = random.randint(-300,-100)
            enemies.append(new_e)
            if life <= 0:
                game_over = True
#-- draw
def draw():
    screen.clear()
    screen.fill(black)
    if game_over:
        screen.draw.text("Game Over", center = (width//2, height//2), color = "white", fontsize = 30)
        screen.draw.text("Final Score{}".format(score), center = (width//2, height//2+80), color = "white", fontsize = 30)
    else:
        for bullet in bullets:
            bullet.draw()
        for enemy in enemies:
            enemy.draw()
        ship.draw()
        displayScore()
        lives()
pgzrun.go()
    