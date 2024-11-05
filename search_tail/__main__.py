"""
Main module of Search Tail
This is a tail-like CLI tool with support for search and keyword highlighting
"""

import argparse


def main():
    """
    Main function
    """
    parser = argparse.ArgumentParser(
        description="A tail-like CLI tool with support for search and keyword highlighting",
    )
    parser.add_argument("file", type=str, help="The log file to tail")
    parser.add_argument("-f", "--follow", action="store_true", help="The search query")
    parser.add_argument(
        "-n", type=int, default=30, help="The number of lines to display"
    )
    parser.add_argument("-s", type=str, help="Search and highlight a keyword")
    args = parser.parse_args()


if __name__ == "__main__":
    main()
