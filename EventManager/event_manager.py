from tkinter import *
from PIL import Image, ImageTk
import datetime

employees = []
events = []

class event():
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end
        self.assigneds = []
    def incharge(self, emplyee):
        self.assigneds.append(employee)
	
class employee():
    def __init__(self, name):
        self.name = name
        self.busy = []
    def atribute(self, event):
        self.busy.append(event)

def create_event():
    event_w = Toplevel()
    event_w.geometry("310x552")
    event_w.config(bg = "#2c465b")
    
    menu = Frame(event_w, bg = "#f4d039", width=310, height = 44)
    menu.pack()
    area = Frame(event_w, bg = "#2c465b", width=310, height = 505)
    area.pack()
    
    logo = Image.open('logo.gif')
    logo = logo.resize((int(logo.width*2/3),int(logo.height*2/3)))
    logo = ImageTk.PhotoImage(logo)
    # logo = logo.zoom(2)
    # logo = logo.subsample(3)
    Label(menu, bg = "#f4d039", image = logo).place(x = 155, y = 22, anchor = CENTER)

    Frame(area, bg = "#2c465b", width=310, height = 88).grid(row = 0, column = 0)
    Label(area, text = "Event Name:", fg = "white", bg = "#2c465b").grid(row = 1, column = 0)
    t_frame = Frame(area, bg = "white", width=215, height = 45)
    t_frame.grid(row = 2, column = 0, pady = 5)
    text = Entry(t_frame, width=35)
    text.pack(fill = X)
    Frame(area, bg = "#2c465b", width=310, height = 40).grid(row = 3, column = 0)
    Label(area, text = "Start Date:", fg = "white", bg = "#2c465b").grid(row = 4, column = 0)
    sdata = Frame(area, bg = "#2c465b", width=310, height = 45)
    sdata.grid(row = 5, column = 0, pady = 5)

    s_d = StringVar(event_w)
    s_d.set("day")
    s_m = StringVar(event_w)
    s_m.set("month")
    s_y = StringVar(event_w)
    s_y.set("year")
    
    p1 = OptionMenu(sdata, s_d, '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
    p1.grid(row = 0, column = 0, padx = 2)
    p1.config(bg = "white", fg = "#2c465b", highlightthickness=0, relief = FLAT)
    p2 = OptionMenu(sdata, s_m, '01','02','03','04','05','06','07','08','09','10','11','12')
    p2.grid(row = 0, column = 1, padx = 2)
    p2.config(bg = "white", fg = "#2c465b", highlightthickness=0, relief = FLAT)
    p3 = OptionMenu(sdata, s_y, '2018','2019','2020')
    p3.grid(row = 0, column = 2, padx = 2)
    p3.config(bg = "white", fg = "#2c465b", highlightthickness=0, relief = FLAT)

    Frame(area, bg = "#2c465b", width=310, height = 45).grid(row = 6, column = 0)
    Label(area, text = "End Date:", fg = "white", bg = "#2c465b").grid(row = 7, column = 0)
    edata = Frame(area, bg = "#2c465b", width=310, height = 45)
    edata.grid(row = 8, column = 0)
    
    e_d = StringVar(event_w)
    e_d.set("day")
    e_m = StringVar(event_w)
    e_m.set("month")
    e_y = StringVar(event_w)
    e_y.set("year")

    p4 = OptionMenu(edata, e_d, '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
    p4.grid(row = 0, column = 0, padx = 2)
    p4.config(bg = "white", fg = "#2c465b", highlightthickness=0, relief = FLAT)
    p5 = OptionMenu(edata, e_m, '01','02','03','04','05','06','07','08','09','10','11','12')
    p5.grid(row = 0, column = 1, padx = 2)
    p5.config(bg = "white", fg = "#2c465b", highlightthickness=0, relief = FLAT)
    p6 = OptionMenu(edata, e_y, '2018','2019','2020')
    p6.grid(row = 0, column = 2, padx = 2)
    p6.config(bg = "white", fg = "#2c465b", highlightthickness=0, relief = FLAT)
    
    Frame(area, bg = "#2c465b", width=310, height = 45).grid(row = 9, column = 0)
    Button(area, text = 'Create', bg = "#f4d039", fg = "#2c465b", width = 12, command = lambda: ev_create(text.get(),s_d.get(),s_m.get(),s_y.get(),e_d.get(),e_m.get(),e_y.get(),event_w)).grid(row = 10, column = 0)
    
    event_w.mainloop()
    
def ev_create(name, s_d, s_m, s_y, e_d, e_m, e_y, event_w):
    start = datetime.date(day = int(s_d), month = int(s_m), year = int(s_y))
    end = datetime.date(day = int(e_d), month = int(e_m), year = int(e_y))
    events.append(event(name, start, end))
    event_w.destroy()

def remove_event():
    events_name = []
    for i in events:
        events_name.append(i.name)
    
    event_w = Toplevel()
    event_w.geometry("310x552")
    event_w.config(bg = "#2c465b")
    
    menu = Frame(event_w, bg = "#f4d039", width=310, height = 44)
    menu.pack()
    area = Frame(event_w, bg = "#2c465b", width=310, height = 505)
    area.pack(expand = 1)
    
    logo = PhotoImage(file="logo.gif")
    logo = logo.zoom(2)
    logo = logo.subsample(3)
    Label(menu, bg = "#f4d039", image = logo).place(x = 155, y = 22, anchor = CENTER)

    dados = Frame(area, bg = "#2c465b")
    dados.pack()
    Label(dados, text = "Event Name:", fg = "white", bg = "#2c465b").pack()
    name = StringVar(dados)
    name.set("Event")
    w = OptionMenu(dados, name, *events_name)
    w.config(bg = "white", fg = "#2c465b", highlightthickness=0, relief = FLAT, width = 35)
    w.pack(pady = 5)
    
    Button(area, text = 'Remove', width = 10, bg = "#f4d039", fg = "#2c465b", command = lambda: ev_remove(name.get(),event_w)).pack(pady = 10)
    Frame(area, bg = "#2c465b", width=310, height = 44).pack()

    event_w.mainloop()

def ev_remove(name, event_w):
    for i in events:
        if i.name == name:
            break
    events.remove(i)
    event_w.destroy()

def create_employee():
    employee_w = Toplevel()
    employee_w.geometry("310x552")
    employee_w.config(bg = "#2c465b")
    
    menu = Frame(employee_w, bg = "#f4d039", width=310, height = 44)
    menu.pack()
    area = Frame(employee_w, bg = "#2c465b", width=310, height = 505)
    area.pack(expand = 1)
    
    logo = PhotoImage(file="logo.gif")
    logo = logo.zoom(2)
    logo = logo.subsample(3)
    Label(menu, bg = "#f4d039", image = logo).place(x = 155, y = 22, anchor = CENTER)

    dados = Frame(area, bg = "#2c465b")
    dados.pack()
    Label(dados, text = "Employee Name:", fg = "white", bg = "#2c465b").pack()
    text = Entry(dados, width=35)
    text.pack(pady = 5)
    Button(dados, text = 'Create', width = 10, bg = "#f4d039", fg = "#2c465b", command = lambda: emp_create(text.get(),employee_w)).pack(pady = 10)
    Frame(area, bg = "#2c465b", width=310, height = 44).pack()
    
    employee_w.mainloop()

def emp_create(name, employee_w):
    employees.append(employee(name))
    employee_w.destroy()

def remove_employee():
    employees_name = []
    for i in employees:
        employees_name.append(i.name)
    
    employee_w = Toplevel()
    employee_w.geometry("310x552")
    employee_w.config(bg = "#2c465b")
    
    menu = Frame(employee_w, bg = "#f4d039", width=310, height = 44)
    menu.pack()
    area = Frame(employee_w, bg = "#2c465b", width=310, height = 505)
    area.pack(expand = 1)
    
    logo = PhotoImage(file="logo.gif")
    logo = logo.zoom(2)
    logo = logo.subsample(3)
    Label(menu, bg = "#f4d039", image = logo).place(x = 155, y = 22, anchor = CENTER)

    dados = Frame(area, bg = "#2c465b")
    dados.pack()
    Label(dados, text = "Employee Name:", fg = "white", bg = "#2c465b").pack()
    name = StringVar(dados)
    name.set("Employee")
    w = OptionMenu(dados, name, *employees_name)
    w.config(bg = "white", fg = "#2c465b", highlightthickness=0, relief = FLAT, width = 35)
    w.pack(pady = 5)
    
    Button(area, text = 'Remove', width = 10, bg = "#f4d039", fg = "#2c465b", command = lambda: emp_remove(name.get(),employee_w)).pack(pady = 10)
    Frame(area, bg = "#2c465b", width=310, height = 44).pack()

    employee_w.mainloop()

def emp_remove(name, employee_w):
    for i in employees:
        if i.name == name:
            break
    employees.remove(i)
    employee_w.destroy()

def show_events():
    event_w = Toplevel()
    event_w.geometry("310x552")
    event_w.config(bg = "#2c465b")
    
    menu = Frame(event_w, bg = "#f4d039", width=310, height = 44)
    menu.pack()
    area = Frame(event_w, bg = "#2c465b", width=310, height = 505)
    area.pack(expand = 1)
    
    logo2 = PhotoImage(file="logo.gif")
    logo2 = logo2.zoom(2)
    logo2 = logo2.subsample(3)
    Label(menu, bg = "#f4d039", image = logo2).place(x = 155, y = 22, anchor = CENTER)

    tabela = Frame(area, bg = "#2c465b")
    tabela.pack()
    Button(tabela, text = "Event Name", bg = "#f4d039", fg = "#2c465b", relief = FLAT, bd = 0, width = 10).grid(row = 0, column = 0, padx = 1)
    Button(tabela, text = "Start Date", bg = "#f4d039", fg = "#2c465b", relief = FLAT, bd = 0, width = 10).grid(row = 0, column = 1, padx = 1)
    Button(tabela, text = "End Date", bg = "#f4d039", fg = "#2c465b", relief = FLAT, bd = 0, width = 10).grid(row = 0, column = 2, padx = 1)
    tabela2 = Frame(area, bg = "#2c465b")
    tabela2.pack(pady = 3)
    for i in range(len(events)):
        Label(tabela2, text = events[i].name, bg = "white", width = 10, fg = "#2c465b", wraplength = 75).grid(row = i, column = 0, padx = 1, sticky = N+S)
        Label(tabela2, text = events[i].start.strftime('%d/%b/%Y'), bg = "white", width = 10, fg = "#2c465b").grid(row = i, column = 1, padx = 1, sticky = N+S)
        Label(tabela2, text = events[i].end.strftime('%d/%b/%Y'), bg = "white", width = 10, fg = "#2c465b").grid(row = i, column = 2, padx = 1, sticky = N+S)
    Frame(area, bg = "#2c465b", width=310, height = 44).pack()
    Button(area, text = 'Close', width = 15, bg = "#f4d039", fg = "#2c465b", command = event_w.destroy).pack(pady = 5)
    Frame(area, bg = "#2c465b", width=310, height = 44).pack()

    event_w.mainloop()

def show_employees():
    employee_w = Toplevel()
    employee_w.geometry("310x552")
    employee_w.config(bg = "#2c465b")
    
    menu = Frame(employee_w, bg = "#f4d039", width=310, height = 44)
    menu.pack()
    area = Frame(employee_w, bg = "#2c465b", width=310, height = 505)
    area.pack(expand = 1)
    
    logo2 = PhotoImage(file="logo.gif")
    logo2 = logo2.zoom(2)
    logo2 = logo2.subsample(3)
    Label(menu, bg = "#f4d039", image = logo2).place(x = 155, y = 22, anchor = CENTER)

    tabela = Frame(area, bg = "#2c465b")
    tabela.pack()
    Button(tabela, text = "Employee Name", bg = "#f4d039", fg = "#2c465b", relief = FLAT, bd = 0, width = 17).grid(row = 0, column = 0, padx = 1)
    Button(tabela, text = "Events", bg = "#f4d039", fg = "#2c465b", relief = FLAT, bd = 0, width = 17).grid(row = 0, column = 1, padx = 1)
    tabela2 = Frame(area, bg = "#2c465b")
    tabela2.pack(pady = 3)
    i = 0
    for emp in employees:
        ev_names = ''
        for ev in emp.busy:
            ev_names += ev.name + '; '
        Label(tabela2, text = emp.name, bg = "white", width = 17, fg = "#2c465b", wraplength = 100).grid(row = i, column = 0, padx = 1, sticky = N+S)
        Label(tabela2, text = ev_names, bg = "white", width = 17, fg = "#2c465b", wraplength = 100).grid(row = i, column = 1, padx = 1, sticky = N+S)
        i += 1
    Frame(area, bg = "#2c465b", width=310, height = 44).pack()
    Button(area, text = 'Close', width = 15, bg = "#f4d039", fg = "#2c465b", command = employee_w.destroy).pack(pady = 5)
    Frame(area, bg = "#2c465b", width=310, height = 44).pack()

    employee_w.mainloop()

def assign_employees():
    events_name = []
    for i in events:
        events_name.append(i.name)

    employees_name = []
    for i in employees:
        employees_name.append(i.name)
    
    event_w = Toplevel()
    event_w.geometry("310x552")
    event_w.config(bg = "#2c465b")
    
    menu = Frame(event_w, bg = "#f4d039", width=310, height = 44)
    menu.pack()
    area = Frame(event_w, bg = "#2c465b", width=310, height = 505)
    area.pack(expand = 1)
    
    logo = PhotoImage(file="logo.gif")
    logo = logo.zoom(2)
    logo = logo.subsample(3)
    Label(menu, bg = "#f4d039", image = logo).place(x = 155, y = 22, anchor = CENTER)

    dados = Frame(area, bg = "#2c465b")
    dados.pack()
    Label(dados, text = "Event Name:", fg = "white", bg = "#2c465b").pack(pady = 5)
    ev = StringVar(dados)
    ev.set("Event")
    w1 = OptionMenu(dados, ev, *events_name)
    w1.config(bg = "white", fg = "#2c465b", highlightthickness=0, relief = FLAT, width = 35)
    w1.pack(pady = 5)
    Frame(dados, bg = "#2c465b", height = 25).pack()
    Label(dados, text = "Employee Name:", fg = "white", bg = "#2c465b").pack(pady = 5)
    emp = StringVar(dados)
    emp.set("Employee")
    w2 = OptionMenu(dados, emp, *employees_name)
    w2.config(bg = "white", fg = "#2c465b", highlightthickness=0, relief = FLAT, width = 35)
    w2.pack(pady = 5)
    Frame(dados, bg = "#2c465b", height = 25).pack()
    Button(area, text = 'Assign', width = 10, bg = "#f4d039", fg = "#2c465b", command = lambda: do_assign(ev.get(),emp.get(),assigned)).pack(pady = 5)
    Frame(area, bg = "#2c465b", width = 310, height = 5).pack(pady = 5)
    assigned = Label(area, text = "", fg = "white", bg = "#2c465b", height = 4, wraplength = 200)
    assigned.pack(pady = 5)
    Frame(area, bg = "#2c465b", width=310, height = 5).pack(pady = 5)
    Button(area, text = 'Close', width = 10, bg = "#f4d039", fg = "#2c465b", command = event_w.destroy).pack(pady = 5)
    Frame(area, bg = "#2c465b", width=310, height = 10).pack(pady = 5)

    event_w.mainloop()

def main_screen():
    screen = Tk()
    screen.geometry("310x552")
    screen.config(bg = "#2c465b")
    
    menu = Frame(screen, bg = "#f4d039", width=310, height = 44)
    menu.pack()
    area = Frame(screen, bg = "#2c465b", width=310, height = 505)
    area.pack(expand = 1)
    
    logo = PhotoImage(file="logo.gif")
    logo = logo.zoom(2)
    logo = logo.subsample(3)
    Label(menu, bg = "#f4d039", image = logo).place(x = 155, y = 22, anchor = CENTER)

    Label(area, text = "Events:", fg = "white", bg = "#2c465b").pack(pady = 5)
    Button(area, text = 'Create Event', width = 15, bg = "#f4d039", fg = "#2c465b", command = create_event).pack(pady = 5)
    Button(area, text = 'Remove Event', width = 15, bg = "#f4d039", fg = "#2c465b", command = remove_event).pack(pady = 5)
    Button(area, text = 'Show Events', width = 15, bg = "#f4d039", fg = "#2c465b", command = show_events).pack(pady = 5)
    Label(area, text = "Employees:", fg = "white", bg = "#2c465b").pack(pady = 5)
    Button(area, text = 'Create Employee', width = 15, bg = "#f4d039", fg = "#2c465b", command = create_employee).pack(pady = 5)
    Button(area, text = 'Remove Employee', width = 15, bg = "#f4d039", fg = "#2c465b", command = remove_employee).pack(pady = 5)
    Button(area, text = 'Show Employees', width = 15, bg = "#f4d039", fg = "#2c465b", command = show_employees).pack(pady = 5)
    Frame(area, bg = "#2c465b", width=310, height = 10).pack(pady = 5)
    Button(area, text = 'Assign Employee to Event', width = 25, bg = "#f4d039", fg = "#2c465b", command = assign_employees).pack(pady = 5)
    Frame(area, bg = "#2c465b", width=310, height = 44).pack(pady = 5)
    Button(area, text = 'Close', width = 15, bg = "#f4d039", fg = "#2c465b", command = screen.destroy).pack(pady = 5)
    
    screen.mainloop()

def do_assign(ev_name,emp_name,assigned):
    for ev in events:
        if ev.name == ev_name:
            break
    for emp in employees:
        if emp.name == emp_name:
            break
    check = check_conflict(ev,emp)
    if check == True:
        ev.incharge(emp)
        emp.atribute(ev)
        assigned["text"] = emp.name + " assigned to " + ev.name
    else:
        assigned["text"] = emp.name + " is busy with " + check

def check_conflict(ev,emp):
    for i in emp.busy:
        if ev.start >= i.start and ev.start <= i.end:
            return i.name
        if ev.end >= i.start and ev.end <= i.end:
            return i.name
    return True
            
ev_create("ev1", '01', '01', '2018', '10', '01', '2018', Tk())
ev_create("ev2", '03', '01', '2018', '01', '02', '2018', Tk())
ev_create("ev3", '30', '12', '2017', '02', '01', '2018', Tk())
ev_create("evento que tem um nome muito grande", '30', '12', '2019', '02', '01', '2019', Tk())
emp_create("Beatriz", Tk())
emp_create("Pedro", Tk())
emp_create("Leonardo", Tk())
emp_create("Funcionário que tem um nome muito grande", Tk())

main_screen()

