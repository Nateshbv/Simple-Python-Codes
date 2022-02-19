# python code to develop random password with 8 characters
# Consists of 2 upper case, 2 lower case, 2 digit and 2 punctuations

import random 
import string


# Shuffle function is used to shuffle the characters in the password

def Shuffle(string):
    tmp_list= list(string)
    random.shuffle(tmp_list)
    return ''.join(tmp_list)

#pick the ASCII values of characters and pick randomly  
# main function will generate the characters first

def main():
 # First two upper case letters ASCII [65-90]     
    up_let1 = chr(random.randint(65,90))
    up_let2 = chr(random.randint(65,90))
    
 # Second Two lower case letters ASCII [97-122]
    lo_let1 = chr(random.randint(97,122))
    lo_let2 = chr(random.randint(97,122))
    
 # two digits from 0 to 9 
    
    dg1 = random.randint(0,9)
    dg2 = random.randint(0,9)
    
 # two punctuations 
    pun1= chr(random.randint(33,47))
    pun2 = chr(random.randint(58,64))
    # pun2= random.sample(string.punctuation,1
    
#   Generate the initial password
    password= up_let1 + up_let2 + lo_let1 + lo_let2 + str(dg1) + str(dg2) + pun1 + pun2
    password = Shuffle(password)
    
    print("the 8 character password is",password)
    
if __name__ == "__main__":
    main()    
