import struct
import os

from config import *

def modemlogparse(logpath):
    ret = 0
    if logpath == "all":
        rootdir = '/data/hisi_logs/'
        if os.path.exists(rootdir):
            dirs = os.listdir(rootdir)
            for dirc in dirs:
                if os.path.isdir(rootdir + dirc) and dirc[:8].isdigit():
                    print(dirc)
                    parsesinglepath(rootdir + dirc + '/cp_log/')
        else:
            print("dir not exists")
    else:
        parsesinglepath(logpath)
    return ret

def parsesinglepath(logpath):
    ret = 0
    if os.path.exists(logpath + "DONE"):
        print('this directory already parse done')
        return ret
    for filetoparse in list(filedict.keys()):
        infile =  logpath + filetoparse
        outfile = logpath + filedict[filetoparse]
        print(("infile: " + infile))
        print(("outfile: " + outfile))
        if os.path.exists(infile):
            (filename,extension) = os.path.splitext(filetoparse)
            import_file = 'import ' + filename + '_parser'
            function = 'ret = ' + filename + '_parser' + '.' + 'entry_' + filename + '_parser' + '(infile, outfile)'
            exec(import_file)
            exec(function)
            ret = 0
        else:
            print((infile + "is not existed"))
            ret  = 1
    if ret == 0:
        os.mknod(logpath + "DONE")
    return ret




def main():
    if len(sys.argv) < 2:
        print("invalid argument")
        return
    else:
        logpath = sys.argv[1]

    for filetoparse in list(filedict.keys()):
        infile =  logpath + filetoparse
        outfile = logpath + filedict[filetoparse]
        print(("infile: " + infile))
        print(("outfile: " + outfile))
        if os.path.exists(infile):
            (filename,extension) = os.path.splitext(filetoparse)
            import_file = 'import ' + filename + '_parser'
            function = 'ret = ' + filename + '_parser' + '.' + 'entry_' + filename + '_parser' + '(infile, outfile)'
            exec(import_file)
            exec(function)
        else:
            print((infile + " is not existed"))

if __name__ == '__main__':
    main()

