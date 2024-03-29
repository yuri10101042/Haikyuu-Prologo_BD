import sys
import os
import threading
import time
from Historico import Historico
from Temporada import Temporada
from Campeonato import Campeonato
from JogadorVolei import JogadorVolei
from Modalidade import Modalidade
from TimeVolei import TimeVolei
from Partida import Partida


def carregar_base_de_dados():
    global historico
    try:
        historico = historico.importar_informacoes()
        print("\nBase de dados principal carregada com sucesso.\n")
    except FileNotFoundError:
        print("\nBase de dados principal não encontrada.\n")
        criar_nova_base = input("Deseja criar uma nova base de dados? (s/n): ")

        if criar_nova_base.lower() == 's':
            historico = Historico()
            print("\nNova base de dados criada com sucesso!\n")
        else:
            sys.exit()
    except Exception as e:
        print(f"\nErro não identificado: {str(e)}\n")
        sys.exit()

def exportar_periodico():
    while True:
        time.sleep(60)
        historico.exportar_informacoes(os.path.join(backup_dir, f"BaseDeDados_{time.strftime('%Y%m%d%H%M%S')}.bin"))



def menu_principal():
    while True:
        print("\nSeja bem-vindo à Interface de Controle de Dados da mesa de RPG Haikyuu-Prólogo!\n")
        print("Escolha a ação que deseja realizar:")
        print("1- Jogar")
        print("2- Consultar Informações")
        print("3- Edição nos Dados")
        print("0- Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            menu_jogar()
        elif escolha == "2":
            menu_consulta()
        elif escolha == "3":
            menu_edicao_dados()
            pass
        elif escolha == "0":
            historico.exportar_informacoes("BaseDeDados_Principal.bin")
            print("\nAté logo!\n")
            sys.exit()
        else:
            print("\nOpção inválida. Tente novamente.\n")



def menu_jogar():
    while True:
        print("\nMenu Jogar:")
        print("1. Escolher Temporada")
        print("2. Criar Temporada")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            if not historico.Temporadas:
                print("Nenhuma temporada disponível.")
            else:
                print("Temporadas Disponíveis:")
                for i, temporada in enumerate(historico.Temporadas, 1):
                    print(f"{i}. Temporada {temporada.ano}")
                escolha_temporada = int(input("Escolha o número da temporada: "))
                if 1 <= escolha_temporada <= len(historico.Temporadas):
                    menu_jogar_temporada(historico.Temporadas[escolha_temporada - 1])
                else:
                    print("Escolha inválida.")

        elif escolha == '2':
            criar_nova_temporada()

        elif escolha == '3':
            print("Saindo do Menu Jogar.")
            break

        else:
            print("Escolha inválida. Tente novamente.")

def criar_nova_temporada():
    ano_temporada = int(input("Digite o ano da temporada: "))
    historico.adicionar_temporada(Temporada(ano_temporada))

def menu_jogar_temporada(temporada):
    while True:
        print("\nMenu Jogar Temporada:")
        print("1. Escolher Campeonato Válido")
        print("2. Escolher Partida Avulsa Válida")
        print("3. Escolher Campeonato Inválido")
        print("4. Escolher Partida Avulsa Inválida")
        print("5. Criar Campeonato")
        print("6. Criar Partida Avulsa")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            campeonatos_validos = temporada.campeonatosValidos
            if not campeonatos_validos:
                print("Nenhum campeonato válido disponível.")
            else:
                print("Campeonatos Válidos:")
                for i, campeonato in enumerate(campeonatos_validos, 1):
                    print(f"{i}. {campeonato.nome}")
                escolha_campeonato = int(input("Escolha o número do campeonato: "))
                if 1 <= escolha_campeonato <= len(campeonatos_validos):
                    menu_campeonato(campeonatos_validos[escolha_campeonato - 1])
                else:
                    print("Escolha inválida.")

        elif escolha == '2':
            partidas_avulsas_validas = temporada.jogosAvulsosValidos
            if not partidas_avulsas_validas:
                print("Nenhuma partida avulsa válida disponível.")
            else:
                print("Partidas Avulsas Válidas:")
                for i, partida in enumerate(partidas_avulsas_validas, 1):
                    print(f"{i}. {partida.time1.nome} vs {partida.time2.nome}")
                escolha_partida = int(input("Escolha o número da partida: "))
                if 1 <= escolha_partida <= len(partidas_avulsas_validas):
                    partidas_avulsas_validas[escolha_partida - 1].SetPorSet()
                else:
                    print("Escolha inválida.")

        elif escolha == '3':
            campeonatos_invalidos = temporada.campeonatosInvalidos
            if not campeonatos_invalidos:
                print("Nenhum campeonato inválido disponível.")
            else:
                print("Campeonatos Inválidos:")
                for i, campeonato in enumerate(campeonatos_invalidos, 1):
                    print(f"{i}. {campeonato.nome}")
                escolha_campeonato = int(input("Escolha o número do campeonato: "))
                if 1 <= escolha_campeonato <= len(campeonatos_invalidos):
                    menu_campeonato(campeonatos_invalidos[escolha_campeonato - 1])
                else:
                    print("Escolha inválida.")

        elif escolha == '4':
            partidas_avulsas_invalidas = temporada.jogosAvulsosInvalidos
            if not partidas_avulsas_invalidas:
                print("Nenhuma partida avulsa inválida disponível.")
            else:
                print("Partidas Avulsas Inválidas:")
                for i, partida in enumerate(partidas_avulsas_invalidas, 1):
                    print(f"{i}. {partida.time1.nome} vs {partida.time2.nome}")
                escolha_partida = int(input("Escolha o número da partida: "))
                if 1 <= escolha_partida <= len(partidas_avulsas_invalidas):
                    partidas_avulsas_invalidas[escolha_partida - 1].SetPorSet()
                else:
                    print("Escolha inválida.")

        elif escolha == '5':
            criar_campeonato(temporada)

        elif escolha == '6':
            criar_partidaavulsa(temporada)

        elif escolha == '7':
            print("Saindo do Menu Jogar Temporada.")
            break

        else:
            print("Escolha inválida. Tente novamente.")

def randomizar_campeonato(campeonato):
    mediasTimes = []
    for time in campeonato.TimesParticipantes:
        mediasJogadores = []
        for jogador in time.elenco_atual:
            mediasJogador = [jogador.]
        mediasTimes.append([time, mediasJogadores])


def criar_campeonato(temporada):
    nome_campeonato = input("Insira o nome do campeonato: ")

    # Listar todas as modalidades disponíveis numeradas
    print("\nModalidades disponíveis:")
    for i, modalidade in enumerate(historico.Modalidades, start=1):
        print(f"{i}. {modalidade.nome}")

    while True:
        escolha_modalidade = input("Escolha o número da modalidade do campeonato: ")
        if escolha_modalidade.isdigit() and 1 <= int(escolha_modalidade) <= len(historico.Modalidades):
            modalidade_escolhida = historico.Modalidades[int(escolha_modalidade) - 1]
            break
        else:
            print("Opção inválida. Escolha um número válido.")

    # Listar todos os times disponíveis numerados
    print("\nTimes disponíveis:")
    for i, time in enumerate(historico.Times, start=1):
        print(f"{i}. {time.nome}")

    times_participantes = []
    while True:
        escolha_time = input("Digite o número do time para adicionar ao campeonato (ou 's' para sair): ")
        if escolha_time.lower() == "s":
            break
        elif escolha_time.isdigit() and 1 <= int(escolha_time) <= len(historico.Times):
            time_escolhido = historico.Times[int(escolha_time) - 1]
            times_participantes.append(time_escolhido)
        else:
            print("Opção inválida. Escolha um número válido ou 's' para sair.")

    # Criar o objeto Campeonato
    campeonato = Campeonato(nome_campeonato, modalidade_escolhida, times_participantes)

    # Perguntar ao usuário se o campeonato é válido ou inválido
    while True:
        escolha = input("Este campeonato é válido? (s/n): ")
        if escolha.lower() == "s":
            temporada.adicionar_campeonatoValido(campeonato)
            break
        elif escolha.lower() == "n":
            temporada.adicionar_campeonatoInvalido(campeonato)
            break
        else:
            print("Opção inválida. Responda 's' para sim ou 'n' para não.")

    print("Campeonato criado com sucesso!")

def menu_campeonato(campeonato):
    while True:
        print("\nMenu do Campeonato:")
        print("1. Jogar o campeonato")
        print("2. Criar nova fase")
        print("0. Voltar ao menu anterior")

        escolha = input("Escolha a opção desejada: ")

        if escolha == "1":
            campeonato.JogarCampeonato()
        elif escolha == "2":
            campeonato.criarProximaFase()
        elif escolha == "0":
            print("Voltando ao menu anterior.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def criar_partidaavulsa(temporada):
    print("Criando uma nova partida avulsa:")
    # Escolha dos times
    print("Selecione os times para a partida:")
    times_participantes = historico.Times
    for i, time in enumerate(times_participantes, 1):
        print(f"{i}. {time.nome}")

    escolha_times = []
    while True:
        escolha = input("Digite o número do time (ou 's' para sair): ")
        if escolha.lower() == 's':
            if len(escolha_times) < 2:
                print("É necessário selecionar pelo menos 2 times.")
                continue
            else:
                break
        elif escolha.isdigit():
            indice_time = int(escolha) - 1
            if indice_time < 0 or indice_time >= len(times_participantes):
                print("Número de time inválido. Tente novamente.")
                continue
            escolha_times.append(times_participantes[indice_time])
        else:
            print("Escolha inválida. Tente novamente.")

    # Escolha da modalidade
    print("Selecione a modalidade da partida:")
    modalidades = historico.Modalidades
    for i, modalidade in enumerate(modalidades, 1):
        print(f"{i}. {modalidade.nome}")

    escolha_modalidade = None
    while True:
        escolha = input("Digite o número da modalidade: ")
        if escolha.isdigit():
            indice_modalidade = int(escolha) - 1
            if indice_modalidade < 0 or indice_modalidade >= len(modalidades):
                print("Número de modalidade inválido. Tente novamente.")
                continue
            escolha_modalidade = modalidades[indice_modalidade]
            break
        else:
            print("Escolha inválida. Tente novamente.")

    # Criar o objeto Campeonato
    partida = Partida(escolha_times[0], escolha_times[1], escolha_modalidade)

    # Escolha se a partida é válida
    while True:
        escolha_validade = input("A partida é válida? (s/n): ")
        if escolha_validade.lower() == 's':
            temporada.adicionar_jogosAvulsosValidos(partida)
            break
        elif escolha_validade.lower() == 'n':
            temporada.adicionar_jogosAvulsosInvalidos(partida)
            break
        else:
            print("Escolha inválida. Responda com 's' para sim ou 'n' para não.")

    print("Partida avulsa criada com sucesso!")




def menu_consulta():
    while True:
        print("\nMenu de Consulta:")
        print("1. Consulta de Rankings")
        print("2. Consulta Avançada")
        print("0. Voltar")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "0":
            print("Saindo do menu de consulta.")
            break
        elif escolha == "1":
            menu_rankings()
        elif escolha == "2":
            menu_consulta_avancada()
        else:
            print("Opção inválida. Tente novamente.")

def menu_rankings():
    while True:
        print("\n### Menu Rankings ###")
        print("1. Rankings de Jogadores")
        print("2. Ranking de Times")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_rankings_jogadores()
        elif opcao == "2":
            menu_rankings_times()
        elif opcao == "0":
            print("Retornando ao Menu Principal...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

def menu_rankings_jogadores():
    print("### Menu Rankings Jogadores ###")
    print("Filtrando jogadores...")
    jogadores_filtrados = filtrar_jogadores(historico.Jogadores)

    averages = []
    pontos = []
    levantamentos = []
    recepcoes = []
    bloqueios = []
    rallys_jogados = []

    print("Resgatando averages dos jogadores...")

    dados = resgatar_average_jogador(jogadores_filtrados)

    for dados_jogador in dados:
        averages.append(dados_jogador[0])
        pontos.append(dados_jogador[1])
        levantamentos.append(dados_jogador[2])
        recepcoes.append(dados_jogador[3])
        bloqueios.append(dados_jogador[4])
        rallys_jogados.append(dados_jogador[5])

    exibe_ranking_jogador(jogadores_filtrados, averages, pontos, levantamentos, recepcoes, bloqueios, rallys_jogados)

def menu_rankings_times():
    print("### Menu Rankings Times ###")
    print("Filtrando times...")
    times_filtrados = filtrar_times(historico.Times)

    averages = []

    print("Resgatando averages dos times...")

    averages = resgatar_average_time(times_filtrados)

    exibe_ranking_times(times_filtrados, averages)

def resgatar_average_jogador(jogadores):

    print("### Resgatar Average ###")
    print("1. Na História")
    print("2. Em uma Temporada")
    print("3. Em um Campeonato")
    print("4. Em uma Fase")
    print("5. Em uma Partida")
    opcao = input("Escolha uma opção pelo número: ")

    resultados = []

    if opcao == "1":  # Calcular average na história
        for jogador in jogadores:
            if historico.contar_rallys_do_jogador(jogador) == 0:
                resultados.append([0 , 0 , 0 , 0, 0, 0])
            else:
                pontos = (historico.calcularPontosJogadorHistorico(jogador))
                levantamentos = (historico.calcularLevantamentosJogadorHistorico(jogador))
                recepcoes = (historico.calcularRecepcoesJogadorHistorico(jogador))
                bloqueios = (historico.calcularBloqueiosJogadorHistorico(jogador))
                resultados.append([historico.jogadorAverageHistorico(jogador), pontos, levantamentos, recepcoes, bloqueios, historico.contar_rallys_do_jogador(jogador)])
    elif opcao == "2":  # Calcular average em uma temporada específica
        temporadas_disponiveis = historico.Temporadas
        print("Temporadas disponíveis:")
        for i, temporada in enumerate(temporadas_disponiveis, start=1):
            print(f"{i}. {temporada.ano}")
        opcao_temporada = int(input("Escolha a temporada pelo número: "))
        temporada_escolhida = temporadas_disponiveis[opcao_temporada - 1]
        for jogador in jogadores:
            if temporada_escolhida.contar_rallys_do_jogador(jogador) == 0:
                resultados.append([0 , 0 , 0 , 0, 0, 0])
            else:
                pontos = (temporada_escolhida.calcularPontosJogadorTemporada(jogador))
                levantamentos = (temporada_escolhida.calcularLevantamentosJogadorTemporada(jogador))
                recepcoes = (temporada_escolhida.calcularRecepcoesJogadorTemporada(jogador))
                bloqueios = (temporada_escolhida.calcularBloqueiosJogadorTemporada(jogador))
                resultados.append([temporada_escolhida.jogadorAverageTemporada(jogador), pontos, levantamentos, recepcoes, bloqueios, temporada_escolhida.contar_rallys_do_jogador(jogador)])
    elif opcao == "3":  # Calcular average em um campeonato específico
        temporadas_disponiveis = historico.Temporadas
        print("Temporadas disponíveis:")
        for i, temporada in enumerate(temporadas_disponiveis, start=1):
            print(f"{i}. {temporada.ano}")
        opcao_temporada = int(input("Escolha a temporada pelo número: "))
        temporada_escolhida = temporadas_disponiveis[opcao_temporada - 1]
        
        campeonatos_disponiveis = temporada_escolhida.campeonatosValidos
        print("Campeonatos disponíveis:")
        for i, campeonato in enumerate(campeonatos_disponiveis, start=1):
            print(f"{i}. {campeonato.nome}")
        opcao_campeonato = int(input("Escolha o campeonato pelo número: "))
        campeonato_escolhido = campeonatos_disponiveis[opcao_campeonato - 1]
        for jogador in jogadores:
            if campeonato_escolhido.contar_rallys_do_jogador(jogador) == 0:
                resultados.append([0 , 0 , 0 , 0, 0, 0])
            else:
                pontos = (campeonato_escolhido.calcularPontosJogadorCampeonato(jogador))
                levantamentos = (campeonato_escolhido.calcularLevantamentosJogadorCampeonato(jogador))
                recepcoes = (campeonato_escolhido.calcularRecepcoesJogadorCampeonato(jogador))
                bloqueios = (campeonato_escolhido.calcularBloqueiosJogadorCampeonato(jogador))
                resultados.append([campeonato_escolhido.jogadorAverageCampeonato(jogador), pontos, levantamentos, recepcoes, bloqueios, campeonato_escolhido.contar_rallys_do_jogador(jogador)])
    elif opcao == "4":  # Calcular average em uma fase específica
        temporadas_disponiveis = historico.Temporadas
        print("Temporadas disponíveis:")
        for i, temporada in enumerate(temporadas_disponiveis, start=1):
            print(f"{i}. {temporada.ano}")
        opcao_temporada = int(input("Escolha a temporada pelo número: "))
        temporada_escolhida = temporadas_disponiveis[opcao_temporada - 1]
        
        campeonatos_disponiveis = temporada_escolhida.campeonatosValidos
        print("Campeonatos disponíveis:")
        for i, campeonato in enumerate(campeonatos_disponiveis, start=1):
            print(f"{i}. {campeonato.nome}")
        opcao_campeonato = int(input("Escolha o campeonato pelo número: "))
        campeonato_escolhido = campeonatos_disponiveis[opcao_campeonato - 1]
        
        fases_disponiveis = campeonato_escolhido.fases
        print("Fases disponíveis:")
        for i, fase in enumerate(fases_disponiveis, start=1):
            print(f"{i}. {fase.numero}")
        opcao_fase = int(input("Escolha a fase pelo número: "))
        fase_escolhida = fases_disponiveis[opcao_fase - 1]
        for jogador in jogadores:
            if fase_escolhida.contar_rallys_do_jogador(jogador) == 0:
                resultados.append([0 , 0 , 0 , 0, 0, 0])
            else:
                pontos = (fase_escolhida.calcularPontosJogadorFase(jogador))
                levantamentos = (fase_escolhida.calcularLevantamentosJogadorFase(jogador))
                recepcoes = (fase_escolhida.calcularRecepcoesJogadorFase(jogador))
                bloqueios = (fase_escolhida.calcularBloqueiosJogadorFase(jogador))
                resultados.append([fase_escolhida.jogadorAverageFase(jogador), pontos, levantamentos, recepcoes, bloqueios, fase_escolhida.contar_rallys_do_jogador(jogador)])
    elif opcao == "5":  # Calcular average em uma partida específica
        temporadas_disponiveis = historico.Temporadas
        print("Temporadas disponíveis:")
        for i, temporada in enumerate(temporadas_disponiveis, start=1):
            print(f"{i}. {temporada.ano}")
        opcao_temporada = int(input("Escolha a temporada pelo número: "))
        temporada_escolhida = temporadas_disponiveis[opcao_temporada - 1]
        
        escolha_seguir = input("Partida Avulsa ou Partida de um Campeonato? 1/2:")

        if escolha_seguir == "1": 

            partidas_disponiveis = temporada_escolhida.jogosAvulsosValidos
            print("Partidas disponíveis:")
            for i, partida in enumerate(partidas_disponiveis, start=1):
                print(f"{i}. {partida.time1.nome} x {partida.time2.nome}")
            opcao_partida = int(input("Escolha a partida pelo número: "))
            partida_escolhida = partidas_disponiveis[opcao_partida - 1]

        else:

            campeonatos_disponiveis = temporada_escolhida.campeonatosValidos
            print("Campeonatos disponíveis:")
            for i, campeonato in enumerate(campeonatos_disponiveis, start=1):
                print(f"{i}. {campeonato.nome}")
            opcao_campeonato = int(input("Escolha o campeonato pelo número: "))
            campeonato_escolhido = campeonatos_disponiveis[opcao_campeonato - 1]
            
            fases_disponiveis = campeonato_escolhido.fases
            print("Fases disponíveis:")
            for i, fase in enumerate(fases_disponiveis, start=1):
                print(f"{i}. {fase.numero}")
            opcao_fase = int(input("Escolha a fase pelo número: "))
            fase_escolhida = fases_disponiveis[opcao_fase - 1]
            
            partidas_disponiveis = fase_escolhida.partidas
            print("Partidas disponíveis:")
            for i, partida in enumerate(partidas_disponiveis, start=1):
                print(f"{i}. {partida.time1.nome} x {partida.time2.nome}")
            opcao_partida = int(input("Escolha a partida pelo número: "))
            partida_escolhida = partidas_disponiveis[opcao_partida - 1]

        for jogador in jogadores:
            if partida_escolhida.contar_rallys_do_jogador(jogador) == 0:
                resultados.append([0 , 0 , 0 , 0, 0, 0])
            else:
                pontos =(partida_escolhida.PontosPorJogadorPartida(jogador))
                levantamentos = (partida_escolhida.LevantamentosPorJogadorPartida(jogador))
                recepcoes = (partida_escolhida.RecepcoesPorJogadorPartida(jogador))
                bloqueios = (partida_escolhida.BloqueiosPorJogadorPartida(jogador))
                resultados.append([partida_escolhida.jogadorAveragePartida(jogador), pontos, levantamentos, recepcoes, bloqueios, partida_escolhida.contar_rallys_do_jogador(jogador)])
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        return None
    return resultados

def resgatar_average_time(times):

    print("### Resgatar Average do Time ###")
    print("1. Na História")
    print("2. Em uma Temporada")
    print("3. Em um Campeonato")
    print("4. Em uma Fase")
    print("5. Em uma Partida")
    opcao = input("Escolha uma opção pelo número: ")

    resultados = []

    if opcao == "1":  # Calcular average na história
        for time in times:
            resultados.append(historico.timeAverageHistorico(time))
    elif opcao == "2":  # Calcular average em uma temporada específica
        temporadas_disponiveis = historico.Temporadas
        print("Temporadas disponíveis:")
        for i, temporada in enumerate(temporadas_disponiveis, start=1):
            print(f"{i}. {temporada.ano}")
        opcao_temporada = int(input("Escolha a temporada pelo número: "))
        temporada_escolhida = temporadas_disponiveis[opcao_temporada - 1]
        for time in times:
            resultados.append(temporada_escolhida.timeAverageTemporada(time))
    elif opcao == "3":  # Calcular average em um campeonato específico
        temporadas_disponiveis = historico.Temporadas
        print("Temporadas disponíveis:")
        for i, temporada in enumerate(temporadas_disponiveis, start=1):
            print(f"{i}. {temporada.ano}")
        opcao_temporada = int(input("Escolha a temporada pelo número: "))
        temporada_escolhida = temporadas_disponiveis[opcao_temporada - 1]
        
        campeonatos_disponiveis = temporada_escolhida.campeonatosValidos
        print("Campeonatos disponíveis:")
        for i, campeonato in enumerate(campeonatos_disponiveis, start=1):
            print(f"{i}. {campeonato.nome}")
        opcao_campeonato = int(input("Escolha o campeonato pelo número: "))
        campeonato_escolhido = campeonatos_disponiveis[opcao_campeonato - 1]
        for time in times:
            resultados.append(campeonato_escolhido.timeAverageCampeonato(time))
    elif opcao == "4":  # Calcular average em uma fase específica
        temporadas_disponiveis = historico.Temporadas
        print("Temporadas disponíveis:")
        for i, temporada in enumerate(temporadas_disponiveis, start=1):
            print(f"{i}. {temporada.ano}")
        opcao_temporada = int(input("Escolha a temporada pelo número: "))
        temporada_escolhida = temporadas_disponiveis[opcao_temporada - 1]
        
        campeonatos_disponiveis = temporada_escolhida.campeonatosValidos
        print("Campeonatos disponíveis:")
        for i, campeonato in enumerate(campeonatos_disponiveis, start=1):
            print(f"{i}. {campeonato.nome}")
        opcao_campeonato = int(input("Escolha o campeonato pelo número: "))
        campeonato_escolhido = campeonatos_disponiveis[opcao_campeonato - 1]
        
        fases_disponiveis = campeonato_escolhido.fases
        print("Fases disponíveis:")
        for i, fase in enumerate(fases_disponiveis, start=1):
            print(f"{i}. {fase.numero}")
        opcao_fase = int(input("Escolha a fase pelo número: "))
        fase_escolhida = fases_disponiveis[opcao_fase - 1]
        for time in times:
            resultados.append(fase_escolhida.timeAverageFase(time))
    elif opcao == "5":  # Calcular average em uma partida específica
        temporadas_disponiveis = historico.Temporadas
        print("Temporadas disponíveis:")
        for i, temporada in enumerate(temporadas_disponiveis, start=1):
            print(f"{i}. {temporada.ano}")
        opcao_temporada = int(input("Escolha a temporada pelo número: "))
        temporada_escolhida = temporadas_disponiveis[opcao_temporada - 1]
        
        escolha_seguir = input("Partida Avulsa ou Partida de um Campeonato? 1/2:")

        if escolha_seguir == "1": 

            partidas_disponiveis = temporada_escolhida.jogosAvulsosValidos
            print("Partidas disponíveis:")
            for i, partida in enumerate(partidas_disponiveis, start=1):
                print(f"{i}. {partida.time1.nome} x {partida.time2.nome}")
            opcao_partida = int(input("Escolha a partida pelo número: "))
            partida_escolhida = partidas_disponiveis[opcao_partida - 1]

        else:

            campeonatos_disponiveis = temporada_escolhida.campeonatosValidos
            print("Campeonatos disponíveis:")
            for i, campeonato in enumerate(campeonatos_disponiveis, start=1):
                print(f"{i}. {campeonato.nome}")
            opcao_campeonato = int(input("Escolha o campeonato pelo número: "))
            campeonato_escolhido = campeonatos_disponiveis[opcao_campeonato - 1]
            
            fases_disponiveis = campeonato_escolhido.fases
            print("Fases disponíveis:")
            for i, fase in enumerate(fases_disponiveis, start=1):
                print(f"{i}. {fase.numero}")
            opcao_fase = int(input("Escolha a fase pelo número: "))
            fase_escolhida = fases_disponiveis[opcao_fase - 1]
            
            partidas_disponiveis = fase_escolhida.partidas
            print("Partidas disponíveis:")
            for i, partida in enumerate(partidas_disponiveis, start=1):
                print(f"{i}. {partida.time1.nome} x {partida.time2.nome}")
            opcao_partida = int(input("Escolha a partida pelo número: "))
            partida_escolhida = partidas_disponiveis[opcao_partida - 1]

        for time in times:
            resultados.append(partida_escolhida.timeAveragePartida(time))
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        return None
    return resultados

def exibe_ranking_jogador(jogadores, averages, pontos, levantamentos, recepcoes, bloqueios, rallys_jogados):
    print(f"{'Posição':<8}{'Jogador':<20}{'Average':<10}{'Pontos':<10}{'Levantamentos':<15}{'Recepções':<15}{'Bloqueios':<10}{'Rallys Jogados':<15}")
    print("-" * 90)
    for i, jogador in enumerate(jogadores, start=1):
        print(f"{i:<8}{jogador.nome:<20}{averages[i-1]:<10.2f}{pontos[i-1]:<10}{levantamentos[i-1]:<15}{recepcoes[i-1]:<15}{bloqueios[i-1]:<10}{rallys_jogados[i-1]:<15}")

def exibe_ranking_times(times, averages):
    print(f"{'Posição':<8}{'Time':<20}{'Average':<10}")
    print("-" * 40)
    for i, time in enumerate(times, start=1):
        print(f"{i:<8}{time.nome:<20}{averages[i-1]:<10.2f}")

def filtrar_jogadores(jogadores):
    categorias = set(jogador.categoria for jogador in jogadores)
    posicoes = set(jogador.posicao for jogador in jogadores)
    paises = set(jogador.pais_nascimento for jogador in jogadores)
    regioes = set(jogador.regiao_nascimento for jogador in jogadores)

    jogadores_filtrados = jogadores

    while True:
        print("\n### Filtros de Jogadores ###")
        print("Categorias disponíveis:")
        for i, categoria in enumerate(categorias, start=1):
            print(f"{i}. {categoria}")
        print("Posições disponíveis:")
        for i, posicao in enumerate(posicoes, start=1):
            print(f"{i}. {posicao}")
        print("Países disponíveis:")
        for i, pais in enumerate(paises, start=1):
            print(f"{i}. {pais}")
        print("Regiões disponíveis:")
        for i, regiao in enumerate(regioes, start=1):
            print(f"{i}. {regiao}")
        print("0. Concluir e Mostrar Lista de Jogadores Filtrada")

        opcao = input("Escolha uma opção pelo número: ")

        if opcao == "0":
            print("Lista de Jogadores Filtrada:")
            for jogador in jogadores_filtrados:
                print(jogador.nome)
            break
        elif opcao.isdigit():
            opcao = int(opcao)
            if opcao == 1:
                categoria = int(input("Digite o número da categoria desejada: "))
                jogadores_filtrados = filtrar_jogadores_por_categoria(jogadores_filtrados, list(categorias)[categoria-1])
            elif opcao == 2:
                posicao = int(input("Digite o número da posição desejada: "))
                jogadores_filtrados = filtrar_jogadores_por_posicao(jogadores_filtrados, list(posicoes)[posicao-1])
            elif opcao == 3:
                pais = int(input("Digite o número do país desejado: "))
                jogadores_filtrados = filtrar_jogadores_por_pais(jogadores_filtrados, list(paises)[pais-1])
            elif opcao == 4:
                regiao = int(input("Digite o número da região desejada: "))
                jogadores_filtrados = filtrar_jogadores_por_regiao(jogadores_filtrados, list(regioes)[regiao-1])
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    return jogadores_filtrados

def filtrar_times(times):
    categorias = set(time.categoria for time in times)
    paises = set(time.pais for time in times)
    regioes = set(time.regiao for time in times)

    times_filtrados = times

    while True:
        print("\n### Filtros de Times ###")
        print("Categorias disponíveis:")
        for i, categoria in enumerate(categorias, start=1):
            print(f"{i}. {categoria}")
        print("Países disponíveis:")
        for i, pais in enumerate(paises, start=1):
            print(f"{i}. {pais}")
        print("Estados disponíveis:")
        for i, regiao in enumerate(regioes, start=1):
            print(f"{i}. {regiao}")
        print("0. Concluir e Mostrar Lista de Times Filtrada")

        opcao = input("Escolha uma opção pelo número: ")

        if opcao == "0":
            print("Lista de Times Filtrada:")
            for time in times_filtrados:
                print(time.nome)
            break
        elif opcao.isdigit():
            opcao = int(opcao)
            if opcao == 1:
                categoria = int(input("Digite o número da categoria desejada: "))
                times_filtrados = filtrar_times_por_categoria(times_filtrados, list(categorias)[categoria-1])
            elif opcao == 2:
                pais = int(input("Digite o número do país desejado: "))
                times_filtrados = filtrar_times_por_pais(times_filtrados, list(paises)[pais-1])
            elif opcao == 3:
                regiao = int(input("Digite o número da região desejada: "))
                times_filtrados = filtrar_times_por_regiao(times_filtrados, list(regioes)[regiao-1])
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    return times_filtrados

def filtrar_jogadores_por_categoria(jogadores, categoria):
    jogadores_filtrados = []

    for jogador in jogadores:
        if jogador.categoria == categoria:
            jogadores_filtrados.append(jogador)

    return jogadores_filtrados

def filtrar_jogadores_por_pais(jogadores, pais):
    jogadores_filtrados = []

    for jogador in jogadores:
        if jogador.pais_nascimento == pais:
            jogadores_filtrados.append(jogador)

    return jogadores_filtrados

def filtrar_jogadores_por_posicao(jogadores, posicao):
    jogadores_filtrados = []

    for jogador in jogadores:
        if jogador.posicao == posicao:
            jogadores_filtrados.append(jogador)

    return jogadores_filtrados

def filtrar_jogadores_por_regiao(jogadores, regiao):
    jogadores_filtrados = []

    for jogador in jogadores:
        if jogador.regiao_nascimento == regiao:
            jogadores_filtrados.append(jogador)

    return jogadores_filtrados

def filtrar_times_por_categoria(times, categoria):
    times_filtrados = []

    for time in times:
        if time.categoria == categoria:
            times_filtrados.append(time)

    return times_filtrados

def filtrar_times_por_pais(times, pais):
    times_filtrados = []

    for time in times:
        if time.pais == pais:
            times_filtrados.append(time)

    return times_filtrados

def filtrar_times_por_regiao(times, regiao):
    times_filtrados = []

    for time in times:
        if time.regiao == regiao:
            times_filtrados.append(time)

    return times_filtrados

def menu_consulta_avancada():
    while True:
        print("\nEscolha a opção de Consulta Avançada:")
        print("1- Consultar Lista Oficial Jogadores")
        print("2- Consultar Lista Oficial Clubes")
        print("3- Consultar Lista Oficial Modalidades")
        print("4- Consultar Temporadas")
        print("0- Voltar ao Menu Principal")

        escolha_consulta_avancada = input("Digite o número da opção desejada: ")

        if escolha_consulta_avancada == "1":
            consultar_jogadores(historico.Jogadores)
        elif escolha_consulta_avancada == "2":
            consultar_times(historico.Times)
        elif escolha_consulta_avancada == "3":
            consultar_modalidades(historico.Modalidades)
        elif escolha_consulta_avancada == "4":
            consultar_temporadas(historico.Temporadas)
        elif escolha_consulta_avancada == "0":
            return
        else:
            print("\nOpção inválida. Tente novamente.\n")

def consultar_temporada(temporada):
    while True:
        print("\nAtributos da Temporada:")
        print("1. Ano")
        print("2. Campeonatos Válidos")
        print("3. Campeonatos Inválidos")
        print("4. Jogos Avulsos Válidos")
        print("5. Jogos Avulsos Inválidos")
        print("0. Sair da edição da temporada")

        escolha = input("\nEscolha o número do atributo para consultar: ")

        if escolha == '0':
            print("Saindo da consulta da temporada.")
            break

        try:
            escolha = int(escolha)
            if escolha == 1:
                print(f"Ano da temporada: {temporada.ano}")
            elif escolha == 2:
                print("\nCampeonatos Válidos:")
                consultar_campeonatos(temporada.campeonatosValidos)
            elif escolha == 3:
                print("\nCampeonatos Inválidos:")
                consultar_campeonatos(temporada.campeonatosInvalidos)
            elif escolha == 4:
                print("\nJogos Avulsos Válidos:")
                consultar_partidas(temporada.jogosAvulsosValidos)
            elif escolha == 5:
                print("\nJogos Avulsos Inválidos:")
                consultar_partidas(temporada.jogosAvulsosInvalidos)
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Escolha inválida. Tente novamente.")

def consultar_temporadas(temporadas):
    while True:
        print("\nTemporadas Disponíveis:")
        for i, temporada in enumerate(temporadas, start=1):
            print(f"{i}. Temporada {temporada.ano}")

        print("0. Sair")

        escolha_temporada = input("\nEscolha o número da temporada que deseja consultar: ")

        if escolha_temporada == '0':
            print("Saindo da consulta de temporadas.")
            break

        try:
            escolha_temporada = int(escolha_temporada)
            if 1 <= escolha_temporada <= len(temporadas):
                temporada_escolhida = temporadas[escolha_temporada - 1]
                print(f"\nConsultando temporada {temporada_escolhida.ano}:")
                consultar_temporada(temporada_escolhida)
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Escolha inválida. Tente novamente.")

def consultar_campeonato(campeonato):
    while True:
        print("\nAtributos do Campeonato:")
        print("1. Nome")
        print("2. Modalidade")
        print("3. Times Participantes")
        print("4. Fases")
        print("5. Classificação dos Times")
        print("0. Voltar")

        escolha_atributo = input("\nEscolha o número do atributo para consultar: ")

        if escolha_atributo == "0":
            print("Saindo da consulta do campeonato.")
            break

        try:
            escolha_atributo = int(escolha_atributo)

            if escolha_atributo == 1:
                print(f"\nNome: {campeonato.nome}")

            elif escolha_atributo == 2:
                print("\nModalidade:")
                print(f"Nome: {campeonato.modalidade.nome}")
                print(f"Pontos Máximos por Set: {campeonato.modalidade.pontosMaxSet}")
                print(f"Número Máximo de Sets: {campeonato.modalidade.setsMax}")

            elif escolha_atributo == 3:
                print("\nTimes Participantes:")
                for i, time in enumerate(campeonato.TimesParticipantes, start=1):
                    print(f"{i}. {time.nome}")
                print("\nConsultar times participantes:")
                consultar_times(campeonato.TimesParticipantes)

            elif escolha_atributo == 4:
                print("\nFases:")
                consultar_fases(campeonato.fases)

            elif escolha_atributo == 5:
                print("\nClassificação dos Times:")
                for i, time in enumerate(campeonato.ClassificacaoTimes, start=1):
                    print(f"{i}. {time.nome}")
                print("\nConsultar classificação dos times:")
                consultar_times(campeonato.ClassificacaoTimes)

            else:
                print("Escolha inválida. Tente novamente.")

        except ValueError:
            print("\nEscolha inválida. Tente novamente.")

def consultar_campeonatos(lista_campeonatos):
    while True:
        print("\nLista de Campeonatos:")
        for i, campeonato in enumerate(lista_campeonatos, start=1):
            print(f"{i}. {campeonato.nome}")

        escolha_campeonato = input("\nEscolha o número do campeonato para consultar (ou '0' para sair): ")

        if escolha_campeonato == '0':
            print("Saindo da consulta de campeonatos.")
            break

        try:
            escolha_campeonato = int(escolha_campeonato)
            if 1 <= escolha_campeonato <= len(lista_campeonatos):
                campeonato_consultar = lista_campeonatos[escolha_campeonato - 1]
                print(f"\nConsultando campeonato: {campeonato_consultar.nome}")
                consultar_campeonato(campeonato_consultar)
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Escolha inválida. Tente novamente.")

def consultar_fase(fase):
    while True:
        print("\nAtributos da Fase:")
        print("1. Número da Fase")
        print("2. Modalidade")
        print("3. Partidas")
        print("4. Times Classificados")

        escolha_atributo = input("\nEscolha o número do atributo para editar (0 para voltar): ")

        if escolha_atributo == "0":
            print("Saindo da consulta de fase.")
            break

        try:
            escolha_atributo = int(escolha_atributo)

            if escolha_atributo == 1:
                print(f"\nNúmero da Fase: {fase.numero}")

            elif escolha_atributo == 2:
                print("\nConsultar Modalidade:")
                consultar_modalidade(fase.modalidade)

            elif escolha_atributo == 3:
                print("\nConsultar Partidas:")
                consultar_partidas(fase.partidas)

            elif escolha_atributo == 4:
                print("\nConsultar Times Classificados:")
                consultar_times(fase.TimesClassificados)

            else:
                print("\nEscolha inválida. Tente novamente.")

        except ValueError:
            print("\nEscolha inválida. Tente novamente.")

def consultar_fases(lista_fases):
    while True:
        print("\nLista de Fases:")
        for i, fase in enumerate(lista_fases, start=1):
            print(f"{i}. Fase {fase.numero}")

        escolha_fase = input("\nEscolha o número da fase para consultar (0 para voltar): ")

        if escolha_fase == "0":
            print("Saindo da consulta de fases.")
            break

        try:
            escolha_fase = int(escolha_fase)
            if escolha_fase < 1 or escolha_fase > len(lista_fases):
                print("Escolha inválida. Tente novamente.")
                continue

            fase_selecionada = lista_fases[escolha_fase - 1]
            print(f"\nConsultando Fase {fase_selecionada.numero}:")
            consultar_fase(fase_selecionada)

        except ValueError:
            print("\nEscolha inválida. Tente novamente.")

def consultar_partida(partida):
    while True:
        print("\nAtributos da Partida:")
        print("1. Time 1")
        print("2. Time 2")
        print("3. Modalidade")
        print("4. Sets")
        print("5. Sets Time 1")
        print("6. Sets Time 2")
        print("7. Consultar Vencedor")
        print("8. Consultar Perdedor")

        escolha_atributo = input("\nEscolha o número do atributo para consultar (0 para voltar): ")

        if escolha_atributo == "0":
            print("Saindo da consulta da partida.")
            break

        if escolha_atributo == "1":
            print(f"Time 1: {partida.time1.nome}")
            consultar_time(partida.time1)
        elif escolha_atributo == "2":
            print(f"Time 2: {partida.time2.nome}")
            consultar_time(partida.time2)
        elif escolha_atributo == "3":
            print(f"Modalidade: {partida.modalidade.nome}")
            consultar_modalidade(partida.modalidade)
        elif escolha_atributo == "4":
            print("Sets:")
            consultar_sets(partida.sets)
        elif escolha_atributo == "5":
            print(f"Sets Time 1: {partida.SetsTime1}")
        elif escolha_atributo == "6":
            print(f"Sets Time 2: {partida.SetsTime2}")
        elif escolha_atributo == "7":
            print("Consultar Vencedor:")
            consultar_time(partida.vencedor)
        elif escolha_atributo == "8":
            print("Consultar Perdedor:")
            consultar_time(partida.perdedor)
        else:
            print("Escolha inválida. Tente novamente.")

def consultar_partidas(partidas):
    while True:
        print("\nLista de Partidas:")
        for i, partida in enumerate(partidas, start=1):
            print(f"{i}. {partida.time1.nome} vs {partida.time2.nome}")

        escolha_partida = input("\nEscolha o número da partida para consultar (0 para voltar): ")

        if escolha_partida == "0":
            print("Saindo da consulta de partidas.")
            break

        try:
            escolha_partida = int(escolha_partida)
            partida_escolhida = partidas[escolha_partida - 1]
            print(f"\nConsulta Partida: {partida_escolhida.time1.nome} vs {partida_escolhida.time2.nome}")
            consultar_partida(partida_escolhida)
        except (ValueError, IndexError):
            print("\nEscolha inválida. Tente novamente.")

def consultar_set(set_objeto):
    while True:
        print("\nAtributos do Set:")
        print("1. Rallys")
        print("2. Pontos do Time 1")
        print("3. Pontos do Time 2")
        print("4. Consultar Vencedor")
        print("5. Consultar Perdedor")

        escolha_atributo = input("\nEscolha o número do atributo para consultar (0 para voltar): ")

        if escolha_atributo == "0":
            print("Saindo da consulta do set.")
            break

        if escolha_atributo == "1":
            consultar_rallys(set_objeto.rallys)
        elif escolha_atributo == "2":
            print(f"Valor de pontos do Time 1: {set_objeto.pontos_time1}")
        elif escolha_atributo == "3":
            print(f"Valor de pontos do Time 2: {set_objeto.pontos_time2}")
        elif escolha_atributo == "4":
            print("Consultar Vencedor:")
            consultar_time(set_objeto.vencedor_set)
        elif escolha_atributo == "5":
            print("Consultar Perdedor:")
            consultar_time(set_objeto.perdedor_set)
        else:
            print("Escolha inválida. Tente novamente.")

def consultar_sets(lista_sets):
    while True:
        print("\nLista de Sets:")
        for i, set_objeto in enumerate(lista_sets, start=1):
            print(f"{i}. Set {i}")

        escolha_set = input("\nEscolha o número do set para editar (0 para sair): ")

        if escolha_set == "0":
            print("Saindo do menu de consulta de sets.")
            break

        try:
            indice_set = int(escolha_set) - 1
            set_consultar = lista_sets[indice_set]
            print(f"\nConsultando Set {indice_set + 1}:")
            consultar_set(set_consultar)
        except (ValueError, IndexError):
            print("\nEscolha inválida. Tente novamente.")

def consultar_rally(rally):
    while True:
        print("Escolha o atributo do rally que deseja consultar:")
        print("1. Ponto")
        print("2. Bloqueios")
        print("3. Recepções")
        print("4. Levantamentos")

        escolha_atributo = input("Digite o número do atributo: ")

        if escolha_atributo == "1":
            valor_atual = rally.ponto
            print(f"Valor de Ponto: {valor_atual}")
            break
        elif escolha_atributo == "2":
            print("Bloqueios:")
            for i, bloqueio in enumerate(rally.bloqueios, start=1):
                print(f"{i}. {bloqueio.nome}")
            break
        elif escolha_atributo == "3":
            print("Recepções:")
            for i, recepcao in enumerate(rally.recepcoes, start=1):
                print(f"{i}. {recepcao.nome}")
            break
        elif escolha_atributo == "4":
            print("Levantamentos:")
            for i, levantamento in enumerate(rally.levantamentos, start=1):
                print(f"{i}. {levantamento.nome}")
            break
        else:
            print("Opção inválida. Tente novamente.")

def consultar_rallys(lista_rallys):
    if not lista_rallys:
        print("Não há rallys na lista para consultar.")
        return

    while True:
        print("Rallys Disponíveis para Consulta:")
        for i, rally in enumerate(lista_rallys, start=1):
            print(f"{i}. Rally {i}")

        escolha_rally = input("Escolha o número do rally que deseja consultar (ou '0' para sair): ")

        if escolha_rally == "0":
            print("Saindo do menu de consulta de rallys.")
            break

        try:
            escolha_rally = int(escolha_rally)
            rally_escolhido = lista_rallys[escolha_rally - 1]
        except (ValueError, IndexError):
            print("Escolha inválida. Tente novamente.")
            continue

        print(f"\nConsultando Rally {escolha_rally}:\n")
        consultar_rally(rally_escolhido)

def consultar_modalidade(modalidade):
    # Mostra todos os atributos da modalidade
    print("\nAtributos da Modalidade:")
    print("1. Nome da Modalidade")
    print("2. Pontos Máximos por Set")
    print("3. Número Máximo de Sets")

    escolha_atributo = input("\nEscolha o número do atributo para consultar: ")

    try:
        escolha_atributo = int(escolha_atributo)
    except ValueError:
        print("\nEscolha inválida. Voltando ao menu anterior.\n")
        return

    if escolha_atributo == 1:
        print(f"\nNome da modalidade: {modalidade.nome}.")
    elif escolha_atributo == 2:
        print(f"\nPontos máximos por set: {modalidade.pontos_max_set}.")
    elif escolha_atributo == 3:
        print(f"\nNúmero máximo de sets: {modalidade.sets_max}.")
    else:
        print("\nAtributo inválido. Voltando ao menu anterior.\n")
        return

def consultar_modalidades(lista_modalidades):
    # Mostra a lista de modalidades para o usuário escolher
    print("\nLista de Modalidades:")
    for i, modalidade in enumerate(lista_modalidades, start=1):
        print(f"{i}. {modalidade.nome}")

    escolha_modalidade = input("\nEscolha o número da modalidade para consultar: ")

    try:
        escolha_modalidade = int(escolha_modalidade)
        modalidade_escolhida = lista_modalidades[escolha_modalidade - 1]
    except (ValueError, IndexError):
        print("\nEscolha inválida. Voltando ao menu anterior.\n")
        return

    consultar_modalidade(modalidade_escolhida)

def consultar_time(time):
    # Mostra todos os atributos do time
    print("\nAtributos do Time:")
    print("1. Nome")
    print("2. País")
    print("3. Região")
    print("4. Modalidade")
    print("5. Elenco Atual")

    escolha_atributo = input("\nEscolha o número do atributo para consultar: ")

    try:
        escolha_atributo = int(escolha_atributo)
    except ValueError:
        print("\nEscolha inválida. Voltando ao menu anterior.\n")
        return

    if escolha_atributo == 1:
        print(f"\nNome do time: {time.nome}")
    elif escolha_atributo == 2:
        print(f"\nPaís do time: {time.pais}")
    elif escolha_atributo == 3:
        print(f"\nRegião do time: {time.regiao}")
    elif escolha_atributo == 4:
        print(f"\nCategoria do time: {time.categoria}")
    elif escolha_atributo == 5:
        consultar_jogadores(time.elenco_atual)
    else:
        print("\nAtributo inválido. Voltando ao menu anterior.\n")
        return

def consultar_times(lista_times):

    # Mostra a lista de times para o usuário escolher
    print("\nLista de Times:")
    for i, time in enumerate(lista_times, start=1):
        print(f"{i}. {time.nome}")

    escolha_time = input("\nEscolha o número do time para consultar: ")

    try:
        escolha_time = int(escolha_time)
        time_escolhido = lista_times[escolha_time - 1]
    except (ValueError, IndexError):
        print("\nEscolha inválida. Voltando ao menu anterior.\n")
        return

    consultar_time(time_escolhido)

def consultar_jogador(jogador):
    print("\nAtributos disponíveis para consulta:")
    atributos = ["nome", "idade", "altura", "regiao_nascimento", "pais_nascimento", "posicao", "maoDominante", "camisaNumero", "genero"]
    for j, atributo in enumerate(atributos, start=1):
        print(f"{j}. {atributo.capitalize()}")

    escolha_atributo = input("\nEscolha o número do atributo para consultar: ")

    try:
        escolha_atributo = int(escolha_atributo)
    except ValueError:
        print("\nEscolha inválida. Voltando ao menu anterior.\n")
        return

    atributo_consultar = atributos[escolha_atributo - 1]

    print(f"\nValor para {atributo_consultar}: {getattr(jogador, atributo_consultar)}")

def consultar_jogadores(lista_jogadores):

    # Mostra a lista de jogadores para o usuário escolher
    print("\nLista de Jogadores:")
    for i, jogador in enumerate(lista_jogadores, start=1):
        print(f"{i}. {jogador.nome}")

    escolha_jogador = input("\nEscolha o número do jogador para consultar: ")

    try:
        escolha_jogador = int(escolha_jogador)
        jogador_escolhido = lista_jogadores[escolha_jogador - 1]
    except (ValueError, IndexError):
        print("\nEscolha inválida. Voltando ao menu anterior.\n")
        return

    consultar_jogador(jogador_escolhido)


def menu_edicao_dados():
    print("\nEscolha a opção de Edição de Dados:")
    print("1- Edição Normal")
    print("2- Edição Avançada")
    print("0- Voltar ao Menu Principal")

    escolha_edicao = input("Digite o número da opção desejada: ")

    if escolha_edicao == "1":
        menu_edicao_normal()
    elif escolha_edicao == "2":
        menu_edicao_avancada()
        pass
    elif escolha_edicao == "0":
        return
    else:
        print("\nOpção inválida. Tente novamente.\n")

def menu_edicao_normal():
    global historico
    while True:
        print("\nEscolha a opção desejada:")
        print("1- Criar Jogador")
        print("2- Criar Time")
        print("3- Inserir Jogador em Time")
        print("4- Criar Modalidade")
        print("5- Remover Jogador de Time")
        print("6- Criar Jogador por String")  
        print("7- Criar Time vazio por String")  
        print("8- Criar Time com Jogadores por String")  
        print("0- Voltar ao Menu Principal")

        escolha_edicao_normal = input("Digite o número da opção desejada: ")

        if escolha_edicao_normal == "1":
            criar_jogador()
        elif escolha_edicao_normal == "2":
            criar_time()
        elif escolha_edicao_normal == "3":
            inserir_jogador_em_time()
        elif escolha_edicao_normal == "4":
            criar_modalidade()
        elif escolha_edicao_normal == "5":
            remover_jogador_de_time()
        elif escolha_edicao_normal == "6":
            string_jogador = input(f"Digite a String para criar o Jogador:")
            criar_jogador_por_string(string_jogador)
        elif escolha_edicao_normal == "7":
            string_time = input(f"Digite a String para criar o Time:")
            criar_time_por_string(string_time)
        elif escolha_edicao_normal == "8":
            string_time = input(f"Digite a String para criar o Time:")
            string_jogadores = input(f"Digite a String para criar os Jogadores:")
            criar_time_e_jogadores_por_string(string_time, string_jogadores)
        elif escolha_edicao_normal == "0":
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")

def remover_jogador_de_time():
    global historico
    jogador_escolhido = escolher_jogador()

    if jogador_escolhido:
        times_com_jogador = [time for time in historico.Times if jogador_escolhido in time.elenco_atual]
        
        if times_com_jogador:
            print("\nEscolha o time do qual deseja remover o jogador:")
            for i, time in enumerate(times_com_jogador, start=1):
                print(f"{i}. {time.nome}")

            escolha_time = input("\nDigite o número do time ou o nome completo: ")

            try:
                escolha_time = int(escolha_time)
                time_escolhido = times_com_jogador[escolha_time - 1]
            except (ValueError, IndexError):
                time_escolhido = next((time for time in times_com_jogador if time.nome.lower() == escolha_time.lower()), None)

            if time_escolhido:
                time_escolhido.remover_jogador(jogador_escolhido)
                jogador_escolhido.time_atual = None
                print(f"\nJogador {jogador_escolhido.nome} removido do time {time_escolhido.nome}.\n")
            else:
                print("\nTime não encontrado.\n")
        else:
            print(f"\nO jogador {jogador_escolhido.nome} não está associado a nenhum time.\n")

def escolher_jogador():
    global historico
    print("\nEscolha um jogador:")
    
    # Mostra a lista de jogadores
    for i, jogador in enumerate(historico.Jogadores, start=1):
        print(f"{i}. {jogador.nome} - {jogador.pais_nascimento}")

    escolha_numero = input("\nDigite o número do jogador ou o nome completo: ")

    try:
        escolha_numero = int(escolha_numero)
        jogador_escolhido = historico.Jogadores[escolha_numero - 1]
    except (ValueError, IndexError):
        jogador_escolhido = next((jogador for jogador in historico.Jogadores if jogador.nome.lower() == escolha_numero.lower()), None)

    if jogador_escolhido:
        return jogador_escolhido
    else:
        print("\nJogador não encontrado.\n")
        return None

def criar_jogador():
    global historico

    print("\nCadastro de Novo Jogador:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    genero = int(input("Genero: "))
    altura = float(input("Altura (em metros): "))
    maoDominante = int(input("Mão Dominante: "))
    regiao_nascimento = input("Região de Nascimento: ")
    pais_nascimento = input("País de Nascimento: ")

    # Mostra as posições disponíveis
    print("\nPosições Disponíveis:")
    print("1. Oposto")
    print("2. Levantador")
    print("3. Líbero")
    print("4. Central")
    print("5. Ponteiro")

    # Solicita a escolha da posição
    escolha_posicao = input("Escolha o número da posição desejada: ")

    # Mapeia a escolha para a posição correspondente
    posicoes = ["Oposto", "Levantador", "Líbero", "Central", "Ponteiro"]
    posicao = posicoes[int(escolha_posicao) - 1]

    # Mostra as posições disponíveis
    print("\nCategorias Disponíveis:")
    print("1. Colegial")
    print("2. Universitário")
    print("3. Profissional")

    escolha_categoria = input("Escolha o número da categoria desejada: ")

    numeroCamisa = input("Número da Camisa: ")

    # Mapeia a escolha para a posição correspondente
    categorias = ["Colegial", "Universitário", "Profissional"]
    categoria = categorias[int(escolha_categoria) - 1]

    novo_jogador = JogadorVolei(nome, idade, altura, regiao_nascimento, pais_nascimento, posicao, categoria, maoDominante, numeroCamisa, genero)
    historico.Jogadores.append(novo_jogador)

    print(f"\nJogador {nome} criado com sucesso!\n")

def criar_jogador_por_string(info_string):
    global historico

    # Divide a string em uma lista de informações
    info_list = info_string.split(',')

    # Extrai as informações individuais da lista
    nome = info_list[0]
    idade = int(info_list[1])
    genero = info_list[2]
    altura = float(info_list[3])
    maoDominante = info_list[4]
    regiao_nascimento = info_list[5]
    pais_nascimento = info_list[6]
    posicao = info_list[7]
    categoria = info_list[8]
    numeroCamisa = info_list[9]

    # Cria o jogador usando a função criar_jogador
    novo_jogador = JogadorVolei(nome, idade, altura, regiao_nascimento, pais_nascimento, posicao, categoria, maoDominante, numeroCamisa, genero)
    historico.Jogadores.append(novo_jogador)

    print(f"\nJogador {nome} criado com sucesso!\n")

def criar_time():

    print("\nCadastro de Novo Time:")
    nome = input("Nome do Time: ")
    pais = input("País do Time: ")
    regiao = input("Região do Time: ")

    # Mostra as posições disponíveis
    print("\nCategorias Disponíveis:")
    print("1. Colegial")
    print("2. Universitário")
    print("3. Profissional")

    escolha_categoria = input("Escolha o número da categoria desejada: ")

    # Mapeia a escolha para a posição correspondente
    categorias = ["Colegial", "Universitário", "Profissional"]
    categoria = categorias[int(escolha_categoria) - 1]

    novo_time = TimeVolei(nome, pais, regiao, categoria)
    historico.Times.append(novo_time)

    print(f"\nTime {nome} criado com sucesso!\n")

def criar_time_por_string(info_string):
    global historico

    # Divide a string em uma lista de informações
    info_list = info_string.split(',')

    # Extrai as informações individuais da lista
    nome = info_list[0]
    pais = info_list[1]
    regiao = info_list[2]
    categoria = info_list[3]

    # Cria o time usando a função criar_time
    novo_time = TimeVolei(nome, pais, regiao, categoria)
    historico.Times.append(novo_time)

    print(f"\nTime {nome} criado com sucesso!\n")

def inserir_jogador_em_time():
    global historico

    print("\nInserção de Jogador em Time:")

    # Mostra a lista de jogadores
    print("\nLista de Jogadores:")
    for i,jogador in enumerate(historico.Jogadores, start=1):
        print(f"{i}. {jogador.nome} - {jogador.pais_nascimento}")

    escolha_jogador = input("Escolha o número ou nome do jogador: ")

    # Tenta converter a escolha para número
    try:
        escolha_jogador = int(escolha_jogador)
        jogador_escolhido = historico.Jogadores[escolha_jogador - 1]
    except (ValueError, IndexError):
        # Se não for possível converter para número ou estiver fora dos limites, tenta encontrar pelo nome
        jogador_escolhido = next((jogador for jogador in historico.Jogadores if jogador.nome.lower() == escolha_jogador.lower()), None)

    if not jogador_escolhido:
        print("\nJogador não encontrado. Voltando ao menu principal.\n")
        return

    # Mostra a lista de times
    print("\nLista de Times:")
    for i, time in enumerate(historico.Times, start=1):
        print(f"{i}. {time.nome} - {time.pais}")

    escolha_time = input("Escolha o número ou nome do time: ")

    # Tenta converter a escolha para número
    try:
        escolha_time = int(escolha_time)
        time_escolhido = historico.Times[escolha_time - 1]
    except (ValueError, IndexError):
        # Se não for possível converter para número ou estiver fora dos limites, tenta encontrar pelo nome
        time_escolhido = next((time for time in historico.Times if time.nome.lower() == escolha_time.lower()), None)

    if not time_escolhido:
        print("\nTime não encontrado. Voltando ao menu principal.\n")
        return

    # Verifica se o jogador está em algum outro time e remove, se necessário
    for outro_time in historico.Times:
        if jogador_escolhido in outro_time.elenco_atual:
            outro_time.remover_jogador(jogador_escolhido)

    # Adiciona o jogador ao novo time
    time_escolhido.adicionar_jogador(jogador_escolhido)

    print(f"\nJogador {jogador_escolhido.nome} inserido no time {time_escolhido.nome} com sucesso!\n")

def criar_time_e_jogadores_por_string(info_time, info_jogadores):
    criar_time_por_string(info_time)
    novo_time = historico.Times[-1]
    
    lista_jogadores = info_jogadores.split('/')
    for info_jogador in lista_jogadores:
        criar_jogador_por_string(info_jogador)
        novo_time.adicionar_jogador(historico.Jogadores[-1])

def criar_modalidade():
    global historico

    print("\nCadastro de Nova Modalidade:")
    nome = input("Nome da Modalidade: ")
    pontos_max_set = int(input("Pontos Máximos por Set: "))
    sets_max = int(input("Número Máximo de Sets: "))

    nova_modalidade = Modalidade(nome, pontos_max_set, sets_max)
    historico.Modalidades.append(nova_modalidade)

    print(f"\nModalidade {nome} criada com sucesso!\n")



def menu_edicao_avancada():
    while True:
        print("\nEscolha a opção de Edição Avançada:")
        print("1- Editar Lista Oficial Jogadores")
        print("2- Editar Lista Oficial Clubes")
        print("3- Editar Lista Oficial Modalidades")
        print("4- Editar Temporadas")
        print("0- Voltar ao Menu Principal")

        escolha_edicao_avancada = input("Digite o número da opção desejada: ")

        if escolha_edicao_avancada == "1":
            editar_jogadores(historico.Jogadores)
        elif escolha_edicao_avancada == "2":
            editar_times(historico.Times)
        elif escolha_edicao_avancada == "3":
            editar_modalidades(historico.Modalidades)
        elif escolha_edicao_avancada == "4":
            editar_temporadas(historico.Temporadas)
        elif escolha_edicao_avancada == "0":
            return
        else:
            print("\nOpção inválida. Tente novamente.\n")

def editar_temporada(temporada):
    while True:
        print("\nAtributos da Temporada:")
        print("1. Ano")
        print("2. Campeonatos Válidos")
        print("3. Campeonatos Inválidos")
        print("4. Jogos Avulsos Válidos")
        print("5. Jogos Avulsos Inválidos")
        print("0. Sair da edição da temporada")

        escolha = input("\nEscolha o número do atributo para editar: ")

        if escolha == '0':
            print("Saindo da edição da temporada.")
            break

        try:
            escolha = int(escolha)
            if escolha == 1:
                print(f"Ano atual da temporada: {temporada.ano}")
                novo_ano = input("Digite o novo ano da temporada: ")
                temporada.ano = novo_ano
                print(f"Ano da temporada atualizado para {temporada.ano}.")
            elif escolha == 2:
                print("\nCampeonatos Válidos:")
                editar_campeonatos(temporada.campeonatosValidos)
            elif escolha == 3:
                print("\nCampeonatos Inválidos:")
                editar_campeonatos(temporada.campeonatosInvalidos)
            elif escolha == 4:
                print("\nJogos Avulsos Válidos:")
                editar_partidas(temporada.jogosAvulsosValidos)
            elif escolha == 5:
                print("\nJogos Avulsos Inválidos:")
                editar_partidas(temporada.jogosAvulsosInvalidos)
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Escolha inválida. Tente novamente.")

def editar_temporadas(temporadas):
    while True:
        print("\nTemporadas Disponíveis:")
        for i, temporada in enumerate(temporadas, start=1):
            print(f"{i}. Temporada {temporada.ano}")

        print("0. Sair")

        escolha_temporada = input("\nEscolha o número da temporada que deseja editar: ")

        if escolha_temporada == '0':
            print("Saindo da edição de temporadas.")
            break

        try:
            escolha_temporada = int(escolha_temporada)
            if 1 <= escolha_temporada <= len(temporadas):
                temporada_escolhida = temporadas[escolha_temporada - 1]
                print(f"\nEditando temporada {temporada_escolhida.ano}:")
                editar_temporada(temporada_escolhida)
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Escolha inválida. Tente novamente.")

def editar_campeonato(campeonato):
    while True:
        print("\nAtributos do Campeonato:")
        print("1. Nome")
        print("2. Modalidade")
        print("3. Times Participantes")
        print("4. Fases")
        print("5. Classificação dos Times")
        print("0. Voltar")

        escolha_atributo = input("\nEscolha o número do atributo para editar: ")

        if escolha_atributo == "0":
            print("Saindo da edição do campeonato.")
            break

        try:
            escolha_atributo = int(escolha_atributo)

            if escolha_atributo == 1:
                print(f"\nNome atual: {campeonato.nome}")
                novo_nome = input("Digite o novo nome: ")
                campeonato.nome = novo_nome

            elif escolha_atributo == 2:
                print("\nModalidade atual:")
                print(f"Nome: {campeonato.modalidade.nome}")
                print(f"Pontos Máximos por Set: {campeonato.modalidade.pontosMaxSet}")
                print(f"Número Máximo de Sets: {campeonato.modalidade.setsMax}")
                print("\nEditando modalidade:")
                editar_modalidade(campeonato.modalidade)

            elif escolha_atributo == 3:
                print("\nTimes Participantes:")
                for i, time in enumerate(campeonato.TimesParticipantes, start=1):
                    print(f"{i}. {time.nome}")
                print("\nEditar times participantes:")
                editar_times(campeonato.TimesParticipantes)

            elif escolha_atributo == 4:
                print("\nFases:")
                editar_fases(campeonato.fases)

            elif escolha_atributo == 5:
                print("\nClassificação dos Times:")
                for i, time in enumerate(campeonato.ClassificacaoTimes, start=1):
                    print(f"{i}. {time.nome}")
                print("\nEditar classificação dos times:")
                editar_times(campeonato.ClassificacaoTimes)

            else:
                print("Escolha inválida. Tente novamente.")

        except ValueError:
            print("\nEscolha inválida. Tente novamente.")

def editar_campeonatos(lista_campeonatos):
    while True:
        print("\nLista de Campeonatos:")
        for i, campeonato in enumerate(lista_campeonatos, start=1):
            print(f"{i}. {campeonato.nome}")

        escolha_campeonato = input("\nEscolha o número do campeonato para editar (ou '0' para sair): ")

        if escolha_campeonato == '0':
            print("Saindo da edição de campeonatos.")
            break

        try:
            escolha_campeonato = int(escolha_campeonato)
            if 1 <= escolha_campeonato <= len(lista_campeonatos):
                campeonato_editar = lista_campeonatos[escolha_campeonato - 1]
                print(f"\nEditando campeonato: {campeonato_editar.nome}")
                editar_campeonato(campeonato_editar)
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Escolha inválida. Tente novamente.")

def editar_fase(fase):
    while True:
        print("\nAtributos da Fase:")
        print("1. Número da Fase")
        print("2. Modalidade")
        print("3. Partidas")
        print("4. Times Classificados")

        escolha_atributo = input("\nEscolha o número do atributo para editar (0 para voltar): ")

        if escolha_atributo == "0":
            print("Saindo da edição de fase.")
            break

        try:
            escolha_atributo = int(escolha_atributo)

            if escolha_atributo == 1:
                print(f"\nNúmero atual da Fase: {fase.numero}")
                novo_numero = input("Digite o novo número da Fase: ")
                fase.numero = int(novo_numero)

            elif escolha_atributo == 2:
                print("\nEditando Modalidade:")
                editar_modalidade(fase.modalidade)

            elif escolha_atributo == 3:
                print("\nEditando Partidas:")
                editar_partidas(fase.partidas)

            elif escolha_atributo == 4:
                print("\nEditando Times Classificados:")
                editar_times(fase.TimesClassificados)

            else:
                print("\nEscolha inválida. Tente novamente.")

        except ValueError:
            print("\nEscolha inválida. Tente novamente.")

def editar_fases(lista_fases):
    while True:
        print("\nLista de Fases:")
        for i, fase in enumerate(lista_fases, start=1):
            print(f"{i}. Fase {fase.numero}")

        escolha_fase = input("\nEscolha o número da fase para editar (0 para voltar): ")

        if escolha_fase == "0":
            print("Saindo da edição de fases.")
            break

        try:
            escolha_fase = int(escolha_fase)
            if escolha_fase < 1 or escolha_fase > len(lista_fases):
                print("Escolha inválida. Tente novamente.")
                continue

            fase_selecionada = lista_fases[escolha_fase - 1]
            print(f"\nEditando Fase {fase_selecionada.numero}:")
            editar_fase(fase_selecionada)

        except ValueError:
            print("\nEscolha inválida. Tente novamente.")

def editar_partida(partida):
    while True:
        print("\nAtributos da Partida:")
        print("1. Time 1")
        print("2. Time 2")
        print("3. Modalidade")
        print("4. Sets")
        print("5. Sets Time 1")
        print("6. Sets Time 2")
        print("7. Editar Vencedor")
        print("8. Editar Perdedor")

        escolha_atributo = input("\nEscolha o número do atributo para editar (0 para voltar): ")

        if escolha_atributo == "0":
            print("Saindo da edição da partida.")
            break

        if escolha_atributo == "1":
            print(f"Time 1 atual: {partida.time1.nome}")
            editar_time(partida.time1)
        elif escolha_atributo == "2":
            print(f"Time 2 atual: {partida.time2.nome}")
            editar_time(partida.time2)
        elif escolha_atributo == "3":
            print(f"Modalidade atual: {partida.modalidade.nome}")
            editar_modalidade(partida.modalidade)
        elif escolha_atributo == "4":
            print("Sets:")
            editar_sets(partida.sets)
        elif escolha_atributo == "5":
            print(f"Sets Time 1 atual: {partida.SetsTime1}")
            novo_sets_time1 = input("Novos Sets Time 1: ")
            partida.SetsTime1 = int(novo_sets_time1)
        elif escolha_atributo == "6":
            print(f"Sets Time 2 atual: {partida.SetsTime2}")
            novo_sets_time2 = input("Novos Sets Time 2: ")
            partida.SetsTime2 = int(novo_sets_time2)
        elif escolha_atributo == "7":
            print("Editar Vencedor:")
            editar_time(partida.vencedor)
        elif escolha_atributo == "8":
            print("Editar Perdedor:")
            editar_time(partida.perdedor)
        else:
            print("Escolha inválida. Tente novamente.")

def editar_partidas(partidas):
    while True:
        print("\nLista de Partidas:")
        for i, partida in enumerate(partidas, start=1):
            print(f"{i}. {partida.time1.nome} vs {partida.time2.nome}")

        escolha_partida = input("\nEscolha o número da partida para editar (0 para voltar): ")

        if escolha_partida == "0":
            print("Saindo da edição de partidas.")
            break

        try:
            escolha_partida = int(escolha_partida)
            partida_escolhida = partidas[escolha_partida - 1]
            print(f"\nEditando Partida: {partida_escolhida.time1.nome} vs {partida_escolhida.time2.nome}")
            editar_partida(partida_escolhida)
        except (ValueError, IndexError):
            print("\nEscolha inválida. Tente novamente.")

def editar_set(set_objeto):
    while True:
        print("\nAtributos do Set:")
        print("1. Rallys")
        print("2. Pontos do Time 1")
        print("3. Pontos do Time 2")
        print("4. Editar Vencedor")
        print("5. Editar Perdedor")

        escolha_atributo = input("\nEscolha o número do atributo para editar (0 para voltar): ")

        if escolha_atributo == "0":
            print("Saindo da edição do set.")
            break

        if escolha_atributo == "1":
            editar_rallys(set_objeto.rallys)
        elif escolha_atributo == "2":
            print(f"Valor atual de pontos do Time 1: {set_objeto.pontos_time1}")
            novo_pontos_time1 = input("Novos pontos do Time 1: ")
            set_objeto.pontos_time1 = int(novo_pontos_time1)
        elif escolha_atributo == "3":
            print(f"Valor atual de pontos do Time 2: {set_objeto.pontos_time2}")
            novo_pontos_time2 = input("Novos pontos do Time 2: ")
            set_objeto.pontos_time2 = int(novo_pontos_time2)
        elif escolha_atributo == "4":
            print("Editar Vencedor:")
            editar_time(set_objeto.vencedor_set)
        elif escolha_atributo == "5":
            print("Editar Perdedor:")
            editar_time(set_objeto.perdedor_set)
        else:
            print("Escolha inválida. Tente novamente.")

def editar_sets(lista_sets):
    while True:
        print("\nLista de Sets:")
        for i, set_objeto in enumerate(lista_sets, start=1):
            print(f"{i}. Set {i}")

        escolha_set = input("\nEscolha o número do set para editar (0 para sair): ")

        if escolha_set == "0":
            print("Saindo do menu de edição de sets.")
            break

        try:
            indice_set = int(escolha_set) - 1
            set_editar = lista_sets[indice_set]
            print(f"\nEditando Set {indice_set + 1}:")
            editar_set(set_editar)
        except (ValueError, IndexError):
            print("\nEscolha inválida. Tente novamente.")

def editar_rally(rally):
    while True:
        print("Escolha o atributo do rally que deseja editar:")
        print("1. Ponto")
        print("2. Bloqueios")
        print("3. Recepções")
        print("4. Levantamentos")

        escolha_atributo = input("Digite o número do atributo: ")

        if escolha_atributo == "1":
            valor_atual = rally.ponto
            novo_valor = input(f"Digite o novo valor para Ponto (atual: {valor_atual}): ")
            rally.ponto = novo_valor
            print(f"Valor de Ponto atualizado para: {novo_valor}")
            break
        elif escolha_atributo == "2":
            print("Escolha qual bloqueio deseja editar:")
            for i, bloqueio in enumerate(rally.bloqueios, start=1):
                print(f"{i}. {bloqueio.nome}")

            escolha_bloqueio = input("Digite o número do bloqueio: ")
            try:
                escolha_bloqueio = int(escolha_bloqueio)
                jogador_bloqueio = rally.bloqueios[escolha_bloqueio - 1]
            except (ValueError, IndexError):
                print("Escolha inválida. Tente novamente.")
                continue

            novo_valor = input(f"Digite o novo valor para o bloqueio (atual: {jogador_bloqueio}): ")
            rally.bloqueios[escolha_bloqueio - 1] = novo_valor
            print(f"Bloqueio atualizado para: {novo_valor}")
            break
        elif escolha_atributo == "3":
            print("Escolha qual recepção deseja editar:")
            for i, recepcao in enumerate(rally.recepcoes, start=1):
                print(f"{i}. {recepcao.nome}")

            escolha_recepcao = input("Digite o número da recepção: ")
            try:
                escolha_recepcao = int(escolha_recepcao)
                jogador_recepcao = rally.recepcoes[escolha_recepcao - 1]
            except (ValueError, IndexError):
                print("Escolha inválida. Tente novamente.")
                continue

            novo_valor = input(f"Digite o novo valor para a recepção (atual: {jogador_recepcao}): ")
            rally.recepcoes[escolha_recepcao - 1] = novo_valor
            print(f"Recepção atualizada para: {novo_valor}")
            break
        elif escolha_atributo == "4":
            print("Escolha qual levantamento deseja editar:")
            for i, levantamento in enumerate(rally.levantamentos, start=1):
                print(f"{i}. {levantamento.nome}")

            escolha_levantamento = input("Digite o número do levantamento: ")
            try:
                escolha_levantamento = int(escolha_levantamento)
                jogador_levantamento = rally.levantamentos[escolha_levantamento - 1]
            except (ValueError, IndexError):
                print("Escolha inválida. Tente novamente.")
                continue

            novo_valor = input(f"Digite o novo valor para o levantamento (atual: {jogador_levantamento}): ")
            rally.levantamentos[escolha_levantamento - 1] = novo_valor
            print(f"Levantamento atualizado para: {novo_valor}")
            break
        else:
            print("Opção inválida. Tente novamente.")

def editar_rallys(lista_rallys):
    if not lista_rallys:
        print("Não há rallys na lista para editar.")
        return

    while True:
        print("Rallys Disponíveis para Edição:")
        for i, rally in enumerate(lista_rallys, start=1):
            print(f"{i}. Rally {i}")

        escolha_rally = input("Escolha o número do rally que deseja editar (ou '0' para sair): ")

        if escolha_rally == "0":
            print("Saindo do menu de edição de rallys.")
            break

        try:
            escolha_rally = int(escolha_rally)
            rally_escolhido = lista_rallys[escolha_rally - 1]
        except (ValueError, IndexError):
            print("Escolha inválida. Tente novamente.")
            continue

        print(f"\nEditando Rally {escolha_rally}:\n")
        editar_rally(rally_escolhido)

def editar_modalidade(modalidade):
    # Mostra todos os atributos da modalidade
    print("\nAtributos da Modalidade:")
    print("1. Nome da Modalidade")
    print("2. Pontos Máximos por Set")
    print("3. Número Máximo de Sets")

    escolha_atributo = input("\nEscolha o número do atributo para editar: ")

    try:
        escolha_atributo = int(escolha_atributo)
    except ValueError:
        print("\nEscolha inválida. Voltando ao menu anterior.\n")
        return

    if escolha_atributo == 1:
        novo_nome = input("Digite o novo nome para a modalidade: ")
        modalidade.nome = novo_nome
        print(f"\nNome da modalidade atualizado para {novo_nome}.")
    elif escolha_atributo == 2:
        novo_pontos_max_set = input("Digite o novo valor para pontos máximos por set: ")
        modalidade.pontos_max_set = int(novo_pontos_max_set)
        print(f"\nPontos máximos por set atualizado para {novo_pontos_max_set}.")
    elif escolha_atributo == 3:
        novo_sets_max = input("Digite o novo valor para número máximo de sets: ")
        modalidade.sets_max = int(novo_sets_max)
        print(f"\nNúmero máximo de sets atualizado para {novo_sets_max}.")
    else:
        print("\nAtributo inválido. Voltando ao menu anterior.\n")
        return

def editar_modalidades(lista_modalidades):
    # Mostra a lista de modalidades para o usuário escolher
    print("\nLista de Modalidades:")
    for i, modalidade in enumerate(lista_modalidades, start=1):
        print(f"{i}. {modalidade.nome}")

    escolha_modalidade = input("\nEscolha o número da modalidade para editar: ")

    try:
        escolha_modalidade = int(escolha_modalidade)
        modalidade_escolhida = lista_modalidades[escolha_modalidade - 1]
    except (ValueError, IndexError):
        print("\nEscolha inválida. Voltando ao menu anterior.\n")
        return

    editar_modalidade(modalidade_escolhida)

def editar_time(time):
    # Mostra todos os atributos do time
    print("\nAtributos do Time:")
    print("1. Nome")
    print("2. País")
    print("3. Região")
    print("4. Modalidade")
    print("5. Elenco Atual")

    escolha_atributo = input("\nEscolha o número do atributo para editar: ")

    try:
        escolha_atributo = int(escolha_atributo)
    except ValueError:
        print("\nEscolha inválida. Voltando ao menu anterior.\n")
        return

    if escolha_atributo == 1:
        novo_nome = input("Digite o novo nome para o time: ")
        time.nome = novo_nome
        print(f"\nNome do time atualizado para {novo_nome}.")
    elif escolha_atributo == 2:
        novo_pais = input("Digite o novo país para o time: ")
        time.pais = novo_pais
        print(f"\nPaís do time atualizado para {novo_pais}.")
    elif escolha_atributo == 3:
        nova_regiao = input("Digite a nova região para o time: ")
        time.regiao = nova_regiao
        print(f"\nRegião do time atualizada para {nova_regiao}.")
    elif escolha_atributo == 4:
        nova_categoria = input("Digite a nova categoria para o time: ")
        time.categoria = nova_categoria
        print(f"\nCategoria do time atualizado para {nova_categoria}.")
        pass
    elif escolha_atributo == 5:
        # Editar elenco atual
        editar_jogadores(time.elenco_atual)
    else:
        print("\nAtributo inválido. Voltando ao menu anterior.\n")
        return

def editar_times(lista_times):
    global historico

    # Mostra a lista de times para o usuário escolher
    print("\nLista de Times:")
    for i, time in enumerate(lista_times, start=1):
        print(f"{i}. {time.nome}")

    escolha_time = input("\nEscolha o número do time para editar: ")

    try:
        escolha_time = int(escolha_time)
        time_escolhido = lista_times[escolha_time - 1]
    except (ValueError, IndexError):
        print("\nEscolha inválida. Voltando ao menu anterior.\n")
        return

    editar_time(time_escolhido)

def editar_jogador(jogador):
    print("\nAtributos disponíveis para edição:")
    atributos = ["nome", "idade", "altura", "regiao_nascimento", "pais_nascimento", "posicao", "maoDominante", "camisaNumero", "genero"]
    for j, atributo in enumerate(atributos, start=1):
        print(f"{j}. {atributo.capitalize()}")

    escolha_atributo = input("\nEscolha o número do atributo para editar: ")

    try:
        escolha_atributo = int(escolha_atributo)
    except ValueError:
        print("\nEscolha inválida. Voltando ao menu anterior.\n")
        return

    atributo_editar = atributos[escolha_atributo - 1]

    print(f"\nValor atual para {atributo_editar}: {getattr(jogador, atributo_editar)}")

    novo_valor = input(f"Digite o novo valor para {atributo_editar} do jogador {jogador.nome}: ")

    setattr(jogador, atributo_editar, novo_valor)

    print(f"\nAtributo {atributo_editar} do jogador {jogador.nome} editado com sucesso!\n")

def editar_jogadores(lista_jogadores):
    global historico

    # Mostra a lista de jogadores para o usuário escolher
    print("\nLista de Jogadores:")
    for i, jogador in enumerate(lista_jogadores, start=1):
        print(f"{i}. {jogador.nome}")

    escolha_jogador = input("\nEscolha o número do jogador para editar: ")

    try:
        escolha_jogador = int(escolha_jogador)
        jogador_escolhido = lista_jogadores[escolha_jogador - 1]
    except (ValueError, IndexError):
        print("\nEscolha inválida. Voltando ao menu anterior.\n")
        return

    editar_jogador(jogador_escolhido)



if __name__ == "__main__":
    
    historico = Historico()
    backup_dir = "ArquivosBackup"
    os.makedirs(backup_dir, exist_ok=True)

    carregar_base_de_dados()

    # Inicia a thread para exportar periodicamente
    thread_exportar_periodico = threading.Thread(target=exportar_periodico)
    thread_exportar_periodico.daemon = True
    thread_exportar_periodico.start()

    # Substitua o loop principal pelo menu principal
    menu_principal()