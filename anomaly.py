from sklearn.ensemble import IsolationForest
from scipy.stats import zscore

# Признаки, по которым будет производиться анализ
anomaly_features = ['Пол_код', 'Возраст', 'Годовой доход (k$)', 'Оценка по внутренним рейтингам']

# Стандартизуем
X_anomaly = scaler.fit_transform(df[anomaly_features])

# Метод 1: Isolation Forest
iso = IsolationForest(contamination=0.1, random_state=0)
df['anomaly_isolation_forest'] = iso.fit_predict(X_anomaly)  # -1 = аномалия

# Метод 2: Z-оценка
z_scores = np.abs(zscore(df[anomaly_features]))
df['anomaly_z_score'] = (z_scores > 3).any(axis=1)  # True = аномалия

# Подсчитаем общее количество аномалий
iso_outliers = df['anomaly_isolation_forest'].value_counts().get(-1, 0)
zscore_outliers = df['anomaly_z_score'].sum()

# Выведем наблюдения, помеченные как аномальные хотя бы одним методом
anomalies_df = df[(df['anomaly_isolation_forest'] == -1) | (df['anomaly_z_score'])]

tools.display_dataframe_to_user(name="Обнаруженные аномалии", dataframe=anomalies_df)

iso_outliers, zscore_outliers, len(df), anomalies_df
