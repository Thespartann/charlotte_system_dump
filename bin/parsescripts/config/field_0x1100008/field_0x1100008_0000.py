#######################################################################################################################################
#   filename        :   exparse_python_frame.py
#
#   author          :   fuxin 00221597
#
#   description     :   config for exparse python sripts frame 
#
#   modify  record  :   2014-07-21 create file
#
#######################################################################################################################################
import sys
import struct
from config import *

CMD_NUM = 17
ASCTRL_REG_NUM = 16

def entry_0x1100008(infile, field, offset, len, version, mode, outfile):
        outfile.writelines("============ABBP============\n")
        ########check parameter start#############
        if not field == '0x1100008':
            print(('abbp field is ', field))
            print(('current field is', '0x1100008'))
            return error['ERR_CHECK_FIELD']
        elif not version == '0x0000':
            print(('hidis version is ', version))
            print(('current version is ', '0x0000'))
            return error['ERR_CHECK_VERSION']
        elif not len == '0x10000':
            print(('hids len is ', len))
            print(('current len is ', '0x10000'))
            return error['ERR_CHECK_LEN']
        #########check parameter end##############
        MyOffset = eval(offset)
        infile.seek(MyOffset)
        while True:
            (magic, ) = struct.unpack('I', infile.read(4))
            MyOffset += 4
            if magic == 0x50424241:
                break
        infile.seek(MyOffset)
        s1 = "******************* [%s] ********************\n" % ('abbpom_cmd_return_value')
        outfile.writelines(s1)
        print("MyOffset = 0x%x\n" %(MyOffset))
        for i in range(0,CMD_NUM):
            (value, ) = struct.unpack('I', infile.read(4))
            outfile.writelines('%-10d%#-20x\n' %(i, value))
        s1 = "******************* [%s] ********************\n" % ('abbpom_apscreg_value')
        outfile.writelines(s1)
        for i in range(0,ASCTRL_REG_NUM):
            (value, ) = struct.unpack('I', infile.read(4))
            outfile.writelines('%-10d%#-20x\n' %(i, value))

        return 0

