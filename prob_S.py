def calculateProb(S,D):
    cnt=0
    for i_set in D:
        if S==i_set:
            cnt+=1
    return cnt/len(D)
