from collections import defaultdict
from enum import Enum
from fileinput import filename
import json
import pathlib
import os
import fcntl

from .config import config

class Rule(Enum):
    
    UNKNOWN = 0, "Unknown Rule"
    CONSTANT_SALT = 1, "Rule-1. Do not use constant salts for password-based encryption (PBE)"
    CONSTANT_KEY = 2, "Rule-2. Do not use constant encryption keys"
    CONSTANT_IV = 3, "Rule-3. Do not use a non-random initialization vector (IV) for ciphertext block chaining (CBC) encryption"
    ECB_MODE = 4, "Rule-4. Do not use electronic code book (ECB) mode for encryption"
    STATIC_SEED = 5, "Rule-5. Do not use static seeds for random number generation (RNG) functions"
    ITERATION = 6, "Rule-6. Do not use fewer than 1000 iterations for PBE"
    
    def __init__(self, code, desc) -> None:
        self.code = code
        self.desc = desc
        
    def __hash__(self) -> int:
        return self.code
    
    def from_code(code):
        if code == 1:
            return Rule.CONSTANT_SALT
        elif code == 2:
            return Rule.CONSTANT_KEY
        elif code == 3:
            return Rule.CONSTANT_IV
        elif code == 4:
            return Rule.ECB_MODE
        elif code == 5:
            return Rule.STATIC_SEED
        elif code == 6:
            return Rule.ITERATION
        else:
            return Rule.UNKNOWN
        
        
        
class ViolationDetail:
    
    def __init__(self, filename="", function_name="", call_stack=list(), path=list(), data="", rule=0, count=1) -> None:
        self.filename = filename
        self.function_name = function_name
        self.call_stack = call_stack
        self.path = path
        self.data = data
        self.rule = rule
        self.count = count
        
    def from_json(json_obj):
        return ViolationDetail(
            json_obj['filename'],
            json_obj['function_name'],
            json_obj['call_stack'],
            json_obj['path'],
            json_obj['data'],
            json_obj['rule'],
            json_obj['count']
        )
    
    def __str__(self) -> str:
        result = f'--------------------------------------\n'\
                    f'File: {self.filename}\n'\
                    f'Rule: {Rule.from_code(self.rule).desc}\n'\
                    f'Function name: {self.function_name}\n'\
                    f'Data: {self.data}\n'\
                    f'Path: {list(map(hex, self.path))}\n'\
                    f'Count: {self.count}\n'\
                    f'Call stack:\n'
        for call in self.call_stack:
            result += f'-> {call}\n'
        result += f'--------------------------------------\n'
        return result
    
    def __repr__(self) -> str:
        self.__str__()
        
    def __hash__(self) -> int:
        return self.rule + self.path[0] + hash(os.path.basename(self.filename)) + hash(self.function_name) + hash(self.data)
    
    def __eq__(self, other):
        if isinstance(other, ViolationDetail):
            return self.rule == other.rule and self.path[0] == other.path[0] \
                and os.path.basename(self.filename) == os.path.basename(other.filename) \
                and self.function_name == other.function_name and self.data == other.data
        return False
    
    def __lt__(self, other):
        if isinstance(other, ViolationDetail):
            if self.rule == other.rule:
                return os.path.basename(self.filename) < os.path.basename(other.filename)
            return self.rule < other.rule
        return False

class Report:
    
    def __init__(self):
        self.stage1_time = 0
        self.stage2_time = 0
        self.stage3_time = 0
        self.stage4_time = 0
        self.stage5_time = 0
        self.total_time = 0
        self.report_path = None
        self.extracted_binaries = set()
        self.cryptolib_imported = defaultdict(set)
        self.vulnerabilities = list()
        
    def __str__(self) -> str:
        result = f"[*] Time cost: {self.total_time}\n"\
                    f"[-] Decompressing firmware: {self.stage1_time}\n"\
                    f"[-] Extracting firmware: {self.stage2_time}\n"\
                    f"[-] Running idc script: {self.stage3_time}\n"\
                    f"[-] CFG construction: {self.stage4_time}\n"\
                    f"[-] Taint analysis: {self.stage5_time}\n\n"\
                    f"[-] Extracted binaries:\n"
        for arch, filename in self.extracted_binaries:
            result += f'[-] {filename} ({arch})\n'
        result += f"\n[*] Crypto libraries imported:\n"
        for cryptolib in self.cryptolib_imported:
            result += f'[-] {cryptolib}: {self.cryptolib_imported[cryptolib]}\n'
        result += f'\n[*] Vulnerabilities:\n'
        result += f'[-] Vulnerablity number: ({len(self.vulnerabilities)})\n'
        for vul in self.vulnerabilities:
            result += f'{str(vul)}'
        return result
    
    def __repr__(self) -> str:
        return self.__str__()
        
    def save(self):
        self.vulnerabilities.sort()
        with open(self.report_path, 'a') as report:
            report.write(self.__str__())
        for vul in self.vulnerabilities:
            stat_path = os.path.join(os.path.dirname(self.report_path), f'rule-{vul.rule }.log')
            with open(stat_path, 'a') as stat:
                fcntl.flock(stat, fcntl.LOCK_EX)
                stat.write(str(vul))
                fcntl.flock(stat, fcntl.LOCK_UN)
                
class GlobalReport:
    
    def __init__(self):
        self.report_path = ""
        self.tmp_path = ""
        self.vul_counter = defaultdict(int)
        
    def save(self, report: Report):
        with open(self.tmp_path, 'r') as fd:
            json_report = json.loads(fd.read())
        vul_nums = json_report['vul_nums']
        vuls = dict()
        for vul in json_report['vuls']:
            vul_obj = ViolationDetail.from_json(vul)
            vuls[vul_obj] = vul_obj
        for vul in report.vulnerabilities:
            vul_nums[vul.rule - 1] += 1
            if vul in vuls:
                vuls[vul].count += 1
            else:
                vuls[vul] = vul
        with open(self.tmp_path, 'w') as fd:
            fcntl.flock(fd, fcntl.LOCK_EX)
            fd.write(json.dumps({
                'vul_nums': vul_nums,
                'vuls': [vul.__dict__ for vul in vuls]
            }))
            fcntl.flock(fd, fcntl.LOCK_UN)
        with open(self.report_path, 'w') as fd:
            result = ''
            for i in range(6):
                result += f'Violation number of rule-{i + 1}: {vul_nums[i]} ({sum(vul.rule == i + 1 for vul in vuls)} unique)\n'
            result += '\n'
            vuls = list(vuls.keys())
            vuls.sort()
            for vul in vuls:
                result += str(vul)
            fcntl.flock(fd, fcntl.LOCK_EX)
            fd.write(result)
            fcntl.flock(fd, fcntl.LOCK_UN)

report = Report()
global_report = GlobalReport()

def init(report_path):
    report.report_path = report_path
    report_dir = os.path.dirname(report_path)
    pathlib.Path(report_dir).mkdir(parents=True, exist_ok=True)
    
    global_report.tmp_path = f'{config.working_dir}/report/_tmp.json'
    global_report.report_path = f'{config.working_dir}/report/report.log'
    if not os.path.exists(global_report.tmp_path):
        with open(global_report.tmp_path, 'w') as fd:
            fcntl.flock(fd, fcntl.LOCK_EX)
            fd.write(json.dumps({
                'vul_nums': [0, 0, 0, 0, 0, 0],
                'vuls': []
            }))
            fcntl.flock(fd, fcntl.LOCK_UN)
    os.system('rm -f debug.log')
        
def dbg(obj):
    with open('debug.log', 'a') as fd:
        fd.write(str(obj) + '\n')