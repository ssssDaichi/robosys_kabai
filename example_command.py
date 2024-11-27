# example_command.py
import sys

def main():
    for line in sys.stdin:
        print(f"入力された内容: {line.strip()}")

if __name__ == "__main__":
    main()
