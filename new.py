shoprite=int(input("enter your price:"))
cp_toothbrush=200
sp_toothbrush=300
pf_toothbrush=100
if shoprite==sp_toothbrush:
    print("wish you a nice breath")
elif shoprite<sp_toothbrush:
    print("oops i think you stink")
elif shoprite>pf_toothbrush:
    print("seem like you need another treatment")
else:
    print("you can use a whitener")           