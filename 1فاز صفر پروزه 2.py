# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:19:12 2026

@author: SMMH
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# دریافت تعداد گل
tedad = int(input("تعداد گل: "))

data = []
for i in range(tedad):
    print(f"\nگل {i+1}:")
    a = float(input("طول گلبرگ: "))
    b = float(input("عرض گلبرگ: "))
    c = float(input("طول کاسبرگ: "))
    d = float(input("عرض کاسبرگ: "))
    data.append([a, b, c, d])

# PCA
X = np.array(data)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# رسم
plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PCA')
plt.show()