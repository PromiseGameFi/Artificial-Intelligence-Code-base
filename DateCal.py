import datetime
import calendar
from tkinter import *

def calculate_days():
    today = datetime.datetime.now()
    year = today.year
    days_in_year = 365
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_year = 366
    month = today.month
    days_in_month = calendar.monthrange(year, month)[1]
    days_used = (today.hour // 8) + (today.day - 1) * 3
    days_left = (days_in_month - today.day)*3 + (days_in_year - days_used)
    days_left_in_month = (days_in_month - today.day)*3
    days_used_list = [0] * days_in_month
    days_left_list = [0] * days_in_month
    for i in range(1,days_in_month+1):
        days_used_list[i-1] = (i-1)*3
        days_left_list[i-1] = (days_in_month - i)*3 + (days_in_year - days_used_list[i-1])
    return days_used, days_left, days_in_month, days_left_in_month, days_used_list, days_left_list

def display_days():
    days_used, days_left, days_in_month, days_left_in_month, days_used_list, days_left_list = calculate_days()
    days_used_label.config(text=f'Days used: {days_used}')
    days_left_label.config(text=f'Days left: {days_left}')
    days_in_month_label.config(text=f'Days in current month: {days_in_month}')
    days_left_in_month_label.config(text=f'Days left in current month: {days_left_in_month}')
    days_used_list_label.config(text=f'Days used for each day: {days_used_list}')
    days_left_list_label.config(text=f'Days left for each day: {days_left_list}')

root = Tk()
root.title('Days Calculator')

days_used_label = Label(root, text='Days used:')
days_used_label.pack()

days_left_label = Label(root, text='Days left:')
days_left_label.pack()

days_in_month_label = Label(root, text='Days in current month:')
days_in_month_label.pack()

days_left_in_month_label = Label(root, text='Days left in current month:')
days_left_in_month_label.pack()

days_used_list_label = Label(root, text='Days used for each day:')
days_used_list_label.pack()

days_left_list_label = Label(root, text='Days left for each day:')
days_left_list_label.pack()

refresh_button = Button(root, text='Refresh', command=display_days)
refresh_button.pack()

display_days()
root.mainloop()

