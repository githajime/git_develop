from calendar import TextCalendar

year = int(input("年を入力："))
month = int(input("月を入力："))

cal = TextCalendar(6)
cal.prmonth(year, month)
