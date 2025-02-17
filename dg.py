from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import json
from datetime import datetime

# JSON 파일 읽기
with open('search_links.json', 'r', encoding='utf-8') as file:
    search_links = json.load(file)

# Chrome 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# WebDriver 초기화
service = Service()
driver = webdriver.Chrome(service=service, options=options)

# CSV 파일 생성
csv_filename = 'dg.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    # CSV 헤더 작성
    writer.writerow(['검색지역', '검색키워드', '제목', '회사정보', '근무조건', '이미지URL', '채용공고링크', '수집일시'])

    # 각 검색 URL에 대해 크롤링 수행
    for search_info in search_links:
        district = search_info['district']
        keyword = search_info['keyword']
        url = search_info['url']
        
        print(f"\n=== 검색 시작: {district} - {keyword} ===")
        
        try:
            # 페이지 접속
            driver.get(url)

            # 페이지가 로드될 때까지 대기
            wait = WebDriverWait(driver, 10)
            job_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "_11bsp583")))

            # 각 채용 공고 정보 추출
            for item in job_items:
                try:
                    # 정보 추출
                    title = item.find_element(By.CLASS_NAME, "abyzch1").text
                    company_info = item.find_element(By.CLASS_NAME, "_1pwsqmm0").text
                    work_info = item.find_elements(By.CLASS_NAME, "_1pwsqmm0")[1].text
                    
                    try:
                        image_url = item.find_element(By.TAG_NAME, "img").get_attribute("src")
                    except:
                        image_url = "이미지 없음"
                        
                    job_link = item.get_attribute("href")
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    # CSV에 데이터 작성
                    writer.writerow([district, keyword, title, company_info, work_info, 
                                   image_url, job_link, current_time])
                    
                    print(f"저장완료: {title}")
                    
                except Exception as e:
                    print(f"항목 추출 중 오류 발생: {e}")
                    continue
                    
        except Exception as e:
            print(f"페이지 처리 중 오류 발생: {e}")
            continue

# 브라우저 종료
driver.quit()

print(f"\nCSV 파일 저장 완료: {csv_filename}")