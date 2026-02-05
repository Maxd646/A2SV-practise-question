# Subdomain Visit Count
# Platform: LeetCode
from collections import Counter
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        result=[]

        seen= Counter()

        for ch in cpdomains:

            arra=ch.split()
            num= arra[0]
            arr1=arra[1].split(".")

            for i in range(len(arr1)-1, -1, -1):

                seen[".".join(arr1[i:len(arr1)])]+=int(num)

        for ch, num in seen.items():

            result.append(str(num) + " " +ch)

        return result


