import os
from .config import config
import json

class Stat:
    
    def __init__(self, path, json_stat):
        self.path = path
        self.json_stat = json_stat
        
    def __getattr__(self, name):
        if name in self.json_stat:
            return self.json_stat[name]
        return None
    
    def __setattr__(self, __name: str, __value):
        if __name not in ['path', 'json_stat']:
            self.json_stat[__name] = __value
        else:
            super().__setattr__(__name, __value)
        
    def save(self):
        with open(config.stat_path, 'w') as stat_file:
            stat_file.write(json.dumps(self.json_stat))
    
def get_stat(path) -> Stat:
    if not os.path.exists(config.stat_path):
        default_stat = {
            "path": path,
            "stage1_time": -1,
            "stage2_time": -1,
            "stage3_time": -1,
            "stage4_time": -1,
            "stage5_time": -1,
            "finished": False,
        }
        with open(config.stat_path, 'w') as stat_file:
            stat_file.write(json.dumps(default_stat))
    with open(config.stat_path, 'r') as stat_file:
        json_stat = json.loads(stat_file.read())
    return Stat(path, json_stat)