import turtle,math,random

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Labirent oyunu")
wn.setup(700,700)
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor()+24
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_left(self):
        move_to_x = player.xcor()-24 #oyuncunun bulunduğu yerin solunda taş yoksa oraya geçebilir.
        move_to_y = player.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = player.xcor()+24
        move_to_y = player.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self,other):
        a=self.xcor()-other.xcor()
        b=self.ycor()-other.ycor()
        distance=math.sqrt((a**2)+(b**2))
        if distance<5:
            return True
        else:
            return False

class Treasures(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class Enemy(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold=25
        self.goto(x,y)
        self.direction=random.choice(["up","left","right","down"])

    def move(self):
        if self.direction=="up":
            dx=0
            dy=24
        elif self.direction=="down":
            dx=0
            dy=-24
        elif self.direction=="right":
            dx=24
            dy=0
        elif self.direction=="left":
            dx=-24
            dy=0
        else:
            dx=0
            dy=0

        move_to_x=self.xcor()+dx
        move_to_y=self.ycor()+dy
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        else:
            self.direction=random.choice(["up","down","left","right"])

        turtle.ontimer(self.move,t=random.randint(100,200))


walls=[]
treasures=[]
enemy= []
levels=[""]

level_1=[
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XPXXXXXXXX       XXXXXXXXXXXXX",
"X XXXXXXXX   XXXXXXX XXXXXXXXX",
"X       XX    XXXXXXX XXXXXXXX",
"XXXXX   XX  XXXXXXXX XXXXXXXXX",
"XXXXX   XXXXXXXXXXX XXXXXXXXXX",
"XXXXX   XXXXXXX X     XXXXXXXX",
"XXXXX   XXXXXXXXXXXXXXX  XXXXX",
"X XXX           XXXXXXXXXXXXXX",
"X XXXXXXXX   XXXXXXX XXXXXXXXX",
"X              XXXXXXX XXXXXXX",
"XXXXXXX      XXXXXXX XXXXXXXXX",
"XXXXX       XXXXXXX XXXXXXXXXX",
"XXXXX        E         XXXXXXX",
"XXXX    XXXXXXXXX        XXXXX",
"XXXXX   XX  XXXXXXXX XXXXXXXXX",
"XXXXX   XXXXXXXXXXX XXXXXXXXXX",
"XXXXX   XXXXXXX X     XXXXXXXX",
"XXXXX   XXXXXXXXXXXXXXX  XXXXX",
"X XXX           XXXXXXXXXXXXXX",
"X XXXXXXXX E  XXXXXXX XXXXXXXX",
"X       E       XXXXXXX XXXXXX",
"XXXXXXX      XXXXXXX XXXXXXXXX",
"XXXXX       XXXXXXX XXXXXXXXXX",
"XXXXXXXXX             XXXXXXXX",
"XXXX    XXXXXXXXX   T    XXXXX",
]

levels.append(level_1)

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #x ve y koordinatlarını bul.
            character=level[y][x]
            screen_x = -288 + (x * 24)#karenin tam oturması için 24 katı seçildi
            screen_y = 288 - (y * 24)

            if character=="X":
                pen.goto(screen_x,screen_y)
                pen.stamp()#taşları yazdır
                walls.append((screen_x,screen_y))#taşların konumlarını kaydet(daha sonra içinden geçilmemesi için kullanılacak)

            if character == "P":#eğer oluşturduğumuz listede p harfi varsa oraya player class'ından oluştuduğumz nesneyi koy
                player.goto(screen_x,screen_y)

            if character=="T":
                treasures.append(Treasures(screen_x,screen_y))

            if character=="E":
                enemy.append(Enemy(screen_x,screen_y))

pen=Pen()
player=Player()
setup_maze(levels[1])
turtle.listen()
turtle.onkey(player.go_up,"w")
turtle.onkey(player.go_down,"s")
turtle.onkey(player.go_left,"a")
turtle.onkey(player.go_right,"d")

wn.tracer(0)

for e in enemy:
    turtle.ontimer(e.move,t=250)
while True:

    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold=player.gold+treasure.gold
            print("Player gold {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)

    for e in enemy:
        if player.is_collision(e):
            exit()


    wn.update()









