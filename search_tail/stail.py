"""
Implementation of Search-Tail
"""

import os
import re
import sys
import termios
import tty

from config import Config


def tail(file, lines):
    """
    Tails last lines of a file
    """
    with open(file, "r", encoding="utf-8") as file_handle:
        return file_handle.readlines()[-lines:]


def print_lines(lines, current_position=None, keyword=None):
    """
    Prints lines
    """
    os.system("clear")
    terminal_size = os.get_terminal_size()
    term_height = terminal_size.lines
    start = (
        max(0, current_position - (term_height // 2) + 2)
        if current_position is not None
        else 0
    )
    end = min(
        len(lines), start + term_height - 2
    )  # -2 to account for the status and user input
    for i in range(start, end):
        bold = i == current_position
        highlight_and_print(lines[i], keyword, bold)
    if current_position is not None:
        print(f"Keyword '{keyword}' found at line {current_position + 1}")


def highlight_and_print(line, keyword=None, bold=False):
    """Highlight and print a line"""
    highlighted_line = line
    for k, color in Config.keywords.items():
        highlighted_line = re.sub(
            f"({k})",
            f"{color}\\1{Config.RESET_COLOR}",
            highlighted_line,
            flags=re.IGNORECASE,
        )
    if keyword:
        highlighted_line = re.sub(
            f"({keyword})",
            f"{Config.HIGHLIGHT_COLOR}\\1{Config.RESET_COLOR}",
            highlighted_line,
            flags=re.IGNORECASE,
        )
    if bold:
        highlighted_line = (
            f"{Config.BOLD_FORMAT}{Config.BACKGROUND_COLOR}"
            f"{highlighted_line}"
            f"{Config.RESET_COLOR}"
        )
    print(highlighted_line, end="")


def search(lines, keyword, direction="next", current_position=None):
    """Search for a keyword and highlight keyword in a list of lines"""
    if keyword is None:
        return None, None
    if direction == "next":
        start = current_position + 1 if current_position is not None else 0
        for i in range(start, len(lines)):
            if re.search(keyword, lines[i], re.IGNORECASE):
                return i, lines[i]
    elif direction == "prev":
        start = current_position - 1 if current_position is not None else len(lines) - 1
        for i in range(start, -1, -1):
            if re.search(keyword, lines[i], re.IGNORECASE):
                return i, lines[i]
    return None, None


def get_key():
    """Read a single key from stdin"""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key


def run(args):
    """
    Main function
    """
    lines = tail(args.file, args.n)

    current_position = None

    current_position, _ = search(
        lines, args.s, direction="next", current_position=current_position
    )
    print_lines(lines, current_position, args.s)

    while True:
        key = get_key()
        if key == "q":
            break
        if key == "r":
            lines = tail(args.file, args.n)
            current_position, _ = search(
                lines, args.s, direction="next", current_position=current_position
            )
        if key == "p" and args.s:
            current_position, _ = search(
                lines, args.s, direction="prev", current_position=current_position
            )
        if key == "n" and args.s:
            current_position, _ = search(
                lines, args.s, direction="next", current_position=current_position
            )
        if key == "s":
            new_keyword = input("Enter search keyword: ")
            args.s = new_keyword
            current_position, _ = search(
                lines, args.s, direction="next", current_position=current_position
            )

        print_lines(lines, current_position, args.s)
