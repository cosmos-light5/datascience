import numpy as np

cost_prices = [100, 150, 200, 250, 300]

cp_ar = np.array(cost_prices)

#Create a NumPy array from it as cp_ar. Display array, it's shape, items data type.
print(cp_ar)
print(cp_ar.shape)
print(cp_ar.dtype)              #int64--> 64bits ma chaleko xa



#Assuming a 13% profit, calculate the selling price for each product. Assign it as sp_ar.
sp_ar=cp_ar + cp_ar * 0.13
print(sp_ar)


#Calculate the profit for each product using sp_ar and cp_ar. Assign it as profit_ar.
profit_ar = sp_ar - cp_ar
print(profit_ar)


# Create function price_range that accepts price & categorizes it as low, medium or high depending if its value is below 150, between 150-250 or above 250.
price=int(input("Enter price: "))

def price_range():
    if  price>250:
        print("High")
    elif price > 150 or price <


