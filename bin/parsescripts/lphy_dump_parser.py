import struct
import os

def entry_lphy_dump_parser(infile, outfile):
    addr = 0
    row = 0
    
    output_fd = open(outfile, 'w')
    input_fd = open(infile, 'rb+')
    filelen = os.path.getsize(infile)
    print("infile " + infile + "outfile " + outfile)
    while input_fd.tell() < filelen:
        str1 = input_fd.read(4)
        str2 = input_fd.read(4)
        str3 = input_fd.read(4)
        str4 = input_fd.read(4)
        charbyte1 = 0
        charbyte2 = 0
        charbyte3 = 0
        charbyte4 = 0
        if len(str1) != 0:
            (charbyte1, ) = struct.unpack("I", str1)
        if len(str2) != 0:
            (charbyte2, ) = struct.unpack("I", str2)
        if len(str3) != 0:
            (charbyte3, ) = struct.unpack("I", str3)
        if len(str4) != 0:
            (charbyte4, ) = struct.unpack("I", str4)
        addr = 0x10 * row
        row = row + 1
        output_fd.writelines("0x%08x: %08x %08x %08x %08x\n" %(addr, charbyte1, charbyte2, charbyte3, charbyte4))
    return 0
