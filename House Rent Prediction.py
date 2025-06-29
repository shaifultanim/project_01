
from sklearn.linear_model import LinearRegression
import pandas as pd
#sample data :Area vs Price
data={
 'Area':[1000,1500,2000,2500,30000],
 'Price':[20000,30000,40000,50000,60000]
}
df=pd.DataFrame(data)

#Show first 5 rows
print("Data Preview:")
print(df.head())
#train a simple model
X=df[['Area']]
Y=df['Price']
#create and train model
model=LinearRegression()
model.fit(X,Y)
#take user input for area
area=float(input("Enter the area of the house in square feet:\n"))
#Predict price of a 2200 sqft house
predicted_price=model.predict([[area]])
print(f"Predicted price:Tk{predicted_price[0]:,.2f}\n")
print(f"Predicted price :Tk{int(predicted_price[0]):,}")
