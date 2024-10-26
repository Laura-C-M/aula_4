print("A torre eiffel tem 330 metros de altura.")
conversor = input("Gostavas de converter para centimetros(cm), quilometros(km) ou milhas(M)? ")

if conversor == "cm":
    cm_torre = 330*100
    print("A torre eiffel tem ", cm_torre, "centimetros de altura." )
if conversor == "km":
    km_torre = 330/1000
    print("A torre eiffel tem ", km_torre, "quilometros de altura." )
if conversor == "M":
    M_torre = 330*0.00062137
    print("A torre eiffel tem ", M_torre, "milhas de altura." )