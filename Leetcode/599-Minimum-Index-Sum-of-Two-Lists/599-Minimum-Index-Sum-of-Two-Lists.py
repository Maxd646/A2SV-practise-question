# Minimum Index Sum of Two Lists
# Platform: LeetCode
class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        seen =set(list1)
        seen2={list1[i]:i for i in range(len(list1))}
        result={}
        minn=float("inf")
        for i in range(len(list2)):
            index=0
            if list2[i] in seen:
                result[list2[i]]=i+seen2[list2[i]]
                minn=min(minn, i+seen2[list2[i]])
        now= [num for num, val in result.items() if val==minn ]
        return now
                