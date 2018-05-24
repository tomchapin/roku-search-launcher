#!/usr/bin/env python
from time import sleep
import sys
from roku_controller import RokuController


def main():
    """
    Accepts a search value, specified as a command line argument.

    Example Usage:
    ./search_and_launch.py "The Secret Life of Pets"

    """
    roku = RokuController()

    # Search for the title
    roku.search(keyword=sys.argv[1])
    sleep(3)

    # Click the right button repeatedly (to select the first search result)
    for i in range(9):
        roku.key_press('Right')
        sleep(0.2)

    # Launch the item and hit play after a short delay
    roku.key_press('Select')
    sleep(5)
    roku.key_press('Play')

    print('Done!')


if __name__ == "__main__":
    main()
