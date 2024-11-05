"""
Main module of Search Tail
This is a tail-like CLI tool with support for search and keyword highlighting
"""

import argparse

from stail import run

DEFAULT_LINES_TO_DISPLAY = 50


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
        default=DEFAULT_LINES_TO_DISPLAY,
        help=(
            "The number of lines to display.\n"
            "If '-f' is not specified, the file will not be followed\n"
            "There is no need to explicitly specify '-n' unless to change the default(50 lines).\n"
            "The following options are available when not in follow mode:\n"
            "    Use 's' to perform another search.\n"
            "    Use 'n' to navigate to next match and 'p' to navigate to previous match.\n"
            "    Use 'q' to quit the program."
        ),
    )
    parser.add_argument("-s", type=str, help="Search and highlight a keyword")
    args = parser.parse_args()

    if args.n is None:
        args.n = DEFAULT_LINES_TO_DISPLAY  # Set default value of -n
    elif args.n is not None and args.n <= 0:
        args.n = (
            DEFAULT_LINES_TO_DISPLAY  # Invalid value for -n. Use default value of -n
        )

    run(args)


if __name__ == "__main__":
    main()
