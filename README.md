# Credit Card Limit Estimator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![scikit-learn](https://img.shields.io/badge/Library-scikit--learn-orange)
![Status](https://img.shields.io/badge/Status-Developing-brightgreen)

## Overview
The **Credit Card Limit Estimator** is a machine learning project designed to predict the credit limit of customers based on various financial and demographic factors. This project leverages a dataset of customer details and applies regression techniques to estimate their credit card limit accurately.

This project is useful for financial institutions to evaluate customer creditworthiness, improve risk management, and offer customized credit solutions.

## Note
The Web Application might take a few seconds/minutes to run when you are running it for the first time or after a long time. This is because it runs on a free server. This server shuts down upon inactivity and starts again once a request to the server is made. 

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model](#model)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features
- Predicts the credit card limit based on customer data.
- Includes preprocessing techniques to clean and prepare data.
- Implements multiple regression algorithms.
- Evaluation and performance metrics are provided.
- Customizable and scalable for additional data inputs.

## Dataset
The dataset used for this project consists of customer financial and demographic information, including:
- Income
- Limit
- Rating
- Cards
- Age
- Education
- Gender
- Student
- Married
- Ethnicity
- Balance


**Note**: The dataset is included in the repository or sourced externally, depending on use case. You can modify the script to include your own data.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jaysheeldodia/Credit-Card-Limit-Estimator.git
   cd Credit-Card-Limit-Estimator
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare the dataset**: Ensure you have the dataset properly formatted. Place it in the appropriate directory as specified in the code or use the default path.

2. **Run the Estimator**: Execute the Python script to train the model and predict credit limits.
   ```bash
   python app.py
   ```

3. **Modify for Custom Data**: If you'd like to use your own data, replace the dataset and update the script accordingly to reflect new feature columns.

4. **Output**: The model will output predicted credit limits.

## Project Structure

```bash
Credit-Card-Limit-Estimator/
│
├── data/                           # Folder for datasets
│   └── credit.csv         # Sample dataset (replace with actual data)
│
├── model/                         # Folder for trained models (saved models)
│   └── LimitEstimator.pkl       # Example: trained model
│
├── notebooks/                      # Jupyter Notebooks for exploration and testing
│   └── train.ipynb                    # Exploratory Data Analysis notebook
│
├── app.py   # Main script to run the model
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation (this file)
```

## Model
The project implements the following machine learning models:
- Linear Regression
<!-- - Decision Trees
- Random Forest Regressor
- Gradient Boosting -->

<!-- You can easily switch between models by modifying the `app.py` script. -->

**Evaluation Metrics**:
- Accuracy 

**ToDo**:
1. Add more evaluation metrics:
    - R2
    - Mean Squared Error (MSE)
    - Root Mean Squared Error (RMSE)
2. Train More Models:
    - Decision Trees
    - Random Forest Regressor
    - Gradient Boosting
3. Give option to switch between models (or run all models simulatneously)
4. Show visualization about the trian and test data and the metrics
5. Add more pages to the website (optional)

These metrics allow you to evaluate the performance of the model in estimating credit limits.

## Contributing
Contributions are welcome! Here's how you can contribute to this project:
1. Fork the repository.
2. Create a new feature branch: `git checkout -b feature-branch-name`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- This project uses open-source libraries such as `scikit-learn`, `pandas`, and `numpy`.
- The dataset used in this project is either publicly available or provided by the user.
- Special thanks to [Jay Sheel Dodia](https://github.com/jaysheeldodia) for developing and maintaining this project.
```

Feel free to customize any part of this template, such as the dataset section, model details, or contributing guidelines, to match the exact functionality of the project.

