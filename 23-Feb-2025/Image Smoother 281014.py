# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        row=len(img)
        col=len(img[0])
        answer=[[0]*col for i in range(row)]
        for r in range(row):
            for c in range(col):
                count=0
                sum=0
                for nr in range(r-1,r+2):
                    for nc in range(c-1,c+2):
                        if 0<=nr<row and 0<=nc<col:
                            sum+=img[nr][nc]
                            count+=1
                answer[r][c]=sum//count
        return answer  
sol=Solution()
img = [[1,1,1],[1,0,1],[1,1,1]]
print(sol.imageSmoother(img))