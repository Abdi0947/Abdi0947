# Problem: Minimum Number of Moves To Seat Everyone - https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        total_moves = sum(abs(seats[i] - students[i]) for i in range(len(seats)))
        return total_moves
sol=Solution()
seats = [3,1,5]
students = [2,7,4]
print(sol.minMovesToSeat(seats,students))
        