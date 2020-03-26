import duka.app.app as import_ticks_method
from duka.core.utils import TimeFrame
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import plotly as py
from plotly import tools
import plotly.graph_objs as go

start_date=datetime.date(2019,1,1)
end_date=datetime.date(2019,1,2)
Assets=["EURUSD"]

#import_ticks_method(Assets,start_date,end_date,1,TimeFrame.M5,".",True)

tick_data = pd.read_csv("EURUSD-2019_01_01-2019_01_02.csv")
tick_data.columns = ['date','open','close','high','low']
tick_data.date=pd.to_datetime(tick_data.date,format='%Y-%m-%d %H:%M:%S.%f')

tick_data=tick_data.set_index(tick_data.date)
del tick_data['date']
# Using DataFrame.insert() to add a column
tick_data.insert(4, "Volume", tick_data['close']-tick_data['open'], True)
#tick_data=tick_data['open','close','high','low']
tick_data=tick_data.drop_duplicates(keep=False)
ma = tick_data.close.rolling(center=False,window=30).mean()
print(tick_data)

trace0=go.Ohlc(x=tick_data.index,open=tick_data.open,high=tick_data.high,low=tick_data.low,close=tick_data.close,name='Currency Quote')
trace1=go.Scatter(x=tick_data.index,y=ma)
trace2=go.Bar(x=tick_data.index,y=tick_data['Volume'])

data=[trace0,trace1,trace2]

py.offline.plot(data,filename='tutorial.html')