import sys
import time

map = [
    [ 1, 1, 1, 1, 1, 2, 1, 1 ],
    [ 1, 0, 1, 0, 0, 0, 0, 1 ],
    [ 1, 0, 0, 0, 1, 1, 0, 1 ],
    [ 1, 1, 0, 1, 1, 0, 1, 1 ],
    [ 1, 0, 0, 0, 0, 0, 0, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1 ]
]


def show_map():
    print()
    for row in map:
        for item in row:
            print(item, end="")
        print()

print("A labyrinth of zeros:", end="")
show_map()

def action(x, y):
    if map[y][x] == 2:
        print()
        print("The way through the labyrinth:", end="")
        show_map()
        print("FINISHED!!!")
        sys.exit()
    if map[y][x] == 0:
        map[y][x] = "*"
        #time.sleep(2)
        AI(x, y)


def AI(x, y):
    action(x+1, y)
    action(x-1, y)
    action(x, y+1)
    action(x, y-1)
    

AI(5, 3)