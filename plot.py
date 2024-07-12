import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('transactions.csv')

# Plot the transaction amounts
plt.figure(figsize=(10, 6))
plt.hist(data['amount'], bins=50, edgecolor='k', alpha=0.7)
plt.xlabel('Transaction Amount')
plt.ylabel('Frequency')
plt.title('Distribution of Transaction Amounts')
plt.show()