# Licensing information can be found at LICENSE.incore
# Test generated by user - sushanth at 2021-12-31 16:01:19

#include "model_test.h" 
#include "arch_test.h"
RVTEST_ISA("RV64IMACSUZicsr_Zifencei")

.section .text.init
.globl rvtest_entry_point
rvtest_entry_point:
RVMODEL_BOOT
RVTEST_CODE_BEGIN
	 li x31 , 0x8f4ddd5a546d75e
	 li x30, 0x567ee59327fc333b
	 addi x30, x31, 0x14bf07e8d32152d
	 addi x29, x30, 0x6d069fc487c76edf
	 li x28, 0x8f4ddd5a546d75e0x14bf07e8d32152d0x6d069fc487c76edf
	 bne x29, x28, trap
	 trap: addi x0, x0, 0

RVTEST_CODE_END
RVMODEL_HALT


RVTEST_DATA_BEGIN
.align 4

sample_data:
.word	0xbabecafe

RVTEST_DATA_END


RVMODEL_DATA_BEGIN

RVMODEL_DATA_END

