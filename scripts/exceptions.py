#
#* Esercizio n° 2
# import math

# def square_root():
#     try: 
#         num = int(input("Inserisci un numero: "))
#         rad = math.sqrt(num)
#         print(f"La radice quadrata di {num} è {rad}")
#     except ValueError:
#         print(f"{num} is an Invalid input! Please enter a positive integer or a float value")

# square_root()
    
#* Esercizio n° 3

#Type your code here
def div5(num):
    try:
        result = num / (num - 5)
        print(result)
    except Exception as e:
        print("An error occurred during calculation")
         
div5(2)