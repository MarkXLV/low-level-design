from dataclasses import dataclass
from enum import Enum


class ChannelType(Enum):
    EMAIL = "EMAIL"
    SMS = "SMS"
    PUSH = "PUSH"


@dataclass(frozen=True)
class Notification:
    user_id: str
    message: str


@dataclass(frozen=True)
class UserPreference:
    user_id: str
    preferred_channels: set[ChannelType]

