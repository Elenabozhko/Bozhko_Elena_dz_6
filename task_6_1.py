with open('nginx_logs.txt') as f:
   num = []
   for line in f:
       splitted = line.split()
       num.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
print(num)