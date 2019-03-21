#!c:\users\alberto\pycharmprojects\mysite\myvenv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'popper==2.0.1','console_scripts','popper'
__requires__ = 'popper==2.0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('popper==2.0.1', 'console_scripts', 'popper')()
    )
