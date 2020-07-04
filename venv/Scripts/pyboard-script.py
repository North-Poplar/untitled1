#!C:\Users\18505\PycharmProjects\untitled1\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'rshell==0.0.28','console_scripts','pyboard'
__requires__ = 'rshell==0.0.28'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('rshell==0.0.28', 'console_scripts', 'pyboard')()
    )
