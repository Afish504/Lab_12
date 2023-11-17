class Television:
    # Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        # Instance variables (private)
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL

    def power(self):
        # Method to turn the TV on and off by changing the value of the status variable
        self._status = not self._status

    def mute(self):
        # Method to mute and unmute the TV when it's on by changing the value of the muted variable
        if self._status:
            self._muted = not self._muted
            if self._muted:
                self._volume = self.MIN_VOLUME

    def channel_up(self):
        # Method to increase the TV channel value when the TV is on
        if self._status:
            if self._channel == self.MAX_CHANNEL:
                self._channel = self.MIN_CHANNEL
            else:
                self._channel += 1

    def channel_down(self):
        # Method to decrease the TV channel value when the TV is on
        if self._status:
            if self._channel == self.MIN_CHANNEL:
                self._channel = self.MAX_CHANNEL
            else:
                self._channel -= 1

    def volume_up(self):
        # Method to increase the TV volume when the TV is on
        if self._status and not self._muted:
            if self._volume < self.MAX_VOLUME:
                self._volume += 1

    def volume_down(self):
        # Method to decrease the TV volume when the TV is on
        if self._status and not self._muted:
            if self._volume > self.MIN_VOLUME:
                self._volume -= 1

    def __str__(self):
        # Method to represent the TV object's values as a formatted string
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"

if __name__ == "__main__":
    main()
