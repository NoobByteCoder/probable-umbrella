# Financial Transaction Anomaly Detection Tool

This tool identifies anomalies in financial transactions using statistical methods. It alerts users via email and saves the detected anomalies to a CSV file. The tool is written in Python and utilizes libraries such as Pandas and NumPy.

## Features

- Loads financial transaction data from a CSV file.
- Identifies anomalies using the Interquartile Range (IQR) method.
- Sends an email alert if anomalies are detected.
- Saves anomalies to a new CSV file.

## Requirements

- Python 3.8 or higher
- Pandas
- NumPy
- smtplib
- email
- Postfix SMTP server (configured for local email delivery)

## Installation

Clone this repository:

git clone https://github.com/NoobByteCoder/probable-umbrella.git

cd probable-umbrella

[OPTIONAL]

python3 -m venv venv

source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install required Python packages:

pip install pandas numpy

## Usage

Place your financial transactions in a CSV file named transactions.csv. The file should have the following columns:

transaction_id
date
customer_id
amount
type
description

Update the detect_anomalies.py script with your SMTP server details and email credentials.

Run the anomaly detection script:

python detect_anomalies.py

The tool will print the anomalies (if any) to the console, save them to anomalies.csv, and send an email alert.

Side Note: plot.py file plots the transactions.csv file (Histogram type plot). By seeing where the the values are nicely clustered we can tweak the IQR factor (1.5 in the code) in detect_anomalies.py file.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Feel free to fork this project, create a branch, and submit a pull request. Contributions are welcome!


This `README.md` file includes the necessary information for users to understand the tool, install the required dependencies, and run the script. The Python script `detect_anomalies.py` provided in the README contains the complete functionality for loading the data, detecting anomalies, saving them to a CSV file, and sending an email alert.
