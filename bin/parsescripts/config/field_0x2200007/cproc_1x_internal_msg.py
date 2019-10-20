#######################################################################################################################################
#   filename        :   cproc_1x_internal_msg.py
#
#   author          :   linchengwen 00322531
#
#   description     :   list cproc1x internal msg
#
#   modify  record  :   2016-03-10 create file
#                            2016-11-09 update
#
#######################################################################################################################################

cproc_1x_internal_msg_enum_table = {
    0x2200  : "ID_CPROC_1X_CM_SMC_OFFSET_REQ",
    0x2201  : "ID_CPROC_1X_CM_SMC_PUF_END_REQ",
    0x2202  : "ID_CPROC_1X_CM_SMC_COMPLETE_CF_SEARCH_REQ",
    0x2203  : "ID_CPROC_1X_SMC_CM_PERIODIC_OLPRM_IND",
    0x2204  : "ID_CPROC_1X_SMC_CM_COMPLETE_CF_SEARCH_IND",
    0x2205  : "ID_CPROC_1X_SMC_CM_HANDOFF_FAIL_IND",
    0x2206  : "ID_CPROC_1X_SMC_CM_PILOT_KNOWN_IND",
    0x2207  : "ID_CPROC_1X_CM_SMC_PILOT_SEARCH_REQ",
    0x2208  : "ID_CPROC_1X_SMC_CM_PILOT_SEARCH_IND",
    0x2209  : "ID_CPROC_1X_CM_SMC_SIGNAL_LEVEL_SCAN_IND",
    0x220A  : "ID_CPROC_1X_SMC_CM_SIGNAL_LEVEL_SCAN_REQ",
    0x220B  : "ID_CPROC_1X_CM_SMC_CF_FAILED_REQ",
    0x220C  : "ID_CPROC_1X_CM_SMC_PUF_START_REQ",
    0x220D  : "ID_CPROC_1X_SMC_CM_PUF_START_CNF",
    0x220E  : "ID_CPROC_1X_SMC_CM_DONE_IND",
    0x220F  : "ID_CPROC_1X_SMC_CM_MEAS_PARAM_IND",
    0x2210  : "ID_CPROC_1X_SCM_CM_NON_SF_MEAS_IND",
    0x2211  : "ID_CPROC_1X_CM_SMC_MEASUREMENT_CONTROL_REQ",
    0x2212  : "ID_CPROC_1X_SMC_CM_MEASUREMENT_CONTROL_CNF",
    0x2213  : "ID_CPROC_1X_CM_SM_RELEASE_ALL_REQ",
    0x2214  : "ID_CPROC_1X_SM_CM_RELEASE_ALL_CNF",
    0x2215  : "ID_CPROC_1X_CM_SM_SET_WORK_MODE_REQ",
    0x2216  : "ID_CPROC_1X_SM_CM_SET_WORK_MODE_CNF",
    0x2217  : "ID_CPROC_1X_SMC_CM_MPS_RESULT_IND",
    0x2218  : "ID_CPROC_1X_CM_SMC_SET_TIMING_REQ",
    0x2219  : "ID_CPROC_1X_CM_SMC_MPS_START_REQ",
    0x221A  : "ID_CPROC_1X_CM_SMC_MPS_STOP_REQ",
    0x221B  : "ID_CPROC_1X_SMC_CM_MPS_STOP_CNF",
    0x221C  : "ID_CPROC_1X_CM_SMC_SUSPEND_REQ",
    0x221D  : "ID_CPROC_1X_SMC_CM_SUSPEND_CNF",
    0x221E  : "ID_CPROC_1X_SMC_CM_SUSPEND_IND",
    0x221F  : "ID_CPROC_1X_CM_SMC_RESUME_REQ",
    0x2220  : "ID_CPROC_1X_SMC_CM_READY_FOR_OFFLINE_IND",
    0x2221  : "ID_CPROC_1X_SMC_CM_NEED_ONLINE_IND",
    0x2222  : "ID_CPROC_1X_CM_SMC_NEED_ONLINE_RSP",
    0x2223  : "ID_CPROC_1X_CM_SM_TRAFFIC_INFO_NTF",
    0xF000  : "ID_CPROC_1X_RFA_ALLOC_REQ",
    0xF001  : "ID_CPROC_1X_RFA_TIMING_UPDATE_REQ",
    0xF002  : "ID_CPROC_1X_RFA_ALLOC_CNF",
    0xF003  : "ID_CPROC_1X_RFA_CM_ALLOC_CNF",
    0xF004  : "ID_CPROC_1X_RFA_SM_ALLOC_CNF",
    0xF005  : "ID_CPROC_1X_RFA_DRX_ALLOC_CNF",
    0xF006  : "ID_CPROC_1X_RFA_BG_ALLOC_CNF",
    0xF007  : "ID_CPROC_1X_RFA_AGPS_ALLOC_CNF",
    0xF008  : "ID_CPROC_1X_RFA_RELEASE_REQ",
    0xF009  : "ID_CPROC_1X_RFA_RELEASE_CNF",
    0xF00A  : "ID_CPROC_1X_RFA_CM_RELEASE_CNF",
    0xF00B  : "ID_CPROC_1X_RFA_DRX_RELEASE_CNF",
    0xF00C  : "ID_CPROC_1X_RFA_BG_RELEASE_CNF",
    0xF00D  : "ID_CPROC_1X_RFA_AGPS_RELEASE_CNF",
    0xF00E  : "ID_CPROC_1X_RFA_DRX_CF_ALLOC_REQ",
    0xF00F  : "ID_CPROC_1X_RFA_DRX_CF_ALLOC_CNF",
    0xF010  : "ID_CPROC_1X_RFA_PAGING_SETUP_REQ",
    0xF011  : "ID_CPROC_1X_RFA_PAGING_EXEC_REQ",
    0xF012  : "ID_CPROC_1X_RFA_PAGING_EXEC_CNF",
    0xF013  : "ID_CPROC_1X_RFA_CM_PAGING_EXEC_CNF",
    0xF014  : "ID_CPROC_1X_RFA_DRX_PAGING_EXEC_CNF",
    0xF015  : "ID_CPROC_1X_RFA_RXOFF_REQ",
    0xF016  : "ID_CPROC_1X_RFA_INIT_REQ",
    0xF017  : "ID_CPROC_1X_RFA_INIT_CNF",
    0xF018  : "ID_CPROC_1X_RFA_RELEASE_ALL_REQ",
    0xF019  : "ID_CPROC_1X_RFA_RELEASE_ALL_CNF",
    0xF01A  : "ID_CPROC_1X_RFA_BG_SUSPEND_IND",
    0xF01B  : "ID_CPROC_1X_RFA_BG_SUSPEND_RSP",
    0xF01C  : "ID_CPROC_1X_RFA_SLEEP_REQ",
    0xF01D  : "ID_CPROC_1X_RFA_SUSPEND_IND",
    0xF01E  : "ID_CPROC_1X_RFA_SUSPEND_STARTED_RSP",
    0xF01F  : "ID_CPROC_1X_RFA_SUSPEND_COMPLETE_RSP",
    0xF020  : "ID_CPROC_1X_RFA_RESUME_IND",
    0xF021  : "ID_CPROC_1X_RFA_SET_DIV_MODE_REQ",
    0xF022  : "ID_CPROC_1X_RFA_SET_DIV_MODE_CNF",
    0xF023  : "ID_CPROC_1X_RFA_WAKE_UP_REQ",
    0xF024  : "ID_CPROC_1X_RFA_CM_WAKE_UP_CNF",
    0xF025  : "ID_CPROC_1X_RFA_SM_SF_RXON_AFTER_CF_GAP_IND",
    0xF026  : "ID_CPROC_1X_RFA_RXOFF_CNF",
    0xF027  : "ID_CPROC_1X_RFA_RESET_ERQ",
    0xF028  : "ID_CPROC_1X_RFA_RESET_CNF",
    0xF029  : "ID_CPROC_1X_RFA_DM_RF_CHANNEL_DIV_CAP_IND",
    0xF02A  : "ID_CPROC_1X_RFA_CAP_UPDATE_REQ",
    0xF02B  : "ID_CPROC_1X_RFA_CAP_UPDATE_CNF",
    0xF040  : "ID_CPROC_1X_DRX_CM_SMC_ACTIVATE_REQ",
    0xF041  : "ID_CPROC_1X_DRX_CM_SMC_DEACTIVATE_REQ",
    0xF042  : "ID_CPROC_1X_DRX_CM_SMC_PILOT_SEARCH_REQ",
    0xF043  : "ID_CPROC_1X_DRX_SMC_CM_PILOT_SEARCH_IND",
    0xF044  : "ID_CPROC_1X_DRX_SM_ONE_SHOT_MPS_REQ",
    0xF045  : "ID_CPROC_1X_DRX_SM_CONTINUOUS_MPS_NO_SLEEP_REQ",
    0xF046  : "ID_CPROC_1X_DRX_SM_CONTINUOUS_MPS_SLEEP_REQ",
    0xF047  : "ID_CPROC_1X_DRX_SMC_CM_MPS_IND",
    0xF048  : "ID_CPROC_1X_DRX_CM_SMC_STOP_MPS_REQ",
    0xF049  : "ID_CPROC_1X_DRX_SMC_CM_DONE_IND",
    0xF04A  : "ID_CPROC_1X_DRX_CM_SM_MEAS_STOP_REQ",
    0xF04B  : "ID_CPROC_1X_DRX_SM_CF_MEASUREMENT_REQ",
    0xF04C  : "ID_CPROC_1X_DRX_SM_SF_MEASUREMENT_REQ",
    0xF04D  : "ID_CPROC_1X_DRX_CM_SMC_TIME_SYNCH_REQ",
    0xF04E  : "ID_CPROC_1X_DRX_CM_SMC_PRE_MEASUREMENT_REQ",
    0xF04F  : "ID_CPROC_1X_DRX_SMC_CM_PRE_MEAS_IND",
    0xF050  : "ID_CPROC_1X_DRX_CM_SMC_SUSPEND_REQ",
    0xF051  : "ID_CPROC_1X_DRX_SMC_CM_SUSPEND_CNF",
    0xF052  : "ID_CPROC_1X_DRX_SMC_CM_READY_FOR_OFFLINE_IND",
    0x2250  : "ID_CPROC_1X_DRX_CPROC_SM_IND",
    0x2251  : "ID_CPROC_1X_DRX_CPROC_SM_PRE_MEAS_IND",
    0x2350  : "ID_CPROC_1X_CPROC_DRX_CM_TIMING_UPDATE_REQ",
    0x2351  : "ID_CPROC_1X_CPROC_DRX_RELEASE_ALL_REQ",     
    0x2352  : "ID_CPROC_1X_DRX_CPROC_RELEASE_ALL_CNF",     
    0x2353  : "ID_CPROC_1X_CPROC_DRX_CM_PILOT_QUALITY_IND",
    0x2354  : "ID_CPROC_1X_CPROC_DRX_CM_PILOT_SEARCH_REQ", 
    0x2355  : "ID_CPROC_1X_DRX_CPROC_CM_PILOT_SEARCH_IND", 
    0x2356  : "ID_CPROC_1X_CPROC_DRX_SIGNAL_LEVEL_REQ",    
    0x2357  : "ID_CPROC_1X_DRX_CPROC_SIGNAL_LEVEL_IND",    
    0x2358  : "ID_CPROC_1X_CPROC_DRX_CH_START_REQ",        
    0x2359  : "ID_CPROC_1X_CPROC_DRX_CH_STOP_REQ",         
    0x235A  : "ID_CPROC_1X_DRX_CPROC_CH_STOP_CNF",         
    0x235B  : "ID_CPROC_1X_CPROC_DRX_CM_CFG_REQ",          
    0x235C  : "ID_CPROC_1X_DRX_CPROC_CM_CFG_CNF",          
    0x235D  : "ID_CPROC_1X_CPROC_DRX_CM_STOP_REQ",         
    0x235E  : "ID_CPROC_1X_DRX_CPROC_CM_STOP_CNF",         
    0x235F  : "ID_CPROC_1X_DRX_CPROC_QPCH_IND",            
    0x2360  : "ID_CPROC_1X_DRX_CPROC_ACTION_IND",          
    0x2361  : "ID_CPROC_1X_DRX_CPROC_CHANNEL_RELEASE_CNF", 
    0x2362  : "ID_CPROC_1X_CPROC_DRX_CM_READY_REQ",        
    0x2363  : "ID_CPROC_1X_DRX_CM_CPROC_READY_CNF",        
    0x2364  : "ID_CPROC_1X_CPROC_DRX_TIME_SYNC_REQ",       
    0x2365  : "ID_CPROC_1X_DRX_CPROC_TIME_SYNC_IND",       
    0x2366  : "ID_CPROC_1X_CPROC_DRX_SLEEP_REQ",           
    0x2367  : "ID_CPROC_1X_CPROC_DRX_PRE_MEASURE_REQ",     
    0x2368  : "ID_CPROC_1X_DRX_CPROC_PRE_MEASURE_CNF",     
    0x2369  : "ID_CPROC_1X_DRX_CPROC_PRE_MEASURE_IND",     
    0x236A  : "ID_CPROC_1X_CPROC_DRX_CH_PREPARE_REQ",      
    0x236B  : "ID_CPROC_1X_DRX_CPROC_CH_PREPARE_CNF",      
    0x236C  : "ID_CPROC_1X_CPROC_DRX_CM_CONTINUE_REQ",     
    0x236D  : "ID_CPROC_1X_CM_DRX_SUSPEND_REQ",            
    0x236E  : "ID_CPROC_1X_DRX_CM_SUSPEND_CNF",            
    0x236F  : "ID_CPROC_1X_DRX_CM_SUSPEND_IND",            
    0x2370  : "ID_CPROC_1X_DRX_CPROC_NO_RF_IND",           
    0x2371  : "ID_CPROC_1X_DRX_CPROC_RF_IND",
    0x2372  : "ID_CPROC_1X_DRX_CPROC_WAKEUP_IND",
    0x2373  : "ID_CPROC_1X_DRX_CPROC_SLEEP_IND",
    0x23C0  : "ID_CPROC_1X_DM_STATE_REQ",
    0x23D0  : "ID_CPROC_1X_TURN_OFF_DIVERSITY_IND",           
    0x23D1  : "ID_CPROC_1X_TURN_ON_DIVERSITY_IND",
    0x3000  : "ID_CPROC_1X_CM_AGPS_ACTIVATE_REQ",
    0x3001  : "ID_CPROC_1X_AGPS_DEACTIVATE_REQ",
    0x3002  : "ID_CPROC_1X_AGPS_SLEEP_REQ",
    0x3003  : "ID_CPROC_1X_CM_AGPS_CONTINUOUS_REQ",
    0x3004  : "ID_CPROC_1X_AGPS_CM_CONTINUOUS_CNF",
    0x2240  : "ID_CPROC_1X_SM_DM_MEAS_IND",
    0x2241  : "ID_CPROC_1X_DM_SM_SET_DIV_MODE_REQ",
    0x2242  : "ID_CPROC_1X_SM_DM_SET_DIV_MODE_CNF",
}

def get_cproc_1x_internal_msg_str( MsgId, usVersion):
    for MsgIdIndex in cproc_1x_internal_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return cproc_1x_internal_msg_enum_table[MsgIdIndex]

    return "unknown"
