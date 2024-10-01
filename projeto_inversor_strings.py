class InversorDeString:
    def __init__(self, entrada):
        # Inicializa a entrada convertida em string
        self.entrada = str(entrada)

    def inverter(self):
        # Inicializa uma nova string vazia que será construída invertida
        string_invertida = ""
        # Itera pelos caracteres da string de trás para frente
        for i in range(len(self.entrada) - 1, -1, -1):
            string_invertida += self.entrada[i]
        return string_invertida


# Função principal para interação com o usuário
def main():
    while True:
        # Solicita a entrada do usuário
        entrada_usuario = input("Digite qualquer coisa: ")

        # Verifica se a entrada é vazia ou contém apenas um caractere
        if len(entrada_usuario) == 0:
            print("Erro: A entrada não pode ser vazia, deve conter no mínimo dois caracteres.Tente novamente.")
        elif len(entrada_usuario) == 1:
            print("Erro: A entrada deve conter no mínimo dois caracteres. Tente novamente.")
        else:
            # Se a entrada for válida, sai do loop
            break

    # Cria uma instância da classe InversorDeString
    inversor = InversorDeString(entrada_usuario)

    # Chama o método inverter e exibe o resultado
    string_invertida = inversor.inverter()
    print(f"Agora veja o que foi digitado de forma invertida: {string_invertida}")


# Executa o programa
if __name__ == "__main__":
    main()
