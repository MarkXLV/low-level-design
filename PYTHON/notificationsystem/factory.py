from notificationsystem.channel import (
    EmailNotificationChannel,
    NotificationChannel,
    PushNotificationChannel,
    SmsNotificationChannel,
)
from notificationsystem.model import ChannelType


class NotificationChannelFactory:
    @staticmethod
    def get_channel(channel_type: ChannelType) -> NotificationChannel:
        if channel_type == ChannelType.EMAIL:
            return EmailNotificationChannel()
        if channel_type == ChannelType.SMS:
            return SmsNotificationChannel()
        if channel_type == ChannelType.PUSH:
            return PushNotificationChannel()
        raise ValueError(f"Unsupported channel type: {channel_type}")

