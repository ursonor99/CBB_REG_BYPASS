from yapsy.IPlugin import IPlugin
from uatg.instruction_constants import base_reg_file, arithmetic_instructions
from typing import Dict, List, Union, Any
import random


class uatg_registers_01(IPlugin):
    """
    This class contains methods to generate and validate the tests for x0 register 
    which is hardwired to 0.
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
            Generates the ASM instructions to perform different operations 
            with register x0.
        """
      reg_file = base_reg_file.copy()
      		
      		asm += f"\t li x1, 0x0\n"
      		for i in ['li', 'addi', 'subi']:
      			asm += f"\t i x0, x0, 0x4\n"
      			asm += "\t bne x0, x1, trap\n"
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
