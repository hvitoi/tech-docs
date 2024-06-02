# %%
import sys
import termios

termios.tcflush(sys.stdin, termios.TCIFLUSH)
