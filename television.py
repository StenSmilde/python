class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, status=False, muted=False, volume=MIN_VOLUME, channel=MIN_CHANNEL, previous_volume=None) -> None:
        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel
        self.__previous_volume = previous_volume  # Initialize __previous_volume

    def power(self) -> None:
        """
        method to turn on or off tv
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        method to mute or unmute tv
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                if self.__previous_volume is not None:
                    self.__volume = self.__previous_volume  # Restore previous volume
                    self.__previous_volume = None
            else:
                self.__previous_volume = self.__volume  # Store current volume before muting
                self.__muted = True
                self.__volume = Television.MIN_VOLUME

    def channel_up(self) -> None:
        """
        method to increase the channel
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        method to decrease the channel
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        method to increase the volume
        """
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume == Television.MAX_VOLUME:
                pass
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        method to decrease the volume
        """
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume == Television.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        method to show the tv status
        :return: tv status
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
