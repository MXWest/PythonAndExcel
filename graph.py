import openpyxl
from openpyxl.chart import PieChart, Reference

wb = openpyxl.Workbook()
ws = wb.active

rows = [
    ["Flavor", "Qty Sold"],
    ["Vanilla", 1599],
    ["Butter Pecan", 1700],
    ["Strawberry", 600],
    ["Pumpkin Spice", 951],
]

for row in rows:
    ws.append(row)

chart = PieChart()
labels = Reference(ws, min_col=1, min_row=2, max_row=5)
values = Reference(ws, min_col=2, min_row=1, max_row=5)
chart.add_data(values, titles_from_data=True)
chart.set_categories(labels)
chart.title = "Ice Cream Sales by Flavor"
ws.add_chart(chart, "C1")
wb.save("data/pie_chart.xlsx")
