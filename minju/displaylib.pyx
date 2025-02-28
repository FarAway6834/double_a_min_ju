DEF __MAIN__ = "__main__"
DEF NEWLINE = "\n"
DEF DOUBLE_A_SAFER = "double_a_safer "
DEF DOUBLE_A_DISPLAY = "echo "

cdef:
    str (*pystdinft)()
    void (*pystdoutft)(str)
    
    struct pystdiofst:
        pystdinft pystdin
        pystdoutft pystdout
    
    struct pystdlogformat:
       pystdoutft pystdout
       str x
    
    void linefeed(pystdoutft pystdout):
        pystdout(NEWLINE)
    
    void command_safer(pystdoutft pystdout):
        pystdout(DOUBLE_A_SAFER)
    
    void command_displayer(pystdoutft pystdout):
        pystdout(DOUBLE_A_DISPLAY)
    
    void pystdloger(pystdlogform pystdlogform):
         pystdlogform.pystdout(pystdlogform.x)
         linefeed(pystdlogform.pystdout)
    
    str rstriping(str x)
        str y
        y = x.strip()
        return y
    
    str rstriped_pystdin(pystdinft pystdin):
        str ret
        ret = pystdin()
        ret = rstriping(ret)
        return ret
    
    bool dose_it_entry_point(str __name__):
        bool is_entry_point
        is_entry_point = __MAIN__ == __name__
        return is_entry_point
     
    void double_a_checker_stdout_part(pystdlogformat pystdlogform):
        command_safer(pystdlogform.pystdout)
        pystdloger(pystdout)
        command_displayer(pystdlogform.pystdout)
        pystdloger(pystdout)
    
    void double_a_checker(pystdiofst pystdio):
        pystdlogformat pystdlogform
        pystdlogform.pystdout = pystdio.pystdout
        
        pystdlogform.x = rstriped_pystdin(pystdio.pystdin)
        double_a_checker_stdout_part(pystdio)
    
    void main(pystdinft pystdin, pystdoutft pystdout):
        pystdiofst pystdio
        pystdio = {pystdin, pystdout}
        double_a_checker(pystdio)
    
    void mainer(str __name__, pystdinft pystdin, pystdoutft pystdout):
        bool __name__is__main__
        __name__is__main__ = dose_it_entry_point(__name__)
        if __name__is__main__: main(pystdinft pystdin, pystdoutft pystdout)