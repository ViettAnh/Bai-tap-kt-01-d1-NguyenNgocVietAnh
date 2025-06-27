import tkinter as tk
from tkinter import messagebox

def is_natural_number(value):
    """
    Kiểm tra xem giá trị nhập vào có phải là số tự nhiên hay không
    """
    try:
        num = int(value)
        return num >= 0
    except ValueError:
        return False

def calculate(operation):
    """
    Thực hiện phép tính dựa trên phép toán được chọn
    """
    # Lấy giá trị từ ô nhập liệu
    num1 = entry_num1.get()
    num2 = entry_num2.get()
    
    # Kiểm tra xem giá trị nhập vào có phải là số tự nhiên hay không
    if not is_natural_number(num1) or not is_natural_number(num2):
        result_label.config(text="Lỗi: Vui lòng nhập số tự nhiên")
        return
    
    # Chuyển đổi giá trị nhập vào thành số nguyên
    num1 = int(num1)
    num2 = int(num2)
    
    # Thực hiện phép tính tương ứng
    if operation == "+":
        result = num1 + num2
        result_label.config(text=f"Kết quả: {result}")
    elif operation == "-":
        result = num1 - num2
        result_label.config(text=f"Kết quả: {result}")
    elif operation == "*":
        result = num1 * num2
        result_label.config(text=f"Kết quả: {result}")
    elif operation == "/":
        # Kiểm tra chia cho 0
        if num2 == 0:
            result_label.config(text="Lỗi: Không thể chia cho 0")
            return
        result = num1 / num2
        # Hiển thị kết quả dưới dạng số nguyên nếu kết quả là số nguyên
        if result.is_integer():
            result = int(result)
        result_label.config(text=f"Kết quả: {result}")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Máy Tính Đơn Giản")
window.geometry("400x300")
window.resizable(False, False)

# Tạo khung chứa các thành phần
frame = tk.Frame(window, padx=20, pady=20)
frame.pack(expand=True)

# Tạo nhãn và ô nhập liệu cho số thứ nhất
label_num1 = tk.Label(frame, text="Số thứ nhất:")
label_num1.grid(row=0, column=0, sticky="w", pady=5)

entry_num1 = tk.Entry(frame, width=15)
entry_num1.grid(row=0, column=1, pady=5, padx=10)

# Tạo nhãn và ô nhập liệu cho số thứ hai
label_num2 = tk.Label(frame, text="Số thứ hai:")
label_num2.grid(row=1, column=0, sticky="w", pady=5)

entry_num2 = tk.Entry(frame, width=15)
entry_num2.grid(row=1, column=1, pady=5, padx=10)

# Tạo khung chứa các nút phép tính
button_frame = tk.Frame(frame)
button_frame.grid(row=2, column=0, columnspan=2, pady=10)

# Tạo các nút phép tính
button_add = tk.Button(button_frame, text="+", width=5, command=lambda: calculate("+"))
button_add.grid(row=0, column=0, padx=5)

button_subtract = tk.Button(button_frame, text="-", width=5, command=lambda: calculate("-"))
button_subtract.grid(row=0, column=1, padx=5)

button_multiply = tk.Button(button_frame, text="×", width=5, command=lambda: calculate("*"))
button_multiply.grid(row=0, column=2, padx=5)

button_divide = tk.Button(button_frame, text="÷", width=5, command=lambda: calculate("/"))
button_divide.grid(row=0, column=3, padx=5)

# Tạo nhãn hiển thị kết quả
result_label = tk.Label(frame, text="Kết quả: ", font=("Arial", 12))
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Thêm hướng dẫn sử dụng
instruction_label = tk.Label(frame, text="Nhập hai số tự nhiên và chọn phép tính", font=("Arial", 8), fg="gray")
instruction_label.grid(row=4, column=0, columnspan=2)

# Khởi chạy vòng lặp chính của ứng dụng
window.mainloop()