class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:

        seen = Counter(s)
        ans = []
        
        for ch in target:

            if seen[ch] >0:

                ans.append(ch)
                seen[ch] -= 1
                continue

            greater = [c for c in s if seen[c] > 0 and c > ch]

            if not greater:
                break

            chh = min(greater)
            ans.append(chh)
            seen[chh] -= 1

            for ch, fre in sorted(seen.items()):

                ans.append(ch*fre)

            return "".join(ans)
      
            
        for i in range(len(ans)-1, -1, -1):

            seen[ans[i]] += 1

            greater = [c for c in s if seen[c] > 0 and  c > ans[i]]

            if greater:

                chh = min(greater)
                seen[chh] -= 1
                res = ans[:i] + [chh]

                for ch, f in sorted(seen.items()):

                    res.append(ch*f)

                return "".join(res)

        return ""
            




