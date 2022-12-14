def menu():   
	opcao= input('''
========================================
      Agenda Pybeezy
      
      Menu:
      		                               
[1] CADASTRAR CONTATO
[2] LISTAR CONTATO 
[3] DELETAR CONTATO
[4] BUSCAR CONTATO PELO NOME
========================================
ESCOLHA UMA OPÇAO ACIMA:
''')

	if opcao =="1":
		cadastrarContato()
	elif opcao== "2":
		listarContato()
	elif opcao =="3":
		deletarContato()
	else:
		buscarContatoPeloNome() 
		
def cadastrarContato():
	idContato = input("Escolha o id do seu contato: ")
	nome = input("Escreva o nome do contato: ")
	telefone = input("Escreva o telefone do contato: ")
	email = input("Escreva o email do contato: ")
	try:
		agenda = open("agenda.txt" , "a")
		dados = f'{idContato};{nome};{telefone};{email} \n'
		agenda.write(dados) 
		agenda.close()
		print("Contato gravado com sucesso !!!")
	except:
		print("Erro na gravaçao do contato")
			
def listarContato():
	agenda = open("agenda.txt","r")
	for contato in agenda:
		print(contato)
	agenda.close()
	
def deletarContato():
		nomeDeletado = input("Digite o nome a ser deletado: ")
		agenda =open("agenda.txt","w")
		aux = []
		aux2 = []
		for i in agenda:
			aux.append(i)
		for i in range(0, len(aux)):
			if nomeDeletado not in aux[i]:
				aux2.append(aux[i])
		agenda = open("agenda.txt","w")
		for i in aux2:
			agenda.write(i)
		print("Contato deletado com sucesso")
		listarContato()
	
def buscarContatoPeloNome():
	nome=input(f'digite o nome a ser procurado: ')
	agenda = open("agenda.txt","r")
	for contato in agenda:
		if nome in contato.split(";"):
			print(contato)
	agenda.close()
	

def main():
       
       menu()
       
main()