#######ISP##############

# if we want to parse the event from several data source in diffrent format say xml and json
# to create this as an interface in python we would use an abstract base class and define method
# as abstract to force derived classes  to implement  them

class EventParser(ABC):
    @abstractmethod
    def from_json(self):
        pass
    @abstractmethod
    def from_xml(self):
        pass
# after following ISP 
class JsonEventParser(EventParser):
    def from_json(self):
        # code here
        pass
    def from_xml(self):
        #code her
        pass

class XMLEventParser(EventParser):
    def from_xml(self):
        #code here
        pass
    def from_json(self):
        #code here
        pass