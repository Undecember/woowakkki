import time

def parseOption():
    with open('power.cfg', 'r') as f:
        pw = f.read().split('\n')[0]
        if pw[:3] == 'max': return 1805
        res = int(pw[:-1])
        if pw[-1] == 'h': res *= 3600;
        if pw[-1] == 'm': res *= 60;
    return res

if __name__ == '__main__':
    while True:
        print(parseOption())
        time.sleep(2)
