import re

# https://adventofcode.com/2022/day/16

SAMPLE = 1
PART = 1


def parse(line):
    v, fr, tunnels = re.findall(r"Valve (\w\w) has flow rate=(\d+); tunnels? leads? to valves? ([\w, ]*)", line)[0]
    return (v, fr, tunnels.split(", "))


with open("input-sample.txt" if SAMPLE else "input.txt", "r") as f:
    valves = {v: (fr, tunnels) for v, fr, tunnels in [parse(l) for l in f.readlines()]}


def proc(v, mins, dtree):
    # Possible actions are open valve v (if not already open), or do any of the tunnels
    # 1) go back along the tree to see if v was opened yet
    # If not,
    if not v in opened:
        paths = paths.copy()
        opened.append(v)
        proc(v, mins - 1, opened, paths)
    for t in v[1]:
        proc(t, mins - 1, opened, paths)


def part1():
    # print(valves)
    vcur = "AA"
    mins = 30
    # For each iteration, build a decision tree of the possible paths that can be taken, up to the
    # number of minutes we have left, weighted by the amount of pressure it would release
    dtree = []
    proc(vcur, mins, [], dtree)
    pass


def part2():
    pass


part1() if PART == 1 else part2()
