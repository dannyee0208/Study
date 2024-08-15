import datetime
#import=모듈(데이터)를 갖고 온다
d=datetime.date.today()
print(d.isoformat())

#code 1,2
import datetime
print(str(datetime.datetime.today()[:10]))
#or 
print(str(datetime.datetime.now())[:10])
