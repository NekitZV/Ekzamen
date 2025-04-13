#kmeans

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import numpy as np
from pandas.plotting import parallel_coordinates
import plotly.express as px
import plotly.graph_objects as go
from io import StringIO

# Вводим данные как строку (как будто считали файл)
data_str = """
ID	Пол	Возраст	Годовой доход (k$)	Оценка по внутренним рейтингам
1	М	19	15	39
2	М	21	15	81
3	Ж	20	16	6
4	Ж	23	16	77
5	Ж	31	17	40
6	Ж	22	17	76
7	Ж	35	18	6
8	Ж	23	18	94
9	М	64	19	3
10	Ж	30	19	72
11	М	67	19	14
12	Ж	35	19	99
13	Ж	58	20	15
14	Ж	24	20	77
15	М	37	20	13
16	М	22	20	79
17	Ж	35	21	35
18	М	20	21	66
19	М	52	23	29
20	Ж	35	23	98
21	М	35	24	35
22	М	25	24	73
23	Ж	46	25	5
24	М	31	25	73
25	Ж	54	28	14
26	М	29	28	82
27	Ж	45	28	32
28	М	35	28	61
29	Ж	40	29	31
30	Ж	23	29	87
31	М	60	30	4
32	Ж	21	30	73
33	М	53	33	4
34	М	18	33	92
35	Ж	49	33	14
36	Ж	21	33	81
37	Ж	42	34	17
38	Ж	30	34	73
39	Ж	36	37	26
40	Ж	20	37	75
41	Ж	65	38	35
42	М	24	38	92
43	М	48	39	36
44	Ж	31	39	61
45	Ж	49	39	28
46	Ж	24	39	65
47	Ж	50	40	55
48	Ж	27	40	47
49	Ж	29	40	42
50	Ж	31	40	42
51	Ж	49	42	52
52	М	33	42	60
53	Ж	31	43	54
54	М	59	43	60
55	Ж	50	43	45
56	М	47	43	41
"""

# Читаем данные
df = pd.read_csv(StringIO(data_str), sep="\t")

# Преобразуем категориальные переменные
le = LabelEncoder()
df['Пол_код'] = le.fit_transform(df['Пол'])

# Выбираем 5 переменных для кластеризации по здравому смыслу:
# возраст, доход, рейтинг, пол (закодированный), ID (неинформативный - исключим)
features = ['Пол_код', 'Возраст', 'Годовой доход (k$)', 'Оценка по внутренним рейтингам']
X = df[features]

# Масштабируем
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# KMeans: подбор числа кластеров
inertia = []
K = range(1, 10)
for k in K:
    km = KMeans(n_clusters=k, random_state=0)
    km.fit(X_scaled)
    inertia.append(km.inertia_)

# Найдём оптимальное число кластеров вручную (на графике), затем построим модель
optimal_k = 4
kmeans = KMeans(n_clusters=optimal_k, random_state=0)
df['kmeans_cluster'] = kmeans.fit_predict(X_scaled)

# DBSCAN
dbscan = DBSCAN(eps=1.2, min_samples=5)
df['dbscan_cluster'] = dbscan.fit_predict(X_scaled)

# Для параллельных координат нужно добавить к признакам номер кластера
df_parallel_kmeans = df[features + ['kmeans_cluster']].copy()
df_parallel_dbscan = df[features + ['dbscan_cluster']].copy()

import ace_tools as tools; tools.display_dataframe_to_user(name="Результаты кластеризации", dataframe=df)

# Построим графики далее
inertia, df_parallel_kmeans, df_parallel_dbscan, X_scaled, df
