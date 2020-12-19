# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape('turtle')
# timmy.forward(100)
#
# myscreen = Screen()
# myscreen.exitonclick()


from prettytable import PrettyTable

Table = PrettyTable()


Table.add_column(
    "Pokemon Name",[
        'Pikachu',
        'Squirtle',
        'Charmandar'])

Table.add_column(
    "Type", [
        "Eletric",
        "Water",
        "Fire"
    ]
)
Table.align = "l"
print(Table)