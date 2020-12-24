from turtle import Turtle

starting_position = [(-40, 0), (-20, 0), (0, 0)]
moving = 20


class Snake:

    def __init__(self):


        self.sagment_List = []
        self.snake_maker()
        self.head = self.sagment_List[0]

    def snake_maker(self):
        for position in starting_position:
            self.add_newsagment(position)


    def add_newsagment(self, position):
        t = Turtle(shape='square')
        t.color('white')
        t.pencolor('white')
        t.penup()
        t.goto(position)
        self.sagment_List.append(t)

    def extant(self):
        self.add_newsagment(self.sagment_List[-1].position())

    def move(self):
        for sag_num in range(len(self.sagment_List) - 1, 0, -1):
            new_x = self.sagment_List[sag_num - 1].xcor()
            new_y = self.sagment_List[sag_num - 1].ycor()
            self.sagment_List[sag_num].goto(new_x, new_y)
        self.head.forward(moving)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
