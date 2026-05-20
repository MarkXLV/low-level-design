from concurrent.futures import ThreadPoolExecutor

from notificationsystem.factory import NotificationChannelFactory
from notificationsystem.model import ChannelType, Notification, UserPreference


class UserPreferenceService:
    def __init__(self) -> None:
        self.preferences: dict[str, UserPreference] = {}

    def save_preference(self, preference: UserPreference) -> None:
        self.preferences[preference.user_id] = preference

    def get_preference(self, user_id: str) -> UserPreference:
        return self.preferences.get(
            user_id,
            UserPreference(user_id, {ChannelType.EMAIL}),
        )


class NotificationDispatcher:
    def __init__(self, preference_service: UserPreferenceService) -> None:
        self.preference_service = preference_service

    def dispatch(self, notification: Notification) -> None:
        preference = self.preference_service.get_preference(notification.user_id)
        for channel_type in preference.preferred_channels:
            channel = NotificationChannelFactory.get_channel(channel_type)
            channel.send(notification)


class NotificationService:
    def __init__(self, dispatcher: NotificationDispatcher) -> None:
        self.dispatcher = dispatcher

    def send_notification(self, notification: Notification) -> None:
        self.dispatcher.dispatch(notification)


class AsyncNotificationService:
    def __init__(self, dispatcher: NotificationDispatcher) -> None:
        self.dispatcher = dispatcher
        self.executor = ThreadPoolExecutor(max_workers=10)

    def send_notification(self, notification: Notification) -> None:
        self.executor.submit(self.dispatcher.dispatch, notification)

    def shutdown(self) -> None:
        self.executor.shutdown(wait=True)

