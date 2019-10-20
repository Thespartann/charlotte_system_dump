#######################################################################################################################################
#   filename        :   exparse_python_frame.py
#
#   author          :   fuxin 00221597
#
#   description     :   exparse python sripts frame 
#
#   modify  record  :   2014-07-21 create file
#
#######################################################################################################################################
import struct
import os
import sys
import string
from config import *

def get_params_dict(my_argv):
    params_dict = {}
    params_string = ""
    for p in my_argv:
        if p.find('=') != -1:
            subs = p.split('=')
            params_dict[subs[0]] = subs[1]
        else:
            params_dict[p] = ""
    print(params_dict)
    return params_dict

def append_dump_scrits(params_dict):
    #define config file
    path = sys.path[0] 
    if os.path.isdir(path): 
        top_dir = path 
    elif os.path.isfile(path): 
        top_dir = os.path.dirname(path) 
    sys.path.append(top_dir)
    file_path = top_dir + '/config/field_' + str(params_dict['field'])
    sys.path.append(file_path)
    print(sys.path)
    return 'python_file'

def get_input_output_handler(params_dict):
    infile_name = params_dict['infile']
    outfile_name = params_dict['outfile']

    #try to open infile
    try:
        infile_handler = open(infile_name, 'rb')
    except IOError as e:
        print("file open error:%s" %(e))
        return error['ERR_OPEN_INFILE']
    else:
        print("open infile %s OK\n" %(infile_name))
    #try to pen out file
    try:
        if params_dict['mode'] == '0' :
            outfile_handler = open(outfile_name, 'a')
        else:
            outfile_handler = open(outfile_name, 'w')
    except IOError as e:
        print("file open error:%s" %(e))
        return error['ERR_OPEN_OUTFILE']
    else:
        print("open outfile %s OK\n" %(outfile_name))
        if params_dict['mode'] == 'c':
            return {'infile': NULL, 'outfile':outfile_handler}
    file_handler = {'infile':infile_handler, 'outfile':outfile_handler}
    return file_handler

def cur_file_dir(): 
    path = sys.path[0] 
    if os.path.isdir(path): 
        return path
    elif os.path.isfile(path): 
        return os.path.dirname(path) 

def call_function(infile, field, offset, len, version, mode, outfile, field_list):
    field_dir = cur_file_dir() + '/config/field_' + field
    print(field_dir)
    if not os.path.exists(field_dir):
        #print('field not exist?')
        return error['ERR_NO_FIELD_SCRIPTS']
    import_file = 'import field_' + field + '_' + version[2:]
    print(import_file)
    if (field == '0x200000C') or (field == '0x2200000'):
        function = 'ret = ' + 'field_' + field + '_' + version[2:] + '.' + 'entry_' + field + '(infile, field, offset, len, version, mode, outfile, field_list)'
    else:
        function = 'ret = ' + 'field_' + field + '_' + version[2:] + '.' + 'entry_' + field + '(infile, field, offset, len, version, mode, outfile)'
    print(function)
    exec(import_file)
    exec(function)
    return error['ERR_SUCCESS']

def main():
    ret = error['ERR_OTHER']
    my_argv = sys.argv[1:]
    if len(my_argv) == 0:
        print("argv lenth = 0\n")
        return error['ERR_PARAMS_ERROR']
    #do something before exparse
    params_dict = get_params_dict(my_argv)
    python_file = append_dump_scrits(params_dict)
    file_handler = get_input_output_handler(params_dict)
    if error['ERR_OPEN_OUTFILE'] == file_handler or error['ERR_OPEN_INFILE'] == file_handler:
        return file_handler
    if 'print' in params_dict.keys():
        file_handler['print']=open( params_dict['print'],'w')
        sys.stdout=file_handler['print']
    if 'error' in params_dict.keys():
        file_handler['error']=open(params_dict['error'],'w')
        sys.stderr=file_handler['error']
    if 'log' in params_dict.keys():  
        file_handler['log']=open( params_dict['log'],'w')
        sys.stdout=file_handler['log']
        sys.stderr=file_handler['log']
    print("================field %s enter================" % (params_dict['field']))
    if 'field_list' in params_dict:
        field_list = params_dict['field_list']
        #print("field list exist")
    else:
        field_list = None
        #print("field not exist")
    if params_dict['mode'] in modeList:
        try:
            ret = call_function(file_handler['infile'], params_dict['field'], params_dict['offset'], params_dict['len'], params_dict['version'], params_dict['mode'], file_handler['outfile'], field_list)
        except IOError as e:
            print ("error in " + params_dict['field'])
    else:
        print("ok in file python_file\n")
    file_handler['infile'].close
    file_handler['outfile'].close
    if 'print' in params_dict.keys():
        file_handler['print'].close
    if 'error' in params_dict.keys():
        file_handler['error'].close
    if ret is None:
        ret = error['ERR_SUCCESS']
    print("================field %s ret %d================" % (params_dict['field'], ret))
    return ret

if __name__ == '__main__':
    main()
