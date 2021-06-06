from myFunction import checkDigit, checkUpper, strSize

green = "\033[2;32;40m"
end_c = "\033[0;0m"

generator = ""

while True:
    generator = input('Genarate your password: ')
    if strSize(generator):
        if checkUpper(generator):
            if checkDigit(generator):
                msg = "(Successful password) "
                password = generator
                print(msg + green + password + end_c)
                break
 