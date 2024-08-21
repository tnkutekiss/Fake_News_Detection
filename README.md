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
