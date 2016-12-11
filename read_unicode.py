def find_utf16_string(addr):
  start = SegStart(addr)
  end = SegEnd(addr)
  addr = start
  while addr < end:
    if Word(addr) > 0x100:
    #read an unicode char
      bytes = GetString(addr, 2)
      try:
        comm = bytes.decode("utf-16")
        if type(comm) == unicode:
          comm = comm.encode("gbk")
          MakeComm(addr, comm)
      except Exception as e:
        pass
    addr = addr + 2

tofind = ["__ustring"]
seg = FirstSeg()
while seg != 0xffffffff:
  if SegName(seg) in tofind:
    find_utf16_string(seg)
  seg = NextSeg(seg)
