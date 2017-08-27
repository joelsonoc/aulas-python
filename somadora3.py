# somadora1.py - somadora infinita - versao 1

print 'Digite os valor a somar seguidos de .'
print 'Para encerrar digite : 0'
total = 0
while 1:
    try:
        n = float(raw_input(':'))
        total = total + n
    except:
        break
print 'TOTAL: %s' % total

