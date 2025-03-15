"""The idea is that we have a part of the system that is in charge of identifying
events as they occur in another system, which is being monitored. At each point,
we want this component to identify the type of event, correctly, according to the
values of the data that was previously gathered"""

class Event:
    def __init__(self, raw_data) -> None:
        self.raw_data=raw_data
    

class UnkownEvent(Event):
    """A type of event that cannot be identified from its data"""

class LoginEvent(Event):
    """A event representing a user that has just entered the system"""

class LogoutEvent(Event):
    """An event representing a user that has just left the system."""

class SystemMonitor:
    """Identify events that occurred in the system."""
    
    def __init__(self, event_data) -> None:
        self.event_data=event_data
    
    def identify_event(self):
        if (self.event_data["before"]["session"]==0
            and self.event_data["after"]["session"]):
            return LoginEvent(self.event_data)
        elif (
            self.event_data["before"]["session"]==1
            and self.event_data['after']['session']==0):
            return LogoutEvent(self.event_data)
        return UnkownEvent(self.event_data)

#Above code does not follow OCP because we are delaing with subclass
# and if we add new new event we have to change system monitor class

##below code follow OCP principle

class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data
    @staticmethod
    def meets_condition(event_data: dict):
        return False
    
class UnknownEvent(Event):
 """A type of event that cannot be identified from its data"""
class LoginEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict):
        return (
 event_data["before"]["session"] == 0
 and event_data["after"]["session"] == 1
 )
class LogoutEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict):
        return (
 event_data["before"]["session"] == 1
 and event_data["after"]["session"] == 0
 )
    
    
class SystemMonitor:
# Identify events that occurred in the system
    
    def __init__(self, event_data) -> None:
        self.event_data=event_data
    
    def identify_event(self):
        for event_cls in Event.__subclasses__():
            try:
                if event_cls.meets_condition(self.event_data):
                    return event_cls(self.event_data)
            except KeyError:
                continue
        return UnknownEvent(self.event_data)