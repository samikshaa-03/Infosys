# 🚀 AI-Powered Ticket Creation & Categorization System

Modern IT helpdesks receive a large volume of user-reported issues every day through emails, chat systems, and web forms. These messages are usually unstructured and require manual effort to read, understand, and convert into structured support tickets.

This project automates the **initial ticket creation and categorization process** using **Natural Language Processing (NLP)** and **Machine Learning**, reducing manual workload and improving consistency in helpdesk operations.

---

## 📌 Problem Statement
Support teams manually analyze incoming user messages to create service tickets. This manual approach results in:

- Delays in ticket creation  
- Inconsistent categorization  
- Human errors  
- Increased workload for support staff  

### 🎯 Goal
Automatically analyze user messages and generate **structured IT support tickets** with **minimal human intervention**.

---

## 🎯 Objectives
✔ Categorize user issues into predefined ticket categories  
✔ Assign an initial priority based on urgency  
✔ Clean and preprocess unstructured text data  
✔ Extract useful information such as entities and error codes  
✔ Generate a structured ticket from raw user input  
✔ Provide an interactive web interface for real-time ticket creation  

---

## 📂 Project Structure


AI_TICKET_PROJECT/
│
├── app.py                     # Streamlit frontend
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── .gitignore                 # Git ignored files
│
├── data/
│   └── all_tickets_processed_improved_v3.csv
│
├── scripts/
│   └── ticket_ai.py           # Backend ML & NLP logic
│
└── docs/
    └── project_overview.txt


---

## 📊 Dataset
The dataset contains historical IT support tickets with real-world issue descriptions and corresponding categories.

### Dataset Fields
- **Document** – Raw user issue description  
- **Topic_group** – Assigned issue category  

The dataset is used to train and evaluate the ticket categorization model.

---

## 🧠 Models & Techniques Used

### 🔹 Ticket Categorization
- TF-IDF Vectorizer for text feature extraction  
- Multinomial Naive Bayes classifier  

### 🔹 Priority Assignment
- Rule-based logic using urgency-related keywords  

### 🔹 NLP Processing
- Text cleaning and normalization  
- Named Entity Recognition (NER) using spaCy  
- Error code detection using regular expressions  

---

## 🔁 End-to-End Workflow


User Issue
    ↓
Text Cleaning & Preprocessing
    ↓
TF-IDF Vectorization
    ↓
Category Prediction (Naive Bayes)
    ↓
Entity & Error Code Extraction
    ↓
Priority Assignment
    ↓
Structured Ticket Generation


---

## 🛠 Technologies Used

| Category         | Tools / Libraries          |
|--------          |------------------          |
| Programming      | Python                     |
| Machine Learning | Scikit-learn               |
| NLP              | spaCy, Regular Expressions |
| Data Handling    | pandas, NumPy              |
| Frontend         | Streamlit                  |

---

## 📅 Milestones Completed

### ✅ Milestone 1 – Data Preparation
✔ Dataset loading and inspection  
✔ Text cleaning and normalization  
✔ Label usage for supervised learning  

### ✅ Milestone 2 – Model Development
✔ Train-test split implemented  
✔ TF-IDF feature extraction  
✔ Naive Bayes classifier trained  
✔ Model accuracy evaluated  

### ✅ Milestone 3 – Ticket Generation Engine
✔ Category prediction implemented  
✔ Priority assignment logic added  
✔ Entity and error code extraction  
✔ Structured ticket output generated  

### ✅ Milestone 4 – User Interface
✔ Streamlit-based web interface  
✔ Real-time ticket generation  
✔ Ticket preview and confirmation view  

---

## 🧪 Sample Input

My laptop is not working urgently and shows error 404.


## 📄 Sample Output
- **Category:** Hardware Issue  
- **Priority:** High  
- **Error Code:** 404  

---

## 🚀 Future Enhancements
- Advanced priority prediction using sentiment analysis  
- Integration with real helpdesk tools (Jira, ServiceNow)  
- REST API deployment using FastAPI  
- Multi-language support  

---

## 👩‍💻 Author
Computer Engineering Student  
AI & Machine Learning Project – 2025
