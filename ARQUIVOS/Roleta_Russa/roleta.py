import tkinter as tk
from tkinter import simpledialog
import random
import time

# Arte de Texto da arma
arte_arma = """
                                                  
                                                  
                                                  
                                                  
                                                  
  ..                                              
####################################  ##          
##########################        ######          
##########################mmmmmm######            
                  ########################        
                      ######--mm########  ####    
                      ####    ##  ####  ########  
                      ####  ####  ##..##########++
                        ####    ####  ############
                          ########    ############
                                        ##########
                                        ##########
                                        ##########
                                        ##########
                                        ##########
                                          ######  
                                                  
                                                  
                                                  
                                                  
"""

# Arte de Texto do disparo
arte_disparo = """
                    @@@@@@@@@@@@@@@@@@@                   `
                 @@@@@@             @@@@@@@                
              @@@@                       @@@@              
             @@@                             @@            
            @@                                @@           
           @@                     `           @@          `
          @@                                   @@          
          @@ @@                             @@ @@          
          @@ @@                             @@  @          
          @@ @@                             @@  @          
          @@  @@                            @@ @@          
          @@  @@                           @@  @@          
           @@ @@   @@@@@@@@     @@@@@@@@   @@ @@           
            @@@@ @@@@@@@@@@     @@@@@@@@@@ @@@@@           
             @@@ @@@@@@@@@@     @@@@@@@@@@ @@@             
    @@@       @@  @@@@@@@@       @@@@@@@@@  @@      @@@@   
   @@@@@     @@   @@@@@@@   @@@   @@@@@@@   @@     @@@@@@  
  @@   @@    @@     @@@    @@@@@    @@@     @@    @@   @@  
 @@@    @@@@  @@          @@@@@@@          @@  @@@@    @@@ 
@@         @@@@@@@@       @@@@@@@       @@@@@@@@@        @@
@@@@@@@@@     @@@@@@@@    @@@@@@@    @@@@@@@@      @@@@@@@@
  @@@@ @@@@@      @@@@@              @@@ @@     @@@@@@ @@@ 
          @@@@@@  @@@  @@           @@  @@@  @@@@@@        
              @@@@@@ @@ @@@@@@@@@@@ @@ @@@@@@              
                  @@ @@ @ @ @ @ @ @ @ @ @@                 
                @@@@  @ @ @ @ @ @ @ @   @@@@@              
            @@@@@ @@   @@@@@@@@@@@@@   @@ @@@@@            
    @@@@@@@@@@     @@                 @@      @@@@@@@@@    
   @@           @@@@@@@             @@@@@@@@          @@   
    @@@     @@@@@     @@@@@@@@@@@@@@@     @@@@@     @@@    
      @@   @@@           @@@@@@@@@           @@@   @@      
      @@  @@                                   @@  @@      
       @@@@                                     @@@@       
"""

def roleta_russa(jogadores):
    # Número de câmaras e uma bala
    chambers = 6
    balas = 1

    # Função para embaralhar o tambor (colocar a bala aleatoriamente)
    def embaralhar_tambor():
        tambor = [1] * balas + [0] * (chambers - balas)
        random.shuffle(tambor)
        return tambor

    rodada = 1
    while len(jogadores) > 0:
        for i in range(len(jogadores)):
            jogador = jogadores[i]
            print(f"Rodada {rodada} - É a vez de {jogador}")
            time.sleep(1)

            # Embaralha o tambor antes de cada disparo
            tambor = embaralhar_tambor()

            # Pergunta ao jogador se ele quer disparar ou desistir
            escolha = simpledialog.askstring("Escolha", f"{jogador}, você deseja disparar ou desistir? (digite 'disparar' ou 'desistir')")
            
            if escolha and escolha.lower() == "desistir":
                print(f"{jogador} desistiu e foi removido do jogo.")
                jogadores.pop(i)  # Remove o jogador da lista
                break  # Sai da rodada atual
            elif escolha and escolha.lower() == "disparar":
                # Simula o disparo da roleta
                print("O tambor está girando...")
                time.sleep(2)
                
                # A bala está no tambor?
                if tambor.pop() == 1:
                    print(f"💥 {jogador} MORREU! A bala estava no tambor!")
                    
                    # Exibe a arte de disparo
                    print(arte_disparo)

                    # Pergunta se os jogadores desejam continuar ou não
                    continuar = simpledialog.askstring("Fim de Jogo", "O jogo terminou! Deseja continuar jogando? (digite 'sim' ou 'não')").lower()
                    if continuar == "sim":
                        print("O jogo continuará com os jogadores restantes.")
                        # Recarrega o tambor (aleatório) para a próxima rodada
                    else:
                        print("O jogo terminou!")
                        return  # Finaliza o jogo

                    jogadores.pop(i)  # Remove o jogador da lista
                    break  # Sai da rodada atual
                else:
                    print(f"🔥 {jogador} sobreviveu! Vai para a próxima rodada!")

            rodada += 1

    print("Fim de Jogo!")

def iniciar_jogo():
    # Função que gerencia o que acontece ao selecionar a opção do jogo
    if jogo_var.get() == 1:  # Jogo Solo
        nome = simpledialog.askstring("Nome", "Qual o seu nome, jogador?")
        print(f"Você escolheu jogar sozinho, {nome}. O jogo vai começar!")
        roleta_russa([nome])  # Inicia o jogo solo

    elif jogo_var.get() == 2:  # Jogo com Amigos
        num_jogadores = int(simpledialog.askstring("Número de jogadores", "Quantos jogadores estão jogando (1 a 6)?"))
        if 1 <= num_jogadores <= 6:
            nomes_jogadores = []
            for i in range(1, num_jogadores + 1):
                nome = simpledialog.askstring("Nome do Jogador", f"Nome do Player {i}:")
                nomes_jogadores.append(nome)
            print(f"Os jogadores são: {', '.join(nomes_jogadores)}. O jogo vai começar!")
            roleta_russa(nomes_jogadores)  # Inicia o jogo com os amigos
        else:
            print("Número de jogadores inválido. O jogo será encerrado.")
    else:
        print("Por favor, selecione uma opção válida.")

# Criando a janela principal
root = tk.Tk()
root.title("Menu do Jogo")

# Exibindo a arte de texto (arma e bala)
arma_imagem = tk.Label(root, text=arte_arma, font=("Courier", 8), padx=10, pady=10)
arma_imagem.grid(row=0, column=0, padx=10, pady=10)

# Caixa de seleção para o tipo de jogo
jogo_var = tk.IntVar()
tk.Radiobutton(root, text="Jogo Solo", variable=jogo_var, value=1).grid(row=1, column=0, padx=10, pady=10)
tk.Radiobutton(root, text="Jogo com Amigos", variable=jogo_var, value=2).grid(row=2, column=0, padx=10, pady=10)

# Botão para iniciar o jogo
botao_iniciar = tk.Button(root, text="Iniciar Jogo", command=iniciar_jogo)
botao_iniciar.grid(row=3, column=0, padx=10, pady=20)

# Rodar a interface gráfica
root.mainloop()
