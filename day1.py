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
    dial = 50

    with open(sys.argv[1], "r") as input:
        for line in input:
            amount = int(line[1:])
            prev_dial = dial

            if line[0] == 'R':
                dial += amount
            else:
                dial -= amount

            while dial < 0:
                dial += 100
                p2_ans += 1
                if prev_dial == 0:
                    prev_dial = 1
                    p2_ans -= 1

            while dial > 100:
                dial -= 100
                p2_ans += 1

            if dial == 100:
                dial -= 100

            if dial == 0:
                p1_ans += 1
                p2_ans += 1

    print(f"Part 1: {p1_ans}\nPart 2: {p2_ans}")
    sys.exit(0)

if __name__ == "__main__":
    main()
