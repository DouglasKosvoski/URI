time = int(input())

hours   = time // (60 ** 2)
minutes = time % (60 ** 2) // 60
seconds = time % 60

print('{0}:{1}:{2}'.format(hours, minutes, seconds))
