class Solution:
    def candy(self, ratings: List[int]) -> int:
        pre = [1]
        c = 1
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                c+=1
                pre.append(c)
            else:
                c=1
                pre.append(c)
        suff = [1]*len(ratings)


        c = 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                c+=1
                suff[i]=c
            else:
                c=1
                suff[i]=c
        # print(pre)
        # print(suff)
        ans=0

        for i in range(len(suff)):
            ans+=max(suff[i], pre[i])
        return ans
            
            

            
            

            

        