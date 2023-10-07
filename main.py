import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib
import requests
from datetime import datetime as dt

matplotlib.use("TkAgg")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("API Cotação do dólar")
        self.figure = Figure(figsize=(15, 6), dpi=100)
        self.figure_canvas = FigureCanvasTkAgg(self.figure, self)
        NavigationToolbar2Tk(self.figure_canvas, self)
        self.chart = self.figure.add_subplot()
        self.current_value = tk.StringVar(value=10)
        self.cmd_executar()
        self.figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.spin_range = ttk.Spinbox(
            self,
            from_=1,
            to=60,
            textvariable=self.current_value,
            wrap=True,
            font=("Arial 18 bold")
        )
        self.spin_range.pack(fill="x", side="left", expand=True, padx=5)
        ttk.Button(
            self, text="Mostrar",
            command=self.cmd_executar
        ).pack(fill="x", side="left", expand=True, padx=5)

    def cmd_executar(self):
        cotacoes = requests.get(f"https://economia.awesomeapi.com.br/json/daily/USD-BRL/{self.current_value.get()}")
        x_data = []
        y_data = []
        y_data2 = []
        y_data3 = []
        y_data4 = []

        for x in cotacoes.json():
            ts = int(x["timestamp"])
            x_eixo = dt.fromtimestamp(ts).strftime("%d/%m\n/%Y")
            x_data.insert(0, x_eixo)
            y_data.insert(0, float(x["bid"]))
            y_data2.insert(0, float(x["ask"]))
            y_data3.insert(0, float(x["low"]))
            y_data4.insert(0, float(x["high"]))

        self.chart.clear()    
            
        self.chart.plot(x_data, y_data, marker="o", label="Compra")
        self.chart.plot(x_data, y_data2, marker="o", label="Venda")
        self.chart.plot(x_data, y_data3, marker="o", label="Mínimo")
        self.chart.plot(x_data, y_data4, marker="o", label="Máximo")     

        self.chart.set_title(cotacoes.json()[0]['name'])
        self.chart.set_xlabel("Datas")
        self.chart.set_ylabel("BRL")
        self.chart.grid()
        self.chart.legend()
        self.figure_canvas.draw()   

if __name__ == "__main__":
    app = App()
    app.mainloop()
