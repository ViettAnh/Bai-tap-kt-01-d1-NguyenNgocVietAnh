# Ứng Dụng Máy Tính Đơn Giản

Đây là một ứng dụng máy tính đơn giản được xây dựng bằng Python và thư viện tkinter. Ứng dụng này cho phép người dùng thực hiện các phép tính cơ bản (cộng, trừ, nhân, chia) với hai số tự nhiên.

## Cách Hoạt Động

### Giao Diện Người Dùng

Ứng dụng có giao diện đồ họa đơn giản với các thành phần sau:

1. **Ô nhập liệu**: Hai ô để nhập số thứ nhất và số thứ hai.
2. **Nút phép tính**: Bốn nút tương ứng với các phép tính cộng (+), trừ (-), nhân (×), và chia (÷).
3. **Nhãn kết quả**: Hiển thị kết quả của phép tính hoặc thông báo lỗi.

### Cách Chương Trình Hoạt Động

1. **Kiểm tra đầu vào**: Khi người dùng nhập hai số và nhấn một nút phép tính, chương trình sẽ kiểm tra xem các giá trị nhập vào có phải là số tự nhiên hay không.
   - Nếu không phải số tự nhiên (số âm, số thập phân, hoặc ký tự chữ), chương trình sẽ hiển thị thông báo lỗi.

2. **Thực hiện phép tính**: Nếu các giá trị nhập vào hợp lệ, chương trình sẽ thực hiện phép tính tương ứng:
   - Cộng: Tính tổng của hai số
   - Trừ: Tính hiệu của hai số
   - Nhân: Tính tích của hai số
   - Chia: Tính thương của hai số (kiểm tra trường hợp chia cho 0)

3. **Hiển thị kết quả**: Kết quả của phép tính sẽ được hiển thị trong nhãn kết quả.

### Các Hàm Chính

- **is_natural_number(value)**: Kiểm tra xem một giá trị có phải là số tự nhiên hay không.
- **calculate(operation)**: Thực hiện phép tính dựa trên phép toán được chọn.

## Cách Chạy Chương Trình

1. Đảm bảo bạn đã cài đặt Python trên máy tính của mình.
2. Mở terminal hoặc command prompt.
3. Di chuyển đến thư mục chứa file `calculator.py`.
4. Chạy lệnh: `python calculator.py`

## Cách Chỉnh Sửa Mã

Bạn có thể chỉnh sửa mã để thêm các tính năng mới hoặc cải thiện giao diện:

1. **Thêm phép tính mới**: Bạn có thể thêm các phép tính như lũy thừa, căn bậc hai, v.v.
2. **Cải thiện giao diện**: Thay đổi màu sắc, font chữ, kích thước của các thành phần.
3. **Thêm tính năng lưu lịch sử**: Lưu lại các phép tính đã thực hiện.
4. **Thêm bàn phím số**: Thêm các nút số để người dùng có thể nhập số mà không cần sử dụng bàn phím.

## Giải Thích Mã

- **Thư viện tkinter**: Được sử dụng để tạo giao diện đồ họa.
- **Lambda functions**: Được sử dụng để truyền tham số cho hàm khi nhấn nút.
- **Grid layout**: Được sử dụng để sắp xếp các thành phần trên giao diện.
- **Exception handling**: Được sử dụng để xử lý các lỗi khi người dùng nhập dữ liệu không hợp lệ.

Chương trình này là một ví dụ đơn giản về cách sử dụng Python và tkinter để tạo ứng dụng có giao diện đồ họa. Bạn có thể sử dụng nó như một điểm khởi đầu để học về lập trình giao diện đồ họa và phát triển các ứng dụng phức tạp hơn.