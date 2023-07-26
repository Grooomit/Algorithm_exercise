'''
- 멀티탭에 꽂을 수 있는 플러그의 수(N)와 전기 용품의 사용 순서(K)를 입력받는다.
- 현재 멀티탭에 꽂혀있는 플러그들을 저장할 리스트를 생성한다.
- 전기 용품의 사용 순서를 반복
  - 해당 전기 용품의 플러그가 이미 멀티탭에 꽂혀있다면, 아무 작업도 수행하지 않는다.
  - 해당 전기 용품의 플러그가 멀티탭에 꽂혀있지 않다면,
    - 멀티탭에 여유 구멍이 있다면, 해당 플러그를 그냥 꽂는다.
    - 멀티탭에 여유 구멍이 없다면, 현재 멀티탭에 꽂혀있는 플러그 중에서 가장 나중에 사용되거나, 더 이상 사용되지 않는 플러그를 빼고, 새 플러그를 꽂는다.
- 플러그를 빼는 횟수를 출력한다.
'''

def solve(N, K, use_order):
    plug = []
    unplugging_count = 0

    for i in range(K):
        if use_order[i] in plug:  # 해당 플러그가 이미 꽂혀있다면, 아무것도 안한다.
            continue
        if len(plug) < N:  # 멀티탭에 자리가 있다면, 그냥 꽂는다.
            plug.append(use_order[i])
            continue

        # 멀티탭에 자리가 없다면, 가장 나중에 사용되거나, 더 이상 사용되지 않는 플러그를 빼고, 새 플러그를 꽂는다.
        out_order = []
        for j in range(N):
            if plug[j] in use_order[i:]:
                out_order.append(use_order[i:].index(plug[j]))
            else:
                out_order.append(101)
        out = out_order.index(max(out_order))
        del plug[out]
        plug.append(use_order[i])
        unplugging_count += 1  # 언플러그 횟수를 증가

    return unplugging_count  # 언플러그 횟수를 출력

N, K = map(int, input().split())
use_order = list(map(int, input().split()))
print(solve(N, K, use_order))