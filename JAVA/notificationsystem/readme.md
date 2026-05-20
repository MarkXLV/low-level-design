notification
 string userID
 string message

notificationService
    dispatcherService
    void dispatch()

dispatchService
    perferenceService
    void dispatch()

preferenceService
    map<string,userPreference>
    setPreference()
    getPreference()

userPreference
    string user
    set<PREFERENCE>preference

ENUM preference{
    EMAIL,
    SMS
}


------
create model -> create channel interface and implementation -> crerate factory 

