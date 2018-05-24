# roku-search-launcher

Roku has an amazingly powerful API for all of their devices. Unfortunately,
they don't seem to have a built-in method in their External Control API for
launching content that is hosted within apps (such as Netflix/Hulu).

They do, however, have a very nifty search function, and they also
allow you to control the remote's buttons via keypresses.

Realizing this, I whipped together this quick tool that will allow you to
automate searches and then script the keypresses required to launch
the content and play it.

Ultimately, my goal for this tool was to be able to use my Amazon Alexa to use
voice commands that launch Netflix and play specific tv shows and movies on my Roku.
I'm happy to report that I'm successfully doing that now!

Feel free to borrow this and use it however you like!

## Requirements

- Python 3+


## Installation

Copy the config.example.yaml file to a file called config.yaml and edit it
so that it points at your Roku device on your network


## Example Usage

Note: These scripts are just examples, and you may need to edit the python
files to adjust delay/sleep timings at different points and what not.

You can also use them as reference for writing your own, more advanced scripts! 

#### Search for a title and launch it:

    ./search_and_launch.py "StoryBots Super Songs"
    
#### Search and launch, then press play (after a short delay):

    ./search_and_launch_and_play.py "StoryBots Super Songs"
    
#### Press a button on the remote:

    ./key_press.py Play