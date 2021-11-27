# PyMC4 - Apresentação Oral sobre a PPL

### Instalação da PPL:
##### Pré-Requesitos:

* **Uma pré-instalação de um VM Software** (Virtual Machine) linux-Ubuntu preferencialmente;
* **Uma ligação à internet**;
* **Jupyter Notebook** (recomendado).


### Uma vez cumpridos os pré-requesitos poderá ser feita a instalação:
Abrir o terminal (ctrl+alt+T, no Gnome Linux, ou procurando no menu).

Atualizar o package manager do (Linux):

	sudo apt update && sudo apt upgrade

Instalar o python e suas dependências:	

	sudo apt install build-essential

Instalar o pip para podermos baixar as bibliotecas de python:

	sudo apt install python3-pip
	
Instalar o Git pois a biblioteca que vamos uar é um repositóriio do GitHub:

	sudo apt install git 

Voltar a verificar se temos todos os packages atualizados:

	sudo apt update && sudo apt upgrade

Para instalar a biblioteca usamos o seguinte comando:
	
	pip install git+https://github.com/pymc-devs/pymc4@1c5e23825271fc2ff0c701b9224573212f56a534

Agora temos tudo pronto para começar a usar a biblioteca.
