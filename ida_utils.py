def get_all_structs():
    #tranverse structures
    idx  = GetFirstStrucIdx()
    while idx != idaapi.BADADDR:
        sid = GetStrucId(idx)
        print "%d\t%x\t%s\t" % (idx, sid, GetStrucName(sid))  
        m = GetFirstMember(sid)
        while (m != -1 and m != idaapi.BADADDR):
            name = GetMemberName(sid, m)
            if name:
                print "\t+%x\t%x\t%s" % (m, GetMemberSize(sid, m), name)
            m = GetStrucNextOff(sid, m)    
        idx = GetNextStrucIdx(idx)

def get_all_localtypes():
    #traverse local types
    ml=GetMaxLocalType()
    for i in range(1, ml):
        print i, GetLocalType(i, 6)

def disasm_func(addr)
    #disassemble a function
    begin=GetFunctionAttr(addr,FUNCATTR_START)
    end=GetFunctionAttr(addr,FUNCATTR_END)
    while begin < end:
        print GetDisasm(begin)
        begin = begin + decode_insn(begin)
