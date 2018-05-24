#!/usr/bin/env python
import sys

from roku_controller import RokuController


def main():
    """
    Accepts keypress values, specified as a command line argument

    Example Usage:
    ./keypress.py Play


    The following are the key names that are recognized by ECP:

      Home
      Rev
      Fwd
      Play
      Select
      Left
      Right
      Down
      Up
      Back
      InstantReplay
      Info
      Backspace
      Search
      Enter

    Roku devices that support the "Find Remote" support:

      FindRemote

    Note that query/device-info includes a supports-find-remote flag that indicates whether the Roku device supports FindRemote.
    However this does not specifically indicate that the device has a paired remote that supports "Find remote" as well.

    Some Roku devices, such as Roku TVs, also support:

      VolumeDown
      VolumeMute
      VolumeUp
      PowerOff

    Roku TV devices also support changing the channel when watching the TV tuner input:

      ChannelUp
      ChannelDown

    Roku TV devices also support keys to set the current TV input UI:

      InputTuner
      InputHDMI1
      InputHDMI2
      InputHDMI3
      InputHDMI4
      InputAV1

    """
    roku = RokuController()
    roku.key_press(sys.argv[1])

    print('Done!')


if __name__ == "__main__":
    main()
