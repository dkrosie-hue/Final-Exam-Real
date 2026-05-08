odds = []
evens = []
finished = False
print("Enter Integers: ")
while not finished:
    num_str = input(" ? ")
    if num_str == "":
        finished = True
    else:
        num = int(num_str)
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
odd_avg = sum(odds)/len(odds)
even_avg = sum(evens)/len(evens)
print(f"The average of the odd numbers is {odd_avg:.2f}") 
print(f"The average of the even numbers is {even_avg:.2f}")
