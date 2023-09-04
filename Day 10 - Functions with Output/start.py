#More Functions
#Normal function
#def my_function():
    #Do This
    #Then Do this
    #Then Finally do this

#Functions with Inputs
#def my_function(something):
    #Do this with something
    #Then do this
    #Finally do this
    
#Functions with Outputs
# def my_function():
#     result = 3*2
#     return result <-output is the return keyword

#return is the end point of the functions, any code after return will not run
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide a valid inputs"
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}"


print(format_name(input("What is your first name? "), input("What is your last name? ")))
   
    
