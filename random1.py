"""
Password string pwd
"""
pwd0 = "1110011000" #3
pwd1 = "100110" #3
pwd2 = "101011" #2

def check(pair):
    return pair[0] == pair[1]

def getMinFlips(pwd):
    counter = 0
    for i in range(1,len(pwd), 2):
        if not check((pwd[i-1], pwd[i])):
            counter += 1
    return counter


print(getMinFlips(pwd0))
print(getMinFlips(pwd1))
print(getMinFlips(pwd2))
