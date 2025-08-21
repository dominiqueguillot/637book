import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import binom

# Load dataset
# pheno = 49 phenotypes
# assay = 7129 x 49 gene expression data

pheno_pd = pd.read_csv('./pheno.csv',delimiter=',')
pheno_pd.loc[pheno_pd['nodal.y']=="positive"] = 1
pheno_pd.loc[pheno_pd['nodal.y']=="negative"] = 0

assay_pd = pd.read_csv('./assay.csv',delimiter=',')

pheno = np.array(pheno_pd['nodal.y'],dtype=np.double)
assay = np.array(assay_pd)

X = assay.T
y = pheno

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

N = 10

perc_correct = np.zeros(N)

lin_model = LinearRegression(fit_intercept=True)

for i in range(N):
	print(i)
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25,)# random_state=42)

	# Standard linear regression
	lin_model.fit(X_train, y_train)
	pred = lin_model.predict(X_test)

	pred[pred > 0.5] = 1
	pred[pred <= 0.5] = 0

	perc_correct[i] = (pred == y_test).sum()/np.double(len(y_test))*100

avg_perc = perc_correct.mean()
std_perc = perc_correct.std()
	
print("Average percentage of features correctly predicted (Standard Linear regression): %1.2f%% (std=%1.2f)\n" % (avg_perc, std_perc))


# Using Lasso

from sklearn.linear_model import LassoCV
 
perc_correct_lasso = np.zeros(N)
lasso_model = LassoCV(n_alphas=200, fit_intercept=True, cv=10)  # Use 10-folds cross-validation
 
for i in range(N):
	print(i)
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25,)# random_state=42)

	# Standard linear regression
	lasso_model.fit(X_train, y_train)
	predictors = abs(lasso_model.coef_) > 1e-6
	print("Nb. predictors %d\n\n" % predictors.sum())
	if predictors.sum() > 0:
		# Predict using selected variables
		lin_model.fit(X_train[:,predictors],y_train)
		pred = lin_model.predict(X_test[:,predictors]) 
	else:
		pred = lasso_model.predict(X_test)

	pred[pred > 0.5] = 1
	pred[pred <= 0.5] = 0

	perc_correct_lasso[i] = (pred == y_test).sum()/np.double(len(y_test))*100

avg_perc_lasso = perc_correct_lasso.mean()
std_perc_lasso = perc_correct_lasso.std()

print("Average percentage of features correctly predicted (Lasso): %1.2f%% (std=%1.2f)\n" % (avg_perc_lasso, std_perc_lasso))

