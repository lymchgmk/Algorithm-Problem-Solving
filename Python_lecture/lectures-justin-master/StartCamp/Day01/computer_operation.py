import webbrowser

heroes = ['iron man', 'batman', 'wonder woman', 'black widow']

for hero in heroes:
    # print(hero)
    webbrowser.open_new('https://search.naver.com/search.naver?query=' + hero)