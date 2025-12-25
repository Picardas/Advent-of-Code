import os
import sys


def main():
    if len(sys.argv) != 2:
        print("Require single filename as argument")
        sys.exit(2)
    if not os.path.exists(sys.argv[1]):
        print("File does not exist")
        sys.exit(2)

    p1_ans = 0
    p2_ans = 0

    with open(sys.argv[1], "r") as input:
        for line in input:
            max = 0
            line = line.strip()
            i = 0
            while i < len(line) - 1:
                for j in line[i + 1 :]:
                    jolts = int(line[i] + j)
                    if jolts > max:
                        max = jolts
                i += 1
            p1_ans += max

    print(f"Part 1: {p1_ans}\nPart 2: {p2_ans}")
    sys.exit(0)


if __name__ == "__main__":
    main()
