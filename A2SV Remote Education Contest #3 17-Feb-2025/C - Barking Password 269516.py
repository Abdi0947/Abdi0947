# Problem: C - Barking Password - https://codeforces.com/gym/588094/problem/C

password = input().strip()

n = int(input().strip())
words = [input().strip() for _ in range(n)]

# Check if password exists in words
if password in words:
    print("YES")
    exit()

first_letter_found = False
second_letter_found = False

for word in words:
    if len(word) >= 2:  # Ensure word has at least 2 characters
        if word[0] == password[1]:
            first_letter_found = True
        if word[1] == password[0]:
            second_letter_found = True

if first_letter_found and second_letter_found:
    print("YES")
else:
    print("NO")
