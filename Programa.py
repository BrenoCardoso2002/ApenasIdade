while True:
    try:
        idade = int(input("\nInsira a sua idade: "))
        print("A sua idade é {}".format(idade))
        break
    except ValueError:
        print("Insira uma idade válida!!!")
