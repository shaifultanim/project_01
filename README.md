# House-rent-predicdion

# 🏠 House Price Predictor using Linear Regression

This is a simple Python program that uses **Linear Regression** from `scikit-learn` to predict the price of a house based on its area (in square feet). The model is trained on sample data and takes user input to make a prediction.

## 📋 Features

* Uses **scikit-learn's LinearRegression** to train a model.
* Sample dataset: Area vs Price.
* Takes user input for the area of a house.
* Predicts and prints the expected price in Bangladeshi Taka (Tk).

## 🧪 Sample Data

The sample training data used in the code:

| Area (sqft) | Price (Tk) |
| ----------- | ---------- |
| 1000        | 20000      |
| 1500        | 30000      |
| 2000        | 40000      |
| 2500        | 50000      |
| 30000       | 60000      |

## 🚀 How to Run

1. Make sure Python is installed on your system.

2. Install the required package if not already installed:

   ```bash
   pip install pandas scikit-learn
   ```

3. Run the script:

   ```bash
   python house_price_predictor.py
   ```

4. Enter the area in square feet when prompted.

## 🧠 Example

```
Enter the are of the house in square feet:
2200
Predicted price: Tk43,636.36
Predicted price : Tk43,636
```

## ⚠️ Note

* This model uses a **very small dataset** and should only be used for learning purposes.
* One of the area values (30,000 sqft) seems unusually high and may affect prediction accuracy. Consider cleaning or scaling data in real-world scenarios.

## 📁 Project Structure

```
house_price_predictor.py
README.md
```

## 📜 License

This project is released under the MIT License.
