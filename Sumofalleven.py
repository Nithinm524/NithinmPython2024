start=int(input("enter start of range:"))
end=int(input("enter end of range:"))
even_sum=0
for num in range(start,end+1):
    if num%2==0:
       even_sum+=num
    print("sum of even numbers:",even_sum)