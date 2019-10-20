# -*- coding: utf-8 -*-
# ccore drx
import sys
from config import *
pm_global_var = (
	"STAMP_START_ADDR: ",
	"PM_ENTER_COUNT:  ",
	"PM_DPM_FAIL_COUNT :  ",
	"STAMP_PM_SUSPEND_START:  ",
	"STAMP_DPM_SUSPEND_FAIL:  ",
	"STAMP_AFTER_DPM_SUSPEND: ",
	"STAMP_AFTER_UART_SUSPEND:  ",
	"STAMP_PM_ENTER_START :  ",
	"STAMP_AFTER_DISABLE_GIC:  ",
	"STAMP_AFTER_BAK_GIC: ",
	"STAMP_AFTER_UTRACE_SUSPEND:  ",
	"STAMP_AFTER_TCXO_SUSPEND :  ",
	"STAMP_AFTER_PIN_POWERDOWN:  ",
	"STAMP_SLEEP_ASM_ENTER: ",
	"STAMP_BAK_COREG_BEGIN:  ",
	"STAMP_BAK_COREG_END :  ",
	"STAMP_BAK_MMUREG_BEGIN:  ",
	"STAMP_BAK_MMUREG_END: ",
	"STAMP_BEFORE_SEND_IPC:  ",
	"STAMP_AFTER_SEND_IPC :  ",
	"STAMP_AFTER_WFI_NOP:  ",
	"STAMP_PWRUP_CODE_BEGIN :  ",
	"STAMP_RSTR_MMUREG_BEGIN:  ",
	"STAMP_RSTR_MMUREG_END: ",
	"STAMP_RSTR_COREG_BEGIN:  ",
	"STAMP_RSTR_COREG_END :  ",
	"STAMP_SLEEP_ASM_OUT:  ",
	"STAMP_AFTER_PIN_NORMAL :  ",
	"STAMP_AFTER_TCXO_RESUME:  ",
	"STAMP_AFTER_UTRACE_RESUME: ",
	"STAMP_AFTER_RSTR_GIC:  ",
	"STAMP_AFTER_ENABLE_GIC :  ",
	"STAMP_PM_ENTER_END:  ",
	"STAMP_AFTER_UART_RESUME:  ",
	"STAMP_BEFORE_DPM_RESUME :  ",
	"STAMP_AFTER_DPM_RESUME:  ",
	)
def parse_ccore_pm_bin(infile, offset, outfile):
	infile.seek(offset+16)
	for index in range(len(pm_global_var)):
		(value, )    = struct.unpack('I', infile.read(4))
		outfile.writelines("%s0x%.8x\n" %(pm_global_var[index], value))


	
def entry_0x200000E(infile, field, offset, len, version, mode, outfile):
	########check parameter start#############
	if not field == '0x200000E':
		print("hidis field is 0x%x"%(field))
		print("current field is 0x200000E")
		return error['ERR_CHECK_FIELD']
	elif not version == '0x0000':
		print("hidis version is 0x%x"%(version))
		print("current version is 0x00")
#		return error['ERR_CHECK_VERSION']
	elif not len == '0x2000':
		print("hids len is 0x%x"%(len))
		print("current len is 0x2000")
#		return error['ERR_CHECK_LEN']
	#########check parameter end##############

	parse_ccore_pm_bin(infile, eval(offset), outfile)
	return 0