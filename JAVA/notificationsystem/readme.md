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
create model -> crrate channel 9interface and inplementation -> crerate factory 

