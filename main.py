import ipcalc

data = input('Geben sie eine IP mit Subnet ein\n')
file = open('textdatei.txt', 'w')

for x in ipcalc.Network(data):
    file.write(str(x))
    file.write('\n')
