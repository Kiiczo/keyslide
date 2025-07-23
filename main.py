lower = ["`1234567890-=",
"qwertyuiop[]\\",
"asdfghjkl;'",
"zxcvbnm,./"]

upper = [
"~!@#$%^&*()_+",
"QWERTYUIOP{}|",
"ASDFGHJKL:",
"ZXCVBNM<>?"]

def encrypt(text, key):
    output = ""
    for letter in text:
        for i in lower:
            for j in range(len(i)):
                if i[j] == letter:
                    k = j + key
                    while k >= len(i):
                        k = k - len(i)
                    output+=i[k]
                    break
        for i in upper:
            for j in range(len(i)):
                if i[j] == letter:
                    k = j + key
                    while k >= len(i):
                        k = k - len(i)
                    output+=i[k]
                    break
    return output