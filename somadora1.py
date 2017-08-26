# somadora1.py - somadora infinita - versao 1

print 'Digite os valor a somar seguidos de .'
print 'Para encerrar digite : 0'
n = float(raw_input(':'))
total = n
while n != 0:
    n = float(raw_input(':'))
    total = total + n
print 'TOTAL: %s' % total

