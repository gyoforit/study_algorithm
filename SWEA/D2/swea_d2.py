# 210202
# 1945. 간단한 소인수분해
T = int(input())
for i in range(1, T+1):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    N = int(input())
    while N > 1:
        if N % 11 == 0:
            e += 1
            N = N//11
        elif N % 7 == 0:
            d += 1
            N = N//7
        elif N % 5 == 0:
            c += 1
            N = N//5
        elif N % 3 == 0:
            b += 1
            N = N//3
        elif N % 2 == 0:
            a += 1
            N = N//2
    print(f"#{i} {a} {b} {c} {d} {e}")

# 1928. Base64 Decoder

# 아스키코드로 변환
# 변환한 숫자를 2진수로 변환
# 숫자부분만 떼어냄
# 만약 숫자 길이가 8이 아니라면 앞에 0붙이기
# 모든 숫자를 다 이어붙이기!
# 6개씩 슬라이싱 해서 다시 10진수 변환
# 이를 알파벳으로 변환....

# 이걸 거꾸로 해야됨...^^
# format, rjust 배워서 써먹기!

# import base64

# N = 'Man'
# binarychars = ''
# binarylist = []
# for char in N:
#     bin_char = ''
#     asc = ord(char)
#     bin_char += bin(asc)[2:]
#     while len(bin_char) < 8:
#         bin_char = '0' + bin_char
#         binarychars += bin_char
# # 01001101011... 출력
# # # print(type(binarychars))
# binarylist.extend(binarychars)
# for i in range(len(binarylist)//6 -1):
#     chars6 = []
#     chars6int = ''
#     chars6 += binarylist[6*i:6*(i+1)]
#     # print(''.join(chars6))
#     chars6int += '0b' + ''.join(chars6)
#     x = str(int(chars6int, 2))

# ascii 이용하여 index 값 구하기
# index를 이진수로 바꿔서 나열하기
# 8개씩 slicing해서 10진수로 변환
# ascii 이용하여 다시 변환

# N = 'TWFu'
# for char in N:
#     print(ord(char))

# 210204  
# 1986. 지그재그 숫자
T = int(input())
for i in range(1, T+1):
    N = int(input())
    result = 0
    for n in range(1, N+1):
        if n % 2:
            result += n
        else:
            result -= n
    print(f"#{i} {result}")

# 1284. 수도 요금 경쟁
T = int(input())
for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    A = 0
    B = 0
    result = 0
    A = numbers[0]*numbers[4] # P*W
    if numbers[4] <= numbers[2]: # W<=R
        B = numbers[1] # Q
    else:
        B = numbers[1] + numbers[3]*(numbers[4]-numbers[2])
    result = min(A, B)
    print(f"#{i} {result}")
# 문제 제대로 읽기!!! 최소요금!!!

# 1288. 새로운 불면증 치료법
T = int(input())
for i in range(1, T+1):
    N = int(input())
    numbers = set()
    count = 0
    while len(numbers) < 10:
        count += 1
        M = N*count
        num = []
        num.extend(str(M))
        for idx in range(len(num)):
            numbers.update(num)
    print(N*count)
# 이것도 문제 좀 제대로....ㅠㅠ

# 채은님 풀이(list에 넣어서 set 변환하면 어차피 중복된거 빠짐)
T = int(input())
for t in range(1, T+1):
    N = int(input())
    cn = 1
    lst = []
    while set(lst) != set(range(10)):
        for n in str(N * cn):
            lst.append(int(n))
        cn += 1
    print(f'#{t} {(cn-1) * N} ')

# 주엽님 아이디어 활용 (숫자 없애기)
T = int(input())
for i in range(1,T+1):
    count = 0
    N = input()
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while numbers != []:
        count += 1
        M = str(int(N)*count)
        for num in M:
            if int(num) in numbers:
                numbers.remove(int(num))
    print(f"#{i} {int(N)*count}")

# 1989. 초심자의 회문 검사
T = int(input())
for i in range(1, T+1):
    chars = input()
    while len(chars) > 2:
        if chars[0] != chars[-1]:
            print(f"#{i} 0")
            break
        else:
            chars = chars[1:-1]
    else:
        print(f"#{i} 1")

# 210208
# 1966. 숫자를 정렬하자
T = int(input())
for t in range(1, T+1):
    N = int(input())
    nb = list(map(int, input().split()))
    result = ''
    for i in range(0, N-1):
        for j in range(i+1, N):
            if nb[i] > nb[j]:
                nb[j], nb[i] = nb[i], nb[j]
    for a in range(len(nb)):
        nb[a] = str(nb[a])
    result = ' '.join(nb)
    print('#%d %s' % (t, result))

# 1970. 쉬운 거스름돈
'''
단위별로 돌아가며 N과 비교.
N이 더 크면 N으로 나눈 몫을 count (해당 돈의 개수니까)
그리고 나머지를 다시 N에다 집어넣음
'''
T = int(input())
for t in range(1, T+1):
    N = int(input()) #32850
    mn = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = [0, 0, 0, 0, 0, 0, 0, 0]
    ans = ''
    for i in range(len(mn)):
        if N >= mn[i]:
            result[i] = N // mn[i]
            N = N % mn[i]
        else:
            result[i] = 0
    for n in range(len(result)):
        result[n] = str(result[n])
    ans = ' '.join(result)
    print('#%d\n%s' % (t, ans))

# 210209
# 1948. 날짜계산기
'''
월/일을 단순히 일로만 계산하는 함수 작성
'''
def howmanydate(m, d):
    result = 0
    if m == 1:
        return d
    else:
        a = 1
        while a < m:
            if a in [1, 3, 5, 7, 8, 10, 12]:
                result += 31
                a += 1
            elif a in [4, 6, 9, 11]:
                result += 30
                a += 1
            elif a == 2:
                result += 28
                a += 1
        return result + d

T = int(input())
for t in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    print(f'#{t} {howmanydate(m2, d2) - howmanydate(m1, d1) + 1}')

# 210210
# 1959. 두 개의 숫자열
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split()) # M이 크다고 가정!
    Nlist = list(map(int, input().split()))
    Mlist = list(map(int, input().split()))
    if N > M:
        N, M = M, N
        Nlist, Mlist = Mlist, Nlist

    mx = float('-inf')
    for i in range(0, M-N+1): # C의 초깃값
        C = []
        for j in range(i, i+N):
            C += [Mlist[j]]

        tmp = 0
        for a in range(N):
            tmp += Nlist[a] * C[a]
        if tmp > mx:
            mx = tmp
    print('#%d %d' % (t, mx))

# 다른 풀이
def check(long, short):
    max_value = -987654321
    for i in range(len(long)-len(short)+1): # 큰 숫자열을 작은 숫자열 길이만큼 자를건데 그 시작 부분의 pointer 역할
        result = 0 # for 문 안에서 초기화를 해야 함. 매 pointer가 바뀔 때마다 새롭게 곱할 값의 합을 알아봐야 하니깐!
        for j in range(len(short)): # 작은 숫자열의 인덱스 차례로 돌면서
            result += long[i+j]*short[j] # 곱한다! 큰 숫자열에는 위에서 구한 시작점을 더해줘서 매 싸이클 마다 달라지게..

        if max_value < result:
            max_value = result
    return max_value

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        ans = check(A, B)
    else:
        ans = check(B, A)

    print("#{} {}".format(tc, ans))

# 210215
# 1943. 달팽이 숫자
# 델타 사용한 풀이
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    result = []
    for a in range(N):
        result.append([0] * N)
    # 현위치
    r = 0
    c = -1
    # 배열에 넣을 숫자
    n = 0
    # 반복 횟수
    k = N
    # 델타(방향키)
    drc = [[0, 1, 0, -1], [1, 0, -1, 0]]
    # 델타의 인덱스
    a = 0
    # k를 -1 할지 말지 결정하는 cnt
    cnt = 0
    # 종료조건 만족할 때까지 무한 반복
    while True:
        # 행 고정, 열 이동
        for i in range(1, k + 1):
            n += 1
            r += drc[0][a]
            c += drc[1][a]
            result[r][c] = n
        # cnt +1 한 다음 cnt가 홀수면 k를 -1 감소
        cnt += 1
        if cnt % 2:
            k -= 1
        # 반복문 종료 조건
        if k <= 0:
            break
        # 방향키 변경(델타 인덱스 +1)
        a += 1
        # 델타 인덱스가 범위 밖을 벗어나는 오류 방지(끝까지 가면 다시 0으로 초기화)
        if a > 3:
            a = 0
    print("#%d" % t)
    for i in range(N):
        print(' '.join(map(str, result[i])))

# 델타 사용하지 않은 풀이
T = int(input())
for t in range(1, T+1):
    N = int(input())
    result = []
    for a in range(N):
        result.append([0]*N)
    # 현 위치
    r = 0
    c = -1
    # 배열에 들어갈 숫자
    n = 0
    # r, c의 방향키 역할(순방향/역방향)
    d = 1
    # 반복횟수
    k = N
    # 반복문 종료조건 만족할 때까지 무한 반복
    while True:
        # 행 고정, 열 이동
        for i in range(1, k+1):
            n += 1
            c += d
            result[r][c] = n
        # 반복횟수 -1
        k -= 1
        # 종료 조건
        if k <= 0:
            break
        # 열 고정, 행 이동
        for i in range(1, k+1):
            n += 1
            r += d
            result[r][c] = n
        # 방향 바꿈
        d *= -1

    # print(result)
    print("#%d" % t)
    for i in range(N):
        print(' '.join(map(str, result[i])))

# 210216
# 1979. 어디에 단어가 들어갈 수 있을까
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    # 가로세로판 만들기
    grid = []
    for g in range(N):
        grid.append(list(map(int, input().split())))
    # 단어가 들어갈 수 있는 경우의 수 세는 용
    cnt = 0
    # 행 고정, 열 탐색
    for r in range(N):
        # 해당 열에서의 1이 있는 길이 측정하기 위한 l 초기화
        l = 0
        for c in range(N):
            # 1이면 l에 +1
            if grid[r][c] == 1:
                l += 1
            # 0이면 앞에까지 더해놨던 l 파악 -> 만약 K라면 cnt +1 한 후에 l을 다시 0으로 초기화
            else:
                if l == K:
                    cnt += 1
                l = 0
        # 마지막 열이 l인 경우를 위해 다시 한번 K랑 같은지 파악
        if l == K:
            cnt += 1
    # 열 고정, 행 탐색 (똑같음)
    for c in range(N):
        l = 0
        for r in range(N):
            if grid[r][c] == 1:
                l += 1
            else:
                if l == K:
                    cnt += 1
                l = 0
        if l == K:
            cnt += 1
    print("#%d %d" % (t, cnt))

# 2001. 파리퇴치
T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    # 이중 배열 만들기
    grid = []
    for n in range(N):
        grid.append(list(map(int, input().split())))
    # 최댓값 저장할 mx
    mx = 0
    # 기준 위치 r, c
    r = 0
    c = 0
    while True:
        # 해당 구간에서의 요소 합 구할 tmp
        tmp = 0
        # 좌상단 모서리를 r, c라고 했을 때 M*M 파리채 만들어서 해당하는 요소들 모두 tmp에 더함
        for i in range(r, r + M):
            for j in range(c, c + M):
                tmp += grid[i][j]
        # tmp가 mx보다 크면 mx에 tmp 할당 후 열을 한칸 이동( c +1 )
        if tmp > mx:
            mx = tmp
        c += 1
        # 열을 계속 더하다가 N-M 보다 커지면 0열로 돌아가고 r을 한칸 +1
        if c == N - M + 1:
            r += 1
            c = 0
        # 좌상단 모서리의 r이 제일 마지막 위치(N-M)의 좌표보다 커지면 반복 종료
        if r > N - M:
            break
    print("#%d %d" % (t, mx))

# 1940. 가랏! RC카!
T = int(input())
for t in range(1, T+1):
    N = int(input())
    now = 0
    vc = 0
    for n in range(N):
        try:
            a, b = map(int, input().split())
            if a == 1:
                vc += b
                now += vc
            elif a == 2:
                if b > vc:
                    vc = 0
                else:
                    vc -= b
                now += vc
        except:
            now += vc
    print("#%d %d" % (t, now))

# 1976. 시각 덧셈
T = int(input())
for t in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    h, m = 0, 0
    if m1 + m2 >= 60:
        m = m1+m2-60
        if h1+h2 > 12:
            h = h1+h2-11
        else:
            h = h1+h2+1
    else:
        m = m1+m2
        if h1+h2 > 12:
            h = h1+h2-12
        else:
            h = h1+h2
    print("#%d %d %d" % (t, h, m))

# 210217
#1974. 스도쿠검증
# 겹치는게 하나라도 있으면 무조건 0이므로 return False가 더 먼저 나와야 함
# 행 검사하는 함수
def test_row(arr):
    N = len(arr)
    for r in range(N):
        test = []
        for c in range(N):
            test.append(arr[r][c])
        if len(set(test)) != 9:
            return False
    else:
        return True
# 열 검사하는 함수
def test_col(arr):
    N = len(arr)
    for c in range(N):
        test = []
        for r in range(N):
            test.append(arr[r][c])
        if len(set(test)) != 9:
            return False
    return True
# 3*3 네모 검사하는 함수
def test_sqr(arr):
    r = 0
    c = 0
    while True:
        test = []
        for i in range(r, r+3):
            for j in range(c, c+3):
                test.append(arr[i][j])
        if len(set(test)) != 9:
            return False
        else:
            c += 3
        if c == 9:
            c = 0
            r += 3
        if r == 9:
            break
    return True

T = int(input())
for t in range(1, T+1):
    puzzle = []
    L = 9
    for i in range(9):
        puzzle.append(list(map(int, input().split())))
    if test_row(puzzle) and test_col(puzzle) and test_sqr(puzzle):
        print("#%d 1" % t)
    else:
        print("#%d 0" % t)

# 210218
# 4861. 회문
# 회문인지 판단하는 함수 정의
def ispalin(x):
    if len(x) <= 1:
        return True
    while len(x) > 1:
        if x[0] == x[-1]:
            return ispalin(x[1:-1])
        else:
            return False

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    # 그리드 만들기
    grid = []
    for n in range(N):
        tmp = []
        tmp.extend(input())
        grid.append(tmp)
    # 찾자마자 반복 끝내기 위해 while 문 안에 flag 장치를 둠
    while True:
        flag = 0
        # 행 고정
        for r in range(N):
            for c in range(N-M+1):
                tmp = ''
                for i in range(M):
                    tmp += grid[r][c+i]
                if ispalin(tmp):
                    flag = 1
                    print("#%d %s" % (t, tmp))
                    break
        if flag == 1:
            break
        # 열 고정
        for c in range(N):
            for r in range(N-M+1):
                tmp = ''
                for i in range(M):
                    tmp += grid[r+i][c]
                if ispalin(tmp):
                    print("#%d %s" % (t, tmp))
                    break
        break

# 4864. 문자열 비교
def compare(A, B):
    a = len(A)
    b = len(B)
    for i in range(b-a+1):
        if B[i] == A[0]:
            if B[i:i+a] == A:
                return 1
    else:
        return 0

T = int(input())
for t in range(1, T+1):
    N = input()
    M = input()
    result = compare(N, M)

    print("#%d %d" % (t, result))

# 4865. 글자수
T = int(input())
for t in range(1, T+1):
    str1 = []
    str1.extend(input())
    str2 = input()
    str_dict = dict.fromkeys(str1, 0)

    for s in str2:
        if s in str_dict.keys():
            str_dict[s] += 1
    result = max(str_dict.values())
    print("#%d %d" % (t, result))

# 1926. 간단한 369 게임
# 3, 6, 9 개수 세는 함수
def cnt(n):
    result = n.count('3') + n.count('6') + n.count('9')
    return result

N = int(input())
for i in range(1, N+1):
    tmp = []
    # 숫자 하나씩 확인하기 위해 string 으로 받아서 extend
    tmp.extend(str(i))
    if cnt(tmp) == 0:
        print(i, end =' ')
    else:
        print('-'*cnt(tmp), end = ' ')

# 1983. 조교의 성적 매기기
scr = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
# 총점 세는 함수 정의
def score(m, f, h):
    total = m*0.35 + f*0.45 + h*0.2
    return total

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    score_list = []
    student = 0
    for n in range(N):
        m, f, h = map(int, input().split())
        s = score(m, f, h)
        score_list.append(s)
    # 등수 확인하고 싶은 번호의 점수를 student에 저장
    student = score_list[M-1]
    rank = 0
    sorted_list = sorted(score_list) # 오름차순
    for a in range(N):
        # 해당 점수의 등수를 뽑음
        if sorted_list[a] == student:
            rank = N-a # 오름차순에서 8등은 상위 2등이기 때문
            break

    if rank % (N//10) != 0:
        rank = rank//(N//10) + 1
    else:
        rank = rank//(N//10)
    print("#%d %s" % (t, scr[int(rank-1)]))

# 1946. 압축풀기
T = int(input())
for t in range(1, T+1):
    N = int(input())
    text = ''
    for n in range(N):
        c, k = input().split()
        text += c*int(k)
    # 한번에 쭉 길게 늘어뜨린다음
    txt = len(text)
    i = 0
    print("#%d" % t)
    # 10개 단위로 잘라서 print (slicing 에서는 index 벗어나도 되는 점을 이용)
    while True:
        print(text[i:i+10])
        i += 10
        if i > txt:
            break

# 1984. 중간 평균값 구하기
def get_max(arr):
    mx = arr[0]
    for i in arr:
        if i > mx:
            mx = i
    return mx

def get_min(arr):
    mn = arr[0]
    for i in arr:
        if i < mn:
            mn = i
    return mn

T = int(input())
for t in range(1, T+1):
    num = list(map(int, input().split()))
    num.remove(get_max(num))
    num.remove(get_min(num))
    total = 0
    n = len(num)
    for i in num:
        total += i
    result = total/n
    print("#%d %d" % (t, int(round(result, 0))))

# 1204. 최빈수 구하기
T = int(input())
for t in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    cnt = [0] * 101
    for n in num:
        cnt[n] += 1
    mx_idx = 0

    for i in range(101):
        if cnt[i] >= cnt[mx_idx]:
            mx_idx = i
    print("#%d %d" % (t, mx_idx))

# 210219
# 1961. 숫자 배열 회전
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = []
    for a in range(N):
        arr.append(list(input().split()))
    print("#%d" % t)
    # i, j는 고정해놓고 각 회전에 따라 i, j를 사용하여 다르게 표현하기
    for i in range(N):
        tmp = ''
        for j in range(N):
            tmp += arr[N-1-j][i]
        tmp += ' '
        for j in range(N):
            tmp += arr[N-1-i][N-1-j]
        tmp += ' '
        for j in range(N):
            tmp += arr[j][N-1-i]
        print(tmp)

# 210222
# 2005. 파스칼의 삼각형
T = int(input())
for t in range(1, T+1):
    pascal = []
    N = int(input())
    for n in range(1, N+1):
        if n == 1:
            pascal.append([1])
        elif n == 2:
            pascal.append([1, 1])
        elif n >= 3:
            tmp = []
            # 바로 이전 리스트의 요소들을 둘씩 더한 값을 tmp에 저장
            for i in range(n-2):
                tmp += [pascal[n-2][i]+pascal[n-2][i+1]]
            # tmp의 양 옆을 1로 감싸서 append
            tmp = [1] + tmp + [1]
            pascal.append(tmp)
    print("#%d" % t)
    for a in range(N):
        print(' '.join(map(str, pascal[a])))

# 11572. 괄호검사
# 열린 괄호와 닫힌 괄호를 인덱스로 구별하기 위한 리스트 생성
opn = ['(', '{', '[']
cls = [')', '}', ']']
T = int(input())
for t in range(1, T + 1):
    bracket = []
    # 규칙에 어긋나면 0으로 바뀜
    result = 1
    S = input()
    for s in S:
        # 열린 괄호일 때: 소/중/대 종류에 맞는 인덱스를 append
        if s in opn:
            for i in range(len(opn)):
                if opn[i] == s:
                    bracket.append(i)
                    break
        # 닫힌 괄호일 때: 가장 최근에 append 된 요소를 비교하여 같으면 pop
        elif s in cls:
            # bracket이 비어있다 = 짝이 안 맞는다 = 규칙에 어긋남
            if len(bracket) == 0:
                result = 0
                break
            else:
                tmp = 0
                poped = bracket.pop(-1)
                for j in range(len(cls)):
                    if cls[j] == s:
                        tmp = j
                # 가장 최근에 append 된 요소와 닫힌 괄호의 종류가 다르면 규칙에 어긋남
                if tmp != poped:
                    result = 0
                    break
    # 문자열을 다 돌았는데 bracket에 요소가 있음 = 짝이 안 맞는다 = 규칙에 어긋남
    if len(bracket) > 0:
        result = 0

    print("#%d %d" % (t, result))