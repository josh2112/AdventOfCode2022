import numpy


FORREAL = 0
PART = 2


def find(ltr):
    p = numpy.where(rows == ltr)
    return p[0][0], p[1][0]


with open("input.txt" if FORREAL else "input-sample.txt", "r") as f:
    rows = numpy.array([list(l.strip()) for l in f.readlines()])


start, end = find("S"), find("E")
rows[start] = "a"
rows[end] = "z"


def part1():
    solution = None

    def climb(p, path=[]):
        global solution
        path.append(p)
        if solution and len(path) >= len(solution):
            return
        if p == end:
            solution = path
            return
        for v in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            p1 = (p[0] + v[0], p[1] + v[1])
            if (
                p1[0] in range(len(rows))
                and p1[1] in range(len(rows[0]))
                and p1 not in path
                and ord(rows[p1]) - ord(rows[p]) < 2
            ):
                climb(p1, [x for x in path])

    climb(start)
    print(len(solution) - 1, solution)


def part2():
    def climb(p, dist, tovisit):
        adjacent = ((p[0] + d[0], p[1] + d[1]) for d in ((-1, 0), (1, 0), (0, -1), (0, 1)))
        adjacent = [v for v in adjacent if v[0] in range(len(rows)) and v[1] in range(len(rows[0]))]
        for p1 in adjacent:
            if ord(rows[p1]) - ord(rows[p]) < 2 and ((not dist[p1]) or dist[p] + 1 < dist[p1]):
                dist[p1] = dist[p] + 1
        for p1 in adjacent:
            if dist[p1]:
                tovisit.append(p1)

    dist = numpy.full(rows.shape, None)
    dist[start] = 0
    tovisit = [start]

    while len(tovisit) > 0:
        p = tovisit[0]
        del tovisit[0]
        climb(p, dist, tovisit)

    print(dist[end])


part1() if PART == 1 else part2()
