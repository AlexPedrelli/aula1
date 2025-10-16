import math

raio = float(input("entre com o valor do raio, para obter a area:"))
area = 3.14 * (raio * raio)
print(" a area do circulo é : " , area)

area_a = raio * raio * 3.1415

area_b = raio **  2 * 3.1415

area_c = raio ** 2 * math.pi

print("area A é", area_a)
print(f"area b é{area_b}")
print(f"area C é {area_c}")