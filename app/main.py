import math
from app.reports.CPI_report import CPI_data
from app.reports.SP500_report import SP500

x = CPI_data.main_report()
y = SP500.main_report()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"CPI (Consumer Price Index) has change {x:.2f}% since {CPI_data.date_start} to 2024-01-01")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"The SP500 has move {y} points since start of year")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

