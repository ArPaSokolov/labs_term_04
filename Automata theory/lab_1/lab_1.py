def compare(str_one, str_two):
    str_one = decompression(str_one)
    str_two = decompression(str_two)
    if str_one == str_two:
        print("Equal!")
    else:
        print("Not equal!")

def decompression(string):
        new_str = str()
        for i in range(len(string)):
            if string[i].isdigit():
                new_str += string[i-1] * (int(string[i]) - 1)
            else:
                new_str += string[i]
        print(new_str)
        return(new_str)
            

str_one = str(input("Enter first string: "))
str_two = str(input("Enter second string: "))
compare(str_one, str_two)