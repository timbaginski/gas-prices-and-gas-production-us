import pandas as pd 
import matplotlib.pyplot as plt 


def main():
     gas_prices = pd.read_csv('gas-prices-and-gas-production-us\prices.csv')
     gas_prices = gas_prices.iloc[::-1]
     oil_production = pd.read_csv('gas-prices-and-gas-production-us\production.csv')
     oil_production = oil_production.iloc[::-1]
     
     fig, ax = plt.subplots()
     ax.plot(gas_prices.Month, gas_prices.PPG, color="Red")
     ax.set_xlabel('Month')
     ax.set_ylabel('Price', color="Red")
     ax2 = ax.twinx()
     ax2.plot(oil_production.Month, oil_production["Barrels"], color="Blue")
     ax2.set_xlabel('Month')
     ax2.set_ylabel('Thousands of barrels', color="Blue")
     ax.get_xaxis().set_visible(False)
     ax2.get_xaxis().set_visible(False)
     plt.show()


if __name__ == '__main__':
    main()
     
