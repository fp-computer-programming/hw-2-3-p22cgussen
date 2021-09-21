# author: CCG 9/21/21

population1 = 331832432
person = 25
#day is amount of seconds in day
day = 60 * 60 * 24
number_days = 365

population2 = population1 + ((day * number_days) // person)

print(population2)