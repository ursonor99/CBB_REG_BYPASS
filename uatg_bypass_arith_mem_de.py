
#asm += "\t nop\n"

from yapsy.IPlugin import IPlugin
from uatg.instruction_constants import base_reg_file, arithmetic_instructions
from typing import Dict, List, Union, Any
import random


class uatg_bypass_arith_mem_de(IPlugin):
    """
    This class contains methods to generate and validate the tests such that
    if the value of register after multiple operations remains unchanged.
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

    def generate_asm(self) -> List[Dict[str, Union[Union[str, list], Any]]]:
        """x
            Generates the ASM instructions to check if the concurrency
            is maintained after multiple operations.
        """
        reg_file = base_reg_file.copy()
        
        for i in range(0,len(reg_file)):
            if i < 29 :
                a = hex(random.getrandbits(self.xlen))
                b = hex(random.getrandbits(self.xlen))
                c = hex(random.getrandbits(self.xlen))
                d = hex(random.getrandbits(self.xlen))
        
                asm =  f"\t li {reg_file[i]} , {a}\n"
                asm += f"\t li {reg_file[i+1]}, {b}\n"
                asm += f"\t addi {reg_file[i+1]}, {reg_file[i]}, {c}\n"
                asm += f"\t nop\n"
                asm += f"\t addi {reg_file[i+2]}, {reg_file[i+1]}, {d}\n"
                asm += f"\t li {reg_file[i+3]}, {a+c+d}\n"
                asm += f"\t bne {reg_file[i+2]}, {reg_file[i+3]}, trap\n"
                asm += f"\t trap: addi {reg_file[0]}, {reg_file[0]}, 0\n" #if this branch is taken it implies the bypass of data from execute stage to decode is not happening properly
            
            if i > 29 :
                a= hex(random.getrandbits(self.xlen))
                b = hex(random.getrandbits(self.xlen))
                c = hex(random.getrandbits(self.xlen))
                d = hex(random.getrandbits(self.xlen))
        
                asm = f"\t li {reg_file[i]} , {a}\n"
                asm += f"\t li {reg_file[i-1]}, {b}\n"
                asm += f"\t addi {reg_file[i-1]}, {reg_file[i]}, {c}\n"
                asm += f"\t nop\n"
                asm += f"\t addi {reg_file[i-2]},{reg_file[i-1]}, {d}\n"
                asm += f"\t li {reg_file[i-3]}, {a+c+d}\n"
                asm += f"\t bne {reg_file[i-2]}, {reg_file[i-3]}, trap\n"
                asm += f"\t trap: addi {reg_file[0]}, {reg_file[0]}, 0\n" #if this branch is taken it implies the bypass of data from memory stage to decode is not happening properly
                
        compile_macros = []
        return [{
                'asm_code': asm,
                'asm_sig': '',
                'compile_macros': compile_macros
            }]
      		
      		
      	

    def check_log(self, log_file_path, reports_dir) -> bool:
        return False

    def generate_covergroups(self, config_file) -> str:
        sv = ""
        return sv
