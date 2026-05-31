"""
Sistema de Calculadora com Operações Matemáticas Básicas e Porcentagem.
Realiza: adição, subtração, multiplicação, divisão e cálculos de porcentagem.
"""


def obter_numero(prompt="Digite um número: "):
	"""
	Solicita um número ao usuário com validação.
	Aceita números inteiros e decimais.
	
	Args:
		prompt (str): Mensagem a exibir ao usuário
		
	Returns:
		float: Número validado fornecido pelo usuário
	"""
	while True:
		try:
			# Tenta converter a entrada para float
			numero = float(input(prompt).strip())
			return numero
		except ValueError:
			# Se não conseguir converter, pede novamente
			print("❌ Erro: Digite um número válido (ex: 10 ou 10.5)")


def exibir_menu():
	"""
	Exibe o menu de operações disponíveis.
	
	Returns:
		str: A opção selecionada pelo usuário
	"""
	print("\n" + "="*50)
	print("CALCULADORA - ESCOLHA UMA OPERAÇÃO")
	print("="*50)
	print("1. ➕ Adição")
	print("2. ➖ Subtração")
	print("3. ✖️  Multiplicação")
	print("4. ➗ Divisão")
	print("5. 📊 Porcentagem")
	print("6. ❌ Sair")
	print("="*50)
	
	# Solicita a escolha do usuário
	opcao = input("\nDigite a opção (1-6): ").strip()
	return opcao


def adicionar(numero1, numero2):
	"""
	Realiza a adição de dois números.
	
	Args:
		numero1 (float): Primeiro número
		numero2 (float): Segundo número
		
	Returns:
		float: Resultado da adição
	"""
	# Realiza a soma dos dois números
	resultado = numero1 + numero2
	
	# Exibe a operação e o resultado
	print(f"\n{numero1} + {numero2} = {resultado}")
	
	return resultado


def subtrair(numero1, numero2):
	"""
	Realiza a subtração de dois números.
	
	Args:
		numero1 (float): Primeiro número (minuendo)
		numero2 (float): Segundo número (subtraendo)
		
	Returns:
		float: Resultado da subtração
	"""
	# Realiza a subtração
	resultado = numero1 - numero2
	
	# Exibe a operação e o resultado
	print(f"\n{numero1} - {numero2} = {resultado}")
	
	return resultado


def multiplicar(numero1, numero2):
	"""
	Realiza a multiplicação de dois números.
	
	Args:
		numero1 (float): Primeiro número
		numero2 (float): Segundo número
		
	Returns:
		float: Resultado da multiplicação
	"""
	# Realiza a multiplicação
	resultado = numero1 * numero2
	
	# Exibe a operação e o resultado
	print(f"\n{numero1} × {numero2} = {resultado}")
	
	return resultado


def dividir(numero1, numero2):
	"""
	Realiza a divisão de dois números com validação.
	Previne divisão por zero.
	
	Args:
		numero1 (float): Dividendo
		numero2 (float): Divisor
		
	Returns:
		float: Resultado da divisão ou None se houver erro
	"""
	# Valida se o divisor é zero
	if numero2 == 0:
		print("\n❌ Erro: Não é possível dividir por zero!")
		return None
	
	# Realiza a divisão
	resultado = numero1 / numero2
	
	# Exibe a operação e o resultado com até 2 casas decimais
	print(f"\n{numero1} ÷ {numero2} = {resultado:.2f}")
	
	return resultado


def calcular_porcentagem():
	"""
	Calcula porcentagem de um valor.
	Oferece duas formas: "X% de Y" ou "Quanto % é X de Y"
	
	Returns:
		float: Resultado do cálculo de porcentagem ou None se houver erro
	"""
	print("\n" + "-"*50)
	print("CÁLCULO DE PORCENTAGEM")
	print("-"*50)
	print("1. Calcular X% de um valor (ex: 20% de 100)")
	print("2. Calcular qual % um valor representa (ex: Qual % é 20 de 100)")
	print("-"*50)
	
	# Solicita qual tipo de cálculo fazer
	tipo = input("Escolha (1 ou 2): ").strip()
	
	if tipo == "1":
		# Tipo 1: Calcular X% de Y
		porcentagem = obter_numero("Digite a porcentagem (ex: 20): ")
		valor = obter_numero("Digite o valor total: ")
		
		# Calcula a porcentagem
		resultado = (porcentagem / 100) * valor
		
		# Exibe o resultado
		print(f"\n{porcentagem}% de {valor} = {resultado:.2f}")
		
		return resultado
		
	elif tipo == "2":
		# Tipo 2: Qual % é X de Y
		parte = obter_numero("Digite o valor da parte: ")
		total = obter_numero("Digite o valor total: ")
		
		# Valida divisão por zero
		if total == 0:
			print("\n❌ Erro: O valor total não pode ser zero!")
			return None
		
		# Calcula a porcentagem
		resultado = (parte / total) * 100
		
		# Exibe o resultado
		print(f"\n{parte} é {resultado:.2f}% de {total}")
		
		return resultado
	else:
		# Opção inválida
		print("❌ Erro: Digite 1 ou 2!")
		return None


def processar_operacao(opcao):
	"""
	Processa a operação escolhida pelo usuário.
	
	Args:
		opcao (str): Opção selecionada no menu
		
	Returns:
		bool: False para sair do programa, True para continuar
	"""
	# Verifica qual operação foi selecionada
	if opcao == "1":
		# Adição
		numero1 = obter_numero("Digite o primeiro número: ")
		numero2 = obter_numero("Digite o segundo número: ")
		adicionar(numero1, numero2)
		
	elif opcao == "2":
		# Subtração
		numero1 = obter_numero("Digite o primeiro número: ")
		numero2 = obter_numero("Digite o segundo número: ")
		subtrair(numero1, numero2)
		
	elif opcao == "3":
		# Multiplicação
		numero1 = obter_numero("Digite o primeiro número: ")
		numero2 = obter_numero("Digite o segundo número: ")
		multiplicar(numero1, numero2)
		
	elif opcao == "4":
		# Divisão
		numero1 = obter_numero("Digite o dividendo: ")
		numero2 = obter_numero("Digite o divisor: ")
		dividir(numero1, numero2)
		
	elif opcao == "5":
		# Porcentagem
		calcular_porcentagem()
		
	elif opcao == "6":
		# Sair do programa
		print("\n" + "="*50)
		print("Obrigado por usar a calculadora! 👋")
		print("="*50 + "\n")
		return False
	else:
		# Opção inválida
		print("\n❌ Erro: Digite uma opção de 1 a 6!")
	
	# Retorna True para continuar o loop
	return True


def main():
	"""
	Função principal que executa o loop da calculadora.
	"""
	try:
		# Exibe mensagem de boas-vindas
		print("\n" + "="*50)
		print("BEM-VINDO À CALCULADORA")
		print("="*50)
		
		# Loop principal
		continuar = True
		while continuar:
			# Exibe menu e obtém opção
			opcao = exibir_menu()
			
			# Processa a operação
			continuar = processar_operacao(opcao)
			
	except EOFError:
		# Trata entrada finalizada inesperadamente
		print("\n❌ Entrada finalizada inesperadamente.")
	except KeyboardInterrupt:
		# Trata Ctrl+C do usuário
		print("\n❌ Operação cancelada pelo usuário.")
	except Exception as erro:
		# Trata qualquer outra exceção inesperada
		print(f"❌ Erro inesperado: {erro}")


if __name__ == "__main__":
	main()
