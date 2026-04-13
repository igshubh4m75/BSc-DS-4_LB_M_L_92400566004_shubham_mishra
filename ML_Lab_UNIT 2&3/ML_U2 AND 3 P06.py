# Program6 unit-2
#Feature Selection and Dimensionality Reduction
# PCA - Principal Component Analysis
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
# Load dataset
df=pd.read_csv('auto-mpg.csv')
# Clean horsepower
df['horsepower']=df['horsepower'].replace('?',np.nan)
df['horsepower']=pd.to_numeric(df['horsepower'])
df['horsepower']=df['horsepower'].fillna(df['horsepower'].mean())
# Select numeric features
x=df.select_dtypes(include=['int64','float64']).drop('mpg',axis=1)
# Standardize data
scaler=StandardScaler()
x_scaled=scaler.fit_transform(x)
# Apply PCA (reduce to 2 components)
pca=PCA(n_components=2)
x_pca=pca.fit_transform(x_scaled)
print('Original Shape:',x.shape)
print('Reduced Shape after PCA:',x_pca.shape)
