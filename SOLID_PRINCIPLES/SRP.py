# In this example, we are going to create the case for an application that is in charge of
# reading information about events from a source (this could be log files, a database, or many
# more sources), and identifying the actions corresponding to each particular log.

class SystemMonitor:
    def load_activity(self):
        """get events from source to process"""
        
    def identify_events(self):
        """Parse the source raw data into events(domain objects)"""
    
    def stream_events(self):
        """send the parsed events to external agent"""


## after applying SRP 

class ActivityReader:
    def load(self):
        """get events from source"""
        
class SystemMonitor:
    def identify_events(self):
        """Parse the source raw data into events(domain objects)"""

class Output:
    def stream_events(self):
        """send the parsed events to external agent"""