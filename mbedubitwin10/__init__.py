import os, sys
import patch
import mbed
from os.path import abspath, dirname, join

PATCH_FOLDER=dirname(abspath(__file__))

def main():
    save_cwd = os.getcwd()
    os.chdir(dirname(abspath(mbed.__file__)))
    print(os.getcwd())

    cmd = '%s %s "%s"' % (sys.executable, patch.__file__, join(PATCH_FOLDER,"mbed_chunk.patch"))
    print(cmd)
    os.system(cmd)

    os.chdir(save_cwd)
    print(os.getcwd())

    cmd_list = [
        "mbed config root .",
        "mbed target NRF51_MICROBIT",
        "mbed toolchain GCC_ARM",

        "@echo http://mbed.org/users/mbed_official/code/mbed/builds/87f2f5183dfb > mbed.bld",
        "mbed deploy",
        
        "mbed add https://developer.mbed.org/teams/Lancaster-University/code/microbit/",
        "mbed add http://os.mbed.com/teams/Lancaster-University/code/mbed-src/",
        
        "copy /Y .\\microbit\\microbit-dal\\source\\asm\\CortexContextSwitch.s.gcc .\\microbit\\microbit-dal\\source\\asm\\CortexContextSwitch.s",

        "rmdir /s /q mbed",
    ]
    for cmd in cmd_list:
        print(cmd)
        os.system(cmd)

    patch_file_list = ["has_key.patch", "sdk_ble_h.patch"]
    for patch_file in patch_file_list:
        cmd = '%s %s "%s"' % (sys.executable, patch.__file__, join(PATCH_FOLDER,patch_file))
        print(cmd)
        os.system(cmd)
