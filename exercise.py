file = open('ramayana.txt', 'r')
stuff = file.read()
file.close()
rama = stuff.count('Rama')
sita = stuff.count('Sita')
hanuman = stuff.count('Hanuman')
laxman = stuff.count('Laxman')
bharat = stuff.count('Bharat')

out = open('out.txt', 'w')
out.write("'Rama': " + str(rama) + '\n')
out.write("'Sita': "  + str(sita) + '\n')
out.write("'Hanuman': " + str(hanuman)  + '\n')
out.write("'Laxman': " + str(laxman) + '\n')
out.write("'Bharat': " + str(bharat) + '\n')
out.close()
