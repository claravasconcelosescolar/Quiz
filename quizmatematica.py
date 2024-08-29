# Introdução à programação
# Alunas: Letícia Beatriz, Kauanny Lorena, Clara Fonseca e Eli Ramalho
# Turma: INFO1M

def perguntar_questao(pergunta, opcoes, resposta_correta):
    """Exibe uma pergunta e coleta a resposta do usuário."""
    print(pergunta)
    for i, opcao in enumerate(opcoes, 1):
        print(f"{i}. {opcao}")
    resposta_usuario = input("Escolha uma opção (1, 2, 3, ou 4): ")
    return resposta_usuario.strip() == resposta_correta

def quiz_matematica(questoes):
    """Executa um quiz de matemática com base nas questões fornecidas."""
    pontuacao = 0
    total_questoes = len(questoes)
    for questao in questoes:
        correta = perguntar_questao(
            questao["pergunta"],
            questao["opcoes"],
            questao["resposta_correta"]
        )
        if correta:
            print("Resposta correta!")
            pontuacao += 1
        else:
            print("Resposta incorreta.")
        print()

    percentual_acerto = (pontuacao / total_questoes) * 100
    percentual_erro = 100 - percentual_acerto
    print(f"Você obteve {pontuacao} de {total_questoes} respostas corretas.")
    print(f"Percentual de acertos: {percentual_acerto:.2f}%")
    print(f"Percentual de erros: {percentual_erro:.2f}%")

def menu_principal():
    """Exibe o menu principal e executa o quiz selecionado."""
    while True:
        print("\nMenu Principal")
        print("1. Quiz de Pitágoras")
        print("2. Quiz de Porcentagem")
        print("3. Quiz de Fração")
        print("4. Sair")
        opcao = input("Escolha uma opção (1, 2, 3, ou 4): ")

        if opcao == "1":
            questoes_pitagoras = [
                {"pergunta": "Em um triângulo com uma base de 4cm e altura de 3cm, qual a sua hipotenusa?", "opcoes": ["6,3m", "5,8m", "6,7m", "9,5"], "resposta_correta": "3"},

                {"pergunta": "Um homem resolve instalar uma antena no telhado de sua casa. A base da antena está a 4 metros da borda do telhado, e o cabo que segura a antena tem 5 metros de comprimento. Qual é a altura da antena acima da base?", "opcoes": ["2,5m", "9m", "7,8m", "3m"], "resposta_correta": "4"},
                
                {"pergunta": "Você está montando um quadro de beisebol em um campo. A base de um dos postes está a 7 metros de distância do topo do poste, e a diagonal do poste, que é o cabo que o sustenta, mede 10 metros. Qual é a altura do poste?", "opcoes": ["7,1m", "7,3m", "6,7m", "8,4m"], "resposta_correta": "1"},

                {"pergunta": "Se a hipotenusa de um triângulo retângulo é 13 e um cateto é 5, qual é o comprimento do outro cateto??", "opcoes": ["8", "10", "12", "15"], "resposta_correta": "1"}
            ]
            quiz_matematica(questoes_pitagoras)

        elif opcao == "2":
            questoes_porcentagem = [
                {"pergunta": "Quanto  é 20/100 de 150?", "opcoes": ["30", "25", "20", "50"], "resposta_correta": "1"},

                {"pergunta": "Um item custa R$ 80 e está com um desconto de 15/100, qual é o preço desse item com o desconto aplicado?", "opcoes": ["68", "72", "64", "70"], "resposta_correta": "1"},

                {"pergunta": "Quanto é 25/100 de 160?", "opcoes": ["30", "40", "25", "45"], "resposta_correta": "2"},

                {"pergunta": "Quanto é 120 + 10/100 dele mesmo", "opcoes": ["132", "124", "130", "140"], "resposta_correta": "1"}
            ]
            quiz_matematica(questoes_porcentagem)

        elif opcao == "3":
            questoes_fracao = [
                {"pergunta": "Qual é a fração equivalente a 1/2?", "opcoes": ["2/4", "3/4", "1/3", "2/3"], "resposta_correta": "1"},
                {"pergunta": "Qual é a soma de 1/4 e 1/4?", "opcoes": ["1/4", "1/2", "2/4", "1"], "resposta_correta": "2"},
                {"pergunta": "Qual fração representa a parte inteira de 3/8?", "opcoes": ["1/4", "1", "0", "3/8"], "resposta_correta": "3"},
                {"pergunta": "Se você tem 3/5 de um bolo e come 1/5, quanto bolo resta?", "opcoes": ["2/5", "1/5", "4/5", "3/5"], "resposta_correta": "1"}
            ]
            quiz_matematica(questoes_fracao)

        elif opcao == "4":
            print("Fim do quiizz :)")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    menu_principal()
