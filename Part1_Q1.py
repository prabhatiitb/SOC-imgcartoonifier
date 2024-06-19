def oddnums(list) :
    idx=0
    while (idx<len(list)) :
        if(list[idx]%2!=0):
            print(list[idx])
            idx+=1
        else:
            idx+=1
    return
nums=[1,2,3,4,5,6,7,8,9,53,64,334,634,63,23]
oddnums(nums)