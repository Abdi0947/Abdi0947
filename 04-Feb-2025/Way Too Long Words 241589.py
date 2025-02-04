# Problem: Way Too Long Words - https://codeforces.com/problemset/problem/71/A

n=int(input())
for i in range(n):
    word=input()
    word=list(word)
    long=[]
    k=len(word)
    if k>10:
        for i in range(1,len(word)):
            long.append(word[i])
        long_words=word[0]+str(len(long)-1)+word[len(word)-1]
        print(long_words)
    else:
        word=''.join(word)
        print(word)