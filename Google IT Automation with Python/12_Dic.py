# The format_address function separates out parts of the address string into new strings: house_number and street_name, 
# and returns: "house number X on street named Y". The format of the input string is: numeric house number, followed by 
# the street name which may contain numbers, but never by themselves, and could be several words long. For example, 
# "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.



def format_address(address_string):
  # Declare variables
    addr = []
    numb = []
    
  # Separate the address string into parts

  # Traverse through the address parts
    for element in address_string.split():
        if element.isnumeric():   #me devuelve si el str es numerico
            numb.append(element)
        else:
            addr.append(element)
                    

    # Determine if the address part is the
    # house number or part of the street name

  # Does anything else need to be done 
  # before returning the result?
    direc = " ".join(addr) # de esta manera vuelvo a armar el string
  # Return the formatted string  
    return "house number {} on street named {}".format(numb[0], direc)


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"