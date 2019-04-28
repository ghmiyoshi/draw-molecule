"""
Teste de Seleção: Serviço Flask para Desenho Molecular

Sistema: SMILES (Simplified molecular-input line-entry system)

Desenvolvedor: Gabriel Hideki Miyoshi   Data: 28/04/2019

"""

# imports
import base64
from io import BytesIO

from rdkit import Chem
from rdkit.Chem import Draw

from flask import Flask

# instância flask
app = Flask(__name__)

# defini rota
@app.route('/drawMolecule/<SMILES>')

# função drawMolecule
def drawMolecule(SMILES):

    # buffer
    buffer = BytesIO()

    # desenha imagem
    desenho = Draw.MolToImage(Chem.MolFromSmiles(SMILES))
    desenho.save(buffer, format='JPEG')

    # converte imagem
    imagem_base64 = base64.b64encode(buffer.getvalue())

    return '<img src=\'data:image/jpeg;base64, ' + str(imagem_base64)[2:-1] + '\'>'
