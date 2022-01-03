
# Chromite-Bug-Bounty
chromite-bug-bounty special topic coursework

This repository consists of python scripts to generate RISC-V assembly for testing the Regfile + Bypass + Scoreboard in the Chromite core developed by incore semiconductors

Register file: The Register file is a part of the decode stage in the pipeline. It consists of 32 registers. There are 2 read ports and 1 write port. The length of each register is parametrizable at instantiation.When debug support is enabled the register file(s) are provided with an extra read port for the debugger to access the registers directly. for more information visit (https://chromite.readthedocs.io/en/latest/chromite.html#register-file)

Bypass hardware : Using pipeline design ,the  RISC processor operates at more than one cycle per instruction; the processor might occasionally encounter a  stall as a  result of data dependencies and branch instructions. When an instruction depends on the previous instruction,data dependency occurs.A particular instruction might need data in a register which has not yet been stored since the preceding instruction which has not yet reached that stage  in the pipeline.
In these cases the bypass logic takes care so that correct values of are used for the exection of each instruction . 


# Code Description

### uatg_registers_1bit_crawl.py
* in this test register write of 0x1 is performed with left shifting it after each write .
* leftshifted 1 bit is loaded . 
* checked if the loaded register has a non zero value . if its zero executinon jumps to trap and incremets x31 
* value of 1 less than the left shifted variable is loaded to the next register and the two registers are anded . 
* if the anded value is not equal to 0 , a trap is raised . 
* This test checks for stuck at 0 glitches .

### uatg_registers_reg0_zero.py
* this test is used to check if the register x0 changes its value after any of the instruction .
* 'li', 'addi', 'subi', 'mul', 'and' are the instructions tested .
* 0x0 is loaded to x1 . 
* after every instruction if the value of x0 doesnt match the value of x1 , trap is raised .


### uatg_bypass_arith_ex_de.py
* a legal random number A is loaded to a register Xi
* a legal random number B is loaded to a register Xi+1
* a legal random number C is added to the Xi and stored to Xi+1
* a legal random number D is added to the Xi+1 and stored to Xi+2
* A+C+D is loaded to Xi+3 
* If the value at Xi+2 doesnt match that aat Xi+3 , a trap is raised .
* this tests if the correct value of Xi+1 is bypassed from the execution stage to the decode stage for the next instruction

### uatg_bypass_arith_mem_de.py
* a legal random number A is loaded to a register Xi
* a legal random number B is loaded to a register Xi+1
* a legal random number C is added to the Xi and stored to Xi+1
* no operation is performed for in this step
* a legal random number D is added to the Xi+1 and stored to Xi+2
* A+C+D is loaded to Xi+3 
* If the value at Xi+2 doesnt match that aat Xi+3 , a trap is raised .
* this tests if the correct value of Xi+1 is bypassed from the memory stage to the decode stage for the next instruction

### uatg_bypass_arith_wb_de.py
* a legal random number A is loaded to a register X3
* a legal random number B is loaded to a register X4
* a legal random number C is loaded to a register X1
* X3 and X4 are multiplied and stored to X6
* no operation is performed for in this step
* no operation is performed for in this step
* X1 is substracted from X6 and stored to X5
* (A*B)-C is loaded to X7
* If the value at X5 doesnt match that aat X7 , a trap is raised .
* this tests if the correct value of Xi+1 is bypassed from the write back stage to the decode stage for the next instruction

References:
1. Chromite core documentation
https://chromite.readthedocs.io/en/latest/chromite.html

2. UATG tests documentation by Incore semiconductors
https://uatg.readthedocs.io/en/stable/index.html

