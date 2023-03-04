log_file = 'Mar3LogStart.txt'
long_file = 'long.txt'

with open(log_file, 'r') as f:
    log_text = f.read()

with open(long_file, 'a') as f:
    f.write(log_text)
    f.write('\n')

with open(log_file, 'w') as f:
    f.write('')
