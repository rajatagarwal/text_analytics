import numpy as np 
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve
from sklearn.metrics import auc

fpr = [0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
tpr = [0.2, 0.5, 0.6, 0.8, 0.88, 0.9, 0.95, 0.96, 0.97, 0.98]

# Compute fpr, tpr, thresholds and roc auc
auc=auc(fpr, tpr)
print("auc for the first class",auc)

# Plot ROC curve
plt.plot(fpr, tpr, label='ROC curve (Area Under Curve (AUC) area = %0.3f)' % auc)
plt.plot([0, 1], [0, 1], 'k--')  # random predictions curve
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate or Sensitivity')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.show()