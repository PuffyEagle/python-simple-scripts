#Pre: Prompt exists and user needs to enter input.
#Post: Prompt is displayed to user in order to get input and input is returned.
def GetStringVal(Prompt):
    return input(Prompt)

#Pre: StringVal exists and a loop needs to keep displaying how many characters,
    # words, and sentences are in StringVal and the average word and
    # and sentence size of StringVal, then ask for another StringVal.
#Post: Until entered StringVal is "done", function loops, finds number of
    # characters, words, and sentences in StringVal and the average word and
    # sentence size, displays a prompt with these numbers, and gets a new
    # StringVal from the user.
def Find_Display_NumbCharWordsSentences():
    StringVal = GetStringVal("Enter a string value:")
    while StringVal != "done":
        NumbCharacters = FindNumbChar(StringVal)
        NumbWords,WordList = FindNumbStringsinList(StringVal," ")
        NumbSentences,SentenceList = FindNumbStringsinList(StringVal,".")
        AvgWordSize = FindAvgNumbCharinString(WordList,NumbWords)
        AvgSentenceSize = FindAvgNumbCharinString(SentenceList,NumbSentences)
        
        DisplayComputations(NumbCharacters,NumbWords,NumbSentences,AvgWordSize,AvgSentenceSize)
        StringVal = GetStringVal("Enter a string value:")

#Pre: Data and Prompt exist and need to be displayed to the user.
#Post: Prompt and Data are displayed for user to see.
def DisplayDataPrompt(Prompt,Data):
    print(Prompt.rjust(35),Data)

#Pre: NumbCharacters, NumbWords, NumbSentences, AvgWordSize, and AvgSentenceSize
    # exist and are valid.
#Post: NumbCharacters, NumbWords,NumbSentences, AvgWordSize, and AvgSentenceSize
    # proceed with a specific prompt to be displayed to the user.
def DisplayComputations(NumbCharacters,NumbWords,NumbSentences,AvgWordSize,AvgSentenceSize):
    DisplayDataPrompt("Number of characters:",NumbCharacters)
    DisplayDataPrompt("Number of words",NumbWords)
    DisplayDataPrompt("Number of sentences",NumbSentences)
    DisplayDataPrompt("Average word size in characters",AvgWordSize)
    DisplayDataPrompt("Average sentence size in characters",AvgSentenceSize)
                
#Pre: String exists and is valid.
#Post: Number of characters in string is found and returned.
def FindNumbChar(String):
    return len(String)

#Pre: String and SplitItem exist and are valid.
#Post: String is split at the SplitItem into a list. If last string in list is
    # an empty string, it is removed. Then this list and its length are returned.
def FindNumbStringsinList(String,SplitItem):
    StringList = String.split(SplitItem)
    if len(StringList[len(StringList)-1]) == 0:
        StringList.remove("")
    return len(StringList),StringList

#Pre: aList and NumbStrings exist and are valid. Average number of characters
    # in a given list needs to be computed.
#Post: Number of characters in a given list of strings is computed(unless
    # NumbStrings is 0)divided by the number of strings in the list, and returned.
def FindAvgNumbCharinString(aList,NumbStrings):
    Characters = 0
    if NumbStrings != 0:
        for string in aList:
            if len(string) != 0:
                if string[0] != " ":
                    Characters = Characters + len(string)
                elif string[0] == " ":
                    Characters = Characters + len(string)-1
        return Characters/NumbStrings
    else:
        return 0.0

def main():
    print("Welcome to the Input Analyzer!")
    print("Enter input to see number of chars, words, and sentences, average word size, and average sentence size.")
    print("Enter 'done' without quotes to exit the program.")
    Find_Display_NumbCharWordsSentences()




#TEST CASES         Output:
#Input            #Char   #Words  #Sentences  Avg Word Size  Avg Sentence Size
#-----------      -----   ------  ----------  -------------  -----------------     
# hello             5       1       1           5.0             5.0
#
# Hi.               3       1       1           3.0             2.0
#
# Hello there.      12      2       1           5.5             11.0
#
# Hi. Bye.          8       2       2           3.5             2.5
#
# Hi. I am happy.   32      7       3           3.71428571      9.0
#   This is working.
#
# Thisisabigmess.   15      1       1           15.0            14.0
#
# ...               3       1       3           3.0             0.0
#
# .                 1       1       1           1.0             0.0
#
# ""  (without      0       0       0           0.0             0.0
#       quotes)
#
# done              Program exits











    
