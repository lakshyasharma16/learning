import datetime

date_1 = date(2014, 7, 2)
date_2 = date(2014, 7, 11)

# date_1_obj=datetime.date(2014,7,2)
# date_2_obj=datetime.date(2014,7,11)

date_1_obj = datetime.date(date_1)
date_2_obj = datetime.date(date_2)

print(date_1_obj)
print(date_2_obj)
