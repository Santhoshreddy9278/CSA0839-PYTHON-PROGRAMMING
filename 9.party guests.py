e = []
l = []
sum,maxi =0,0
n = int(input("Enter the Time: "))

print("Enter the no of guests entering(* to quit): ")
while True:
  s = input()
  if s =='*':
    break
  else:
    e.append(int(s))
print("Enter the no of guests leaving(* to quit): ")
while True:
  s = input()
  if s =='*':
    break
  else:
    l.append(int(s))

for i in range(0,n):
  sum+= e[i]-l[i]
  maxi = max(sum,maxi)
print(maxi)
