# =================
# Regresión lineal
# =================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# 1) Dataset sintético: horas -> nota (relación lineal con ruido)
rng = np.random.RandomState(42)
horas = rng.uniform(0, 10, size=60).reshape(-1, 1)
nota = 20 + 6 * horas + rng.normal(0, 3, size=(60, 1))
df = pd.DataFrame({"horas_estudio": horas.ravel(), "nota": nota.ravel()})

# 2) X / y
X = df[["horas_estudio"]]
y = df["nota"]

# 3) Train / Test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4) Modelo y ajuste
model = LinearRegression()
model.fit(X_train, y_train)

# 5) Predicción y métricas
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("=== REGRESIÓN LINEAL ===")
print(f"Modelo: y = {model.intercept_:.2f} + {model.coef_[0]:.2f} * horas_estudio")
print(f"MAE: {mae:.2f}")
print(f"R^2: {r2:.3f}")

# 6) Gráfico: dispersión (train/test) + recta aprendida
plt.figure()
plt.scatter(X_train["horas_estudio"], y_train, label="Train")
plt.scatter(X_test["horas_estudio"], y_test, marker="s", label="Test")

x_line = np.linspace(X["horas_estudio"].min(), X["horas_estudio"].max(), 100).reshape(-1, 1)
y_line = model.predict(pd.DataFrame({"horas_estudio": x_line.ravel()}))

plt.plot(x_line, y_line, label="Recta de regresión")
plt.title("Regresión lineal: horas de estudio vs. nota")
plt.xlabel("Horas de estudio")
plt.ylabel("Nota")
plt.legend()
plt.tight_layout()
plt.show()