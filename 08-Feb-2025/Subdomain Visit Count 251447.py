# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        
        cp = {}
        for cpdomain in cpdomains:
            current = cpdomain.split(' ')  
            count = int(current[0])      
            domain = current[1]        
            
            currentDomain = ""
            
            for sub in domain.split('.')[::-1]:
                if currentDomain == "":
                    currentDomain = sub
                else:
                    currentDomain = sub + "." + currentDomain
                if currentDomain in cp:
                    cp[currentDomain] += count
                else:
                    cp[currentDomain] = count

       
        results = []
        for key in cp:
            results.append(str(cp[key]) + " " + key)

        return results

sol = Solution()
cpdomains = ["9001 discuss.leetcode.com"]
print(sol.subdomainVisits(cpdomains))
