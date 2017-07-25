import math

#Pre: The user wants to find circumference of a circle with their radius.
#Post: The circumference of a circle with user's radius is computed.
def ComputeCircumference(users_radius):
    Circumference = 2 * math.pi * users_radius
    PrintResults("Circumference is", Circumference)
    
#Pre: The user wants to find the area of a circle using their radius.
#Post: The area of a circle with the user's radius computed.
def ComputeArea(users_radius):
    Area = math.pi * (users_radius ** 2)
    PrintResults("Area is", Area)
    
#Pre: User wants to find volume of a box with their length, width, and height.
#Post: The volume given user's length, width, and height is computed.
def ComputeVolume(boxLength,boxWidth,boxHeight):
    volume = boxLength * boxWidth * boxHeight
    PrintResults("Box volume is", volume)

#Pre: The user wants to convert their number of degrees in Fahrenheit to Celsius.
#Post: The degrees in Celsius is converted from Fahrenheit.
def ConvertFahrenheitCelsius(DegreesF):
    celsius = (DegreesF - 32) * 5 / 9
    PrintResults("Equivalent celsius is", celsius)

#Pre: The user wants to find degrees in Kelvin given their degrees in Fahrenheit.
#Post: The degrees in Fahrenheit is converted to degrees in Kelvin.
def ConvertFahrenheitKelvin(DegreesF):
    kelvin = (DegreesF + 459.67) * 5 / 9
    PrintResults("Equivalent kelvin is", kelvin)

#Pre: The user wants to find the quotient of two numbers.
#Post: The quotient is computed given the two numbers.
def Quotients_of_Numbs(Number1,Number2,SpecificPrompt):
    NumberQuotient = Number1//Number2
    PrintResults(SpecificPrompt, NumberQuotient)

#Pre: User wants to find the remainder of two numbers after they are divided.
#Post: The remainder is computed with the two numbers.
def Remainders_of_Numbs(Number1,Number2,SpecificPrompt):
    NumberRemainder = Number1%Number2
    PrintResults(SpecificPrompt, NumberRemainder)

#Pre: Some specific input is needed from the user for another function.
#Post: The user enters specific input and it is returned for use in the function.
def Input_from_user(Prompt_String):
    UsersInput = input(Prompt_String)
    return UsersInput

#Pre: A message and data value from computations needs to be displayed to user.
#Post: The message and data value is displayed to the user.
def PrintResults(StringToDisplayValue,resultFromComputation):
    print(StringToDisplayValue, resultFromComputation)
    
def main():
    users_radius = int(Input_from_user("Enter radius for a circle:"))
    ComputeCircumference(users_radius)
    ComputeArea(users_radius)
    boxLength = float(Input_from_user("Enter length of a box:"))
    boxWidth = float(Input_from_user("Enter width of a box:"))
    boxHeight = float(Input_from_user("Enter height of a box:"))
    ComputeVolume(boxLength,boxWidth,boxHeight)
    DegreesF = int(Input_from_user("Enter degrees in Fahrenheit:"))
    ConvertFahrenheitCelsius(DegreesF)
    ConvertFahrenheitKelvin(DegreesF)
    NumberA = int(Input_from_user("Enter first number:"))
    NumberB = int(Input_from_user("Enter second number:"))
    Quotients_of_Numbs(NumberA,NumberB,"Quotient of First Number/Second Number is")
    Quotients_of_Numbs(NumberB,NumberA,"Quotient of Second Number/First Number is")
    Remainders_of_Numbs(NumberA,NumberB,"Remainder of First Number/Second Number is")
    Remainders_of_Numbs(NumberB,NumberA,"Remainder of Second Number/First Number is")
