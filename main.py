# import matplotlib.pyplot as plt 
# fig, ax = plt.subplots()
# ax.plot([1, 2, 3, 4], [1, 4, 2, 5])
# plt.ylabel('some numbers')
# plt.savefig('plot.png') # сохранение рафика в файл 

# from sklearn.datasets import make_blobs
# import pandas as pd
# # dataset, classes = make_blobs(n_samples=200, n_features=2, centers=4, cluster_std=0.5, randome_state=0)
# df = pd.DataFrame(dataset, columns=['var1', 'var2'])
# print(df.head(2))

import sklearn
print(sklearn.__version__) # проверка версии библиотеки 
 
# №3: Генерация данных и создание DataFrame
from sklearn.datasets import make_blobs #генерация данных 
import pandas as pd # работа с данными 

dataset, classes = make_blobs(n_samples=200, n_features=2, centers=4, cluster_std=0.5, random_state=0)
df = pd.DataFrame(dataset, columns=['var1', 'var2'])
print(df.head(2)) # вывод первых двух строк 

# №3: Elbow метод для определения оптимального числа кластеров
from yellowbrick.cluster import KElbowVisualizer # визуализация 
from sklearn.cluster import KMeans # алгоритм кластеризации 
import matplotlib.pyplot as plt 

plt.rcParams["font.family"] = "sans-serif" # шрифт 
plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]

X, y = make_blobs(n_samples=300, centers=4, n_features=2, random_state=42) # генерация данных 
df = pd.DataFrame(X, columns=['var1', 'var2']) # создание DataFrame

model = KMeans(random_state=42) 
visualizer = KElbowVisualizer(model, k=(1,12)) # визуализация 
visualizer.fit(df) # обучение модели 

plt.savefig("elbow_method.png", dpi=150, bbox_inches="tight")
plt.close()

# №4: Обучение модели KMeans с 4 кластерами
kmeans = KMeans(n_clusters=4, init='k-means++', random_state=0).fit(df) # обучение модели 
print(kmeans.labels_) # метки кластеров 
print(kmeans.cluster_centers_) # координаты центроидов 
print(kmeans.inertia_) # сумма квадратов расстояний от каждой точки до ближайшего центроида 
print(kmeans.n_iter_) # количество итераций 

# №5: Подсчет объектов в кластерах
from collections import Counter 
labels = kmeans.labels_.tolist() # преобразование меток кластеров в список 
print(Counter(labels)) # подсчет кол-ва объектов в каждом кластере 

# №6-7: Визуализация результатов кластеризации
import seaborn as sns # визуализация данных 
sns.scatterplot(data=df, x="var1", y="var2", hue=kmeans.labels_) 
plt.scatter(kmeans.cluster_centers_[:,0],
            kmeans.cluster_centers_[:,1], marker="X", c="r", s=80, label="centroids") # центроиды 
plt.legend()
plt.savefig("clust.png") # сохранение графика 