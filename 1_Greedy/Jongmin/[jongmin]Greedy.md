# Greedy 
## Hints
* 체육복: 예약한 친구들이 도난당한 경우도 고려해서 초기화 하고 앞뒤사람 체육복 빌리자
* 조이스틱: 왜인지는 모르겠지만 하도 안풀려서 질문게시판 찾아보니 왼, 오 같을 경우는 오른쪽으로 가야 풀린다고 함... 문제오류인듯. 그러나 기본은 1. 위치 조작 최소거리 2. 알파벳 변경 최소거리(z로 돌아서 갈거냐 정방향으로 갈거냐)
를 비교해서 가장 빠른쪽만 계속 greedy하게 선택해보자
* 큰 수 만들기: 문제자체는 쉽다. 근데 효율성통과하는거 만드느라 고생을 했는데 k가 얼마일때 최대한 어디까지 커서가 이동해갈수있는지 limit을 파악하고, 숫자가 뭐이면 아얘 다음것 안봐도 되는지 파악해서 시간을 줄이자
* 구명 보트: 문제 조건을 잘읽자... 한보트에 두명까지만 탈 수 있대.. 이거도 문제자체는 쉽다.무거운사람부터 greedy하게 태우고 남는 무게 채워서 태워보내면되는데 역시 효율성이 문제다. 효율적인 코드를 위해서 "투포인터 알고리즘"을 찾아서 해결해보자. 거창한건 아니고 아이디어 정도이다.
* 섬 연결하기: 음.. 이문제는 level3인 이유가 greedy때문은 아닌거같다. 코드자체는 짧고 풀이도 제일 빨리 풀린 문제였는데 아이디어가 안떠오른다면 1. greedy하게 가장 최소가 되도록! 2. 이미 통행가능한 섬들사이를 또 엮을 필요는 없다! "union-find" 알고리즘에 대해 찾아보자. 의외로 union find만 잘 알고있으면 빨리 풀리는 문제였다. +) 크루스칼 알고리즘 MST
* 예전에 그리디알고리즘 백준문제풀다가 '회의실예약'문제였나를 본 기억이 있어서 그 아이디어를 이용해서 풀었다. 간트차트에서 안겹치게 가장 많이 예약하는걸 고를 때 퇴실시간으로 정렬부터하고 본다. 이거 참고해서 풀면 level3임에도 쉽게 풀린다.

## 그리디 알고리즘
* 현재 상황에서 지금 당장 좋은 것만 고르는 방법
* 그리디 해법은 정당성 분석이 중요! - 그냥 좋아보이는거만 계속 선택해도 최적의 해인가?에 대해 확신해야함. 실제로 그리디로 생각했는데 DP인 경우가 많았음

### 문제 풀이 과정
1. 문제 조건 확인
2. 문제 해결 아이디어 확인
3. 정당성 확인: 이렇게 그리디하게 선택하는 과정이 최적의 해를 항상 보장할 수 있을까?

### From 종만북
탐욕법은 가장 직관적인 알고리즘 설계 패러다임 중 하나.
탐욕법을 이용한 알고리즘은 우리가 원하는 답을 재귀 호출과 같이 여러 개의 조각으로 쪼개고, 각 단계마다 답의 한 부분을 만들어간다는 점에서 완전 탐색이나 동적 계획법 알고리즘과 같다.
그러나 모든 선택지를 고려해보고 그중 전체 답이 가장 좋은 것을 찾는 두 방법과는 달리, 탐욕법은 각 단계마다 지금 당장 가장 좋은 방법만을 선택

주의: 탐욕적 알고리즘은 많은 경우 최적해를 찾지 못한다. 그래서 다음 두 가지 경우에만 사용한다.
1. 탐욕법을 사용해도 항상 최적 해를 구할 수 있는 문제를 만난 경우, 탐욕법은 동적 계획법보다 수행시간이 훨씬 빠르기 때문에 유용
2. 시간이나 공간적 제약으로 인해 다른 방법으로 최적해를 찾기 너무 어렵다면 최적해 대신 근사값을 찾을 수 있어 최적은 아니지만 임의의 답보다는 좋은 답을 구하는 용도로 유용하게 사용.

#### 탐욕적 알고리즘 레시피
1. 문제의 답을 만드는 과정을 여러 조각으로 나누기
2. 각 조각마다 어떤 우선순위로 선택을 내려야 할지 결정(직접 예제 입력, 손으로 몇개 해보기)
3. 어떤 방식이 동작할 거 같으면 두 가지 속성을 증명해보자: a) 탐욕적 선택 속성: 항상 각 단계에서 우리가 선택한 답을 포함하는 최적해가 존재함을 보임 b) 최적 부분 구조: 각 단계에서 항상 최적의 선택만을 했을 때 전체 최적해를 구할 수 있는지 여부 증명

과연 조이스틱 문제가 정말 Greedy일까?
앞으로는 백준을 풀도록하겠슘다...

![image](https://user-images.githubusercontent.com/46064193/111978899-c771e080-8b47-11eb-9dbb-fee40dbfa58d.png)
