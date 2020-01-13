#!/usr/bin/env python3

'''
Author: Nick Ascoli
Credits: Kevin Foster (pefile logic), Steve Miller (inspiration)
'''

import pefile
import os
import sys
import csv
import string
import re
import pandas
import argparse
import numpy as np
from time import sleep
from datetime import datetime
from termcolor import colored, cprint

# ----------------------------------------
# INTRO TEXT
# ----------------------------------------

cprint("\n  )' .                                                                                      ",
       'yellow', file=sys.stderr)
cprint("  /    \      (\-./                                                                         ",
       'yellow', file=sys.stderr)
cprint(" /     |    _/ o. \                ___   ___   ___         ___   ___   ___   ___   ___       ",
       'yellow', file=sys.stderr)
cprint("|      | .-'      y)-             |   |   | |   | | |     |   | |       |   |     |   |     ",
       'yellow', file=sys.stderr)
cprint("|      |/       _/ \ __,_____     |-+-    + |   +-  |     |-+-|  -+-    +   |-+-  |-+-      ",
       'yellow', file=sys.stderr)
cprint("\     /j   _'.\(@)  / __.==--'    |       | |   | | |     |   |     |   |   |     |  \      ",
       'yellow', file=sys.stderr)
cprint(" \   ( |    `.''  )/#(-'          |      ---   ---   ---         ---         ---             ",
       'yellow', file=sys.stderr)
cprint("  \  _`-     |   / `-'                                                                      ",
       'yellow', file=sys.stderr)
cprint("    '  `-._  <_ (                                                                           ",
       'yellow', file=sys.stderr)
cprint("          `-.                                                                               \n",
       'yellow', file=sys.stderr)

# ----------------------------------------
# ESTABLISH ARGS
# ----------------------------------------

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--samples",
                    help="Specify the location of your samples", required=True)
parser.add_argument(
    "-o", "--output", help="Specify the location for your csv output", required=True)
parser.add_argument(
    "-p", "--pause", help="Specify a sleep interval for every 500 files (default is 0)", default=0.0, type=float)
parser.add_argument(
    "-u", "--users", help="Print discovered usernames", action='store_true')
parser.add_argument(
    "-r", "--repeats", help="Check for PDB and username repeats across samples", action='store_true')
parser.add_argument(
    "--summary", help="Print a sumamry of samples with PDB paths", action='store_true')
parser.add_argument(
    "--sherlock", help="Run discovered usernames through sherlock username checker", action='store_true')
args = parser.parse_args()

if args.sherlock and not args.users:
    parser.error('-u or --users is required for sherlock')
    sys.exit(1)

if args.samples:
    # ----------------------------------------
    # ASSIGN ARGS TO VARIABLES
    # ----------------------------------------

    directory = args.samples
    outputs = args.output
    pause = args.pause
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    output = "output"+now+".csv"

    # ----------------------------------------
    # CREATE OUTPUT FILE
    # ----------------------------------------

    f = open(outputs+'/'+output, "w+")
    f.write("file,pdbname,username\n")

    # ----------------------------------------
    # COUNT FILES
    # ----------------------------------------

    path, dirs, files = next(os.walk(directory))
    file_count = len(files)
    cprint("\nPulling PDB path from "+str(file_count) +
           " samples!", 'white', file=sys.stderr)

    # ----------------------------------------
    # DISPLAY OUTPUT
    # ----------------------------------------

    cprint("Output saved to: "+outputs+output,
           'white', file=sys.stderr)

    # ----------------------------------------
    # PULL PDB PATHS
    # ----------------------------------------

    paths = []
    status = 0
    for filename in os.listdir(directory):

        file = (os.path.join(directory, filename))
        status += 1

        if((status % 500) == 0):
            sleep(pause)
            sys.stdout.write('\rProcessing File: ' +
                             str(status) + ' of ' + str(file_count))
        if(status == file_count):
            sys.stdout.write('\rProcessing File: ' +
                             str(status) + ' of ' + str(file_count))
        try:
            pe = pefile.PE(file, fast_load=True)
            rva = pe.OPTIONAL_HEADER.DATA_DIRECTORY[6].VirtualAddress
            size = pe.OPTIONAL_HEADER.DATA_DIRECTORY[6].Size
            INFO = pe.parse_debug_directory(rva, size)

            for i in INFO:
                try:
                    pdbname = i.entry.PdbFileName
                    if(pdbname is not None):
                        f = open(outputs+output, "a+")
                        pdbnameStr = str(pdbname)
                        pdbnameStr = pdbnameStr[2:]
                        pdbnameClean = pdbnameStr.rstrip('\x00')
                        f.write(filename+",")
                        f.write(pdbnameClean)
                        hasUser = re.search(
                            '(?i)Users\\\\(.+?)\\\\', pdbnameClean)
                        if hasUser:
                            username = hasUser.group(1)
                            username = username[1:]
                            f.write(","+username)
                        f.write("\n")
                        f.close()
                        paths.append(pdbnameClean)
                except:
                    pass
        except:
            pass

# ----------------------------------------
# PRINT CSV
# ----------------------------------------

if args.summary:
    cprint("\n\n--------------------FILENAMES WITH PDB PATHS--------------------",
           'cyan', file=sys.stderr)
    df = pandas.read_csv(outputs+'/'+output)
    cprint(df, 'cyan', file=sys.stderr)

# ----------------------------------------
# PRINT PDB AND USERNAME REPEATS
# ----------------------------------------

if args.repeats:
    dfPDB = pandas.read_csv(outputs+'/'+output)
    cprint("\n\n--------------------PDB PATH REPEATS--------------------",
           'cyan', file=sys.stderr)
    pdbRepeats = pandas.concat(
        g for _, g in dfPDB.groupby("pdbname") if len(g) > 1)
    pdbRepeats = pdbRepeats[['pdbname', 'file', 'username']]
    pdbRepeats.loc[pdbRepeats.duplicated(subset=['pdbname']), [
        'pdbname']] = ""
    pdbRepeatsClean = pdbRepeats.to_string(index=False)
    cprint(pdbRepeatsClean, 'cyan', file=sys.stderr)

    dfUser = pandas.read_csv(outputs+'/'+output)
    cprint("\n\n--------------------USERNAME REPEATS--------------------",
           'cyan', file=sys.stderr)
    usernameRepeats = pandas.concat(
        g for _, g in dfUser.groupby("username") if len(g) > 1)
    usernameRepeats = usernameRepeats[['username', 'pdbname', 'file']]
    usernameRepeats.loc[usernameRepeats.duplicated(subset=['username']), [
        'username']] = ""
    usernameRepeatsClean = usernameRepeats.to_string(index=False)
    cprint(usernameRepeatsClean, 'cyan', file=sys.stderr)


# ----------------------------------------
# PRINT USERNAMES
# ----------------------------------------

if args.users:
    uNames = []
    cprint("\n--------------------USERNAMES FOUND--------------------",
           'green', file=sys.stderr)
    with open(outputs+'/'+output, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            user = row['username']
            if user is not None:
                if user not in uNames:
                    uNames.append(user)
            line_count += 1

    for i in uNames:
        cprint(" - "+i+"\n", 'green', end='')
    print("")

# ----------------------------------------
# RUN SHERLOCK
# ----------------------------------------

if args.sherlock:
    input1 = ""
    while input1 != "done":
        cprint(
            "Enter the usernames you would like to remove from search: ('done' to end)")
        try:
            input1 = input()
            uNames.remove(input1)
            cprint("[-] "+input1+" removed", 'red')
            cprint("\nCurrent Name List: ", 'green')
            for i in uNames:
                cprint(" - "+i+"\n", 'green', end='')
            continue
        except:
            continue
        else:
            break
    os.chdir("sherlock")
    namesForSherlock = ' '.join(map(str, uNames))
    os.system("python3 sherlock.py "+namesForSherlock)

print("")
