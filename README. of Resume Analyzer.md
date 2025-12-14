Smart Resume Analyzer

📌 Project Description

AI-powered Resume Analyzer using NLP and sentiment analysis to extract entities, evaluate tone, and suggest the best job category.

✨ Features

Preprocessing text with spaCy (lemmatization, stopword removal).

Named Entity Recognition (NER) for PERSON, ORG, GPE.

Sentiment classification (Positive, Negative, Neutral).

Job category matching using semantic similarity.

🚀 Usage

Run the main script with:

python main.py

📂 Project Structure

resume-analyzer/
├── src/                # Source code
└── README.md           # Project overview

📊 Example Output

Result for Resume 1:
{
  "Entities": [("Python", "ORG"), ("Java", "ORG")],
  "Sentiment": "Positive",
  "Best Job Category": "Project Manager"
}

📜 License

This project is licensed under the MIT License.

🌍 Future Work

Add categories for Data Scientist and Machine Learning Engineer.

Improve sentiment analysis with ML models.

Build a web interface for uploading resumes.
