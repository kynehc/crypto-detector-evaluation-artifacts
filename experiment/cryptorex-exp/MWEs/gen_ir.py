import sys
import logging
import os

import angr
import ailment

logging.getLogger('angr').propagate = False
logging.getLogger('pyvex').propagate = False
logging.getLogger('cle').propagate = False

if __name__ == '__main__':
    vex_file = sys.argv[1].replace('bin/', 'vex/') + '.vex'
    ail_file = sys.argv[1].replace('bin/', 'ail/') + '.ail'
    
    os.system(f'rm -f {vex_file}')
    os.system(f'rm -f {ail_file}')
    
    proj = angr.Project(sys.argv[1], load_options={'auto_load_libs': False})
    cfg = proj.analyses.CFGFast()

    for node in cfg.nodes():
        vex_block = proj.factory.block(node.addr).vex
        ail_block = ailment.IRSBConverter().convert(vex_block, ailment.Manager(arch=proj.arch))
        
        with open(vex_file, 'a+') as fd:
            fd.write(str(vex_block) + '\n\n')
        with open(ail_file, 'a+') as fd:
            fd.write(str(ail_block) + '\n\n')