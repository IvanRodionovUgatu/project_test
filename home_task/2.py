s = input()
first_h = s.find('h')
last_h = s.rfind('h')

res = s[:first_h + 1] + s[first_h + 1:last_h].replace('h', 'H') + s[
                                                                  last_h:] if first_h != -1 and first_h != last_h else s
print(res)
