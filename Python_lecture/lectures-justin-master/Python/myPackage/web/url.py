def my_url(itemPerPage=10, **kwargs):
    # kwargs -> dict
    if 'key' not in kwargs or 'targetDt' not in kwargs:
        return '필수 요청 변수가 누락되었습니다.'
    if int(itemPerPage) not in range(1, 11):
        return '1~10까지의 값을 넣어주세요.'
    
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
    base_url += f'itemPerPage={itemPerPage}&'
    
    for key, value in kwargs.items():
        base_url += f'{key}={value}&'
        
    return base_url[:-1]