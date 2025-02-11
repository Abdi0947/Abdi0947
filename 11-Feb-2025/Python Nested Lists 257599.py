# Problem: Python Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    data = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append({'name': name, 'score': score})
    unique_scores = sorted(set(item['score'] for item in data))
    second_lowest_score = unique_scores[1]  

    arr = [item['name'] for item in data if item['score'] == second_lowest_score]
    
    arr.sort()
    
    for name in arr:
        print(name)
