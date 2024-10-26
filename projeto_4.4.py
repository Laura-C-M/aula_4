from logging import lastResort

parede = print(input("Gostavas de pintar uma parede?"))
if parede == "sim":
   altura_parede = print(float(input("Qual a altura da parede em metros?")))
   largura_parede = print(float(input("Qual a largura da parede em metros?")))
elif parede == "nao" :
   print("Então porque é que estás aqui?")
#um litro de tinta dá para 9 metros
tamanho_parede = altura_parede*largura_parede
tinta_necessaria = tamanho_parede/9
print("Vais precisar de ", tinta_necessaria, " baldes de tinta.")