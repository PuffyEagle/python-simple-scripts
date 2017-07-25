import string

#Pre: Prompt exists and user needs to enter a input.
#Post: Prompt is displayed to user in order to get input and input is returned.
def GetNewStringVal(Prompt):
    return input(Prompt)

#Pre: StringVal exists and a loop needs to keep displaying if an entered
    # StringVal is a palindrome, then ask for another StringVal.
#Post: Until the entered StringVal is  "exit", the function loops, assesses
    # the StringVal, displays a prompt saying if the StringVal is a palindrome
    # or not, and gets a new StringVal from the user.
def ContinuousPalindromeComparer():
    StringVal = GetNewStringVal("Enter a string:")
    while StringVal != "exit":
        Prep_StringVal = PrepPalindromeStr(StringVal)
        if IsStringPalindrome(Prep_StringVal) == True:
            DisplayPrompt("This is a palindrome.")
            StringVal = GetNewStringVal("Enter a string:")
        else:
            DisplayPrompt("This is NOT a palindrome.")
            StringVal = GetNewStringVal("Enter a string:")

#Pre: String exists and needs to be confirmed or denied a palindrome.
#Post: If String is found to not be a palindrome, False is returned; otherwise,
    # True is returned.
def IsStringPalindrome(String):
    Position = 0
    for character in range(len(String)//2):
        if String[0+Position] != String[-1-Position]:
            return False
        else:
            Position = Position + 1
    return True

#Pre: String exists and needs to be prepped for assessing if it is a palindrome.
#Post: String is made lowercase and whitespaces and punctuation are removed; 
    # then NewestStr is returned.
def PrepPalindromeStr(String):
    NewStr = String.lower()
    NewerStr = RemoveWhiteSpace(NewStr)
    NewestStr = RemovePunctuation(NewerStr)
    return NewestStr

#Pre: String exists and needs the whitespaces removed from it.
#Post: The whitespaces are removed from String and StrNoSpace is returned.
def RemoveWhiteSpace(String):
    WhiteSpace = string.whitespace
    StrNoSpace = ""
    for character in String:
        if character not in WhiteSpace:
            StrNoSpace = StrNoSpace + character
    return StrNoSpace

#Pre: String exists and needs punctuation removed from it.
#Post: The punctuation is removed from String and StrNoPunct is returned.
def RemovePunctuation(String):
    punctuation = string.punctuation
    StrNoPunct = ""
    for character in String:
        if character not in punctuation:
            StrNoPunct = StrNoPunct + character
    return StrNoPunct

#Pre: Prompt exists and needs to be displayed to the user.
#Post: Prompt is displayed for user to see.
def DisplayPrompt(Prompt):
    print(Prompt)

def main():
    print("Welcome to the Continuous Palindrome Comparer!")
    print("Enter input and press enter to see if it is a palindrome.")
    print("Enter 'exit' without quotes to exit the program.")
    ContinuousPalindromeComparer()




# Test Cases
#   Input                               Expected Result
#   ------------------------------      ---------------
#   1234321                             This is a palindrome.
#   radar                               This is a palindrome.
#   RadAr                               This is a palindrome.
#   rad ar                              This is a palindrome.
#   Rad Ar.                             This is a palindrome.
#   Racecar                             This is a palindrome.
#   App le                              This is NOT a palindrome.
#   Cat                                 This is NOT a palindrome.
#   number.                             This is NOT a palindrome.
#   "CHeeSe!"                           This is NOT a palindrome.
#   Dammit I'm mad.                     This is a palindrome.
#   A man, a plan, a canal, Panama.     This is a palindrome.
#   "exit"                              This is NOT a palindrome
#   exit                                *Program ends*

