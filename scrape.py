from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

SBR_WEBDRIVER = "C:/Users/viet/OneDrive/Desktop/AI-Web-Scraper-main/chromedriver.exe"  # Đường dẫn đến WebDriver

def setup_webdriver():
    # Cấu hình Chrome Options để chạy WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Chạy chế độ không hiển thị trình duyệt
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Khởi tạo WebDriver từ đường dẫn được chỉ định
    driver = webdriver.Chrome(service=Service(SBR_WEBDRIVER), options=chrome_options)
    return driver

def scrape_website(website):
    # Kết nối và điều khiển trình duyệt
    print("Connecting to Scraping Browser...")
    driver = setup_webdriver()

    driver.get(website)
    print("Waiting for the page to load...")
    time.sleep(3)  # Đợi một chút để trang web tải xong (tùy chỉnh thời gian theo trang web cụ thể)
    print("Navigated! Scraping page content...")

    # Lấy HTML của trang web
    html = driver.page_source

    # Đóng trình duyệt sau khi lấy dữ liệu
    driver.quit()

    print("Scraped page content successfully!")
    return html

def extract_body_content(html_content):
    # Kiểm tra xem html_content có phải là chuỗi và không rỗng không
    if not isinstance(html_content, str) or not html_content.strip():
        print("HTML content is empty or not a string.")
        return {
            "body": "",  # Trả về một chuỗi rỗng nếu không có nội dung
            "links": [],
            "images": []
        }
    
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body

    # Lấy các liên kết và hình ảnh
    links = [a['href'] for a in soup.find_all('a', href=True)]
    images = [img['src'] for img in soup.find_all('img', src=True)]

    if body_content:
        return {
            "body": str(body_content),
            "links": links,
            "images": images
        }
    
    return {
        "body": "",  # Trả về một chuỗi rỗng nếu không có nội dung
        "links": [],
        "images": []
    }

def clean_body_content(body_content):
    # Kiểm tra xem nội dung có rỗng không
    if not body_content:
        return ""

    # Đảm bảo nội dung là dạng chuỗi
    body_content = str(body_content)

    # Tạo đối tượng BeautifulSoup
    soup = BeautifulSoup(body_content, "html.parser")

    # Xóa các thẻ script và style
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Lấy text hoặc xử lý thêm nội dung
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]

if __name__ == "__main__":
    # Test với một trang web
    website_url = "https://example.com"
    
    # Scrape nội dung từ website
    html_content = scrape_website(website_url)
    
    # Trích xuất nội dung body, links và images
    extracted_data = extract_body_content(html_content)
    
    # Dọn dẹp nội dung body
    cleaned_content = clean_body_content(extracted_data["body"])

    # In ra nội dung đã dọn dẹp và các liên kết, hình ảnh
    print("\nCleaned Content:\n", cleaned_content[:500])  # In 500 ký tự đầu tiên
    print("\nLinks Found:\n", extracted_data["links"])
    print("\nImages Found:\n", extracted_data["images"])
