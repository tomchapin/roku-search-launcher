#!/usr/bin/env python
from time import sleep
import sys
from roku_controller import RokuController


def main():
    """
    Accepts a search value, specified as a command line argument

    Example Usage:
    ./search_and_launch.py "StoryBots Super Songs"

    """
    roku = RokuController()

    # Grab the search keyword from the first parameter on the command line
    search_keyword = sys.argv[1]

    # Search for the title
    roku.search(keyword=search_keyword)

    sleep(3)

    # Click the right button repeatedly (to select the first search result)
    for i in range(9):
        roku.key_press('Right')
        sleep(0.2)

    # Launch the item
    roku.key_press('Select')

    print('Done!')


if __name__ == "__main__":
    main()
