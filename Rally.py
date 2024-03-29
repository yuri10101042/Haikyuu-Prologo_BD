import random

class Rally:
    def __init__(self, ponto=False, bloqueios=None, recepcoes=None, levantamentos=None, vencedor_rally=None, EmQuadra=None):
        self.ponto = ponto
        self.bloqueios = bloqueios if bloqueios is not None else []
        self.recepcoes = recepcoes if recepcoes is not None else []
        self.levantamentos = levantamentos if levantamentos is not None else []
        self.vencedor_rally = vencedor_rally
        self.EmQuadra = EmQuadra if EmQuadra is not None else []

    def adicionar_bloqueio(self, jogador):
        self.bloqueios.append(jogador)

    def adicionar_recepcao(self, jogador):
        self.recepcoes.append(jogador)

    def adicionar_levantamento(self, jogador):
        self.levantamentos.append(jogador)

    def JogarRally(self, time1, time2, EmQuadra1, EmQuadra2):
        times = [time1, time2]

        for jogador in EmQuadra1:
            self.EmQuadra.append(jogador)
        
        for jogador in EmQuadra2:
            self.EmQuadra.append(jogador)

        while True:
            print("Escolha a ação:")
            print("1. Ponto")
            print("2. Bloqueio")
            print("3. Levantamento")
            print("4. Recepção")

            escolha = input("Digite o número da opção desejada: ")

            if escolha not in ["1", "2", "3", "4"]:
                print("Opção não válida. Tente novamente.")
                continue

            if escolha == "1":
                print("Em qual time foi o ponto?")
                for i, time in enumerate(times):
                    print(f"{i + 1}. {time.nome}")

                numero_time = input("Digite o número do time: ")

                if not numero_time.isdigit() or int(numero_time) not in range(1, len(times) + 1):
                    print("Opção não válida. Tente novamente.")
                    continue

                elenco_atual = EmQuadra1 if int(numero_time) == 1 else EmQuadra2

                print("Que jogador fez o ponto?")
                for i, jogador in enumerate(elenco_atual):
                    print(f"{i + 1}. {jogador.nome}")
                print(f"{len(elenco_atual) + 1}. Erro do Time Adversário")

                numero_jogador = input("Digite o número do jogador: ")

                if not numero_jogador.isdigit() or int(numero_jogador) not in range(1, len(elenco_atual) + 2):
                    print("Opção não válida. Tente novamente.")
                    continue

                if int(numero_jogador) == len(elenco_atual) + 1:  # Verifica se é "Erro do Time Adversário"
                    self.vencedor_rally = times[int(numero_time) - 1].nome  # Define o time que está pontuando como vencedor
                    self.ponto = False  # Define o ponto como False
                    break

                self.ponto = elenco_atual[int(numero_jogador) - 1].nome
                self.vencedor_rally = times[int(numero_time) - 1].nome
                break

            elif escolha == "2":
                print("Em qual time foi o bloqueio?")
                for i, time in enumerate(times):
                    print(f"{i + 1}. {time.nome}")

                numero_time = input("Digite o número do time: ")

                if not numero_time.isdigit() or int(numero_time) not in range(1, len(times) + 1):
                    print("Opção não válida. Tente novamente.")
                    continue

                elenco_atual = EmQuadra1 if int(numero_time) == 1 else EmQuadra2

                print("Que jogador fez o bloqueio?")
                for i, jogador in enumerate(elenco_atual):
                    print(f"{i + 1}. {jogador.nome}")

                numero_jogador = input("Digite o número do jogador: ")

                if not numero_jogador.isdigit() or int(numero_jogador) not in range(1, len(elenco_atual) + 1):
                    print("Opção não válida. Tente novamente.")
                    continue

                self.adicionar_bloqueio(elenco_atual[int(numero_jogador) - 1].nome)
                continue

            elif escolha == "3":
                print("Em qual time foi o levantamento?")
                for i, time in enumerate(times):
                    print(f"{i + 1}. {time.nome}")

                numero_time = input("Digite o número do time: ")

                if not numero_time.isdigit() or int(numero_time) not in range(1, len(times) + 1):
                    print("Opção não válida. Tente novamente.")
                    continue

                elenco_atual = EmQuadra1 if int(numero_time) == 1 else EmQuadra2

                print("Que jogador fez o levantamento?")
                for i, jogador in enumerate(elenco_atual):
                    print(f"{i + 1}. {jogador.nome}")

                numero_jogador = input("Digite o número do jogador: ")

                if not numero_jogador.isdigit() or int(numero_jogador) not in range(1, len(elenco_atual) + 1):
                    print("Opção não válida. Tente novamente.")
                    continue

                self.adicionar_levantamento(elenco_atual[int(numero_jogador) - 1].nome)
                continue

            elif escolha == "4":
                print("Em qual time foi a recepção?")
                for i, time in enumerate(times):
                    print(f"{i + 1}. {time.nome}")

                numero_time = input("Digite o número do time: ")

                if not numero_time.isdigit() or int(numero_time) not in range(1, len(times) + 1):
                    print("Opção não válida. Tente novamente.")
                    continue

                elenco_atual = EmQuadra1 if int(numero_time) == 1 else EmQuadra2

                print("Que jogador fez a recepção?")
                for i, jogador in enumerate(elenco_atual):
                    print(f"{i + 1}. {jogador.nome}")

                numero_jogador = input("Digite o número do jogador: ")

                if not numero_jogador.isdigit() or int(numero_jogador) not in range(1, len(elenco_atual) + 1):
                    print("Opção não válida. Tente novamente.")
                    continue

                self.adicionar_recepcao(elenco_atual[int(numero_jogador) - 1].nome)
                continue

    def JogarRallyRandomizada(self, time1, time2, EmQuadra1, EmQuadra2, mediasTime1, mediasTime2):
        times = [time1, time2]

        for jogador in EmQuadra1:
            self.EmQuadra.append(jogador)
        
        for jogador in EmQuadra2:
            self.EmQuadra.append(jogador)

        while True:
            # Calcula as médias de pontos, bloqueios, levantamentos e recepções para cada time
            media_time1_pontos = sum(media[0] for media in mediasTime1) / len(mediasTime1)
            media_time2_pontos = sum(media[0] for media in mediasTime2) / len(mediasTime2)
            media_time1_bloqueios = sum(media[1] for media in mediasTime1) / len(mediasTime1)
            media_time2_bloqueios = sum(media[1] for media in mediasTime2) / len(mediasTime2)
            media_time1_levantamentos = sum(media[2] for media in mediasTime1) / len(mediasTime1)
            media_time2_levantamentos = sum(media[2] for media in mediasTime2) / len(mediasTime2)
            media_time1_recepcoes = sum(media[3] for media in mediasTime1) / len(mediasTime1)
            media_time2_recepcoes = sum(media[3] for media in mediasTime2) / len(mediasTime2)

            # Randomiza os resultados com base nas médias e uma taxa de variação
            pontuacao_time1 = random.gauss(media_time1_pontos, 0.2 * media_time1_pontos)  # Variação de 20%
            pontuacao_time2 = random.gauss(media_time2_pontos, 0.2 * media_time2_pontos)  # Variação de 20%
            bloqueios_time1 = max(0, int(random.gauss(media_time1_bloqueios, 0.2 * media_time1_bloqueios)))  # Variação de 20%
            bloqueios_time2 = max(0, int(random.gauss(media_time2_bloqueios, 0.2 * media_time2_bloqueios)))  # Variação de 20%
            levantamentos_time1 = max(0, int(random.gauss(media_time1_levantamentos, 0.2 * media_time1_levantamentos)))  # Variação de 20%
            levantamentos_time2 = max(0, int(random.gauss(media_time2_levantamentos, 0.2 * media_time2_levantamentos)))  # Variação de 20%
            recepcoes_time1 = max(0, int(random.gauss(media_time1_recepcoes, 0.2 * media_time1_recepcoes)))  # Variação de 20%
            recepcoes_time2 = max(0, int(random.gauss(media_time2_recepcoes, 0.2 * media_time2_recepcoes)))  # Variação de 20%

            # Determina o time vencedor com base na pontuação
            if pontuacao_time1 > pontuacao_time2:
                self.vencedor_rally = time1.nome
                for _ in range(pontuacao_time1):
                    jogador_ponto = random.choices(EmQuadra1, weights=[media[0] for media in mediasTime1])[0]
                    self.ponto = jogador_ponto.nome
                break
            elif pontuacao_time2 > pontuacao_time1:
                self.vencedor_rally = time2.nome
                for _ in range(pontuacao_time2):
                    jogador_ponto = random.choices(EmQuadra2, weights=[media[0] for media in mediasTime2])[0]
                    self.ponto = jogador_ponto.nome
            else:
                self.vencedor_rally = random.choice([time1.nome, time2.nome])  # Escolhe aleatoriamente entre os dois times
                if(self.vencedor_rally == time1.nome):
                    jogador_ponto = random.choices(EmQuadra1, weights=[media[0] for media in mediasTime1])[0]               
                elif(self.vencedor_rally == time1.nome):
                    jogador_ponto = random.choices(EmQuadra2, weights=[media[0] for media in mediasTime2])[0]    


            for _ in range(bloqueios_time1):
                jogador_bloqueio = random.choices(EmQuadra1, weights=[media[2] for media in mediasTime1])[0]
                self.adicionar_bloqueio(jogador_bloqueio.nome)

            for _ in range(bloqueios_time2):
                jogador_bloqueio = random.choices(EmQuadra2, weights=[media[2] for media in mediasTime2])[0]
                self.adicionar_bloqueio(jogador_bloqueio.nome)

            for _ in range(levantamentos_time1):
                jogador_levantamento = random.choices(EmQuadra1, weights=[media[3] for media in mediasTime1])[0]
                self.adicionar_levantamento(jogador_levantamento.nome)

            for _ in range(levantamentos_time2):
                jogador_levantamento = random.choices(EmQuadra2, weights=[media[3] for media in mediasTime2])[0]
                self.adicionar_levantamento(jogador_levantamento.nome)

            for _ in range(recepcoes_time1):
                jogador_recepcao = random.choices(EmQuadra1, weights=[media[4] for media in mediasTime1])[0]
                self.adicionar_recepcao(jogador_recepcao.nome)

            for _ in range(recepcoes_time2):
                jogador_recepcao = random.choices(EmQuadra2, weights=[media[4] for media in mediasTime2])[0]
                self.adicionar_recepcao(jogador_recepcao.nome)

            break