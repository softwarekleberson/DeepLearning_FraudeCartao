import pandas as pd

dados = pd.read_csv('C:\\Users\\User\\OneDrive\\Área de Trabalho\\Artigo\\aplicacao\\creditcard.csv')

#Treinamento do modelo, balanceando os dados que são desbalanceados
#garantindo a divisão correta dos dados
from sklearn.model_selection import StratifiedShuffleSplit
def executar_validador(x,y):
    validador = StratifiedShuffleSplit(n_splits=1, test_size=0.1, random_state=0)
    for treino_id, teste_id in validador.split(x,y):
        x_train, x_test = x[treino_id], x[teste_id]
        y_train, y_test = y[treino_id], y[teste_id]
    return x_train, x_test, y_train, y_test


#Em resumo, essa função treina um modelo de classificação (como uma árvore de decisão) nos dados de treinamento e usa esse modelo treinado para fazer variações nos dados de teste
from sklearn import tree
def executar_classificador(classificador, x_train,  x_test, y_train,):
    arvore = classificador.fit(x_train, y_train)
    y_pred = arvore.predict(x_test)
    return y_pred


#Cria a arvore na forma de imagem
import matplotlib.pyplot as plt
def salvar_arvore(classificador, nome):
    plt.figure(figsize=(200, 100))
    tree.plot_tree(classificador, filled=True, fontsize=14)
    plt.savefig(nome)
    plt.close()


from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
def validar_arvore(y_test, y_pred):
    print('Acuracia do modelo ', accuracy_score(y_test, y_pred))
    print('Matriz de confucao ', confusion_matrix(y_test, y_pred))
    print('Precisao ', precision_score(y_test, y_pred))
    print('Recall ', recall_score(y_test, y_pred))

#execução do validador
x = dados.drop('Class', axis=1).values
y = dados['Class'].values
x_train, x_test, y_train, y_test = executar_validador(x,y)

#execução do classificador DecisionTreeClassifier
classificador_arvore_decisao = tree.DecisionTreeClassifier(max_depth=10, random_state=0)
y_pred_arvore_decisao = executar_classificador(classificador_arvore_decisao, x_train, x_test, y_train)

#criação da figura da arvore de decisão
salvar_arvore(classificador_arvore_decisao, "arvore_decisao.png")

#AdaBoot
from sklearn.ensemble import AdaBoostClassifier

classificador_adaboost = AdaBoostClassifier(random_state=0, n_estimators=200)
y_pred_adaboost = executar_classificador(classificador_adaboost, x_train, x_test, y_train)

salvar_arvore(classificador_adaboost.estimators_[0], "adaboost1")
salvar_arvore(classificador_adaboost.estimators_[1], "adaboost2")
validar_arvore(y_test, y_pred_adaboost)





