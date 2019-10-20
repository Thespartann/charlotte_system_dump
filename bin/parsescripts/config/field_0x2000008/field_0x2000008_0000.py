# coding=utf-8
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import struct
import os
import sys
import string

def PrintExcInfo(infile, field, offset, slen, version, mode, outfile):
        MyOffset = eval(offset)
        infile.seek(MyOffset)
        #print("got entry 0x2000008 PrintExcInfo")
        (g_magic, ) = struct.unpack('I',infile.read(4))
        (g_write, ) = struct.unpack('I',infile.read(4))
        (g_read, ) = struct.unpack('I',infile.read(4))
        (g_size, ) = struct.unpack('I',infile.read(4))
        (g_app_is_active, ) = struct.unpack('I',infile.read(4))
        (g_logged_chars, ) = struct.unpack('I',infile.read(4))
        (g_w_mark, ) = struct.unpack('i',infile.read(4))
        (g_reserved, ) = struct.unpack('i',infile.read(4))
        (g_log_buf, ) = struct.unpack('I',infile.read(4))
        if g_magic==0x32325445:
                outfile.writelines("Ring Buffer Write Offset    :0x%x\n" % g_write)
                outfile.writelines("Ring Buffer Read Offset     :0x%x\n" % g_read)
                outfile.writelines("Ring Buffer Size            :0x%x\n" % g_size)
                outfile.writelines("app_is_active               :%u\n" % g_app_is_active)
                outfile.writelines("Log Chars Num               :0x%x\n" % g_logged_chars)
                outfile.writelines("Water Mark                  :0x%x\n" % g_w_mark)
                outfile.writelines("Data Area                   :0x%x\n" % g_log_buf)
                outfile.writelines("-----------------------------\n")
                MyLen = int(slen,16) - 36
                #print("got entry 0x2000008 PrintExcInfo dot 1, Mylen is %d" %(MyLen))
                for i in range(0, MyLen):
                    #tag = struct.unpack('s',infile.readline(1))
                    #tag = struct.unpack('B', infile.readline(1))
                    tag = infile.readline(1)
                    if ord(tag.decode()) >= 0x20 and ord(tag.decode()) <= 0x7E:
                        outfile.writelines(tag.decode(encoding="utf-8"))
                    elif tag == b'\x0A':
                        outfile.writelines('\n')
                    #if tag == b'\x00':
                    #    continue
                    #elif tag == b'\x0D':
                    #    continue
                    #elif tag == b'\x0A':
                    #    outfile.writelines('\n')
                    #else:
                    #    outfile.writelines(tag.decode(encoding="utf-8"))
                outfile.writelines("dmesg end\n")
                return
        #print("got entry 0x2000008 PrintExcInfo dot 2")
        outfile.writelines('magic %u is wrong' % g_magic)
        return
 	
def entry_0x2000008(infile, field, offset, slen, version, mode, outfile):
        try:
            if not field == '0x2000008':
                print('hidis field is ', field)
                print('current field is', '0x2000008')
                return error['ERR_CHECK_FIELD']
            elif not version == '0x0000':
                print('hidis version is ', version)
                print('current version is ', '0x0000')
                return error['ERR_CHECK_VERSION']
            elif not slen == '0x10000':
                print('hids len is ', slen)
                print('current len is ', '0x10000')
                return error['ERR_CHECK_LEN']
            #print("got entry 0x2000008")
            outfile.writelines("============CP DMESG============\n")
            PrintExcInfo(infile, field, offset, slen, version, mode, outfile)
            return 0

        except Exception as e:
            print(str(e))
            outfile.writelines(str(e))
            return 1
