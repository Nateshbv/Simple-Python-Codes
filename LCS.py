def LCS_Length(S, i, j):
    if i>j:
        return 0
    if i==j:
        return 1
    if S[i]==S[j]:
        return LCS_Length(S,i+1,j-1)+2
    return max(LCS_Length(S,i,j-1),LCS_Length(S,i+1,j))

if __name__== '__main__':
    S= 'nata'
    n=len(S)
    print("The length of the LCS palindrome Substring is", LCS_Length(S,0,n-1))
