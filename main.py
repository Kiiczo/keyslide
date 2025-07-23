lower = [
['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'"],
['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']]

upper = [
['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+'],
['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|'],
['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"'],
['Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?']]

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

print(encrypt("haslo",-9))