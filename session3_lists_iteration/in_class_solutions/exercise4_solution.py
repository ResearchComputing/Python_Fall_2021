def append_index(a):
    b = []
    for i, v in enumerate(a):
        new_string = v+' '+str(i)
        b.append(new_string)
    return b

my_input = ['Hello', 'There']
my_output = append_index(my_input)
print(my_output)
