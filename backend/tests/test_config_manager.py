import sys 
import os.path as osp
from pathlib import Path 
FILE = Path(__file__).resolve().parent.parent
sys.path.append(osp.join(FILE))

from configs.config_manager import ConfigManager


print(ConfigManager.get_json_schema())
print(ConfigManager.get_json_schema()['TrainConfig'])
'''
{"properties": {"device": {"enum": ["gpu", "cpu"], "title": "Device", "type": "string"}, "device_ids": {"items": {"type": "integer"}, "title": "Device Ids", "type": "array"}, "learning_rate": {"title": "Learning Rate", "type": "number"}}, "required": ["device", "device_ids", "learning_rate"], "title": "TrainConfig", "type": "object"}
'''