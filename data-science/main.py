# Write line to file
exmp2 = 'Example.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")

# Write lines to file

with open(exmp2, 'w') as writefile: #? Sovrascivo il file iniziale
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

# Check whether write to file

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

with open('Example.txt', 'a') as writefile: #? Aggiungo nuove righe al file Example2.txt
    writefile.write("This is line C\n")
    writefile.write("This is line D\n")
    writefile.write("This is line E\n")

with open('Example.txt', 'a+') as testwritefile:
    testwritefile.write("This is line F\n")
    print(testwritefile.read())

with open('Example.txt','r') as readfile: #? Metodo per copiare il contenuto di un file in un altro file
    with open('Example2.txt','w') as writefile:
        for line in readfile:
            writefile.write(line)