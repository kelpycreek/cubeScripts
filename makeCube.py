import os, sys
from subprocess import call

if len(sys.argv) != 3:
    print("intake driectory, output filename")
    print(sys.argv)
    1/0
    
intake_dir = sys.argv[1]
out_file = open(sys.argv[2], 'w')

cmd = "ls " + intake_dir
clist = os.popen(cmd).read().split('\n')

counter = 0

for card in clist:
    filename = intake_dir + card
    out_file.write('<img src="{}" width="319" height="212">\n'.format(filename))
    if counter == 0:
        counter = 1
    else:
        out_file.write('<br>\n')
        counter = 0
