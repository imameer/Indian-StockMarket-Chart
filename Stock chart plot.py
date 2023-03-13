from nsepy import get_history
from datetime import date

tikcer = input("enter stock name: ")
data = get_history(symbol=tikcer, start=date(2023,1,1), end=date(2023,3,9))
data[['Close']].plot()
