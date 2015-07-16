import sys

def is_linux():
    # Return True if os based on the Linux kernel's
    return sys.platform.startswith('linux')