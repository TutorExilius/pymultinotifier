"""All type definitions"""

import enum


class PlatformType(str, enum.Enum):
    """The supported platform types"""

    DISCORD = "discord"
    TELEGRAM = "telegram"
    TWITTER = "twitter"
