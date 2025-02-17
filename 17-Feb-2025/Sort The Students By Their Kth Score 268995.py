# Problem: Sort The Students By Their Kth Score - https://leetcode.com/problems/sort-the-students-by-their-kth-score/


class Solution:
    def sortTheStudents(self, score, k):
        score.sort(key=lambda x: x[k], reverse=True)
        return score
solution = Solution()
print(solution.sortTheStudents([[10,6,9,1],[7,5,11,2],[4,8,3,15]], 2))
print(solution.sortTheStudents([[3,4],[5,6]], 0))

