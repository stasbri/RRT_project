import os
os.system('rm src/logs')


def log(*args):
    s = ''
    for i in args:
        s += str(i) + ' '
    os.system(f'echo {s} >> src/logs')
