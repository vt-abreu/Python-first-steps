import tkinter as tk

janela = tk.Tk()
janela.title("Jogo da Velha Invencível (Minimax)")

# Frame para o tabuleiro
frame_tabuleiro = tk.Frame(janela)
frame_tabuleiro.grid(row=0, column=0, padx=10, pady=10)

botoes = []
jogador_humano = "X"
jogador_pc = "O"
jogo_ativo = True

combinacoes = [
    [0,1,2], [3,4,5], [6,7,8],
    [0,3,6], [1,4,7], [2,5,8],
    [0,4,8], [2,4,6]
]

def resetar_jogo():
    global jogo_ativo
    for botao in botoes:
        botao.config(text="", state=tk.NORMAL, bg="SystemButtonFace")
    jogo_ativo = True
    label_status.config(text="Sua vez (X)")
    btn_jogar_novamente.grid_remove()
    btn_sair.grid_remove()

def sair():
    janela.destroy()

def verificar_vitoria_tabuleiro(tabuleiro, jogador):
    for combo in combinacoes:
        if all(tabuleiro[i] == jogador for i in combo):
            return True
    return False

def verificar_empate_tabuleiro(tabuleiro):
    return all(c != "" for c in tabuleiro)

def verificar_vitoria():
    for combo in combinacoes:
        valores = [botoes[i]["text"] for i in combo]
        if valores == [jogador_humano]*3:
            for i in combo:
                botoes[i].config(bg="red")
            return True
        elif valores == [jogador_pc]*3:
            for i in combo:
                botoes[i].config(bg="red")
            return True
    if all(botao["text"] != "" for botao in botoes):
        return "Empate"
    return False

def minimax(tabuleiro, profundidade, is_max):
    if verificar_vitoria_tabuleiro(tabuleiro, jogador_pc):
        return 10 - profundidade
    elif verificar_vitoria_tabuleiro(tabuleiro, jogador_humano):
        return profundidade - 10
    elif verificar_empate_tabuleiro(tabuleiro):
        return 0

    if is_max:
        melhor_pontuacao = -float('inf')
        for i in range(9):
            if tabuleiro[i] == "":
                tabuleiro[i] = jogador_pc
                pontuacao = minimax(tabuleiro, profundidade + 1, False)
                tabuleiro[i] = ""
                if pontuacao > melhor_pontuacao:
                    melhor_pontuacao = pontuacao
        return melhor_pontuacao
    else:
        melhor_pontuacao = float('inf')
        for i in range(9):
            if tabuleiro[i] == "":
                tabuleiro[i] = jogador_humano
                pontuacao = minimax(tabuleiro, profundidade + 1, True)
                tabuleiro[i] = ""
                if pontuacao < melhor_pontuacao:
                    melhor_pontuacao = pontuacao
        return melhor_pontuacao

def jogada_pc():
    global jogo_ativo
    if not jogo_ativo:
        return

    tabuleiro = [botao["text"] for botao in botoes]
    melhor_pontuacao = -float('inf')
    melhor_jogada = None

    for i in range(9):
        if tabuleiro[i] == "":
            tabuleiro[i] = jogador_pc
            pontuacao = minimax(tabuleiro, 0, False)
            tabuleiro[i] = ""
            if pontuacao > melhor_pontuacao:
                melhor_pontuacao = pontuacao
                melhor_jogada = i

    if melhor_jogada is not None:
        botoes[melhor_jogada].config(text=jogador_pc)

    resultado = verificar_vitoria()

    if resultado == True:
        jogo_ativo = False
        label_status.config(text="Computador venceu!")
        mostrar_botoes_fim()
    elif resultado == "Empate":
        jogo_ativo = False
        label_status.config(text="Empate!")
        mostrar_botoes_fim()
    else:
        label_status.config(text="Sua vez (X)")

def clique(i):
    global jogo_ativo

    if not jogo_ativo:
        return

    if botoes[i]["text"] == "":
        botoes[i].config(text=jogador_humano)
        resultado = verificar_vitoria()
        if resultado == True:
            jogo_ativo = False
            label_status.config(text="Você venceu!")
            mostrar_botoes_fim()
            return
        elif resultado == "Empate":
            jogo_ativo = False
            label_status.config(text="Empate!")
            mostrar_botoes_fim()
            return

        label_status.config(text="Vez do computador...")
        janela.update()
        jogada_pc()

def mostrar_botoes_fim():
    btn_jogar_novamente.grid(row=1, column=0, pady=10)
    btn_sair.grid(row=1, column=2, pady=10)
    for botao in botoes:
        botao.config(state=tk.DISABLED)

# Criar botões dentro do frame_tabuleiro para manter alinhamento
for i in range(9):
    botao = tk.Button(frame_tabuleiro, text="", font=("Arial", 24), width=5, height=2,
                      command=lambda i=i: clique(i))
    botao.grid(row=i//3, column=i%3)
    botoes.append(botao)

label_status = tk.Label(janela, text="Sua vez (X)", font=("Arial", 14))
label_status.grid(row=1, column=0, columnspan=3, pady=10)

btn_jogar_novamente = tk.Button(janela, text="Jogar Novamente", command=resetar_jogo)
btn_sair = tk.Button(janela, text="Sair", command=sair)
btn_jogar_novamente.grid_remove()
btn_sair.grid_remove()

janela.mainloop()