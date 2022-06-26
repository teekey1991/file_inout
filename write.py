import os
import sys

def main():
    output_dir = os.path.abspath(sys.argv[0])
    output_file = output_dir + "users.csv"
    with open(file=output_file, mode="w", encoding="utf-8") as f:
        f.write("Bob,79\n")
        f.write("Tom,59")


if __name__ == "__main__":
    main()