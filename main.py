import pygame
pygame.init()

win = pygame.display.set_mode((1600, 900))

pygame.display.set_caption("The Game")

walkRight = [pygame.image.load('images/walk_r_01.png'), pygame.image.load('images/walk_r_02.png'), pygame.image.load('images/walk_r_03.png'), pygame.image.load('images/walk_r_03.png'), pygame.image.load('images/walk_r_04.png'), pygame.image.load('images/walk_r_05.png'), pygame.image.load('images/walk_r_06.png'), pygame.image.load('images/walk_r_07.png'), pygame.image.load('images/walk_r_08.png')]
walkLeft = [pygame.image.load('images/walk_l_01.png'), pygame.image.load('images/walk_l_02.png'), pygame.image.load('images/walk_l_03.png'), pygame.image.load('images/walk_l_03.png'), pygame.image.load('images/walk_l_04.png'), pygame.image.load('images/walk_l_05.png'), pygame.image.load('images/walk_l_06.png'), pygame.image.load('images/walk_l_07.png'), pygame.image.load('images/walk_l_08.png')]

hitRight = [pygame.image.load('images/hit_r_01.png'), pygame.image.load('images/hit_r_02.png'), pygame.image.load('images/hit_r_03.png'), pygame.image.load('images/hit_r_01.png'), pygame.image.load('images/hit_r_02.png'), pygame.image.load('images/hit_r_03.png'), pygame.image.load('images/hit_r_01.png'), pygame.image.load('images/hit_r_02.png'), pygame.image.load('images/hit_r_03.png')]
hitLeft = [pygame.image.load('images/hit_l_01.png'), pygame.image.load('images/hit_l_02.png'), pygame.image.load('images/hit_l_03.png'), pygame.image.load('images/hit_l_01.png'), pygame.image.load('images/hit_l_02.png'), pygame.image.load('images/hit_l_03.png'), pygame.image.load('images/hit_l_01.png'), pygame.image.load('images/hit_l_02.png'), pygame.image.load('images/hit_l_03.png')]

bg = pygame.image.load('images/background1.jpg')
char = pygame.image.load('images/stand01.png')

clock = pygame.time.Clock()

screenWidth = 1600
# First character
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True

    def draw(self,win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

        if keys[pygame.K_j]:
            if self.left:
                win.blit(hitLeft[self.walkCount//3], (self.x, self.y))
                self.right = False
                self.left = True
                self.standing = True
            else:
                win.blit(hitRight[self.walkCount//3], (self.x, self.y))
                self.right = True
                self.left = False
                self.standing = True


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
# drawing circle
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redrawGameWindow():
    win.blit(bg, (0, 0))
    hero.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

#Main Loop
hero = player(300, 400, 140, 67)
bullets = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < screenWidth and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

# try hit
    # if keys[pygame.K_j]:
    #     if hero.left:
    #         win.blit(hitLeft[0], (hero.x, hero.y))
    #     else:
    #         win.blit(hitRight[0], (hero.x, hero.y))

    if keys[pygame.K_k]:
        if hero.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 30:
            bullets.append(projectile(round(hero.x + hero.width // 2), round(hero.y + hero.height // 2), 6, (0, 0, 0), facing))

    if keys[pygame.K_a] and hero.x > hero.vel:
        hero.x -= hero.vel
        hero.left = True
        hero.right = False
        hero.standing = False
    elif keys[pygame.K_d] and hero.x < screenWidth - hero.width - hero.vel:
        hero.x += hero.vel
        hero.right = True
        hero.left = False
        hero.standing = False
    else:
        hero.standing = True
        hero.walkCount = 0

    if not(hero.isJump):
        if keys[pygame.K_SPACE]:
            hero.isJump = True
            hero.right = False
            hero.left = False
            hero.walkCount = 0
    else:
        if hero.jumpCount >= -10:
            neg = 1
            if hero.jumpCount < 0:
                neg = -1
            hero.y -= (hero.jumpCount ** 2) * 0.5 * neg
            hero.jumpCount -= 1
        else:
            hero.isJump = False
            hero.jumpCount = 10

    redrawGameWindow()

pygame.quit()