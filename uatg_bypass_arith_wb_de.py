from yapsy.IPlugin import IPlugin
from uatg.instruction_constants import base_reg_file, arithmetic_instructions
from typing import Dict, List, Union, Any
import random


class uatg_bypass_03(IPlugin):
    """
    This class contains methods to generate and validate the tests such that
    if the value of register after multiple operations data dependency holds.
    """

    def __init__(self) -> None:
        super().__init__()

        pass


    def execute(self, core_yaml, isa_yaml) -> bool:
        self.isa = isa_yaml['hart0']['ISA']
        if 'RV32' in self.isa:
            self.isa_bit = 'rv32'
            self.xlen = 32
            self.offset_inc = 4
        else:
            self.isa_bit = 'rv64'
            self.xlen = 64
            self.offset_inc = 8
        return True

    def generate_asm(self) -> Dict[str, str]:

        test_dict = []
        reg_file = base_reg_file.copy()
        a=  random.getrandbits(self.xlen)
        b = random.getrandbits(self.xlen)
        c = random.getrandbits(self.xlen)
        asm = f"\tli {reg_file[3]},{a}\n"  
        asm += f"\tli {reg_file[4]},{b}\n"   
        asm += f"\t li {reg_file[1]},{c}\n"
        asm += f"\tmul {reg_file[6]},{reg_file[3]},{reg_file[4]} \n"
        asm += f"\t nop\n"    
        asm += f"\t nop\n"       
        asm += f"\t sub {reg_file[5]},{reg_file[6]},{reg_file[1]}\n"                                                                  
        asm += f"\t li {reg_file[7]},{(a*b)-c}\n"
        asm += f"\t bne {reg_file[5]} ,{reg_file[7]} , trap \n"
        asm += f"\t trap: addi {reg_file[0]}, {reg_file[0]}, 0\n" #this trap is taken if bypass fails
        
        compile_macros = []

        test_dict.append({
            'asm_code': asm,
            'asm_sig' : '',
            'compile_macros': compile_macros,
            })


        return test_dict


    def check_log(self, log_file_path, reports_dir) -> bool:
        return False

    def generate_covergroups(self, config_file) -> str:
        sv = ""
        return sv
