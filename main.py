import requests
from urllib.parse import urljoin
import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)

# Streamlit UI
st.title("Web Scraper ")
url = st.text_input("Enter Website URL")

#Buoc1: Scrape the Website
if st.button("Scrape Website"):
    if url:
        st.write("Scraping the website...")

        # Scrape the website
        dom_content = scrape_website(url)
        body_content = extract_body_content(dom_content)
        #cleaned_content = clean_body_content(body_content)
        cleaned_content = clean_body_content(body_content['body'])
        # Store the DOM content in Streamlit session state
        st.session_state.dom_content = cleaned_content

        # Hiển thị DOM content trong text box
        with st.expander("View DOM Content"):
            st.text_area("DOM Content", cleaned_content, height=300)
            
         # Hiển thị các links tìm đc trên trang web
        with st.expander("Links found on the page"):
            for link in body_content['links']:
                st.write(link)
        
        # Hiển thị các hình ảnh
        with st.expander("Images found on the page", expanded=True):
            cols = st.columns(3)  # Số cột (có thể điều chỉnh tùy thích)
            for idx, img in enumerate(body_content['images']):
                # Chuyển đổi URL tương đối thành URL tuyệt đối
                absolute_url = urljoin(url, img)  
                try:
                    # Kiểm tra xem hình ảnh có thể truy cập không
                    response = requests.head(absolute_url)
                    if response.status_code == 200:
                        cols[idx % 3].image(absolute_url, use_column_width='auto')  # Hiển thị hình ảnh trong cột
                    else:
                        cols[idx % 3].write(f"Image not found: {absolute_url}")
                except Exception as e:
                    cols[idx % 3].write(f"Error loading image {absolute_url}: {e}")



