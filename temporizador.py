import time

time_user = input('Digite o tempo (em segundos): ')

if time_user.isdigit():
    time_user = int(time_user)

else:
    print('Não foi digitado um número!')
    quit()

while time_user != 0:
    minutes, seconds = divmod(time_user, 60)
    timer = '{:02d}:{:02d}'.format(minutes, seconds)
    print(timer, end='\r')
    time.sleep(1)
    time_user = time_user - 1

print('Tempo encerrado!')
