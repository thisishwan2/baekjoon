h, m, s=map(int, input().split())
ts=int(input())

s=s+ts         #초에 소요 초를 더해준다
m1=s//60       #분1은 초를 60으로 나눈 몫을 받는다
s1=s%60        #초1은 60이면 안되니 60으로 나머지(소요되고 남은 초)

m=m+m1         #분은 원래 입력받은 분과 위에서 소요초를 60으로 나눈 몫인 분 1의 합이다
h1=m//60       #시간1은 위의 분을 60으로 나눈 몫이다
m2=m%60        #분2는 60이면 안되니 60으로 나눈 나머지아다(소요초 반영된 분)

h=h1+h         #시간은 시간1(총 분을 60으로 나눈 몫)+입력받은 원래 시간
h2=h%24        #시간은 24이면 안되므로 나머지를 시간2에 저장

print(h2,m2,s1)