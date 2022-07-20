def runLengthEncoding(string):
    # Write your code here.
    ans =''
    i=0
    j =1
    while i <len(string)-2:
        count = 1
        letter =string[i]
        while string[i]==string[j]:
            count +=1
            if i < len(string)-2:
                i+=1
                j+=1
            else:break
        if count>9:
            ans = ans+'9'+letter+str(count-9)+letter
        else: ans = ans+str(count)+letter
        i+=1
        j+=1
    if string[-1] == string[-2]:
        # ans[-2] = str(int(ans[-2]) + 1)
        return ans
    else:
        ans = ans + str(1) + string[-1]
    return ans

print(runLengthEncoding("aaaabbbbccccccccccccd"))