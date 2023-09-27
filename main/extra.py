with open("C:/VSCode/recipes_project/main/text/recipe1.txt") as file: # "r" --> reads text file

    file1 = file.read()  # --> STRING, looks exactly like file reads

    print(file1)

    list_of_strings = file1.split('\n') # splits with new line as separator --> ['1 unit(s) egg(s)', '250 gr flour']

    print(list_of_strings)

    times = len(list_of_strings)

    print(times)

    list_of_words = []

    for i in range(0,times):
        list_of_words = list_of_words  + list_of_strings[i].split(' ') # splits with space as separator

    length = len(list_of_words)
    

    for i in range(0,length): 
        if i == 0 or i%3 == 0:
                list_of_words[i] = float(list_of_words[i])  #gives a list of words with correct floats

    print(list_of_words)   #gives a list of words with correct floats --> [1.0, 'unit(s)', 'egg(s)', 250.0, 'gr', 'flour']

    length = len(list_of_words)

    # match this list to class Ingredient

    # from Ingredient import Ingredient

    # empty_ingr_list = []

    # for i in range(0,length):
        




