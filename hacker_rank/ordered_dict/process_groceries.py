from collections import OrderedDict

n = int(raw_input().strip())

dicter = OrderedDict()
for _ in xrange(n):
    line = [elem for elem in raw_input().strip().split(" ") if elem != '']
    item_name = " ".join(line[:-1])
    net_price = int(line[-1])
    if item_name in dicter.keys():
        dicter[item_name] += net_price
    else:
        dicter[item_name] = net_price

for key in dicter.keys():
    print key,dicter[key]
