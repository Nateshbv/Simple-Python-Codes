# Function to find the substring using the DPTable 
def LCS_String(M,N, i,j,DPT):
    if i==0 or j==0:
        return ""
    if M[i-1]==N[j-1]:
        return LCS_String(M,N,i-1,j-1,DPT)+ M[i-1]
    if DPT[i-1][j] > DPT [i][j-1]:
        return LCS_String(M,N,i-1,j,DPT)
    return LCS_String(M,N,i,j-1,DPT)

# Function to find the length of the substring using the DP Table 
def LCS_Length(M,N, j, DPT):
    for i in range(1,n+1):
        for j in range(1, n+1):
            if M[i-1]==N[j-1]:
                DPT[i][j]=DPT[i-1][j-1]+1
            else:
                DPT[i][j]= max(DPT[i-1][j], DPT[i][j-1])
    return DPT[i][j]

if __name__=='__main__':
    
    S="nata"
    
    T=S[::-1] #reverse of the String S
    
#     Make DP Table
    DPTable= [[0 for x in range(len(S)+1)] for y in range(len(S)+1)]
    print("The length of the LCS",LCS_Length(S,T,len(S),DPTable))
    
    print("the substring is", LCS_String(S,T, len(S), len(T), DPTable))
    
