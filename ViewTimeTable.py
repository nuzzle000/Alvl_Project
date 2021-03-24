from tkinter import ttk
from tkcalendar import Calendar
cal = Calendar(top, selectmode='none')
date = cal.datetime.today() + cal.timedelta(days=2)
cal.calevent_create(date, 'Hello World', 'message')
cal.calevent_create(date, 'Reminder 2', 'reminder')
cal.calevent_create(date + cal.timedelta(days=-2), 'Reminder 1', 'reminder')
cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')

cal.tag_config('reminder', background='red', foreground='yellow')

cal.pack(fill="both", expand=True)
ttk.Label(top, text="Hover over the events.").pack()