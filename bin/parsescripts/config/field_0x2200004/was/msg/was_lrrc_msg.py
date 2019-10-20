#######################################################################################################################################
#   filename        :   was_errc_msg.py
#
#   author          :   sunbing 00184266
#
#   description     :   list LRrcWRrcInterface.h
#
#   modify  record  :   2016-01-07 create file
#
#######################################################################################################################################

was_lrrc_msg_enum_table = {
0x1230 : "ID_LRRC_WRRC_CELL_RESEL_CNF",
0x1231 : "ID_LRRC_WRRC_CELL_RESEL_STOP_CNF",
0x1232 : "ID_LRRC_WRRC_REDIRECTED_CNF",
0x1233 : "ID_LRRC_WRRC_REDIRECTED_STOP_CNF",
0x1234 : "ID_LRRC_WRRC_HANDOVER_CNF",
0x1235 : "ID_LRRC_WRRC_HANDOVER_STOP_CNF",
0x1236 : "ID_LRRC_WRRC_SET_DSP_POWER_CNF",
0x1237 : "ID_LRRC_WRRC_GETUECAPINFO_CNF",
0x1238 : "ID_LRRC_WRRC_PLMN_SEARCH_CNF",
0x1239 : "ID_LRRC_WRRC_PLMN_SEARCH_STOP_CNF",
0x123a : "ID_LRRC_WRRC_IDLE_MEASURE_CNF",
0x123b : "ID_LRRC_WRRC_IDLE_MEASURE_IND",
0x123c : "ID_LRRC_WRRC_CONNECTED_MEASURE_CNF",
0x123d : "ID_LRRC_WRRC_CONNECTED_MEASURE_IND",
0x123e : "ID_LRRC_WRRC_RELALL_CNF",
0x123f : "ID_LRRC_WRRC_CELL_RESEL_REQ",
0x1240 : "ID_LRRC_WRRC_CELL_RESEL_STOP_REQ",
0x1241 : "ID_LRRC_WRRC_REDIRECTED_REQ",
0x1242 : "ID_LRRC_WRRC_REDIRECTED_STOP_REQ",
0x1243 : "ID_LRRC_WRRC_HANDOVER_REQ",
0x1244 : "ID_LRRC_WRRC_HANDOVER_STOP_REQ",
0x1245 : "ID_LRRC_WRRC_SET_DSP_POWER_REQ",
0x1246 : "ID_LRRC_WRRC_GETUECAPINFO_REQ",
0x1247 : "ID_LRRC_WRRC_IDLE_MEASURE_REQ",
0x1248 : "ID_LRRC_WRRC_CONNECTED_MEASURE_REQ",
0x124b : "ID_LRRC_WRRC_RELALL_REQ",
0x124c : "ID_LRRC_WRRC_CELL_SRCH_REQ",
0x124d : "ID_LRRC_WRRC_CELL_SRCH_STOP_REQ",
0x124e : "ID_LRRC_WRRC_BG_PLMN_SEARCH_REQ",
0x124f : "ID_LRRC_WRRC_BG_SEARCH_STOP_REQ",
0x1250 : "ID_LRRC_WRRC_BG_SEARCH_SUSPEND_REQ",
0x1251 : "ID_LRRC_WRRC_BG_SEARCH_RESUME_REQ",
0x1252 : "ID_LRRC_WRRC_BG_PLMN_SEARCH_CNF",
0x1253 : "ID_LRRC_WRRC_BG_PLMN_SEARCH_IND",
0x1254 : "ID_LRRC_WRRC_BG_SEARCH_STOP_CNF",
0x1255 : "ID_LRRC_WRRC_BG_SEARCH_SUSPEND_CNF",
0x1256 : "ID_LRRC_WRRC_BG_SEARCH_RESUME_CNF",
0x1257 : "ID_LRRC_WRRC_GET_W_CGI_REQ",
0x1259 : "ID_LRRC_WRRC_GET_CGI_STOP_REQ",
0x1260 : "ID_LRRC_WRRC_CAMP_PLMN_INFO_NTF",
0x1261 : "ID_LRRC_WRRC_AREA_LOST_NTF",
0x1262 : "ID_LRRC_WRRC_FR_INFO_CNF",
0x1263 : "ID_LRRC_WRRC_BG_PLMN_SEARCH_CSG_IND",
0x1264 : "ID_LRRC_WRRC_SEARCHED_PLMN_INFO_IND",
0x1270 : "ID_WRRC_LRRC_CELL_RESEL_REQ",
0x1271 : "ID_WRRC_LRRC_CELL_RESEL_STOP_REQ",
0x1272 : "ID_WRRC_LRRC_REDIRECTED_REQ",
0x1273 : "ID_WRRC_LRRC_REDIRECTED_STOP_REQ",
0x1274 : "ID_WRRC_LRRC_HANDOVER_REQ",
0x1275 : "ID_WRRC_LRRC_HANDOVER_STOP_REQ",
0x1276 : "ID_WRRC_LRRC_SET_DSP_POWER_REQ",
0x1277 : "ID_WRRC_LRRC_GETUECAPINFO_REQ",
0x1278 : "ID_WRRC_LRRC_PLMN_SEARCH_REQ",
0x1279 : "ID_WRRC_LRRC_PLMN_SEARCH_STOP_REQ",
0x127a : "ID_WRRC_LRRC_IDLE_MEASURE_REQ",
0x127b : "ID_WRRC_LRRC_CONNECTED_MEASURE_REQ",
0x127c : "ID_WRRC_LRRC_RELALL_REQ",
0x127d : "ID_WRRC_LRRC_CELL_RESEL_CNF",
0x127e : "ID_WRRC_LRRC_CELL_RESEL_STOP_CNF",
0x127f : "ID_WRRC_LRRC_REDIRECTED_CNF",
0x1280 : "ID_WRRC_LRRC_REDIRECTED_STOP_CNF",
0x1281 : "ID_WRRC_LRRC_HANDOVER_CNF",
0x1282 : "ID_WRRC_LRRC_HANDOVER_STOP_CNF",
0x1283 : "ID_WRRC_LRRC_SET_DSP_POWER_CNF",
0x1284 : "ID_WRRC_LRRC_GETUECAPINFO_CNF",
0x1285 : "ID_WRRC_LRRC_IDLE_MEASURE_CNF",
0x1286 : "ID_WRRC_LRRC_IDLE_MEASURE_IND",
0x1287 : "ID_WRRC_LRRC_CONNECTED_MEASURE_CNF",
0x1288 : "ID_WRRC_LRRC_CONNECTED_MEASURE_IND",
0x128c : "ID_WRRC_LRRC_RELALL_CNF",
0x128d : "ID_WRRC_LRRC_CELL_SRCH_CNF",
0x128e : "ID_WRRC_LRRC_CELL_SRCH_STOP_CNF",
0x128f : "ID_WRRC_LRRC_BG_PLMN_SEARCH_CNF",
0x1290 : "ID_WRRC_LRRC_BG_PLMN_SEARCH_IND",
0x1291 : "ID_WRRC_LRRC_BG_SEARCH_STOP_CNF",
0x1292 : "ID_WRRC_LRRC_BG_SEARCH_SUSPEND_CNF",
0x1293 : "ID_WRRC_LRRC_BG_SEARCH_RESUME_CNF",
0x1294 : "ID_WRRC_LRRC_BG_PLMN_SEARCH_REQ",
0x1295 : "ID_WRRC_LRRC_BG_SEARCH_STOP_REQ",
0x1296 : "ID_WRRC_LRRC_BG_SEARCH_SUSPEND_REQ",
0x1297 : "ID_WRRC_LRRC_BG_SEARCH_RESUME_REQ",
0x1298 : "ID_WRRC_LRRC_GET_W_CGI_CNF",
0x1299 : "ID_WRRC_LRRC_GET_W_CGI_IND",
0x12A2 : "ID_WRRC_LRRC_GET_CGI_STOP_CNF",
0x12A3 : "ID_WRRC_LRRC_FR_INFO_REQ",
0x12A4 : "ID_WRRC_LRRC_SEARCHED_PLMN_INFO_IND",
}

def get_was_lrrc_msg_str( MsgId):
    for MsgIdIndex in was_lrrc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return was_lrrc_msg_enum_table[MsgIdIndex]

    return "none"