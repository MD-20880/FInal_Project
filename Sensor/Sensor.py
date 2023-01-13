from enum import Enum
import Sensor.SensorEntity as SensorEntity


class NodeType(Enum):
    pass

    


class Sensor:
    
    def __init__(self, params : list, entity : SensorEntity) -> None:
        self.params = params
        self.entity = entity
         
        
    def collect(self) -> dict:
        return self.entity.collect()
    
    
    #OPERATIONS
    
    def halt(self):
        pass
    