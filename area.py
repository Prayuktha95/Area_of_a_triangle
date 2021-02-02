s1 = float(input('Length of the first side of the triangle  '))
s2 = float(input('Length of the second side of the triangle  '))
s3 = float(input('Length of the third side of the triangle  '))
s = (s1 + s2 + s3)/2
area = (s*(s-s1)*(s-s2)*(s-s3))**0.5
print(f'The area of the traingle is {area}')
