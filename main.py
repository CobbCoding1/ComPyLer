import sys


def main():
    if(len(sys.argv) < 2):
        print("Please provide a file to read")
        return
    file = open(sys.argv[1], "r")

if __name__ == "__main__":
    main()