def apache404(file):
    with open(file, 'r')as f:
        for line in f.readlines():
            log_entry = line.split()
            if '404' in log_entry:
                print(log_entry[0])


apache404('apache2.log')
print()
apache404('apache.log')
