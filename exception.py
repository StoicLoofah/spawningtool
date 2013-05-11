"""
exception
~~~~~~~~~
"""


class CutoffTimeError(Exception):
    def __init__(self):
        super(CutoffTimeError, self).__init__(
            "You must enter a valid cutoff time! eg: 10:05"
        )


class ReplayFormatError(Exception):
    def __init__(self, message):
        super(ReplayFormatError, self).__init__(message)
