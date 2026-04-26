from collections import defaultdict
    arr = defaultdict(list)
    for _ in range(n):
        n, m = input().split()
        arr[m].append(int(n))
  
    count = {}
    for key, ch in arr.items():
        count[key] = min(ch)
    if "11" in arr:
        if "01" not in arr or "10" not in arr:
            print(count["11"])
        else:
            print(min(count["11"], count["01"] + count["10"]))
    elif "01" in arr and "10" in arr:
        print(count["01"] + count["10"])
    else:
        print(-1)