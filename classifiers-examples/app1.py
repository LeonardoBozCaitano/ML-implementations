from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

# features (1 sim, 0 não)
# pelo longo? 
# perna curta?
# faz auau?
porco1 = [0, 1, 0]
porco2 = [0, 1, 1]
porco3 = [1, 1, 0]

cachorro1 = [0, 1, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [1, 1, 1]

# 1 => porco, 0 => cachorro
treino_x = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
treino_y = [1,1,1,0,0,0]

model = LinearSVC()
model.fit(treino_x, treino_y)

animal1 = [1,1,1]
animal2 = [1,1,0]
animal3 = [0,1,1]

teste_x = [animal1, animal2, animal3]
texte_y = [0, 1, 1]

predict = model.predict(teste_x)

taxa_acerto = accuracy_score(texte_y, predict)

print("Taxa de acerto: %.2f" %  (taxa_acerto * 100))