phone = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}
digitele = []
def findPhoneNumber(digits):
    for i in range(len(digits)):
        digitele.append(phone[digits[i]])
    return digitele
def searchPhone(digitele, j):
    if len(temp) == len(digitele):
        result.append(temp[:])
        return
    for i in range(0, len(digitele[j])):
        temp.append(digitele[j][i])
        searchPhone(digitele, j+1)
        temp.pop()
    
temp = []
result = []
print(findPhoneNumber("567"))
searchPhone(digitele, 0)
print(result)