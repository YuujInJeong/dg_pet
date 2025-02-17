from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# 서울시 구별 ID 매핑
district_ids = {
    '강남구': '381',
    '송파구': '404',
    '강서구': '257',
    '강동구': '432',
    '강북구': '140',
    '관악구': '340',
    '광진구': '71',
    '구로구': '278',
    '금천구': '294',
    '노원구': '169',
    '도봉구': '154',
    '동대문구': '87',
    '동작구': '324',
    '마포구': '221',
    '서대문구': '206',
    '서초구': '362',
    '성동구': '53',
    '성북구': '119',
    '성북구·종로구': '12411',
    '양천구': '238',
    '영등포구': '305',
    '용산구': '36',
    '은평구': '189',
    '종로구': '2',
    '중구-성동구': '4172',
    '중랑구': '102'
}

keywords = ['강아지', '고양이']
search_links = []

# Chrome 설정
options = webdriver.ChromeOptions()
service = Service()
driver = webdriver.Chrome(service=service, options=options)

try:
    for district, district_id in district_ids.items():
        print(f"\n===== {district} 검색 시작 =====")
        
        for keyword in keywords:
            try:
                # URL 직접 접근
                url = f"https://www.daangn.com/kr/jobs/?in={district}-{district_id}&search={keyword}"
                search_links.append({
                    'district': district,
                    'keyword': keyword,
                    'url': url
                })
                print(f"  > {district} - {keyword}: URL 저장 완료")
                
            except Exception as e:
                print(f"  {district} - {keyword} 처리 중 오류: {e}")
                continue

except Exception as e:
    print(f"실행 중 오류 발생: {e}")

finally:
    driver.quit()

# 수집된 링크를 JSON 파일로 저장
with open('search_links.json', 'w', encoding='utf-8') as f:
    json.dump(search_links, f, ensure_ascii=False, indent=2)

print(f"\n총 {len(search_links)}개의 검색 링크가 search_links.json 파일에 저장되었습니다.")