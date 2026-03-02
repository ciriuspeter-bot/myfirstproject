import requests

def get_github_user_info(username):
    url = f"https://api.github.com/users/{username}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        print(f"사용자명: {data['login']}")
        print(f"이름: {data.get('name', '정보 없음')}")
        print(f"팔로워: {data['followers']}")
        print(f"팔로잉: {data['following']}")
        print(f"공개 저장소: {data['public_repos']}")
        
    except requests.exceptions.RequestException as e:
        print(f"API 호출 실패: {e}")

# 테스트
get_github_user_info("python")