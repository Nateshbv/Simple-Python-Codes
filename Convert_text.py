# Python program for code generator 
#""" Accepts string and display the Encrypted Text and the Function for Decrypt the Cipher to Plain text"""

shift= 5

# Function for the Encryption with linear shift or subsitituion 

def Encrypt(text):
    encoded=''
    for c in text:
        if c.islower():
            c_uni=ord(c)
            c_ind= ord(c)-ord('a')
            
            new_ind = (c_ind + shift)%26
            new_uni = new_ind + ord('a')
            new_character = chr(new_uni)
            encoded+= new_character
        else:
            c_uni=ord(c)
            c_ind= ord(c)-ord('A')
            
            new_ind = (c_ind + shift)%26
            new_uni = new_ind + ord('A')
            new_character = chr(new_uni)
            encoded+= new_character
    
    return encoded

# Function for the Decryption with Linear shift/Substitution 
def Decrypt(encoded):
    Original= ""
    for c in encoded:
        if c.islower():
            c_uni=ord(c)
            c_ind= ord(c)-ord('a')
            
            new_ind = (c_ind - shift) % 26
            new_uni = new_ind + ord('a')
            new_char = chr(new_uni)
            Original+= new_char
#        Check for the Upper Case Letters and perform the reverse shift operation      
        else:
            c_uni=ord(c)
            c_ind= ord(c)-ord('A')
            
            new_ind = (c_ind - shift)%26
            new_uni = new_ind + ord('A')
            new_char = chr(new_uni)
            Original+= new_char
    
    return Original
        

def main():
    string=input("enter the string to be encoded")
    Cipher = Encrypt(string)
    Plain = Decrypt(Cipher)
    print("The Encrypted String is", Cipher)
    print("the Decrypted String is", Plain)

    
if __name__ == "__main__":
    main()
    
