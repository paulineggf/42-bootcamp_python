from decimal import Decimal

t = (0, 4 , 132.42222, 10000, 12345.67)

print ('day_', str(t[0]).zfill(2), ', ', sep='', end='')
print ('ex_', str(t[1]).zfill(2), ' : ', sep='', end='')
print ('%.2f, ' % float(t[2]), end='')
print ('%.2e' % Decimal(str(t[3])), ', ', sep='', end='')
print ('%.2e' % Decimal(str(t[4])), sep='')

