import math
from app.reports import CPI_report
from app.reports.SP500_report import SP500
from .tools.get_requests import WebRequest # I don't think I need this cause I won't actaully call any webrequests in main

x = CPI_report.CPI_data.main_report()
y = SP500.main_report()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"CPI (Consumer Price Index) has change {x:.2f}% since {CPI_report.start_date} to 2024-01-01")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"The SP500 has move {y} points since start of year")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

