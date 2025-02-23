# Problem: A - Harmonic Melody - https://codeforces.com/gym/590201/problem/A

def is_perfect_melody(notes):
    for i in range(len(notes) - 1):
        interval = abs(notes[i] - notes[i + 1])
        if interval not in {5, 7}:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    notes = list(map(int, input().split()))
    if is_perfect_melody(notes):
        print("YES")
    else:
        print("NO")