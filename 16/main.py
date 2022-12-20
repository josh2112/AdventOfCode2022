import re

# https://adventofcode.com/2022/day/16

SAMPLE = 1
PART = 1


def parse(line):
    v, fr, tunnels = re.findall(r"Valve (\w\w) has flow rate=(\d+); tunnels? leads? to valves? ([\w, ]*)", line)[0]
    return (v, fr, tunnels.split(", "))


with open("input-sample.txt" if SAMPLE else "input.txt", "r") as f:
    valves = {v: (int(fr), tunnels) for v, fr, tunnels in [parse(l) for l in f.readlines()]}

START = None
MOVE = 1
OPEN = 2

dist = {}


class Move:
    def __init__(self, prev, action, valve, timeleft):
        global valves
        self.prev, self.action, self.valve, self.timeleft = prev, action, valve, timeleft
        self.score = self.prev.score if self.prev else 0
        if self.prev and self.prev.action == OPEN:
            self.score += valves[prev.valve][0] * timeleft
        if self.action == OPEN:
            self.valves_open = self.prev.valves_open.copy() + [prev.valve]
        else:
            self.valves_open = self.prev.valves_open if self.prev else []

    def __repr__(self) -> str:
        return f"{'move' if self.action == MOVE else ('open' if self.action == OPEN else 'start')} {self.valve} ({self.score})"


solutions = []

dist = {}

for i in valves.keys():
    for j in valves.keys():
        if i == j:
            dist[(i,j)] = 0
        else:
            q = [i]
            while q:
                n = q[0]
                del q[0]
                


def explore(prev, q):
    global valves
    if prev.timeleft <= 1 or len(prev.valves_open) == len(valves):
        return
    if valves[prev.valve][0] and not prev.valve in prev.valves_open:
        q.append(Move(prev, OPEN, prev.valve, prev.timeleft - 1))
    for t in valves[prev.valve][1]:
        q.append(Move(prev, MOVE, t, prev.timeleft - 1))


def part1():
    q = [Move(None, None, "AA", 30)]
    curtime = 30
    while q:
        m = q[0]
        del q[0]
        if m.timeleft < curtime:
            curtime = m.timeleft
            print("minute", curtime)
        if m.timeleft == 15:
            break
        explore(m, q)

    q.sort(key=lambda m: m.score, reverse=True)

    for s in q[:10]:
        path = [s]
        cur = s.prev
        while cur:
            path.insert(0, cur)
            cur = cur.prev
        print(path, "score:", s.score)


def part2():
    pass


part1() if PART == 1 else part2()
