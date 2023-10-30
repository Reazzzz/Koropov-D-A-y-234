
def proverka(num):
    digs = [int(dig) for dig in str(num)]
    for dig in digs:
        if dig == 0 or num % dig != 0:
            return False
    return True
def poisk(n):
    for num in range(1, n + 1):
        if poisk(num):
            print(num)
poisk(100)
