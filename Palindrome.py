def Palindrome(string):
    reversed=""
    for fan in string:
        reversed = fan + reversed
    if(reversed==string):
        print("Palindrome")
    else:
        print("Not a Palindrome")



string=input()
Palindrome(string)
