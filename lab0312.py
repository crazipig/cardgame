age=int(input("Please input your age:"))
if age<3:
    fee=0
else:
    categorie=str(input("Please input your movie genre(normal/3D): "))
    if age<=12:
        fee=10
    else:
        if categorie=="normal":
            fee=15
        if categorie=="3D":
            fee=20
        if age>=65:
            fee-=5
print("your age is ",age,"fee:$",fee)