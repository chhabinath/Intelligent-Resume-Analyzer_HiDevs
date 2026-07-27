# 📄 Intelligent Resume Analyzer

A Python-based Resume Analysis System that automates resume screening by parsing resumes, matching candidates against job requirements, calculating ATS match scores, and generating professional analysis reports. The application includes a user-friendly Streamlit interface, batch processing, database integration, analytics, and multiple report export options.

---

## 🚀 Features

### Resume Parsing
- Extract candidate name
- Extract email address
- Extract phone number
- Extract skills
- Extract work experience
- Extract education

### Job Description Management
- Load job descriptions from JSON files
- Validate job requirements
- Compare resumes against selected jobs

### ATS Matching Engine
- Skill matching
- Experience matching
- Education matching
- ATS score calculation (0–100)
- Hiring recommendations

### Resume Analysis
- Single resume analysis
- Batch resume analysis
- Resume validation
- Error handling

### Report Generation
- Text reports (.txt)
- JSON reports (.json)
- Excel reports (.xlsx)
- PDF reports (.pdf)

### Database Management
- SQLite database integration
- Candidate storage
- Search candidates
- Filter candidates
- Delete candidates
- View candidate details

### Analytics Dashboard
- ATS score statistics
- Recommendation distribution
- Skill analysis
- Candidate analytics
- Interactive charts

### Logging
- Application logging
- Error logging
- Activity tracking

---

# 🛠️ Technology Stack

- Python 3.x
- Streamlit
- SQLite
- Matplotlib
- Pandas
- OpenPyXL
- ReportLab
- JSON

---

# 📂 Project Structure

```
Intelligent-Resume-Analyzer/
│
├── app.py
├── parser.py
├── matcher.py
├── reporter.py
├── validator.py
├── batch_processor.py
├── database.py
├── candidate_repository.py
├── job_loader.py
├── excel_exporter.py
├── pdf_exporter.py
├── logger.py
├── models.py
├── exceptions.py
│
├── jobs/
├── resumes/
├── reports/
├── database/
│
├── pages/
│   ├── 1_Single_Resume.py
│   ├── 2_Batch_Analysis.py
│   ├── 3_Reports.py
│   ├── 4_About.py
│   ├── 5_Candidate_Database.py
│   └── 6_Analytics.py
│
├── utils/
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone [https://github.com/your-username/Intelligent-Resume-Analyzer.git](https://github.com/chhabinath/Intelligent-Resume-Analyzer_HiDevs.git)

cd Intelligent-Resume-Analyzer
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the Application

```bash
streamlit run app.py
```

---

# 📋 How to Use

## Single Resume Analysis

1. Open the application.
2. Navigate to **Single Resume Analysis**.
3. Upload a resume (.txt).
4. Select a job description.
5. Click **Analyze Resume**.
6. View:
   - Candidate information
   - ATS score
   - Recommendation
   - Skill analysis
   - Charts
   - Generated report

---

## Batch Resume Analysis

1. Open **Batch Analysis**.
2. Upload multiple resumes.
3. Select a job description.
4. Start batch processing.
5. View ranking and summary report.

---

## Candidate Database

- View all analyzed candidates
- Search candidates
- Filter by score
- Filter by experience
- Filter by recommendation
- Download reports
- Delete candidates

---

## Analytics Dashboard

- Total candidates
- Average ATS score
- Recommendation distribution
- Score charts
- Experience charts

---

# 🎯 ATS Scoring System

| Criteria | Weight |
|----------|--------|
| Skills | 50 Points |
| Experience | 30 Points |
| Education | 20 Points |
| **Total** | **100 Points** |

---

# 💡 Hiring Recommendations

| Score | Recommendation |
|--------|---------------|
| 80–100 | Strongly Recommend |
| 60–79 | Recommend |
| 40–59 | Maybe |
| 0–39 | Not Recommended |

---

# 📊 Reports Generated

The system generates professional reports including:

- Candidate Details
- Job Details
- Matched Skills
- Missing Skills
- ATS Score
- Hiring Recommendation

Reports are available in:

- TXT
- JSON
- Excel
- PDF

---

# 🗄️ Database Features

The SQLite database stores:

- Candidate information
- ATS scores
- Recommendations
- Skills
- Generated report paths
- Analysis history

---

# 🧪 Error Handling

The application handles:

- Invalid resumes
- Missing email
- Missing skills
- Invalid job descriptions
- Empty files
- Database errors
- File errors

---

# 📸 Screenshots

Add screenshots of:

- Home Page
- Single Resume Analysis
- Batch Analysis
- Candidate Database
- Analytics Dashboard
- Generated Reports

Example:

```
assets/
├── home.png
├── single_resume.png
├── batch_analysis.png
├── candidate_database.png
└── analytics.png
```

---

# 🔮 Future Enhancements

- AI-powered resume analysis
- Semantic skill matching
- Resume ranking
- Interview scheduling
- Email notifications
- REST API
- Cloud deployment
- Authentication system

---

# 👨‍💻 Author

**Your Name**

Python Developer

---

# 📜 License

This project is licensed under the MIT License.

See the **LICENSE** file for details.

---

# 🙏 Acknowledgements

- Python
- Streamlit
- SQLite
- Pandas
- Matplotlib
- ReportLab
- Open Source Community

MIT License

Copyright (c) 2026 Chhabinath Sahoo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
