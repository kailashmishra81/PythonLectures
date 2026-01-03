rows=int(input("Please enter the number of rows:"))
cols=int(input("Please enter the number of columns:"))
symbol=input("Please enter the symbol:")
for i in range(rows):
    for j in range(cols):
        print(symbol,end=" ")  ##Prevents moving to the new line and also adds a space after each symbol
    print()                     ## Moves to the next line once the iteration of the inner loop gets completed
