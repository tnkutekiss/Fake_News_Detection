# Fake News Detection System

## Overview

This project implements a **Fake News Detection System** using the PhoBERT model and MongoDB for storing and processing news articles. The system aims to classify news articles as either "Fake" or "Real" by leveraging a pre-trained PhoBERT model, which is specifically designed for the Vietnamese language.

## Features

- **PhoBERT Model Integration**: Utilizes the PhoBERT model for sequence classification to detect fake news.
- **MongoDB Integration**: Stores and retrieves news articles from a MongoDB database.
- **Text Preprocessing and Data Augmentation**: Implements text preprocessing techniques and data augmentation through synonym replacement.
- **Prediction and Reporting**: Provides predictions for news articles and generates statistics on the number of fake and real news articles.

## Installation

### Prerequisites

- Python 3.x
- MongoDB
- Git
- Required Python packages (see `requirements.txt`)

### Clone the Repository

```bash
git clone https://github.com/yourusername/fake_news_detection.git
cd fake_news_detection
```

Install Dependencies
Install the required Python packages:

bash
Sao chép mã
pip install -r requirements.txt
Setup MongoDB
Ensure MongoDB is installed and running. If not, you can download it from MongoDB's official website.

Download PhoBERT Model
Download the pre-trained PhoBERT model from Hugging Face:

bash
Sao chép mã
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("vinai/phobert-base")
tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base")
Running the System
Load the Model and Tokenizer:

Make sure the model and tokenizer are properly loaded before running predictions.
Connect to MongoDB:

Ensure that the MongoDB service is running and the necessary news articles are stored in the database.
Run the Prediction Script:

bash
Sao chép mã
python predict.py
This script will load the news articles from MongoDB, process them using the PhoBERT model, and output the number of fake and real news articles along with the detailed text of fake articles.

Usage
Training:

The system is trained on Vietnamese text data using PhoBERT, with data augmentation through synonym replacement.
Prediction:

After training, the model can predict whether a new article is fake or real by running the predict.py script.
MongoDB:

MongoDB is used to store and manage the news articles. The connection is established within the script, and the articles are retrieved and processed.
Data
The dataset used in this project is a Vietnamese fake news dataset (vn_news_226_tlfr.csv). It contains labeled articles that have been preprocessed and augmented for better model training.

Folder Structure
graphql
Sao chép mã
fake_news_detection/
│
├── Data/                              # Contains the dataset and other data files
│   └── VFND-vietnamese-fake-news-datasets/
│
├── phobert_fake_news_model/           # Contains the PhoBERT model files
│
├── scripts/
│   ├── preprocess.py                  # Script for preprocessing text data
│   ├── train.py                       # Script for training the model
│   └── predict.py                     # Script for running predictions
│
├── requirements.txt                   # Python packages required
├── README.md                          # Project documentation
└── .gitignore                         # Git ignore file
Contributing
Feel free to contribute to this project by submitting a pull request. Ensure your code follows the existing style and conventions.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgements
PhoBERT by VinAI Research
Transformers by Hugging Face
MongoDB
markdown
Sao chép mã

### Key Sections:
- **Overview**: Describes what the project does.
- **Features**: Highlights the key functionalities.
- **Installation**: Guides users through setting up the project.
- **Usage**: Explains how to use the system.
- **Data**: Provides information about the dataset used.
- **Folder Structure**: Helps users navigate the project structure.
- **Contributing**: Invites others to contribute to the project.
- **License**: Specifies the licensing of the project.
- **Acknowledgements**: Credits the tools and resources used.

You can modify the content as needed to better fit your project specifics.
