import os

class Config:
    
    def __init__(self):
        self.working_dir = os.getcwd()
        home_path = self.working_dir + "/CryptoREX_rebuilt"
        self.output_path = home_path + "/rex/output"
        self.ida_path = "./IDA_Pro_v6.4"
        self.script_path = home_path + "/idascript/bin2iridc.idc"
        self.misuseprofile_path = home_path + "/rex/misuseprofile"
        self.execfunction_path = home_path + "/rex/execfunction"
        self.debug_path = self.working_dir + "/tmp/debug.log"
        self.report_path = self.working_dir + "/tmp/report.log"
        self.stat_path = self.working_dir + "/tmp/stat.json"

config = Config()