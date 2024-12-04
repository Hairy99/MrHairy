import pandas as pd

file_path = r"C:\Users\DELL\Desktop\Book28.xlsx"

data_dd = pd.read_excel(file_path)

ten_tre_1 = sheet_g["Unnamed: 4"]
ngay_sinh_1 = sheet_g["Unnamed: 6"]
cao_1 = sheet_g["Unnamed: 8"]
can_1 = sheet_g["Unnamed: 9"]

ten_tre_2 = sheet_g["Unnamed: 13"]
ngay_sinh_2 = sheet_g["Unnamed: 15"]
cao_2 = sheet_g["Unnamed: 16"]
can_2 = sheet_g["Unnamed: 17"]

roup_1 = pd.DataFrame({
    "TenTre": ten_tre_1,
    "NgaySinh": ngay_sinh_1,
    "Cao": cao_1,
    "Can": can_1
}).dropna(how="all")

group_2 = pd.DataFrame({
    "TenTre": ten_tre_2,
    "NgaySinh": ngay_sinh_2,
    "Cao": cao_2,
    "Can": can_2
}).dropna(how="all")
print(data_dd.sort_values(by = 'Can'))