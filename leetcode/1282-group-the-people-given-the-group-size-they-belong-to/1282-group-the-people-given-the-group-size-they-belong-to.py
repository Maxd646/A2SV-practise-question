class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        seen = defaultdict(list)

        for i, num in enumerate(groupSizes):

            seen[num].append(i)
   
        ans = []

        for gr, pope in seen.items():
            
            if len(pope) == gr:

                ans.append(pope)
                continue

            for i in range(0, len(pope), gr):

                ans.append(pope[i:i+gr])

        return ans
            

        

        
        