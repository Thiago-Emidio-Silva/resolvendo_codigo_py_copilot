"""
Programa para concatenar informações pessoais do usuário.
Coleta múltiplos dados (nome, sobrenome, email, data de nascimento)
e exibe um resumo completo com formatação.
"""

from datetime import datetime


def validar_nome(nome):
	"""
	Valida se o nome contém apenas letras e espaços.
	
	Args:
		nome (str): O nome a ser validado
		
	Returns:
		bool: True se válido, False caso contrário
	"""
	# Remove espaços em branco das extremidades
	nome = nome.strip()
	
	# Verifica se o nome está vazio
	if not nome:
		return False
	
	# Verifica se contém apenas letras e espaços
	return all(char.isalpha() or char.isspace() for char in nome)


def validar_email(email):
	"""
	Valida o formato básico de um email.
	
	Args:
		email (str): O email a ser validado
		
	Returns:
		bool: True se possui formato válido, False caso contrário
	"""
	# Remove espaços em branco das extremidades
	email = email.strip()
	
	# Verifica se está vazio
	if not email:
		return False
	
	# Verifica se contém exatamente um '@' e um '.'
	return '@' in email and '.' in email.split('@')[-1]


def validar_data(data_str):
	"""
	Valida se a data está em formato correto (DD/MM/YYYY).
	
	Args:
		data_str (str): String com a data a ser validada
		
	Returns:
		bool: True se válida, False caso contrário
	"""
	try:
		# Tenta fazer o parse da data no formato DD/MM/YYYY
		datetime.strptime(data_str.strip(), "%d/%m/%Y")
		return True
	except ValueError:
		# Se não conseguir fazer o parse, a data é inválida
		return False


def obter_nome():
	"""
	Solicita o nome do usuário com validação.
	
	Returns:
		str: Nome validado e limpo
	"""
	while True:
		nome = input("\nDigite o nome: ").strip()
		
		# Verifica se o nome é válido
		if validar_nome(nome):
			return nome
		else:
			print("❌ Erro: Nome inválido! Use apenas letras e espaços.")


def obter_sobrenome():
	"""
	Solicita o sobrenome do usuário com validação.
	
	Returns:
		str: Sobrenome validado e limpo
	"""
	while True:
		sobrenome = input("Digite o sobrenome: ").strip()
		
		# Verifica se o sobrenome é válido
		if validar_nome(sobrenome):
			return sobrenome
		else:
			print("❌ Erro: Sobrenome inválido! Use apenas letras e espaços.")


def obter_email():
	"""
	Solicita o email do usuário com validação (campo opcional).
	
	Returns:
		str: Email validado ou string vazia se deixar em branco
	"""
	while True:
		email = input("Digite o email (opcional, pressione Enter para pular): ").strip()
		
		# Se deixar em branco, retorna string vazia (campo opcional)
		if not email:
			return ""
		
		# Valida o email se foi fornecido
		if validar_email(email):
			return email
		else:
			print("❌ Erro: Email inválido! Formato esperado: exemplo@dominio.com")


def obter_data_nascimento():
	"""
	Solicita a data de nascimento do usuário com validação (campo opcional).
	
	Returns:
		str: Data validada ou string vazia se deixar em branco
	"""
	while True:
		data = input("Digite a data de nascimento em DD/MM/YYYY (opcional, pressione Enter para pular): ").strip()
		
		# Se deixar em branco, retorna string vazia (campo opcional)
		if not data:
			return ""
		
		# Valida a data se foi fornecida
		if validar_data(data):
			return data
		else:
			print("❌ Erro: Data inválida! Use o formato DD/MM/YYYY")


def exibir_resumo(nome, sobrenome, email, data_nascimento):
	"""
	Exibe um resumo formatado com todas as informações fornecidas.
	
	Args:
		nome (str): Nome do usuário
		sobrenome (str): Sobrenome do usuário
		email (str): Email do usuário (pode estar vazio)
		data_nascimento (str): Data de nascimento (pode estar vazia)
	"""
	# Linha divisória para melhor visualização
	print("\n" + "="*50)
	print("RESUMO DAS INFORMAÇÕES")
	print("="*50)
	
	# Exibe nome completo
	nome_completo = f"{nome} {sobrenome}".strip()
	print(f"✓ Nome completo: {nome_completo}")
	
	# Exibe email se foi fornecido
	if email:
		print(f"✓ Email: {email}")
	else:
		print("✓ Email: Não fornecido")
	
	# Exibe data de nascimento se foi fornecida
	if data_nascimento:
		print(f"✓ Data de nascimento: {data_nascimento}")
	else:
		print("✓ Data de nascimento: Não fornecida")
	
	# Linha divisória final
	print("="*50 + "\n")


def main():
	"""
	Função principal que coordena a coleta de dados e exibição do resumo.
	"""
	try:
		# Exibe mensagem de boas-vindas
		print("\n" + "="*50)
		print("BEM-VINDO AO CONCATENADOR DE DADOS PESSOAIS")
		print("="*50)
		
		# Coleta informações obrigatórias
		nome = obter_nome()
		sobrenome = obter_sobrenome()
		
		# Coleta informações opcionais
		email = obter_email()
		data_nascimento = obter_data_nascimento()
		
		# Exibe o resumo com todas as informações
		exibir_resumo(nome, sobrenome, email, data_nascimento)
		
	except EOFError:
		# Trata o caso de entrada finalizada inesperadamente (uso em pipes)
		print("\n❌ Entrada finalizada inesperadamente.")
	except KeyboardInterrupt:
		# Trata o caso do usuário pressionar Ctrl+C
		print("\n❌ Operação cancelada pelo usuário.")
	except Exception as erro:
		# Trata qualquer outra exceção inesperada
		print(f"❌ Erro inesperado: {erro}")


if __name__ == "__main__":
	main()
