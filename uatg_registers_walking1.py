from yapsy.IPlugin import IPlugin
from uatg.instruction_constants import base_reg_file, arithmetic_instructions
from typing import Dict, List, Union, Any
import random


class uatg_registers_walking1(IPlugin):
    """
    This class contains methods to generate and validate the tests such that
    1. No bit in RTL is stuck at 0
    2. all 32 bits are present in RTL
    3. Only RW/WO bits are being written
    """

    def __init__(self) -> None:
        super().__init__()
        self.a = hex(1)
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
            Generates the ASM instructions to perform a register write with 
            0x1 shifted to left on each write
        """
      reg_file = base_reg_file.copy()

      for i in reg_file:
      	for j in range(0, xlen):
      		a = a << j
      		asm += "\t li i, a\n"
      		asm += "\t beq i, x0, trap\n"
      		asm += "\t li i+1, a-1\n"
      		asm += "\t AND i+2, i, i+1\n"
      		asm += "\t bne i+2, x0, trap\n"
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
