from abc import ABC, abstractmethod

from notificationsystem.model import Notification


class NotificationChannel(ABC):
    @abstractmethod
    def send(self, notification: Notification) -> None:
        pass


class EmailNotificationChannel(NotificationChannel):
    def send(self, notification: Notification) -> None:
        print(f"Sending EMAIL to user {notification.user_id}: {notification.message}")


class SmsNotificationChannel(NotificationChannel):
    def send(self, notification: Notification) -> None:
        print(f"Sending SMS to user {notification.user_id}: {notification.message}")


class PushNotificationChannel(NotificationChannel):
    def send(self, notification: Notification) -> None:
        print(f"Sending PUSH to user {notification.user_id}: {notification.message}")

