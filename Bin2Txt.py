import os
import argparse
import struct

def transfer_Bin2Txt(a_input_bin, a_output_txt, a_byte_per_line):
  # a_byte_per_line = 4
  byte_per_line = int(a_byte_per_line, 10)
  Txt = open(a_output_txt, 'w')
  Bin = open(a_input_bin, 'rb')
  Entry = 0
  # with open(a_input_bin, 'rb') as Bin:
  length = len(Bin.read())
  Bin.seek(0)
  for i in xrange(0, length):
    buf = Bin.read(1)
    Entry = Entry | (struct.unpack("B", buf)[0] << 8*(i%byte_per_line))
    
    if i % byte_per_line == byte_per_line-1:
      # print "%X" % Entry
      if byte_per_line == 1:
        Txt.write('{0:02X}\n'.format(Entry))
      elif byte_per_line == 2:
        Txt.write('{0:04X}\n'.format(Entry))
      elif byte_per_line == 4:
        Txt.write('{0:08x}\n'.format(Entry))
      elif byte_per_line == 8:
        Txt.write('{0:016X}\n'.format(Entry))
      else:
        print "Not support output %d byte per line." % byte_per_line
      
      Entry = 0
    else:
      if i == length-1:
        if byte_per_line == 1:
          Txt.write('{0:02X}\n'.format(Entry))
        elif byte_per_line == 2:
          Txt.write('{0:04X}\n'.format(Entry))
        elif byte_per_line == 4:
          Txt.write('{0:08x}\n'.format(Entry))
        elif byte_per_line == 8:
          Txt.write('{0:016X}\n'.format(Entry))
        else:
          print "Not support output %d byte per line." % byte_per_line


if __name__ == "__main__":
    # Create argument of this application by argparse.
    parser = argparse.ArgumentParser(description="Transfer Binary File to Text File")
    parser.add_argument("Input_bin_path",           help="Input binary file full path.")
    parser.add_argument("Output_txt_path",          help="Output text file full path.")
    parser.add_argument("Output_txt_byte_per_line", help="Output text file byte per line. Support 1,2,4,8 byte.")

    args = parser.parse_args()
    
    transfer_Bin2Txt(args.Input_bin_path, args.Output_txt_path, args.Output_txt_byte_per_line)

