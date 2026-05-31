"""
Programa para obter um texto do usuário e repetir sua exibição
um número específico de vezes.
"""


def obter_texto():
	"""
	Solicita um texto/mensagem do usuário.
	
	Returns:
		str: O texto fornecido pelo usuário (sem espaços nas extremidades)
	"""
	# Solicita o texto ao usuário
	texto = input("Digite o texto que deseja repetir: ").strip()
	
	# Verifica se o texto está vazio
	if not texto:
		print("❌ Erro: Texto não pode estar vazio!")
		return obter_texto()  # Chama recursivamente até obter um texto válido
	
	return texto


def obter_numero_repeticoes():
	"""
	Solicita o número de vezes que o texto deve ser repetido.
	Garante que o valor seja um inteiro positivo.
	
	Returns:
		int: Número de repetições (sempre maior que 0)
	"""
	while True:
		try:
			# Solicita o número de repetições
			numero = input("Quantas vezes você quer repetir? ").strip()
			
			# Converte para inteiro
			numero = int(numero)
			
			# Valida se é um número positivo
			if numero <= 0:
				print("❌ Erro: Digite um número maior que 0!")
				continue
			
			return numero
			
		except ValueError:
			# Trata o caso onde o usuário digita algo que não é um número
			print("❌ Erro: Digite um número inteiro válido!")


def repetir_texto(texto, vezes):
	"""
	Repete o texto um número especificado de vezes.
	Exibe cada repetição em uma nova linha com numeração.
	
	Args:
		texto (str): O texto a ser repetido
		vezes (int): Quantidade de vezes a repetir
	"""
	print("\n" + "="*50)
	print("RESULTADO DAS REPETIÇÕES")
	print("="*50 + "\n")
	
	# Loop que repete o texto a quantidade de vezes solicitada
	for i in range(1, vezes + 1):
		# Exibe a repetição com número de sequência
		print(f"{i}. {texto}")
	
	print("\n" + "="*50 + "\n")


def main():
	"""
	Função principal que coordena o fluxo do programa.
	"""
	try:
		# Exibe mensagem de boas-vindas
		print("\n" + "="*50)
		print("REPETIDOR DE TEXTO")
		print("="*50 + "\n")
		
		# Obtém o texto do usuário
		texto = obter_texto()
		
		# Obtém quantas vezes repetir
		numero_repeticoes = obter_numero_repeticoes()
		
		# Repete e exibe o texto
		repetir_texto(texto, numero_repeticoes)
		
	except EOFError:
		# Trata entrada finalizada inesperadamente (uso em pipes)
		print("\n❌ Entrada finalizada inesperadamente.")
	except KeyboardInterrupt:
		# Trata Ctrl+C do usuário
		print("\n❌ Operação cancelada pelo usuário.")
	except Exception as erro:
		# Trata qualquer outra exceção inesperada
		print(f"❌ Erro inesperado: {erro}")


if __name__ == "__main__":
	main()
