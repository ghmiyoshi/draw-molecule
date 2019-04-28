## SMILES
Foi desenvolvido um sistema SMILES para representar moléculas.

## Resumo
Existem inúmeras maneiras de se representar moléculas. Uma destas formas consiste em empregar uma série de regras para escrever, literalmente, a fórmula molecular por extenso,
preservando, inclusive as ligações e ordem entre os átomos. Este sistema é chamado de Simplified molecular-input line-entry system (SMILES).

## Tecnologias e ferramentas
   * Python 3.6;
   * IDE PyCharm;
   * Anaconda;
   * rdkit;
   * Flask;

## Preparar o ambiente
#### Instalar o Anaconda
Fazer o download no site [https://www.anaconda.com/distribution/](https://www.anaconda.com/distribution/) 
   
Executar o seguinte comando para instalar:

 `bash ~/Downloads/Anaconda3-2019.03-Linux-x86_64.sh`
 
 
 #### Instalar o rdkit
 Executar o seguinte comando para instalar:
 
 `conda install -c rdkit rdkit`
 
 #### Instalar o flask
 Executar o seguinte comando para instalar:
 
 `conda install -c anaconda flask`
 
 ## Executar o sistema
 No diretório do projeto executar os seguintes comandos:
 
 `export FLASK_APP=draw_molecule.py`
 
 `flask run`
 
 Acessar o endereço: 
 [http://localhost:5000/drawMolecule/`<SMILES>`](http://localhost:5000/drawMolecule/<SMILES>), sendo `SMILES` a fórmula molecular. 
 
 Segue alguns exemplos:
 * CN1C=NC2=C1C(=O)N(C(=O)N2C)C
 * O=C(C)Oc1ccccc1C(=O)O
 * CC(=O)Nc1ccc(O)cc1
 
 
 
