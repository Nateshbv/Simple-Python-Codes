1. # Dynamic Programming (DP) and Examples 

# DP solves the problem by finding and combining the solutions for the subproblems 
def Knapsack_Dp(W,N,weight,profit,dp):
    # Base Condition
    if N==0 or W==0:
        return 0
    # If sub problem is previously solved then return it.
    if dp[N][W] is not None:
        return dp[N][W]
    if wt[N-1] <= W:
        dp[N][W] = max(profi[N-1]+ Knapsack_Dp(W-weight[N-1], N-1,weight,profit,dp), Knapsack_Dp(W,N-1,weight,profit,dp))
        return dp[N][W]
    else:
        dp[N][W] = Knapsack_Dp(W,N-1,weight,profit,dp)
        return dp[N][W]

def main():
    N = int(input("enter the Number of Elements"))
    cap= int(input("enter the capacity"))
    Weight= []
    Profit= []
    for i in range(0,N):
        Weight. append(int(input("enter the weights")))
        Profit. append(int(input("enter the profit")))
    print("Weight=",Weight,"Profit=",Profit)
#     Use table for Knapsack using DP
    DP_table=[[None] * (cap+1) for i in range(N+1)]
    Max_profit= Knapsack_Dp(cap,N, Weight,Profit,DP_table)
    print("The Maximum Profit is", Max_profit)

if __name__ == "__main__":
    main()
