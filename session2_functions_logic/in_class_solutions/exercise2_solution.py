def ageis(name,age):
    """ Returns a sentence of the form '{name} is {age} years old.' 
        input parameters:  name -- string value
                            age -- integer value
        return value:       msg -- string value containing the sentence above"""
    #The text in triple-double quotes above is referred to as a docstring 
    msg = name+' is '+str(age)+' years old.'
    return msg

#By passing our function name to the help function, we can see the docstring (if any)
#help(ageis)

m = ageis('Erin',16)
print(m)

# We don't have to explicitly accept a return value, and can
# instead implicitly pass the value to the print function.
print(ageis('Steven', 12))
print(ageis('Howard', 37))
print(ageis('Mary', 27))

