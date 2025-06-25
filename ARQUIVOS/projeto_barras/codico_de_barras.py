import requests

API_KEY = "ooloc7qtyfykd7agtpi6qthjambfab"

def buscar_produto_por_barcode(barcode):
    url = f"https://api.barcodelookup.com/v3/products?barcode={barcode}&key={API_KEY}"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        if 'products' not in dados or not dados['products']:
            print("Produto não encontrado.")
            return

        produto = dados['products'][0]
        print("\n=== Detalhes do Produto ===")
        print(f"Nome: {produto.get('product_name', 'N/A')}")
        print(f"Marca: {produto.get('brand', 'N/A')}")
        print(f"Categoria: {produto.get('category', 'N/A')}")
        print(f"Fabricante: {produto.get('manufacturer', 'N/A')}")
        print(f"Descrição: {produto.get('description', 'N/A')}")
        print(f"Imagem: {produto.get('images', ['N/A'])[0]}")

    except requests.exceptions.HTTPError as err:
        print("Erro na requisição HTTP:", err)
    except Exception as e:
        print("Erro inesperado:", e)

if __name__ == "__main__":
    codigo_barra = input("Digite o código de barras do produto: ").replace(" ", "")
    buscar_produto_por_barcode(codigo_barra)
