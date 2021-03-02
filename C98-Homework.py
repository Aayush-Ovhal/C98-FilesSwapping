def swapFiles():
    inputFile_a = input("Enter the file name: ")
    inputFile_b = input("Enter the second file name: ")


    with open(inputFile_b, 'r') as b:
        data_b = b.read()
    with open(inputFile_a, 'r') as a:
        data_a = a.read()
        
    with open(inputFile_a, 'w') as a:
        a.write(data_b)
    with open(inputFile_b, 'w') as b:
        b.write(data_a)

    print("Done swapping you can check the files!")

swapFiles()

    
