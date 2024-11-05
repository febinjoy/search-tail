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
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "file",
        type=str,
        help="The log file to tail",
    )
    parser.add_argument(
        "-f",
        "--follow",
        action="store_true",
        help=(
            "Enables the follow mode.\n"
            "Users will not be able to search when in follow mode.\n"
            "Keyword highlighting will work."
        ),
    )
    parser.add_argument(
        "-n",
        type=int,
        default=30,
        help=(
            "The number of lines to display. Will not follow the file.\n"
            "While in this mode, use 's' to perform another search.\n"
            "Use 'n' to navigate to next match and 'p' to navigate to previous match.\n"
            "Use 'q' to quit the program."
        ),
    )
    parser.add_argument("-s", type=str, help="Search and highlight a keyword")
    args = parser.parse_args()


if __name__ == "__main__":
    main()
