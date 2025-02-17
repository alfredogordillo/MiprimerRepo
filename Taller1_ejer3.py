num_items=int(input("Ingresar cantidad de items: "))
print(f"Cantidad de items: {num_items}")
precio_unit=4000
print(f"El precio unitario del item es: {precio_unit}")
if num_items <=4:
    porcentaje=0.20
    precio_total=precio_unit*num_items
    descuento=precio_total*porcentaje
    precio_final=precio_total-descuento
    print(f"El valor de la compra antes del descuento es: {precio_total}")
    print(f"El valor de la compra despues del descuento es: {precio_final}")
    print(f"El descuento de la compra es: {descuento}")
    print(f"El porcentaje de descuento es: {porcentaje*100}%")
elif num_items >= 5 and num_items <= 10:
     porcentaje=0.30
     precio_total=precio_unit*num_items
     descuento=precio_total*porcentaje
     precio_final=precio_total-descuento
     print(f"El valor de la compra antes del descuento es: {precio_total}")
     print(f"El valor de la compra despues del descuento es: {precio_final}")
     print(f"El descuento del item es: {descuento}")
     print(f"El porcentaje de descuento es: {porcentaje*100}%")


else:
     print("Se pasé el tope de máximo 10 items")






