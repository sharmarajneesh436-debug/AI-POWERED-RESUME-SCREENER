# 📄 AI Powered Resume Screener

An AI-powered Resume Screening System built using **Python**, **Streamlit**, **Machine Learning**, and **MySQL**. The application automatically parses resumes, extracts candidate skills, calculates an ATS (Applicant Tracking System) compatibility score against a Job Description, stores candidate information in a database, and ranks applicants based on their scores.

---

## 🚀 Features

* 📂 Upload multiple PDF resumes
* 📝 Enter a Job Description
* 🤖 Automatic resume text extraction
* 🎯 AI-based ATS score calculation using TF-IDF and Cosine Similarity
* 🛠 Skill extraction from resumes
* 💾 Store candidate information in MySQL database
* 🏆 Rank candidates using Heap-based Priority Queue
* 📊 Interactive Streamlit web interface

---

## 🛠 Tech Stack

* Python
* Streamlit
* Scikit-learn
* Pandas
* PyPDF2
* MySQL
* Python Dotenv

---

## 📂 Project Structure

```
AI-Powered-Resume-Screener/
│
├── app.py                 # Main Streamlit Application
├── parser.py              # Resume PDF Parser
├── skill_extractor.py     # Extract Skills from Resume
├── ats_scorer.py          # ATS Score Calculator
├── candidate.py           # Candidate Class
├── db.py                  # Database Operations
├── heap_ranking.py        # Candidate Ranking Logic
├── skills.csv             # Skills Dataset
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Powered-Resume-Screener.git

cd AI-Powered-Resume-Screener
```

### Create Virtual Environment

**Windows**

```bash
python -m venv venv

venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄 Configure Database

Create a MySQL database and update your `.env` file.

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=resume_db
```

Create the following tables:

### Candidates Table

```sql
CREATE TABLE candidates(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(150),
    score FLOAT
);
```

### Candidate Skills Table

```sql
CREATE TABLE candidate_skills(
    id INT PRIMARY KEY AUTO_INCREMENT,
    candidate_id INT,
    skill_name VARCHAR(100)
);
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📌 Workflow

1. Enter the Job Description.
2. Upload one or more PDF resumes.
3. Extract resume text.
4. Identify candidate skills.
5. Calculate ATS compatibility score.
6. Store candidate data in MySQL.
7. Rank candidates based on their scores.
8. Display the Top Candidates.

---

## 📊 ATS Scoring Method

The project uses:

* TF-IDF Vectorization
* Cosine Similarity

to compare the Job Description with the Resume text and generate an ATS compatibility score between **0–100%**.

---

## 🎯 Future Enhancements

* Resume recommendation system
* Email notification to shortlisted candidates
* Semantic similarity using BERT or Sentence Transformers
* Experience extraction
* Education extraction
* Resume keyword highlighting
* Recruiter Dashboard
* Authentication System
* Interview Scheduling

---

## 📷 Application Preview

```
Enter Job Description

Upload Resumes (PDF)

Analyze

---------------------------------
Candidate A
Score : 91%

Candidate B
Score : 87%

Candidate C
Score : 82%
---------------------------------
```

---

## 📄 Requirements

```
streamlit
pandas
scikit-learn
mysql-connector-python
PyPDF2
python-dotenv
```

---

## 👨‍💻 Author

**Sharvatosh Pandey**

B.Tech CSE | AI & Machine Learning Enthusiast

---

## 📜 License

This project is licensed under the MIT License.
