num1, num2 = map(int, input().split())

if num1 % num2 == 0:
    print('Sao Multiplos')
elif num2 % num1 == 0:
    print('Sao Multiplos')

else:
    print('Nao sao Multiplos')
