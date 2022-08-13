import random

h1 = 1
h2 = 1
c1 = 1
c2 = 1
def h(n):
    p = n[0]
    o = n[2]
    print(f"{p},{o}")
    match p:
        case 1:
            x = h1
        case 2:
            x = h2
    match o:
        case 1:
            y = c1
        case 2:
            y = c2
    return x,y

def f(input):
    hand,hand2 = h(input)
    print(f"hand 1 is {hand}\n hand 2 is {hand2}")
    hand2 += hand
    if hand2 > 4:
        hand2 = 0
    print("passed")
    return hand2

while True:
    p1 = input("hand -> hand - f#/f#:\n")
    if p1 == "break":
        break
    try:
        f(p1)
    except:
        print("Error")