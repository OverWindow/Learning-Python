#백준(2869번)
#음수로 나머지나 몫을 구하게 되다면...
# 5 = -3 * (-2) + (-1)
#이렇게 된다

A,B,V = map(int,input().split())

#print(5//-3)               #결과: -2
#print(5%-3)                #결과: -1
print(1-(V-A)//(B-A))
