class PythonSearch:
  def __init__(self):
    try:import Tkinter as tk
    except:import tkinter as tk
    self.r=tk.Tk()
    self.r.title('파이썬 관련 검색')
    self.r['bg'] = 'blue'
    p=__import__('os').path.join(__import__('os').path.dirname(__file__),'python.ico')
    if __import__('os').path.isfile(p):self.r.iconbitmap(p)
    self.r.geometry('400x200+100+100')
    self.e=tk.Entry(self.r)
    self.e.pack()
    self.b=tk.Button(self.r,text='검색',command=self.bc)
    self.b.pack()
    self.r.mainloop()
  def bc(self):
    ev=self.e.get()
    __import__('webbrowser').open(f'https://www.google.com/search?q=파이썬 {ev}')
app=PythonSearch()
