input = 20

#소수는 자기 자신과 1외 에는 아무것도 나눌 수 없다.!!
def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1): #n의 범위는 2부터 number까지
        #n = 19 면
        #i = 2, 3, 4, 5, 6 ,7, 8.... 18까지 할 필요가 없다.
        # if n % i == 0 이라는 코드를 적었을 때는 모두를 비교하면서 코드가 작성되고
        # 그 뒤에 and i * i <= n 를 적으면 2, 3, 4, 5, 6 ,7, 8.... 18 다 비교하는게 아닌
        # 2, 3 을 비교해도 결과값이 똑같이 나온다.
        for i in prime_list: #i 의 범위는 2부터 n - 1 까지
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_list.append(n)
            
    return prime_list


result = find_prime_list_under_number(input)
print(result)