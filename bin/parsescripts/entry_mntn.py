#!/usr/bin/python
# -*- coding: UTF-8 -*-

#打开xml文档
import os
import sys
import string
import struct
import config
#from config import *


def cur_file_dir():
    #print('syspath:')
    #print(sys.path)
    #print('cwd:')
    #print(os.getcwd())
    #print('realpath')
    #print(os.path.realpath(__file__))
    #print('splitpath')
    #print(os.path.split(os.path.realpath(__file__))[0])
    #path = sys.path[0]
    #if os.path.isdir(path):
    #    return path
    #elif os.path.isfile(path):
    #    return os.path.dirname(path)
    return os.path.split(os.path.realpath(__file__))[0]

class entry_parse:
    def __init__(self):
        self.python_file = ''
        self.file_dir = ''
        self.params_dict = {}
        return
    
    def append_dump_scrits(self):
        #define config file
        path = sys.path[0] 
        if os.path.isdir(path): 
            top_dir = path 
        elif os.path.isfile(path): 
            top_dir = os.path.dirname(path) 
        #top_dir = top_dir.decode().replace(top_dir, '//', '/')
        sys.path.append(top_dir)
        file_path = top_dir + '/config/field_' + str(self.params_dict['field'])
        sys.path.append(file_path)
        self.python_file = 'python_file'
        return

    def get_input_output_handler(self):
        #try to pen out file
        outfile_handler = self.params_dict['outfile']
        params_dict = self.params_dict
        file_handler = {'outfile':outfile_handler}
        return file_handler

    def call_function(self):
        self.file_dir = cur_file_dir()
        field = self.params_dict['field']
        version = self.params_dict['version']
        field_dir = self.file_dir+ '/config/field_' + field
        if not os.path.exists(field_dir):
            print(field_dir)
            return config.error['ERR_NO_FIELD_SCRIPTS']

        import_file = "import field_%s_%s" % (field,version[2:])#'import field_' + field + '_' + version[2:]
        print(import_file)

        if (field == '0x200000C') or (field == '0x2200000'):
            function = "ret = field_%s_%s.entry_%s(self.params_dict['infile'], self.params_dict['field'], self.params_dict['offset'], self.params_dict['len'], self.params_dict['version'], self.params_dict['mode'], self.params_dict['outfile'], self.params_dict['field_list'])" % (field, version[2:], field)
        else:
            function = "ret = field_%s_%s.entry_%s(self.params_dict['infile'], self.params_dict['field'], self.params_dict['offset'], self.params_dict['len'], self.params_dict['version'], self.params_dict['mode'], self.params_dict['outfile'])" % (field, version[2:], field)
            
        #if  (field == '0x220000A') or (field == '0x2200006'):
        #    self.params_dict['outfile'].writelines('暂不支持解析')
        #    return 0
        #sys.path.append(field_dir+'\\')
        try:
            print("import field ing")
            #print(sys.path)
            exec(import_file)
        except Exception as e:
            self.params_dict['outfile'].writelines("%s fail\n" % import_file)
            return 9
        else:
            try:
                print("exec function ing")
                print(self.params_dict)
                exec(function)
                print("exec function done")
                return 0
            except Exception as e:
                self.params_dict['outfile'].writelines("%s fail\n" % function)
                print("exec function except")
                return 1

    def entry_mntn(self):
        ret = config.error['ERR_OTHER']
        #do something before exparse
        params_dict=self.params_dict
        self.append_dump_scrits()
        python_file = self.python_file
        file_handler = self.get_input_output_handler()
        if file_handler == config.error['ERR_OPEN_OUTFILE']:
            return file_handler
        self.params_dict['outfile'] = file_handler['outfile']
        #file_handler['outfile'].writelines('###########[parse  start]##########\n')
        
        if config.error['ERR_OPEN_OUTFILE'] == file_handler or config.error['ERR_OPEN_INFILE'] == file_handler:
            return file_handler
        if 'print' in list(params_dict.keys()):
            file_handler['print']=open( params_dict['print'],'w')
            sys.stdout=file_handler['print']
        if 'error' in list(params_dict.keys()):
            file_handler['error']=open(params_dict['error'],'w')
            sys.stderr=file_handler['error']
        #重定向log输出
        if 'log' in list(params_dict.keys()):  
            file_handler['log']=open(params_dict['log'],'w')
            sys.stdout=file_handler['log']
            sys.stderr=file_handler['log']
        print("================field %s enter================" % (params_dict['field']))
        if 'field_list' in params_dict:
            field_list = params_dict['field_list']
        else:
            field_list = None
        if params_dict['mode'] in config.modeList:
            try:
                ret = self.call_function()
                print(ret)
            except IOError as e:
                print("error in ", params_dict['field'])
        else:
            print("ok in file python_file\n")
        #file_handler['outfile'].writelines('\n###########[parse    end]##########\n')
        file_handler['outfile'].close
        if 'print' in list(params_dict.keys()):
            file_handler['print'].close
        if 'error' in list(params_dict.keys()):
            file_handler['error'].close
        #调用模块无返回值，默认处理成功
        if ret is None:
            ret = config.error['ERR_SUCCESS']
        print("================field %s ret %d================" % (params_dict['field'], ret))
        return ret

class area_base:
    def __init__(self):
        self.list_area = []
        self.path = ''
        self.dirs = []
        return
        
    def global_area(self,area_offset,inhander):
        if inhander == None:
            print("file did not open\n")
            return
        #seek to area info
        magic,=struct.unpack("I", inhander.read(4))
        #if not magic==0x44656164 || not magic==0x4E524D53:
        #    print("magic is error 0x%x" % magic)
        #    return
        version,=struct.unpack("I", inhander.read(4))
        area_num,=struct.unpack("I", inhander.read(4))
        
        inhander.seek(area_offset,0)#inhander.seek(232,0)
        for i in range(area_num):
            offset,=struct.unpack("I", inhander.read(4))
            length,=struct.unpack("I", inhander.read(4))
            areainfo={           
                'name':config.get_core_name(1<<i),
                'offset':int(offset),
                'length':int(length),
                'coreid':(1<<i)
            }
            if i == 0:
                dumploadbase = int(offset)
            dumploadbase += int(length)
            print(areainfo)
            #print(config.mntnbase)
            self.list_area.append(areainfo)
        dumploadbase += 1036
        print(dumploadbase)
        inhander.seek(dumploadbase,0)
        config.mntnbase = struct.unpack("I", inhander.read(4))
        print(config.mntnbase)
        return
        
    def get_dirs(self):
        self.path = cur_file_dir() + "/config"
        path = self.path
        if not os.path.isdir(path):
            print(path+" is not exist")
            return
        my_dirs = os.listdir(path)
        for eachdir in my_dirs:
            if os.path.isdir(path + '/' + eachdir):
                self.dirs.append(eachdir)
        return

class parse_base:
    def __init__(self):
        self.list_field = []
        self.list_field_id = []
        return
		
    def global_field(self,inhander,order,list_area):
        self.list_field = []
        if list_area == None or inhander == None:
            print("list_area or inhander is invaild\n")
            print(list_area)
            print(inhander)
            return
        areainfo = list_area[order]
        off=int(areainfo['offset'])
        inhander.seek(off)
        magic,      =   struct.unpack('I', inhander.read(4))
        if magic != 0x4e656464:
            print("%x" % magic)
            print(areainfo['name'])
        field_num,area_name,  =   struct.unpack('I8s',inhander.read(12))
        one,two, = struct.unpack('qq',inhander.read(16))
        for i in range(0,field_num):
            field,  =   struct.unpack('I',inhander.read(4))
            t_off,  =   struct.unpack('I',inhander.read(4))
            offset  =   t_off + off
            length,  =   struct.unpack('I',inhander.read(4))
            version, =   struct.unpack('I',inhander.read(4))
            temp_name,    =   struct.unpack('16s',inhander.read(16))
            fieldinfo={
                'field':field,
                'offset':offset,
                'length':length,
                'version':version&0xFFFF,
                'name':temp_name.decode().strip("\x00")
                }
            self.list_field.append(fieldinfo)
            print(fieldinfo)
        return

    def fieldparse(self, dirs):
        self.list_field_id = []
        if self.list_field == None:
            print("list_field is invaild\n")
            return
        if dirs == None:
            print("dirs is invaild")
            return
        for eachfield in self.list_field:
            field = int(eachfield['field'])
            field_str = str(hex(field))[2:].upper()
            field_name = 'field_0x' + field_str
            if field_name in dirs:           
                self.list_field_id.append(eachfield)
        return

    def entry_module(self,dirs,infile, version, mode, outfile, field_list):
        try:
            parse = entry_parse()
            ret = 0
            if dirs == None:
                print('dirs is null')
                return 1
            else:
                self.fieldparse(dirs)
                if self.list_field_id == None:
                    print("fieldparse faild\n")
                    return 1
            for eachlist in self.list_field_id:
                field_str = '0x' + str(hex(eachlist['field']))[2:].upper()
                offset_str = '0x' + str(hex(eachlist['offset']))[2:].upper()
                length_str = '0x' + str(hex(eachlist['length']))[2:].upper()
                version_str = "%s%04x" % ('0x',eachlist['version'])                
                #version_str = "%s%04x" % ('0x',version)
                mode_str = str(mode)
                length_str = '0x' + str(hex(eachlist['length']))[2:].upper()
                if (field_str == '0x200000C') or (field_str == '0x2200000'):
                    field_list = '0x' + str(hex(config.errmodid))[2:].upper()
                    print("field_list:", field_list)
                    print("errmodid:", config.errmodid)
                #outfile_str = '%s%s%s%s' % (outfile, '\\', str(eachlist['name']), r'.txt')
                parse.params_dict = {'infile':infile, 'field':field_str, 'offset':offset_str, 'len':length_str, 'version':version_str, 'mode':mode_str, 'outfile':outfile, 'field_list':field_list}
                ret |= parse.entry_mntn()
                print("ret = %u" % ret)
            return ret
        except IOError as e:
            print("rdr parse faild:", e)
            return config.error['ERR_OTHER']    
	
def entry(area_offset,infile,outfile,version,mode=1,field_list=None):
    try:
        ret = 0
        
        if infile == None:
            return 4
        infile.seek(0)
        areabase = area_base()
        areabase.get_dirs() #add path of field to sys.path
        areabase.global_area(area_offset,infile)
        list_area = areabase.list_area
        print("entry  gloabal_area done.\n")
        parsebase = parse_base()
        print("entry  parse_base done.\n")
        parsebase.global_field(infile, config.core_order['CP'],list_area)
        ret |= parsebase.entry_module(areabase.dirs, infile, version, mode, outfile, field_list)
        print("entry  parse cp done.\n")
        parsebase.global_field(infile, config.core_order['MODEMAP'],list_area)
        ret |= parsebase.entry_module(areabase.dirs, infile, version, mode, outfile, field_list)
        print("entry  parse cp done.\n")

        return
    except IOError as e:
        print("rdr parse faild:", e)
        return config.error['ERR_OTHER']
