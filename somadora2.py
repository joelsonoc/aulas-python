# somadora1.py - somadora infinita - versao 1

print 'Digite os valor a somar seguidos de .'
print 'Para encerrar digite : 0'
total = 0
while 1:
    n = float(raw_input(':'))
    if n == 0: break
    total = total + n
print 'TOTAL: %s' % total

