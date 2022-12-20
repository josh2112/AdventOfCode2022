import numpy

with open("input-sample.txt", "r") as f:
    jets = [-1 if c == "<" else 1 for c in f.read().strip()]

rocks = (
    [[1, 1, 1, 1]],
    [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
    [[0, 0, 1], [0, 0, 1], [1, 1, 1]],
    [[1], [1], [1], [1]],
    [[1, 1], [1, 1]],
)

rockheight = 0
terrain = [1, 1, 1, 1, 1, 1, 1]


def print_line(line):
    print(f"|{''.join('@' if b else '.' for b in line)}|")


def print_room(roomheight, rock, rx, ry, terrain):
    room = [[0 for x in range(7)] for y in range(roomheight)]
    for r in range(len(rock)):
        room[r + ry][rx : len(rock[r]) + rx] = rock[r]
    if sum(terrain) > 0:
        room[roomheight - 1] = terrain

    for r in room:
        print_line(r)


ij = 0
for ir in range(2):
    rock = rocks[ir % len(rocks)]
    roomheight = len(rock) + 4
    rx, ry = 2, 0

    while True:
        # Apply jet
        jet = jets[ij % len(jets)]
        ij += 1
        if (jet == -1 and rx > 0) or (jet == 1 and rx + len(rock[0]) < 7):
            # TODO: Also check collision with terrain
            print("Applying jet", jet)
            rx += jet
        # Apply fall
        # - If bottom line of rock is more than 1 above room height, drop it
        print_room(roomheight, rock, rx, ry, terrain)
        if ry + len(rock) < roomheight - 1:
            print("Applying fall")
            ry += 1
        # Else, see if terrain and bottom line of rock have any overlap
        else:
            overlap = next((a + b for a, b in zip(terrain, rock[len(rock) - 1]) if a + b > 1), None)
            if not overlap:
                print("Applying fall")
                ry += 1
            else:
                terrain = [0, 0, 0, 0, 0, 0, 0]
                terrain[rx : len(rock[0]) + rx] = rock[0]
                break

    print_room(roomheight, rock, rx, ry, terrain)
    print("New terrain: ", end="")
    print_line(terrain)
