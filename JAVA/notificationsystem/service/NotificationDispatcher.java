package notificationsystem.service;

import java.util.Set;
import notificationsystem.model.UserPreference;
import notificationsystem.channel.NotificationChannel;
import notificationsystem.factory.NotificationChannelFactory;
import notificationsystem.model.ChannelType;
import notificationsystem.model.Notification;

public class NotificationDispatcher {
    private final UserPreferenceService preferenceService;

    public NotificationDispatcher(UserPreferenceService preferenceService) {
        this.preferenceService = preferenceService;
    }

    public void dispatch(Notification notification) {
        UserPreference preference =
                preferenceService.getPreference(notification.getUserId());

        Set<ChannelType> channels = preference.getPreferredChannels();

        for (ChannelType channelType : channels) {
            NotificationChannel channel =
                    NotificationChannelFactory.getChannel(channelType);

            channel.send(notification);
        }
    }
}
