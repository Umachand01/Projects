try:
    total_income_=int(input("enter your income: "))
    total_income=total_income_*100/total_income_
    print(f"{total_income}%")
    def spend():
        investing_=int(input("enter investing amount: "))
        investing=(investing_*100/total_income_)
        grosary_=int(input("enter grosary expence prices: "))
        grosary=(grosary_*100/total_income_)
        education_=int(input("enter education expence: "))
        education=(education_*100/total_income_)
        income_tex_=int(input("enter income tax amount: "))
        income_tex=(income_tex_*100/total_income_)
        cloths_and_other_=int(input("enter cloths and other expence amount: "))
        cloths_and_other=(cloths_and_other_*100/total_income_)
        saving_=int(input("enter savig amount: "))
        saving=(saving_*100/total_income_)
        total_expence=investing+grosary+education+income_tex+cloths_and_other+saving
    
        print(f"total expence:--->{int(total_expence*total_income_/100)}Rs. __________ {int(total_expence)}%")
        if total_income>=total_expence:
                print("its going find")
        else:  
                print(f"-->{int(total_income_*(total_income_-total_expence)/100)}Rs. _________ {int(total_income-total_expence)}% your expence is over!")
    spend()    
except Exception as e:
    print(f"error:--?{e}") 
       