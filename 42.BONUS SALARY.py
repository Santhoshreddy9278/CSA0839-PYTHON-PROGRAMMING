grade = input("Grade: ")
salary = int(input("Salary: "))
bonus = 0
if salary < 10000:
  bonus+=salary * (2/100)
match(grade):
  case 'A' | 'a':
    bonus += salary * (5/100)
    print(f"Bonus: {int(bonus)}")
    print(f"Total to be paid: {int(salary+bonus)}")
  case 'B' | 'b':
    bonus += salary * (10/100)
    print(f"Bonus: {int(bonus)}")
    print(f"Total to be paid: {int(salary+bonus)}")
  case _:
    print("Enter valid grade")
