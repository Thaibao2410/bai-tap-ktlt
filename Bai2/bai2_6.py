j= []  
for i in range(2000,3201):
   
    if(i%7==0) and (i%5!=0): 
       
        j.append(str(i))
        """ Với các số i liên tiếp trong đoạn 2000 đến 3201 nếu i chia 7 dư o và i chia 5 dư khác 0 
        thì thêm vào trong danh sách"""
print(','.join(j))
""".join() là phương thức của chuỗi string dùng để nối các phần tử trong danh sách 
thành 1 chuỗi sử dụng một kỹ tự phân tách """
print("Sinh viên: nguyen thai bao")
print(" MSSV: 235752020710028")
# print: in ra màn hình