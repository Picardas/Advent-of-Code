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
	ranges = []

	with open(sys.argv[1], "r") as input:
		line = input.read()
		tmp_spans = line.strip().split(",")

		for span in tmp_spans:
			span_string = span.split("-")
			ranges.append([int(val) for val in span_string])

	for span_start, span_end in ranges:
		for sequence in range(span_start, span_end + 1):
			seq_string = str(sequence)
			digits = len(seq_string)
			mid = digits // 2
			for i in range(1, mid + 1):
				if digits % i != 0:
					continue
				repeats = digits // i
				if seq_string[:i] * repeats == seq_string:
					p2_ans += sequence
					if repeats == 2:
						p1_ans += sequence
					break

	print(f"Part 1: {p1_ans}\nPart 2: {p2_ans}")
	sys.exit(0)


if __name__ == "__main__":
	main()
