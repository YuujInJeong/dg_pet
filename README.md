
# 당근마켓 반려동물 관련 구인구직 정보 수집기

## 소개
이 프로젝트는 당근마켓의 반려동물(강아지, 고양이) 관련 구인구직 정보를 수집하는 파이썬 스크립트입니다.

## 주의사항
이 크롤러는 교육 및 연구 목적으로 제작되었습니다. 수집된 데이터의 상업적 활용은 권장되지 않으며, 크롤링으로 인한 문제가 발생할 경우 즉시 레포지토리를 내릴 예정입니다. 관련 문의사항은 [이메일 주소]로 연락 바랍니다.

## 설치 방법

1. Python 3.x 버전 설치 ([Python 공식 웹사이트](https://www.python.org/downloads/))

2. Chrome 브라우저 및 ChromeDriver 설치
```bash
brew install --cask chromium
brew install chromedriver
```

3. 프로젝트 클론
```bash
git clone https://github.com/YuujInJeong/dg_pet.git
cd dg_pet
```

4. 가상환경 생성 및 활성화
```bash
python3 -m venv venv
source venv/bin/activate  # Windows의 경우: venv\Scripts\activate
```

5. 필요한 패키지 설치
```bash
pip install selenium
```

## 사용 방법

1. search_links.json 파일에 검색하고 싶은 지역과 키워드 정보가 포함되어 있습니다.

2. 다음 명령어로 크롤러 실행:
```bash
python dg.py
```

3. 실행이 완료되면 `dg.csv` 파일이 생성됩니다. 이 파일에는 다음 정보들이 포함됩니다:
   - 검색지역
   - 검색키워드
   - 채용공고 제목
   - 회사정보
   - 근무조건
   - 이미지URL
   - 채용공고링크
   - 수집일시

## 프로젝트 구조
- `dg.py`: 메인 크롤링 스크립트
- `search_links.json`: 검색 조건 정보
- `make_link.py`: 검색 링크 생성 스크립트
- `requirements.txt`: 필요한 파이썬 패키지 목록

## 라이선스
이 프로젝트는 MIT 라이선스를 따릅니다.

## 연락처
크롤링과 관련하여 문제가 있을 경우, 즉시 [이메일](yujin010917@khu.ac.kr)로 연락 주시기 바랍니다. 레포지토리를 즉시 내리도록 하겠습니다.