import psutil

def listar_processos_listening():
    """
    Lista os processos que estão em estado de 'listening' para conexões de rede.
    Retorna uma lista com informações sobre o processo e o número da porta.
    """
    processos_listening = []

    # Iterando sobre todas as conexões de rede
    for conn in psutil.net_connections(kind='inet'):
        if conn.status == 'LISTEN':
            pid = conn.pid
            processo = psutil.Process(pid)
            nome_processo = processo.name()
            port = conn.laddr.port

            processos_listening.append({
                "nome_processo": nome_processo,
                "pid": pid,
                "porta": port,
                "endereco_local": conn.laddr.ip
            })

    return processos_listening

def exibir_processos_listening():
    """
    Exibe os processos em estado de 'listening' com informações detalhadas.
    """
    processos = listar_processos_listening()

    if not processos:
        print("Nenhum processo em listening encontrado.")
    else:
        print(f"{'Nome do Processo':<30} {'PID':<10} {'Porta':<10} {'Endereço Local'}")
        print("="*60)
        for processo in processos:
            print(f"{processo['nome_processo']:<30} {processo['pid']:<10} {processo['porta']:<10} {processo['endereco_local']}")

if __name__ == '__main__':
    exibir_processos_listening()
