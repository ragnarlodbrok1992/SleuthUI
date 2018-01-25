import os
from pprint import pprint
import subprocess

if __name__ == '__main__':
    cygwin_bin = "C:\\cygwin64\\bin\\"
    make = "make.exe"
    make_clean = "make.exe clean"
    cygwin_mintty = "C:\\cygwin64\\bin\\mintty.exe"
    cygwin_bash = "C:\\cygwin64\\bin\\bash.exe"

    current_dir = os.path.dirname(__file__)
    grow_dir = current_dir + "/Sleuth3/"
    grow_exe_dir = grow_dir + "grow.exe"
    scenario_dir = grow_dir + "Scenarios/"
    pprint(grow_dir)
    pprint(scenario_dir)
    pprint(os.getcwd())
    pprint(os.path.exists(scenario_dir))
    os.chdir(scenario_dir)
    p = subprocess.Popen("../grow.exe calibrate scenario.gdansk_fun1")
    p.wait()
    out, err = p.communicate()
    return_code = p.returncode
    pprint(out)
    pprint(err)
    pprint(return_code)
