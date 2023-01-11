from enum import Enum
import SensorEntity

class SensorType(Enum):
    TemperatureSensor = 0
    HumiditySensor = 1
    
    


class Sensor:
    
    def __init__(self, type : SensorType , entity : SensorEntity) -> None:
        self.type = type
        self.entity = entity
        
        
    def collect(self) -> dict:
        return self.entity.collect()
        