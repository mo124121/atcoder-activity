N = int(input())
S = input()

ret =[chr((ord(c)+N-ord("A"))%26+ord("A")) for c in S]
print("".join(ret))
