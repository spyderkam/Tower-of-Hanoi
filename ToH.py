#!/user/bin/env python3

# Python version of Hanoi Towers game originally written in Ruby 

winning_pile = [1, 2, 3, 4]
p1 = [1, 2, 3, 4]
p2 = []
p3 = []

print("\nTOWERS OF HANOI\n\nLet's Play",)

while True:
    print(f"\np1 = {p1}\np2 = {p2}\np3 = {p3}")
    print("select a disk")
    disk = int(input())     # expand on this

    if (p1 == [] or disk != p1[0]) and (p2 == [] or disk != p2[0]) \
        and (p3 == [] or disk != p3[0]):
        while True:
            print("please select the top existing disk from any pile")
            disk = int(input())
            if (p1 != [] and disk == p1[0]) or (p2 != [] and disk == p2[0]) \
                and (p3 != [] and disk != p3[0]):
                break

    def condition(input, pile1, pile2, pile3):
        if pile1 and input == pile1[0]:
            del pile1[0]
        elif pile2 and input == pile2[0]:
            del pile2[0]
        elif pile3 and input == pile3[0]:
            del pile3[0]
        # print(f"xxx ~ p1 = {p1}, p2 = {p2}, p3 = {p3} ~ xxx")

    print("Which pile would you like to stack this disk on?")
    pile = input()
    if pile == 'p1' and (p1 == [] or disk < p1[0]):
        condition(disk, p1, p2, p3)
        p1.insert(0, disk)
    elif pile == 'p2' and (p2 == [] or disk < p2[0]):
        condition(disk, p1, p2, p3)
        p2.insert(0, disk)
    elif pile == 'p3' and (p3 == [] or disk < p3[0]):
        condition(disk, p1, p2, p3)
        p3.insert(0, disk)
    else:
        print("You can't do that!")

    if p3 == winning_pile:  # easy version: p2 == winning_pile or p3 == winning_pile 
        print("WE HAVE A WINNER!!!")
        break
