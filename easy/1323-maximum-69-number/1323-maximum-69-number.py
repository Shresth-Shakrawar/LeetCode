        for j in range(len(s)):
            if s[j] == "6":
                index = j
                break
        if index == -1:
            return num
        else:
            return int(s[:index]+"9"+s[index+1:])
        
        