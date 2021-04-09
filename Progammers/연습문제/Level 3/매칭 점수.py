def solution(word, pages):
    import re
    
    # 매칭 점수 = 기본 점수 + 링크 점수
    basic_points_dict = {}
    a_links_dict = {}
    
    for idx, page in enumerate(pages):
        # 페이지 지정
        current_page_url = re.search('<meta property="og:url" content="https://(.*)"/>', page).group(1)
        
        # 기본 점수
        basic_point = len(re.findall(word, page, re.IGNORECASE))
        basic_points_dict[current_page_url] = basic_point
        
        # 외부 링크 수
        a_links = re.findall('<a href="https://(.*)">', page)
        a_links_dict[current_page_url] = a_links
        
    # 링크 점수
    link_points_dict = {}
    for current_page, linked_pages in a_links_dict.items():
        link_points_dict[current_page] = basic_points_dict[current_page] / len(linked_pages)
        
    # 매칭 점수
    print(basic_points_dict)
    print(a_links_dict)
    print(link_points_dict)
    
    
    
    matching_points_dict = basic_points_dict.copy()
    for current_page, linked_pages in a_links_dict.items():
        for linked_page in linked_pages:
            try:
                matching_points_dict[linked_page] += link_points_dict[current_page]
            except KeyError:
                continue
    print(matching_points_dict)

    # answer index 추출
    result = [[idx, val[1]] for idx, val in enumerate(matching_points_dict.items())]
    result.sort(key=lambda x: -x[1])
    return result[0][0]


word = 'Muzi'
# pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print(solution(word, pages))
