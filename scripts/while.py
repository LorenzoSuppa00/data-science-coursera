
#* 1° Esercizio While Loop
# ratings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
# i = 0
# while (i < len(ratings)):
#     score = ratings[i]
#     print(score)
#     i += 1
#     if (score < 6):
#         break 

#* 2° Esercizio While Loop
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0

while (i < len(squares)):
    square = squares[i]
    if (square != "orange"):
        break
    new_squares.append(square)
    i += 1

print(new_squares)
    
#* Roba che ho voluto fare io in più    
# tutt_orange = []

# for square in squares:
#     if (square == "orange"):
#         tutt_orange.append(square)

# print(tutt_orange)
