import os
from pprint import pprint
import subprocess
from subprocess import Popen, PIPE

if __name__ == '__main__':
    cygwin_bin = "C:\\cygwin64\\bin\\"
    make = "make.exe"
    make_clean = "make.exe clean"
    cygwin_mintty = "C:\\cygwin64\\bin\\mintty.exe"
    cygwin_bash = "C:\\cygwin64\\bin\\bash.exe"

    # print(os.getcwd())
    # print(os.path.abspath(cygwin_path))
    # pprint(os.listdir(os.path.abspath(cygwin_path)))
    # pprint(os.system("dir"))
    # pprint(os.system(cygwin_bin + " --help"))
    # pprint(os.system(cygwin_bin + " /bin/bash"))
    # p = Popen(cygwin_bash, stdin=PIPE, stdout=PIPE)
    # p.stdin.write("echo $PWD")
    # p.stdin.write("echo $PATH")
    # p = Popen("cmd", stdin=PIPE, stdout=PIPE)
    #
    # p.stdin.write("dir")
    # p.stdin.close()
    # out = p.stdout.read()
    # pprint(out)
    # output = subprocess.check_output(['cmd', 'dir'])
    # output = os.system('cmd dir')
    # output = subprocess.call('', shell=True)
    # output = subprocess.call(cygwin_bin + "gcc.exe", shell=True)
    current_dir = os.path.dirname(__file__)
    p = subprocess.Popen(current_dir + "/Sleuth3/grow.exe")
    # p.communicate()
    # out = p.stdout.read()
    p.wait()
    # pprint(p.stdout.read())
    out, err = p.communicate()
    return_code = p.returncode
    pprint(current_dir + "/Sleuth3/grow.exe")
    pprint(out)
    pprint(err)
    pprint(return_code)
    pass
