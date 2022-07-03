start=input("start: ")
# end=int(input("start: "))
spl=start.split(":")
if ":" in start:
    print("yes")
    start=(int(spl[0])*60)+(int(spl[1]))
else:
    print("no :")
    start=int(start)
print(start)

time=int("12")
min=int("30")
t=f"{(time*60)+ min}"
print(t)