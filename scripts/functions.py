# Python Program to Count words in a String using Dictionary
# def freq(string):
    
#     #step1: A list variable is declared and initialized to an empty list.
#     words = []
    
#     #step2: Break the string into list of words
#     words = string.split() # or string.lower().split()
    
#     #step3: Declare a dictionary
#     Dict = {}
    
#     #step4: Use for loop to iterate words and values to the dictionary
#     for key in words:
#         Dict[key] = words.count(key) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! BHOOOOOOOOOOOOOOOOOO
        
#     #step5: Print the dictionary
#     print("The Frequency of words is:",Dict)
    
# #step6: Call function and pass string in it
# freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
# Everywhere that Mary went The lamb was sure to go")

#* Altro esempio
# def isGoodRating(rating=4): #? Valore di default 4
#     if(rating < 7):
#         print("this album sucks it's rating is",rating)
        
#     else:
#         print("this album is good its rating is",rating)

# isGoodRating()
# isGoodRating(10)


def conta_little(stringa, parola_da_contare):
    parole = []
    parole = stringa.lower().split()

    for parola in parole:
        counter = parole.count(parola_da_contare)

    print(f"{parola_da_contare} è stato scritto {counter} volte")


conta_little("Mary had a little lamb Little lamb , little lamb Mary had a little lamb . Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go", "mary")