nota_1 = int(input("por favor ingrese nota 1 :"))
nota_2 = int(input("por favor ingrese nota 2 :"))
nota_3 = int(input("por favor ingrese nota 3 :"))
nota_1 = nota_1 * 0.2
nota_2 = nota_2 * 0.3
nota_3 = nota_3 * 0.5
total = 0.2 + 0.3 + 0.5 
promedio_ponderado  = nota_1 + nota_2 + nota_3 / total
print("la nota final es :" ,promedio_ponderado)