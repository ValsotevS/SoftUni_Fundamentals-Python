given_string = str(input())
double_char_string = ""
while given_string != "End":

    if given_string == "SoftUni":
        given_string = str(input())

    for char in given_string:
        current_char = char 
        double_char_string += current_char * 2

    print(double_char_string)
    double_char_string = ""
    given_string = str(input())