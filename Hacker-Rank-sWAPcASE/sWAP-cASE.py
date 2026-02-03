def swap_case(s):
    result=""
    for i in range(len(s)):
        if s[i].islower():
            result+=s[i].upper()
        elif  s[i].isupper():
            result+=s[i].lower()
        else:
             result+=s[i]
            
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)