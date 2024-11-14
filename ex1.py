velocidade = float(input("Digite a velocidade do carro em km/h: "))

limite = 80


if velocidade > limite:
    
    excesso = velocidade - limite
  
    multa = excesso * 20
    
    print(f"Você foi multado ´por excesso de velocidade ! O valor da multa é R$ {multa:.2f} ")
else:
    
    print("Você está dentro do limite de velocidade. Sem multas!")