#Programa1 - Calcular promedio del Alumno
#Declaración
nota1,nota2,nota3=0.0,0.0,0.0
promedio=0

#Input
nota1=15
nota2=11
nota3=14

#Processing
promedio=(nota1+nota2+nota3)/3

#Output
print("Promedio= ",promedio)

#Programa2- Calcular Masa corporal de una persona
#Declaración
edad=0
altura_persona=0.0
peso_persona=0.0
masa_corporal=0.0

#Input
edad=30
altura_persona=1.60
peso_persona=58

#Processing
masa_corporal=(peso_persona/altura_persona)

#Output
print("Masa corporal de una persona= ",masa_corporal)

#Programa3- Calcular promedio general de un alumno
#Declaración
promedio_biologia=0
promedio_quimica=0
promedio_raz_verbal=0
promedio_raz_matematico=0
promedio_general=0

#Input
promedio_biologia=12
promedio_quimica=11
promedio_raz_verbal=14
promedio_raz_matematico=16

#Processing
promedio_general=(promedio_biologia+promedio_quimica+promedio_raz_verbal+promedio_raz_matematico)/4

#Output
print("Promedio general= ",promedio_general)

#Programa4- Calcular Total de deuda
#Declaración
deuda_bcp=0.0
deuda_otras_inst=0.0
deuda_cajas=0.0
total=0.0

#Input
deuda_bcp=70.6
deuda_otras_inst=98.6
deuda_cajas=156.3

#Processing
total=(deuda_bcp+deuda_otras_inst+deuda_cajas)

#Output
print("Total de deuda= ",total)

#Programa5- Calcular Importe total
#Declaración
total_base_imponible=0.0
IVA21=0.0
retención15=0.0
importe_total=0.0

#Input
total_base_imponible=230.00
IVA21_p=48.30
retención15=34.50
importe_total=0.0
#Processing
importe_total=(total_base_imponible+IVA21-retención15)

#Output
print("Importe total: ",importe_total)

#Programa6- Calcular el IGV
#Declaración
valor_total=0.0
tasa_IGV=0.0
valor_neto=0.0
IGV=0.0

#Input
valor_total=315
tasa_IGV=0.18
valor_neto=266.95
IGV=0.0

#Processing
IGV=(valor_neto*tasa_IGV)
#Output
print("IGV: ",IGV)

#Programa7- Calcular Total de pagó
#Declaración
libro_auditoría_t=0.0
libro_manual_c=0.0
compendio_l=0.0
total_pago=0.0

#Input
libro_auditoría_t=250
libro_manual_c=250
compendio_l=300
total_pago=0.0

#Processing
total_pago=(libro_auditoría_t+libro_manual_c+compendio_l)

#Output
print("Total de pagó= ",total_pago)

#Programa8- Calcular Sub total
#Declaración
costo_directo=0.0
gasto_general_fijo=0.0
gasto_general_variable=0.0
utilidad=0.0
sub_total=0.0

#Input
costo_directo=100
gasto_general_fijo=5
gasto_general_variable=10
utilidad=10
sub_total=0.0

#Processing
sub_total=(costo_directo+gasto_general_fijo+gasto_general_variable+utilidad)

#Output
print("Sub total: ",sub_total)

#Programa9- Calcular presupuesto total
#Declaración
Sub_total=0.0
IGV_19=0.0
Factor_relacion=0.0
Presupuesto_total=0.0

#Input
Sub_total=125
IGV_19=20.65
Factor_relacion=108.7
Presupuesto_total=0.0

#Processing
Presupuesto_total=(IGV_19+Factor_relacion)

#Output
print("Presupuesto total: ",Presupuesto_total)


#Programa10- Calcular presupuesto total de Administración Directa
#Declaración
Costo_directo=0.0
gasto_generales=0.0
Sub_total=0.0
presupuesto_total=0.0

#Input
Costo_directo=100
gasto_generales=10
Sub_total=110
presupuesto_total=0.0

#Processing
presupuesto_total=(Costo_directo+gasto_generales)

#Output
print("Presupuesto total: ",presupuesto_total)

#Programa11- Calcular el precio final con descuento
#Declaración
descuento=0.0
precio_original=0.0
precio_descuento=0.0
precio_final=0.0

#Input
descuento=0.4
precio_original=120
precio_descuento=48
precio_final=0.0

#Processing
precio_final=(precio_original-precio_descuento)

#Output
print("Precio final: ",precio_final)

#Programa12- Calcular el área y périmetro de un terreno
#Declaración
base=0
altura=0
area=0
perimetro=0

#Input
base=43
altura=17
area=0
perimetro=0

#Processing
area=(base*altura)
perimetro=(2*(base+altura))

print("Área y Perímetro: ",area,"y",perimetro )

#Programa13- Calcular el semi perímetro de un tríangulo
#Declaración
ladoA=0
ladoB=0
ladoC=0
perimetro_T=0
semi_perimetro=0
#Input
ladoA=5
ladoB=7
ladoC=4
perimetro_T=0
semi_perimetro=0

#Processing
perimetro=(ladoA+ladoB+ladoC)
semi_perimetro=(perimetro/2)

#Output
print("Semi perímetro de un tríangulo: ",semi_perimetro)

#Programa14- Calcular promedio ponderado
#Declaración
Matematica=0
credit_mat=0
geometria=0
credit_geo=0
quimica=0
credit_quim=0
lenguaje=0
credit_leng=0
promedio_ponderado=0

#Input
Matematica=15
credit_mat=5
geometria=16
credit_geo=5
quimica=10
credit_quim=4
lenguaje=11
credit_leng=2
promedio_ponderado=0

#Processing
promedio_ponderado=((Matematica*credit_mat)+(geometria*credit_geo)+(quimica*credit_quim)+(lenguaje*credit_leng))/(credit_mat+credit_geo+credit_quim+credit_leng)

#Output
print("Promedio ponerado: ",promedio_ponderado)

#Programa15- Calcular el costo de ventas
#Declaración
inventario_inicial=0.0
compras=0.0
inventario_final=0.0
costo_ventas=0.0

#Input
inventario_inicial=75.000
compras=120.750
inventario_final=40.250
costo_ventas=0.0

#Processing
costo_ventas=(inventario_inicial+compras-inventario_final)

#Output
print("Costo de ventas: ",costo_ventas)

#Programa16- Calcular el porcentaje
#Declaración
x=0
y=0
a=0
porcentaje=0.0

#Input
x=25
y=120
a=100
porcentaje=0.0

#Processing
porcentaje=(x*y)/a

#Output
print("Porcentaje: ",porcentaje)

#Programa17- Calcular total de ventas netas
#Declaración
ventas2005=0.0
ventas2006=0.0
ventas2007=0.0
ventas2008=0.0
total_v=0.0

#Input
ventas2005=15.321
ventas2006=18.249
ventas2007=20.893
ventas2008=20.131
total_v=0.0

#Processing
total_v=(ventas2005+ventas2006+ventas2007+ventas2008)

#Output
print("Total de ventas netas: ",total_v)

#Programa18- Calcular remuneración computable
#Declaración
sueldo=0.0
asig_familiar=0.0
prom_comisiones=0.0
prom_horas_extras=0.0
otro=0.0
sexto_gratif=0.0
total_remuneracion=0.0

#Input
sueldo=930.0
asig_familiar=93.0
prom_comisiones=0.0
prom_horas_extras=0.0
otro=0.0
sexto_gratif=185.84
total_remuneracion=0.0

#Processing
total_remuneracion=(sueldo+asig_familiar+sexto_gratif)

#Output
print("Remuneración computable: ",total_remuneracion)

#Programa19- Calcular el promedio de total activos
#Declaración
t_activos2006=0.0
t_activos2008=0.0
t_activos2005=0.0
promedioT=0.0

#Input
t_activos2006=29.972
t_activos2008=49.662
t_activos2005=26.763
promedioT=0.0

#Processing
promedioT=(t_activos2005+t_activos2006+t_activos2008)/3

#Output
print("Promedio de total activos: ",promedioT)

#Programa20- Calcular el promedio total de capital contable
#Declaración
t_cap_contable2006=0.0
t_cap_contable2007=0.0
t_cap_contable2008=0.0
promedioC=0.0

#Input
t_cap_contable2006=14.779
t_cap_contable2007=18.695
t_cap_contable2008=17.268
promedioC=0.0


#Processing
promedioC=(t_cap_contable2006+t_cap_contable2007+t_cap_contable2008)/3

#Output
print("Promedio total de capital contable: ",promedioC)
