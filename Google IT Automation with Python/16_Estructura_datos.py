# Complete el código para iterar a través de las claves y valores del diccionario car_prices, imprimiendo 
# información sobre cada uno.

def car_listing(car_prices):
  result = ""
  for auto, precio in car_prices.items():
    result += "{} costs {} dollars".format(auto, precio) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))