"""
Implementation of Search-Tail
"""


def tail(file, lines):
    """
    Tails last lines of a file
    """
    with open(file, "r", encoding="utf-8") as file_handle:
        return file_handle.readlines()[-lines:]


def print_lines(lines):
    """
    Prints lines
    """
    for line in lines:
        print(line, end="")


def run(args):
    """
    Main function
    """
    lines = tail(args.file, args.n)
    print_lines(lines)
