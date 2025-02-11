def collatz(number):
    if number % 2 != 1:
        print(number // 2)
        return number // 2
    else:
        print(3*number+1)
        return 3*number+1

testnum = 703
while testnum != 1:
    testnum = collatz(testnum)
