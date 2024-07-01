marketpricerice=int(input("enter an ammount:"))
cost_price_rice=50,000
selling_price_rice=70,000
profit_price_rice=selling_price_rice-cost_price_rice
if marketpricerice==selling_price_rice:
    print("you can now purchase this product")
elif marketpricerice<cost_price_rice:    
    print("you can not purchase this product")
elif marketpricerice>selling_price_rice:
    print("seem like you are a rich kid")
else:
    print("go back home")          
