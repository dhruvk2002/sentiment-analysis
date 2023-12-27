# Sentiment Analysis Project

This project focuses on sentiment analysis using a Twitter dataset consisting of 50,000 tweets. The dataset is split into training and testing sets, with 80% used for training and 20% for testing. The sentiment analysis model achieved an accuracy of 90%.
The alogorithm which I have used is RandomForest along with vectorization and preprocessing containing in a single machine learning pipeline
## Project Structure

- `data_process/`: It is custom made python module which consists of all the neccessary function for data preprocessing pipeline.
- `main.ipynb`: Jupyter notebook file with training history and results.
- `requirements.txt`: File listing the required dependencies for the project.
- `app.py`: File which contains the neccessary coding for the frontend interaction using streamlit.
- `sentiment_analysis.pkl`: It is exported trained model after training

## Getting Started

### Prerequisites

Make sure you have Python installed. You can install the project dependencies using:

```bash
pip install -r requirements.txt
