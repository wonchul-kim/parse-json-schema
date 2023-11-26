import sys 
import os.path as osp
from pathlib import Path 
FILE = Path(__file__).resolve().parent.parent
sys.path.append(osp.join(FILE))

from configs.configs import Configs


print(Configs.model_json_schema())