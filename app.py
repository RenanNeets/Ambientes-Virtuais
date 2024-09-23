""""""
# O que são Ambientes Virtuais


# Ambientes virtuais em Python (venv)
# Um ambiente virtual carrega toda a sua instalação
# do Python para uma pasta no caminho escolhido.
# Ao ativar um ambiente virtual, a instalação do
# ambiente virtual será usada.
# venv é o módulo que vamos usar para
# criar ambientes virtuais.
# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env

#Cria o ambiente virtual
#"python -m venv ambiente"

#Ativando e desativando o meu ambiente virtual
#Windowns
#".\ambiente\Scripts\activate" -> Um caminho até o programa "activate" da sua pasta 'venv'/'ambiente'
#"deactivate" -> Desativa o Amb. Virt.
#Ios ou Linux
#". ambiente\bin\activate"
#Ou "source venv\bin\activate"


#pip - instalando pacotes e bibliotecas
#Instalar usa o comando
#   "pip install 'O que quer instalar'"
#   Ou "python -m pip install 'Coisa'"
#   Ex:"pip install autopep8"
#Atualizar o pip
#   "python.exe -m pip install --upgrade pip"
#Desinstalar 
#   "pip uninstall 'Coisa'"
#Mostar os pacotes instalados
#   "pip freeze"


#Criando e usando um requirements.txt
#Criando:
#   "pip freeze > requirements.txt"
#   Se já tiver uma, ele atualiza