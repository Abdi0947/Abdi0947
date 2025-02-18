# Problem: E - Zombie Invasion! - https://codeforces.com/gym/588094/problem/E

def solve():
    n, k = map(int, input().split())
    damage = list(map(int, input().split()))
    position = list(map(int, input().split()))

    new_damage = {} 

    for i in range(n):
        pos = abs(position[i])
        if pos not in new_damage:
            new_damage[pos] = 0
        new_damage[pos] += damage[i]

    positions = sorted(new_damage.keys()) 

    is_dead = False
    prev_position = 0  
    carry = 0

    for pos in positions:  
        total = (k * (pos - prev_position)) + carry
        if total < new_damage[pos]:
            is_dead = True
            break
        carry = total - new_damage[pos]
        prev_position = pos

    if is_dead:
        print("NO")
    else:
        print("YES")

t = int(input())
for _ in range(t):
    solve()