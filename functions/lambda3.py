numbers = list(map(int,input().split()))
print(numbers)

numbers_halfed = list (map(lambda i : int(i)/2 , input().split()))
print(numbers_halfed)

x = [12,13,14,15,16,17,18,20,30,34,44]
x_odd = list(filter(lambda i:i%2!=0))
print(x_odd)