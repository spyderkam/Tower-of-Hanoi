#!/user/bin/env python3

# Python version of Hanoi Towers game originally written in Ruby

#winning_pile = [1, 2, 3, 4]  # easy version
p1 = [1,2,3,4]
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

    def condition(input):
        if p1 and input == p1[0]:
            del p1[0]
        elif p2 and input == p2[0]:
            del p2[0]
        elif p3 and input == p3[0]:
            del p3[0]

    print("Which pile would you like to stack this disk on?")
    pile = input()
    if pile == 'p1' and (p1 == [] or disk < p1[0]):
        condition(disk)
        p1.insert(0, disk)
    elif pile == 'p2' and (p2 == [] or disk < p2[0]):
        condition(disk)
        p2.insert(0, disk)
    elif pile == 'p3' and (p3 == [] or disk < p3[0]):
        condition(disk)
        p3.insert(0, disk)
    else:
        print("You can't do that!")

    if p3 == [1,2,3,4]:  # easy version: p2 == winning_pile or p3 == winning_pile
        print("WE HAVE A WINNER!!!")
        break
