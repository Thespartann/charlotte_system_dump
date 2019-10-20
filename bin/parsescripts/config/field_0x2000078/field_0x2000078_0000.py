#coding=utf-8
'''
Created on 2014-11-14
 
@author: Neo
'''
import os
import re
import struct
import sys

ipf_field_def = [
     "HI_IPF_SRST_OFFSET", 
     "HI_IPF_SRST_STATE_OFFSET",
     "HI_IPF_CH_EN_OFFSET",               
     "HI_IPF_EN_STATE_OFFSET",            
     "HI_IPF_GATE_OFFSET",                
     "HI_IPF_CTRL_OFFSET",                
     "HI_IPF_DMA_CTRL0_OFFSET",           
     "HI_IPF_DMA_CTRL1_OFFSET",           
     "HI_IPF_VERSION_OFFSET",             
     "HI_IPF_INT0_OFFSET",                
     "HI_IPF_INT1_OFFSET",                
     "HI_IPF_INT_MASK0_OFFSET",           
     "HI_IPF_INT_MASK1_OFFSET",           
     "HI_IPF_INT_STATE_OFFSET",           
     "HI_IPF_TIME_OUT_OFFSET",            
     "HI_IPF_PKT_LEN_OFFSET",             
     "HI_IPF_FILTER_ZERO_INDEX_OFFSET",   
     "HI_IPF_EF_BADDR_L_OFFSET",         
     "HI_IPF_EF_BADDR_H_OFFSET",         
     "HI_IPF_FLT_CHAIN_LOOP_OFFSET",      
     "HI_IPF_TRANS_CNT_CTRL_OFFSET",      
     "HI_IPF_TIMER_LOAD_OFFSET",          
     "HI_IPF_TIMER_COUNTER_OFFSET",       
     "HI_IPF_CH0_PKT_CNT_OFFSET",         
     "HI_IPF_CH1_PKT_CNT_OFFSET",         
     "HI_IPF64_CH0_CTRL_OFFSET",          
     "HI_IPF64_CH0_STATE_OFFSET",         
     "HI_IPF64_CH0_BDQ_BADDR_L_OFFSET",   
     "HI_IPF64_CH0_BDQ_BADDR_H_OFFSET",   
     "HI_IPF64_CH0_BDQ_SIZE_OFFSET",      
     "HI_IPF64_CH0_BDQ_WPTR_OFFSET",      
     "HI_IPF64_CH0_BDQ_RPTR_OFFSET",      
     "HI_IPF64_CH0_BDQ_WADDR_L_OFFSET",   
     "HI_IPF64_CH0_BDQ_WADDR_H_OFFSET",   
     "HI_IPF64_CH0_BDQ_RADDR_L_OFFSET",   
     "HI_IPF64_CH0_BDQ_RADDR_H_OFFSET",   
     "HI_IPF64_CH0_BDQ_DEPTH_OFFSET",    
     "HI_IPF64_CH1_CTRL_OFFSET",          
     "HI_IPF64_CH1_STATE_OFFSET",         
     "HI_IPF64_CH1_RDQ_BADDR_L_OFFSET",   
     "HI_IPF64_CH1_RDQ_BADDR_H_OFFSET",   
     "HI_IPF64_CH1_RDQ_SIZE_OFFSET",      
     "HI_IPF64_CH1_RDQ_WPTR_OFFSET",      
     "HI_IPF64_CH1_RDQ_RPTR_OFFSET",      
     "HI_IPF64_CH1_RDQ_WADDR_L_OFFSET",   
     "HI_IPF64_CH1_RDQ_WADDR_H_OFFSET",   
     "HI_IPF64_CH1_RDQ_RADDR_L_OFFSET",   
     "HI_IPF64_CH1_RDQ_RADDR_H_OFFSET",   
     "HI_IPF64_CH1_RDQ_DEPTH_OFFSET",     
     "HI_IPF64_CH1_ADQ_CTRL_OFFSET",      
     "HI_IPF64_CH1_ADQ0_BASE_L_OFFSET",   
     "HI_IPF64_CH1_ADQ0_BASE_H_OFFSET",   
     "HI_IPF64_CH1_ADQ0_STAT_OFFSET",     
     "HI_IPF64_CH1_ADQ0_WPTR_OFFSET",     
     "HI_IPF64_CH1_ADQ0_RPTR_OFFSET",     
     "HI_IPF64_CH1_ADQ1_BASE_L_OFFSET",   
     "HI_IPF64_CH1_ADQ1_BASE_H_OFFSET",   
     "HI_IPF64_CH1_ADQ1_STAT_OFFSET",     
     "HI_IPF64_CH1_ADQ1_WPTR_OFFSET",     
     "HI_IPF64_CH1_ADQ1_RPTR_OFFSET",     
     "HI_IPF64_SEC_ATTR_OFFSET",          
     "HI_IPF64_BURST_CFG_OFFSET",         
     "HI_IPF64_CH0_RDQ_BADDR_L_OFFSET",   
     "HI_IPF64_CH0_RDQ_BADDR_H_OFFSET",   
     "HI_IPF64_CH0_RDQ_SIZE_OFFSET",      
     "HI_IPF64_CH0_RDQ_WPTR_OFFSET",      
     "HI_IPF64_CH0_RDQ_RPTR_OFFSET",      
     "HI_IPF64_CH0_RDQ_WADDR_L_OFFSET",   
     "HI_IPF64_CH0_RDQ_WADDR_H_OFFSET",   
     "HI_IPF64_CH0_RDQ_RADDR_L_OFFSET",   
     "HI_IPF64_CH0_RDQ_RADDR_H_OFFSET",   
     "HI_IPF64_CH0_RDQ_DEPTH_OFFSET",     
     "HI_IPF64_CH1_BDQ_BADDR_L_OFFSET",   
     "HI_IPF64_CH1_BDQ_BADDR_H_OFFSET",   
     "HI_IPF64_CH1_BDQ_SIZE_OFFSET",      
     "HI_IPF64_CH1_BDQ_WPTR_OFFSET",      
     "HI_IPF64_CH1_BDQ_RPTR_OFFSET",      
     "HI_IPF64_CH1_BDQ_WADDR_L_OFFSET",   
     "HI_IPF64_CH1_BDQ_WADDR_H_OFFSET",   
     "HI_IPF64_CH1_BDQ_RADDR_L_OFFSET",   
     "HI_IPF64_CH1_BDQ_RADDR_H_OFFSET",   
     "HI_IPF64_CH1_BDQ_DEPTH_OFFSET",     
     "HI_IPF64_CH0_ADQ_CTRL_OFFSET",      
     "HI_IPF64_CH0_ADQ0_BASE_L_OFFSET",   
     "HI_IPF64_CH0_ADQ0_BASE_H_OFFSET",   
     "HI_IPF64_CH0_ADQ0_STAT_OFFSET",     
     "HI_IPF64_CH0_ADQ0_WPTR_OFFSET",     
     "HI_IPF64_CH0_ADQ0_RPTR_OFFSET",     
     "HI_IPF64_CH0_ADQ1_BASE_L_OFFSET",   
     "HI_IPF64_CH0_ADQ1_BASE_H_OFFSET",   
     "HI_IPF64_CH0_ADQ1_STAT_OFFSET",     
     "HI_IPF64_CH0_ADQ1_WPTR_OFFSET",     
     "HI_IPF64_CH0_ADQ1_RPTR_OFFSET",     
]

def ipf_entry_parse(infile, outfile, offset):
    infile.seek(0 + offset)
    for i in range(0, int(len(ipf_field_def))):
        (reg, ) = struct.unpack("I", infile.read(4))
        outfile.writelines("%s 0x%08x\n" %(ipf_field_def[i], reg))
    return

def entry_0x2000078(infile, field, offset, slen, version, mode, outfile):
        try:
            if not field == '0x2000078':
                print('hidis field is ', field)
                print('current field is', '0x2000078')
                return error['ERR_CHECK_FIELD']
            elif not version == '0x0000':
                print('hidis version is ', version)
                print('current version is ', '0x0000')
                return error['ERR_CHECK_VERSION']
            elif not slen == '0x400':
                print('hids len is ', slen)
                print('current len is ', '0x400')
                return error['ERR_CHECK_LEN']
            #outfile.writelines("got entry entry_0x2000078")
            outfile.writelines("============ IPF ============\n")
            offset_v = eval(offset)
            ipf_entry_parse(infile, outfile, offset_v)
            return 0

        except Exception as e:
            print((str(e)))
            outfile.writelines(str(e))
            return 1


    
