import sys

def solve():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        L, N = map(int, line.split())
        intervals = []

        for _ in range(N):
            x, r = map(int, sys.stdin.readline().split())
            left = x - r
            right = x + r
            intervals.append((left, right))

        # Sort by left endpoint, and by right descending if tie
        intervals.sort(key=lambda x: (x[0], -x[1]))

        current = 0
        i = 0
        used = 0

        while current < L:
            best = current

            # Find the interval starting before or at 'current'
            # that extends coverage the farthest
            while i < N and intervals[i][0] <= current:
                best = max(best, intervals[i][1])
                i += 1

            # No progress → impossible
            if best == current:
                print(-1)
                break

            current = best
            used += 1
        else:
            # Successfully covered [0, L]
            print(N - used)


if __name__ == "__main__":
    solve()
