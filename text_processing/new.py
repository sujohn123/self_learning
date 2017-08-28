import re
#for match in re.finditer(r':', 'a1b:2c3:d4'):
#   print(type(match.span()[0]))

line='abcd:fdfdsffff:sss'
#print(line.find(':'))

print(line[line.find(':')+1:len(line)])
