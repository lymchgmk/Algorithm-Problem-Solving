# 마크다운(Markdown)

> 일반 텍스트 형식 구문을 사용하는 마크업 언어의 일종으로 사용법이 쉽고 간단하여 빠르게 문서를 정리할 수 있습니다. 단, 모든 HMTL 마크업을 대체하지는 않습니다.





## 1. 문법

### 1.1 Header

>  헤더는 제목을 표현할 때 사용합니다. 단순히 글자의 크기를 표현하는 것이 아니라 의미론적인 중요도를 나타냅니다. 

- `<h1>` 부터 `<h6>`까지 표현 가능합니다.
- `#` 의 개수로 표현하거나 `<h1></h1>` 의 형태로 표현 가능합니다.

# h1 태그입니다.

## h2 태그입니다. 

...

###### h6 태그입니다.



### 1.2 List

> 목록을 나열할 때 사용합니다. 순서가 필요한 항목과 그렇지 않은 항목으로 구분할 수 있습니다. 
>
> 순서가 있는 항목 아래 순서가 없는 항목을 지정할 수 있고 반대도 가능합니다.

- 순서가 없는 목록
  - `-` 를 누르고 스페이스 바를 누르면 생성할 수 있습니다. 
  - `tab` 키를 눌러서 하위 항목을 생성할 수 있고 `shift + tab` 키를 눌러서 상위 항목으로 이동할 수 있습니다. 



1. 순서가 있는 항목
   1. 순서가 있는 항목의 하위 항목
   2. 순서가 있는 항목의 하위 항목



- 순서가 없는 항목
  1. 순서가 있는 항목
  2. 순서가 있는 항목



1. 순서가 있는 항목
   - 순서가 없는 항목
   - 순서가 없는 항목



### 1.3 Code Block 

>  코드 블럭은 작성한 코드를 정리하거나 강조하고 싶은 부분을 나타낼 때 사용합니다.
>
> 인라인과 블럭 단위로 구분할 수 있습니다.

- Inline
  - 인라인으로 처리하고 싶은 부분은 `(백틱)으로 감싸줍니다.
- Block
  - `(백틱)을 3번  Enter를 눌러 생성합니다.



`requests`  는 파이썬에서 코드를 사용해 서버에 요청을 보낼 수 있도록 하는 `module` 입니다.

```bash
#1. requests 설치(cmd)
> pip install requests
```

```python
import requets 

response = requests.get('https://www.naver.com').text # 요청을 보내 응답을 저장
print(response)
```



### 1.4 Image

> 로컬(내 컴퓨터)에 있는  이미지를 넣거나 이미지 주소를 복사하여 활용합니다.

- `![이미지 파일의 이름](이미지 주소)` 

![](.\images\python.jpg)

![python-image](data:image/png;base64,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)







### 1.5 Link

[python documentation type link](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)



### 1.6 Table

- `|` 를 활용하여 컬럼을 구분할 수 있습니다.
- 마지막 컬럼을 작성하고 뒤에 `|` 를 붙여줍니다.

| 오픈소스                                                     | API                               |
| ------------------------------------------------------------ | --------------------------------- |
| 제작자의 권리를 지키면서 누구나 열람 가능한 공개된 (소스)코드 | 서로 다른 서비스들 간의 대화 방식 |



### 1.7 기타

- 보드체

  >**"Life is too short, you need python."**

- 이탤릭체

  >"*Hello*"

- 취소선

  >"~~Hello~~"

- 수평선

  `___` / `---` / `***` + `Enter`

  ---

  ***

  ___

  