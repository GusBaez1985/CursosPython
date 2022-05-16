
# 6.5 Escriba código usando find() y corte de cadenas (consulte la sección 6.10) para extraer el número al final de la línea a 
# continuación. Convierta el valor extraído en un número de coma flotante e imprímalo.


text = "X-DSPAM-Confidence:    0.8475"

buscarinicio = text.find("0")
print(buscarinicio)
buscarfin = text.find("5", buscarinicio)
print(buscarfin)
num = float(text[buscarinicio : buscarfin+1])
print(num)