sent = input()
cros = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
num = 0
for cro in cros:
    if cro in sent:
        num += sent.count(cro)
        sent = sent.replace(cro, ' ')
sent = sent.replace(' ', '')
num += len(sent)
print(num)