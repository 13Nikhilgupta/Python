def marcsCakewalk(calorie):
    min_walk=0
    for i in range(len(calorie)):
        sum=0
        j=i
        p=0
        while(True):
            sum+=((2**p)*calorie[j])
            p+=1
            j=(j+1)%len(calorie)
            if j==i:
                break
        
        if i==0:
            min_walk=sum
        else:
            if min_walk>sum:
                min_walk=sum
            
    return min_walk

if __name__ == '__main__':
    c=[1,3,2]
    result=marcsCakewalk(c)
    print(result)