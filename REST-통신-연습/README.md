## Rest 통신을 이용한 문제풀이 - 싸피 스무고개

__풀이 과정__

1. REST 통신 모듈 구현 및 요청

   - 사용 언어 : Python

   - 사용 프로그램 : VScode

   - 코드

     - 처음 응답을 받는 부분에서 많이 헤맸다. 
     - 처음엔 리턴값을 request.get(url).json()으로 받으려 하였으나 get을 지원하지 않아 405에러가 떴다. 
     - 따라서 아래와 같이 요청 자체를 data에 할당하여 json으로 출력해보니 응답이 정상적으로 왔다.

     ```python
     import requests
     from pprint import pprint
     
     url = "http://13.125.222.176/quiz/alpha"
     data = requests.post(url, json={
         "nickname" : "구미3반배혜진",
         "yourAnswer" : "hellossafy",
     })
     print()
     pprint(data.json())
     ```

   

2. 응답 형식 확인 및 결과

   - 산출물

   ![image-20220615003645514](README.assets/image-20220615003645514.png)

   > dfs

   

   ![image-20220615004053881](README.assets/image-20220615004053881.png)

   > SSAFYcial

   

![image-20220615004319484](README.assets/image-20220615004319484.png)

> protocol



![image-20220615004617164](README.assets/image-20220615004617164.png)

> json



![image-20220615004703717](README.assets/image-20220615004703717.png)

>singleton



![image-20220615004825546](README.assets/image-20220615004825546.png)

> cookie



![image-20220615005135668](README.assets/image-20220615005135668.png)

> redis



![image-20220615005243042](README.assets/image-20220615005243042.png)

> MVVM



![image-20220615005409238](README.assets/image-20220615005409238.png)

> pandas



![image-20220615005503562](README.assets/image-20220615005503562.png)

> bluetooth



![image-20220615005537197](README.assets/image-20220615005537197-16552221405961.png)

> fittymon



![image-20220615005750667](README.assets/image-20220615005750667.png)

> Memoization



![image-20220615005853481](README.assets/image-20220615005853481.png)

> IoC(Inversion of Control), 제어 반전



![image-20220615005954907](README.assets/image-20220615005954907.png)

> Docker



![image-20220615010050043](README.assets/image-20220615010050043-16552224510802-16552224512393.png)

> dfs



![image-20220615010141642](README.assets/image-20220615010141642.png)

> bloom



![image-20220615010230154](README.assets/image-20220615010230154.png)

> A



![image-20220615010311827](README.assets/image-20220615010311827.png)

> quick



![image-20220615010353939](README.assets/image-20220615010353939.png)

> Kubernetes



![image-20220615010452665](README.assets/image-20220615010452665.png)
