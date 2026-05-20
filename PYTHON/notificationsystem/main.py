from notificationsystem.model import ChannelType, Notification, UserPreference
from notificationsystem.service import (
    AsyncNotificationService,
    NotificationDispatcher,
    NotificationService,
    UserPreferenceService,
)


def main() -> None:
    preference_service = UserPreferenceService()
    preference_service.save_preference(
        UserPreference("user123", {ChannelType.EMAIL, ChannelType.SMS})
    )

    dispatcher = NotificationDispatcher(preference_service)
    async_service = AsyncNotificationService(dispatcher)
    sync_service = NotificationService(dispatcher)

    notification = Notification("user123", "Your order has been shipped!")

    sync_service.send_notification(notification)
    async_service.send_notification(notification)
    async_service.shutdown()


if __name__ == "__main__":
    main()

