# ===================================
# Clasificación logística + Curva ROC
# ===================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc

# 1) Dataset sintético: horas, asistencia -> aprueba (0/1)
rng = np.random.RandomState(42)
horas = rng.uniform(0, 10, size=200)
asistencia = rng.uniform(50, 100, size=200)
logit_real = 0.6 * horas + 0.04 * asistencia - 5.0 + rng.normal(0, 0.5, size=200)
aprueba = (logit_real >= 0).astype(int)

df = pd.DataFrame({
    "horas_estudio": horas,
    "asistencia_pct": asistencia,
    "aprueba": aprueba
})

# 2) X / y
X = df[["horas_estudio", "asistencia_pct"]]
y = df["aprueba"]

# 3) Train / Test (estratificado)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# 4) Modelo y ajuste
model = LogisticRegression()
model.fit(X_train, y_train)

# 5) Curva ROC + AUC
y_proba = model.predict_proba(X_test)[:, 1]
fpr, tpr, _ = roc_curve(y_test, y_proba)
roc_auc = auc(fpr, tpr)

print("=== CLASIFICACIÓN LOGÍSTICA ===")
print(f"AUC ROC: {roc_auc:.3f}")
print(f"Modelo: sigmoide({model.intercept_[0]:.3f} + "
      f"{model.coef_[0,0]:.3f}*horas + {model.coef_[0,1]:.3f}*asistencia)")

# 6) Gráfico: ROC
plt.figure()
plt.plot(fpr, tpr, label=f"ROC (AUC = {roc_auc:.3f})")
plt.plot([0, 1], [0, 1], linestyle="--", label="Azar")
plt.title("Curva ROC — Clasificación logística")
plt.xlabel("FPR (False Positive Rate)")
plt.ylabel("TPR (True Positive Rate)")
plt.legend()
plt.tight_layout()
plt.show()