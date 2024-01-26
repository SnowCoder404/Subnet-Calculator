import ipcalc
import sys

file = open('textdatei.txt', 'w')

for x in ipcalc.Network(sys.argv[1]):
    file.write(str(x))
    file.write('\n')
