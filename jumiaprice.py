jumiaprice=int(input("enter your price:"))
cp_buscuit=100
sp_buscuit=150
pf_buscuit=sp_buscuit-cp_buscuit
if jumiaprice==cp_buscuit:
    print("you can purchase")
elif jumiaprice>sp_buscuit:
    print("you can not purchase")
elif jumiaprice<pf_buscuit:
    print("you are broke")
else:
    print("thank you for patronising us") 





foodcity=int(input("enter your request:"))
cp_jollof=1,500
sp_jollof=2,000
pf_jollof=500
if foodcity==pf_jollof:
    print("enjoy your meal") 
elif foodcity>cp_jollof:
    print("i do not think you are hungry")
elif foodcity<sp_jollof:
    print("you can go home to eat")
else:
    print("man shall not live by bread alone")                      
