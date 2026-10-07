import requests

def consultar_cep():
    print("-" * 30)
    print("    CONSULTA DE CEP (ViaCEP)    ")
    print("-" * 30)
    
   
    cep = input("Digita o CEP (apenas números): ").strip()
    
    
    if len(cep) != 8 or not cep.isdigit():
        print("Erro: O CEP deve conter exatamente 8 números.")
        return

    
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
       
        resposta = requests.get(url)
        
       
        if resposta.status_code == 200:
            dados = resposta.json()
            
            
            if "erro" in dados:
                print("Erro: O CEP introduzido não foi encontrado.")
            else:
                print("\n--- Resultados da Consulta ---")
                print(f"CEP:         {dados.get('cep')}")
                print(f"Logradouro:  {dados.get('logradouro')}")
                print(f"Complemento: {dados.get('complemento', 'N/A')}")
                print(f"Bairro:      {dados.get('bairro')}")
                print(f"Localidade:  {dados.get('localidade')} - {dados.get('uf')}")
                print(f"DDD:         {dados.get('ddd')}")
                print("-" * 30)
        else:
            print(f"Erro na comunicação com a API. Código de estado: {resposta.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro de ligação: {e}")

if __name__ == "__main__":
    while True:
        consultar_cep()
        continuar = input("\nQueres consultar outro CEP? (S/N): ").strip().upper()
        if continuar != 'S':
            print("A encerrar a aplicação...")
            break