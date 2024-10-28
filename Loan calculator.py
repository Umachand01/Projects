try:


    loan_amount=int(input("enter your loan amount: "))
    loan_turnue=int(input("enter loan turnue(months): "))
    rate_of_loan=int(input("enter rate of loan % : "))

    #loan_turnue in 12M/100 = 0.12
    calculated_amount=((loan_amount*rate_of_loan*(loan_turnue)*0.12)/100)
    total_amount=loan_amount+calculated_amount

    print(f"calculated loan = {calculated_amount}") 
    print(F"total amount = {total_amount}")
except KeyboardInterrupt:
    print("please enter correct input")    
except Exception as f:
    print(f"error {f}")    