from yapsy.IPlugin import IPlugin
from uatg.instruction_constants import base_reg_file, arithmetic_instructions
from typing import Dict, List, Union, Any
import random


class uatg_bypass_02(IPlugin):
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
            Generates the ASM instructions to check if the bypassed 
            instruction holds good with no operation
        """
      reg_file = base_reg_file.copy()

      for i in reg_file:
      	a_val = hex(random.getrandbits(self.xlen))
      	b_val = hex(random.getrandbits(self.xlen))
      	c_val = hex(random.getrandbits(self.xlen))
      	d_val = hex(random.getrandbits(self.xlen))
 
      		asm += "\t li i, a\n"
      		asm += "\t li i+1, b\n"
      		asm += "\t addi i+1, a, c\n"
      		asm += "\t nop\n"
      		asm += "\t addi i+2, i+1, d\n"
      		asm += "\t li i+3, a+c+d\n"
      		asm += "\t bne i+2, i+3, trap\n"
      		asm += "\t trap: addi x30, x30, 1\n"
      		
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
