a=int(input("enter first number: "))
operator=input("enter operator: ")
b=int(input("enter second number: "))

match operator:

  case "+":
   print(f"sum is: {a+b}")
  case "-":
    print(f"subtract is: {a-b}")
  case "*":
    print(f"product is: {a*b}")
  case "/":
    print(f"devide is: {a/b}")
  case "**":
    print(f"square is: {a**b}")
