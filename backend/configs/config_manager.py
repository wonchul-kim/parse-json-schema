from configs.configs import TrainConfig, AugmentationConfig, NetworkConfig

class ConfigManager:
    _json_schema = {}


    @classmethod
    def json_schema(cls):
        return cls._json_schema 
    
    @classmethod 
    def update_json_schema(cls, key, value):
        cls._json_schema[key] = value 

    @classmethod
    def get_json_schema(cls):
        for obj in [
                TrainConfig, AugmentationConfig, NetworkConfig]:
            cls.update_json_schema(obj.__name__, obj.model_json_schema())

        return cls._json_schema
    
    def __init__(self):
        self.train = None
        self.augmentations = None 
        self.network = None 


    @property 
    def json_schema(self):
        return self._json_schema 
    
