import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def descriptive_statistics(x) :
    return pd.Series([x.mean(), x.median(), x.std(), x.var(),
                      x.kurt(), x.skew(), x.min(), x.max(), x.sum(),
                      x.count(), x.quantile(.25), x.quantile(.75)], index=['mean', 'median', 'std', 'var', 'kurtosis', 'skewness', 'min', 'max', 'sum', 'count', '25%', '75%'])

def calculate_return(x):
    return np.log(x) - np.log(x.shift(1))

# Open file
data = pd.read_excel("YEAR.xlsx")

# Calculate return
data["TAIEX_RETURN"] = calculate_return(data.TAIEX_CLOSE)
data["EMC_RETURN"] = calculate_return(data.EMC_CLOSE)
data["YML_RETURN"] = calculate_return(data.YML_CLOSE)
data["TSMC_RETURN"] = calculate_return(data.TSMC_CLOSE)
data["MTK_RETURN"] = calculate_return(data.MTK_CLOSE)
data["FFHVCC_RETURN"] = calculate_return(data.FFHVCC_CLOSE)
data["FFHC_RETURN"] = calculate_return(data.FFHC_CLOSE)

# Construct the columns of data
descriptive_statistics_result = pd.DataFrame(data, columns=["TAIEX_RETURN", "EMC_RETURN", "YML_RETURN", "TSMC_RETURN", "MTK_RETURN", "FFHVCC_RETURN", "FFHC_RETURN"])

print(descriptive_statistics_result.apply(descriptive_statistics))

# illustrate
plt.hist(data.EMC_RETURN, bins=100, density=True, label='EMC_RETURN', color='r')
plt.hist(data.YML_RETURN, bins=100, density=True, label='YML_RETURN', color='blue')
plt.hist(data.TAIEX_RETURN, bins=100, density=True, label="TAIEX_RETURN", color="g")
plt.hist(data.TSMC_RETURN, bins=100, density=True, label="TSMC_RETURN", color="pink")
plt.hist(data.MTK_RETURN, bins=100, density=True, label="MTK_RETURN", color="yellow")
plt.hist(data.FFHVCC_RETURN, bins=100, density=True, label="FFHVCC_RETURN", color="brown")
plt.hist(data.FFHC_RETURN, bins=100, density=True, label="FFHC_RETURN", color="purple")

plt.legend()
plt.xlabel('Return')
plt.ylabel('Probability density')
plt.title("Return")
plt.show()

#直方圖 
# fig=plt.figure(figsize=(10,10))
# p1=fig.add_subplot(211)
# plt.hist(data.TAIEX_RETURN,bins=100,rwidth=0.9)
# plt.xlabel('Return')
# plt.title("TAIEX Return")
# plt.show()
