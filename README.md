
# Web Scraper Project

# Giới thiệu

Dự án Web Scraper này cho phép người dùng thu thập dữ liệu (Gồm DOM Content, các links và tất cả các ảnh) từ các trang web một cách dễ dàng thông qua giao diện người dùng trực quan được xây dựng bằng Streamlit. Dự án sử dụng các công nghệ như Selenium và BeautifulSoup để trích xuất thông tin từ các trang web.

# Công nghệ sử dụng

- Python: Ngôn ngữ lập trình chính cho dự án.
- Selenium: Thư viện cho phép tự động hóa trình duyệt web.
- BeautifulSoup: Thư viện dùng để phân tích cú pháp HTML và XML, giúp trích xuất dữ liệu dễ dàng.
- Streamlit: Thư viện giúp xây dựng giao diện người dùng một cách nhanh chóng và dễ dàng.
- ChromeDriver: Trình điều khiển cho phép Selenium tương tác với trình duyệt Google Chrome.
- venv: Công cụ quản lý môi trường ảo cho Python.

# Cài đặt

# 1. Cài đặt Python

Đảm bảo rằng bạn đã cài đặt Python (tối thiểu phiên bản 3.6). Bạn có thể tải Python tại [python.org](https://www.python.org/downloads/).

# 2. Tạo môi trường ảo

Mở terminal và chạy các lệnh sau để tạo và kích hoạt môi trường ảo:

```bash
# Tạo môi trường ảo
python -m venv venv

# Kích hoạt môi trường ảo
# Trên Windows
venv\Scripts\activate

# Trên macOS/Linux
source venv/bin/activate
```

### 3. Cài đặt các thư viện cần thiết

Cài đặt các thư viện cần thiết bằng pip:

```bash
pip install selenium beautifulsoup4 streamlit
```

# 4. Cài đặt ChromeDriver

Tải ChromeDriver từ [trang chủ ChromeDriver](https://sites.google.com/chromium.org/driver/downloads) và đảm bảo rằng phiên bản tương thích với phiên bản Chrome của bạn. Giải nén và lưu trữ ChromeDriver trong một thư mục trên máy của bạn.

## 5. Chạy ứng dụng

Sau khi hoàn thành các bước trên, bạn có thể chạy ứng dụng Streamlit bằng lệnh sau:

```bash
streamlit run main.py
```

# Sử dụng

1. Mở trình duyệt và truy cập vào địa chỉ được cung cấp trong terminal.
2. Nhập URL của trang web bạn muốn thu thập dữ liệu.
3. Nhấn nút "Scrape" để bắt đầu quá trình thu thập dữ liệu.
4. Dữ liệu thu thập sẽ được hiển thị trên giao diện người dùng.

# Ghi chú

- Đảm bảo rằng bạn tuân thủ các quy định về quyền riêng tư và điều khoản sử dụng của các trang web khi thu thập dữ liệu.
- Nếu bạn gặp phải lỗi NoSuchDriverException, hãy kiểm tra xem ChromeDriver đã được cài đặt đúng cách và có đường dẫn chính xác trong mã của bạn.

# Liên hệ

Nếu bạn có bất kỳ câu hỏi nào, vui lòng liên hệ với tôi qua email: [huynhvanvietkt@gmail.com]

---

Cảm ơn bạn đã xem dự án Web Scraper này!

