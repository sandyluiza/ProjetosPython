#Replace all ______ with rjust, ljust or center.
#rjust - ride
#ljust - left
#center - center
#
# thickness = int(input()) #This must be an odd number
# c = 'H'
#
# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#
# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))
#
# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

numero = int(input())
c = 'S'

for i in range((numero+1)//2):
    print((c*numero*5).center(numero*6))

for i in range(numero+1):
    print((c*numero).center(numero*2))

for i in range((numero + 1) // 2):
    print((c * numero*5).center(numero*6))

for i in range(numero+1):
    print((c*numero).center(numero*10))

for i in range((numero+1)//2):
    print((c*numero*5).center(numero*6))