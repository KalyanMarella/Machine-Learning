from datetime import datetime
now=datetime.now()
print("Date and time: ",now)
print("Date: ",now.date())
print("Year: ",now.year)
print("Month: ",now.month)
print("Day: ",now.day)
print("Time: ",now.time())

## time delta
delta=datetime.now()-datetime(2011,4,10)
print("Days: ",delta.days)
print("Time: ",delta.seconds)


## Conversion from datetime to string
strg1=str(now)
strg2=now.strftime('%Y-%m-%d')
print(strg1,"\n",strg2)
print(type(strg1),"\n",type(strg2))

## Conversion from string to datetime
strg1="2023-4-10"
strg2="2023-4-17"
date1=datetime.strptime(strg1,"%Y-%m-%d")
date2=datetime.strptime(strg2,"%Y-%m-%d")
print(date1,"\n",date2)
print(type(date1),"\n",type(date2))


## Converting from string to datetime using dateutil parser
from dateutil.parser import parse
print(parse('2024-4-17'))
print(parse('Apr 17,2024'))
print(parse('17/4/2024',dayfirst=True))

## converting string to datetime using pd.to_datetime
import pandas as pd
dates=['2024/4/17','2024/3/8','2024/6/15']
print(pd.to_datetime(dates))

print(datetime(2003,4,10).strftime("%A"))  # weekday name
print(datetime(2003,4,10).strftime("%B"))  # month name
print(datetime(2003,4,10).strftime("%c"))   # date and time stamp
print(datetime(2003,4,10,20,20).strftime("%p"))  # AM or PM for the time


## date range
import numpy as np
df=pd.Series(np.random.randn(1000),index=pd.date_range('2024-4-17',periods=1000))
print(df[:10])
print(df['2024'][:10])
print(df['2024-05'][:10])

print(df['2024/4'])

## timeseries index with duplicate index

dates=[datetime(2003,4,11),datetime(2003,4,11),datetime(2003,4,10),datetime(2003,4,10),datetime(2006,11,17),datetime(2006,11,17)]
df=pd.Series(np.random.randn(6),index=dates)

print(df)

grpd=df.groupby(level=0)
grpd.mean()
print(grpd.mean())


## truncate after/before specific date 
df1=pd.Series(np.random.randn(100),index=pd.date_range('2024-3-29',periods=100))
print(df1.truncate(after='2024/4/17'))
print(df1.truncate(before='2024-4-17'))

## using .loc method

df2=pd.DataFrame(np.random.randn(50,4),pd.date_range('2024-3-29',periods=50),columns=['A','B','C','D'])
print(df2.head())
print(df2.loc['2024-5'])

## Frqeuencies,date_ranges,shifting

# converting from non-frequent to frequent
dates=[datetime(2024,3,29),datetime(2024,3,31),datetime(2024,4,1),datetime(2024,4,4),datetime(2024,4,5),datetime(2024,4,7),datetime(2024,4,9),datetime(2024,3,11),datetime(2024,4,15),datetime(2024,4,17)]
df3=pd.Series(np.random.randn(10),index=dates)
print(df3)
samp=df3.resample('D')
print(samp)
## revisting 


# date_ranges
print(pd.date_range('4/1/2024',periods=10)) ## if / used in mentioning date,use format m/d/y
print(pd.date_range('2024-4-17',periods=10)) ## if - used in mentioning date,use format y-m-d

## date ranges with frequency
# 1 is business end of month use "BM"
print(pd.date_range('2024-4-1',periods=10,freq='BM'))

# date_ranges with time along
print(pd.date_range('5/2/2012 12:56:31',periods=5))
# to normalize or to bring the time to 0:0:0 use normalize as True
print(pd.date_range('5/2/2012 12:56:31',periods=10,normalize=True))


## printing date_range with frequency 2Hrs
print(pd.date_range('2024-3-29',periods=10,freq='2h'))

## printing date_range with frequency 2Hrs30min
print(pd.date_range('2024-3-29',periods=10,freq='2h30min'))


## printing date_range with frequency 2Days
print(pd.date_range('2024-3-29',periods=10,freq='2D'))


## printing date_range with frequency Month begining
print(pd.date_range('2024-3-29',periods=10,freq='MS')) # MS for month start,just M for Month end

## printing date_range with frequency Business Month Begining
print(pd.date_range('2024-3-29',periods=10,freq='BMS'))


## printing date_range with frequency last business day of month
print(pd.date_range('2024-3-29',periods=10,freq='BM'))


## printing date_range with frequency end of month
print(pd.date_range('2024-3-29',periods=10,freq='M'))


## printing date_range with frequency 1st tuesday of every month
print(pd.date_range('2024-3-29',periods=10,freq='WOM-1TUE'))

## printing date_range with frequency 2 wednesday of every month
print(pd.date_range('2024-3-29',periods=10,freq='WOM-2WED'))

## printing date_range with frequency 3rd wednesday of every month
print(pd.date_range('2024-3-29',periods=10,freq='WOM-3WED'))

# printing date_range with frequency week day
print(pd.date_range('2024-3-29',periods=10,freq='W-WED'))



## printing date_range with frequency mentioned month end of every year
print(pd.date_range('2024-3-29',periods=10,freq='A-JAN'))

## printing date_range with frequency mentioned month start of every year
print(pd.date_range('2024-3-29',periods=10,freq='AS-JAN'))

print(datetime(2024,7,31).strftime('%A'))

## time shifting or shifting

df=pd.Series(np.random.randn(10),pd.date_range('2024-03-31',periods=10,freq='M'))
print(df)

print(df.shift(2))

print(df.shift(-2))

print(df.shift(2,freq='M'))

print(df.shift(2,freq='W'))

dates=['2024-4-10','2024-5-5','2024-6-1','2024-7-13']
dates=pd.to_datetime(dates)
print(dates)

df=pd.DataFrame(np.random.randn(4,4),index=dates,columns=['Abc','Def','Ghi','Jkl'])

print(df)
from pandas.tseries.offsets import Day,MonthEnd
offset=MonthEnd()
print(df.groupby(offset.rollback).mean())

print(df.groupby(offset.rollforward).mean())


print(df.shift(freq='M'))

now=datetime(2024,4,6)

print(now)

print(now+MonthEnd())

print(now+MonthEnd(2))

print(df)


print(df.index.tz)

## localizing to timezone i.e to 'UTC'

df_utc=df.tz_localize('UTC')
print(df_utc)

## conversion of timezones
print(df_utc.tz_convert('US/Eastern'))

timest=pd.Timestamp('2024-3-31 15:36')
timest=timest.tz_localize('Asia/Kolkata')
print(timest.tz_convert('UTC'))
print(timest)
print(timest.tz_convert('Europe/Berlin'))
print(timest.tz_convert('Asia/Kolkata'))

## combination of two time zones addition makes the timezone as UTC

df_time=pd.Series(np.random.randn(14),index=pd.date_range('2024-3-31',periods=14,freq='2D'))
print(df_time)
time1=df_time[:7].tz_localize('Asia/Kolkata')
time2=df_time[7:].tz_localize('Europe/Berlin')

print(time1)

print(time2)

res=time1+time2
print(res.index)