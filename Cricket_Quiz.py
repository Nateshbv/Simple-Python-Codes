class CricketQuiz:
    def __init__(self, Ques, Ans):
        self.Ques = Ques
        self.Ans = Ans
    
Questions_List =[ "Who is the highest Run Getter in Test Cricket?\n (a) Sachin \n (b) Virat \n (c) Ponting", 
                  "Who is the second highest Run Getter in Odi Cricket?\n (a) Sachin \n (b) Virat \n (c) Ponting", 
                  "Who is the highest Run Getter in T20 Cricket?\n (a) Rohit \n (b) Virat \n (c) Gayle",
                  "Who is the highest wicket taker in Test Cricket?\n (a) Warne \n (b) Murali \n (c) Anderson",
                  "Cricket Kashi\n (a) MCG \n (b) Eden \n (c) Lords", 
                  "ICC T20 Worldcup 2021 winner \n (a) Australia \n (b) India \n (c) England",                  
                 "ICC T20 Worldcup 2023 to be held in\n (a) Australia \n (b) India \n (c) England", ]


Questions = [CricketQuiz(Questions_List[0],'a'), 
             CricketQuiz(Questions_List[1],'c'),
             CricketQuiz(Questions_List[2],'b'),
             CricketQuiz(Questions_List[3],'b'),
             CricketQuiz(Questions_List[4],'c'),
             CricketQuiz(Questions_List[5],'a'),
             CricketQuiz(Questions_List[5],'b')]


def Quiz(Questions):
    Score = 0
    for Qn in Questions:
        ans = input(Qn.Ques)
        if ans == Qn.Ans:
            Score += 1
    print ("Your score", Score)

# Just for understanding used main you can skip the main function    
def main():
    Quiz(Questions)

if __name__ == "__main__":
    main()


