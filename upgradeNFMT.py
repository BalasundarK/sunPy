#! /usr/bin/python

import os
import sys
import subprocess


def isLoadExists(path, load):
    full_path = path + "/" + load
    try:
        if not os.path.exists(full_path):
            print
            "Load Not Found"
            return False

        else:
            print
            "Load Found"
            return True
    except IOError as ex:
        print
        "I/O error({0}): {1}".format(ex.errno, ex.strerror)
    except Error as ex:
        print
        "Error({0}): {1}".format(ex.errno, ex.strerror)
    return False


def execute(command, pwd):
    print(command)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=pwd)

    # Poll process for new output until finished
    while True:
        nextline = process.stdout.readline()
        if nextline == '' and process.poll() is not None:
            break
        sys.stdout.write(nextline)
        sys.stdout.flush()


path = "/alu/DEPOT/NR17.6/"

print("Enter the IT-Load to be upgraded: ")

load = raw_input()

pwd = "/alu/DEPOT/NR17.6/" + load

upPath = "/var/autoinstall/R17.6/"

if isLoadExists(path, load):
    print("Upgrade is in progress")
    execute("rpm -Uvh 1350OMS-MW_OS*rpm", pwd)
    execute("rpm -Uvh autoinstall*.noarch.rpm", pwd)
    execute("./1350OMS_upgrade.sh prefix=SNR176 depot=/alu/DEPOT/NR17.6/" + load, upPath)








