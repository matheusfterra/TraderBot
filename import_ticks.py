import duka.app.app as import_ticks_method
from duka.core.utils import TimeFrame
import datetime
import pandas as pd
import matplotlib.pyplot as plt

start_date=datetime.date(2019,1,1)
end_date=datetime.date(2019,1,2)
Assets=["EURUSD"]

#import_ticks_method(Assets,start_date,end_date,1,TimeFrame.M5,".",True)

tick_data = pd.read_csv("EURUSD-2019_01_01-2019_01_02.csv")
print(tick_data)
plt.plot(tick_data['high'])
plt.plot(tick_data['low'])
plt.show()