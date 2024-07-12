import pandas as pd
import numpy as np
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load the data
data = pd.read_csv('transactions.csv')

# Print the first few rows to verify the column names
print(data.head())

# Calculate Q1 (25th percentile) and Q3 (75th percentile) for each customer
data['Q1'] = data.groupby('customer_id')['amount'].transform(lambda x: x.quantile(0.25))
data['Q3'] = data.groupby('customer_id')['amount'].transform(lambda x: x.quantile(0.75))

# Calculate IQR
data['IQR'] = data['Q3'] - data['Q1']

# Identify anomalies using the IQR method
data['anomaly'] = (data['amount'] < (data['Q1'] - 1.5 * data['IQR'])) | (data['amount'] > (data['Q3'] + 1.5 * data['IQR'])) # the factor 1.5 can be tweaked according to the input dataset

# Filter out the anomalies
anomalies = data[data['anomaly'] == True]

# Save anomalies to a new CSV file
anomalies.to_csv('anomalies.csv', index=False)

# Define the function to send an email alert
def send_alert(anomalies):
    smtp_server = 'ubuntu.localdomain'
    smtp_port = 25 # Use port 25 or sometime port 587 shall be used if 25 doesn't work
    sender_email = 'abc@yourdomain.com' #replace with sender's email
    recipient_email = 'def@yourdomain.com' # #replace with recipient's email

    subject = 'Anomaly Detected in Financial Transactions'
    body = anomalies.to_string()

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print("Alert sent successfully!")
    except Exception as e:
        print(f"Failed to send alert: {e}")

# Output anomalies and send alert if anomalies are found
if not anomalies.empty:
    print("Anomalies detected:")
    print(anomalies)
    send_alert(anomalies)
else:
    print("No anomalies detected.")
