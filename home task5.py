#Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
x1,y1=map(int,input('X1,Y1:').split())
x2,y2=map(int,input('X2,Y2:').split())
d = ((x1-x2)**2+(y1-y2)**2)**0.5
print('Distance =', d )

