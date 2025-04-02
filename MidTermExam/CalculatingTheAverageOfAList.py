def average_of_a_list(list):
    sum = 0
    average = 0
    for num in list:
        sum += num
    average = sum / length
    print(f"The average of {list} numbers is {average}")

length = int(input("Enter a length of list: "))
n = []
for i in range(length):
    n.append(int(input("Enter a number: ")))
average_of_a_list(n)
