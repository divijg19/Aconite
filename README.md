# Aconite
Python Practice and Testing Repo

<div align="center">

# Python

*A structured 13-week sprint to master production-grade Python for data science and machine learning.*

[![Project Status: Active](https://img.shields.io/badge/status-active-success.svg)](https://github.com/divijg19/Aconite)
[![Python Version](https://img.shields.io/badge/python-3.14%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

---

## The Mission

In today's tech landscape, knowing Python isn't enough. **Project Aconite** is a deliberate and intensive journey to bridge the gap between academic knowledge and job-ready, professional-grade Python development- a living project, showcasing a commitment to best practices and continuous learning.

This repository documents a three-month curriculum focused on writing clean, efficient, and production-ready code. The goal is not just to learn libraries, but to internalize the "Pythonic" way of thinking and to master the complete workflow—from data cleaning and model training to API deployment and testing.


## The 13-Week Curriculum

The roadmap is divided into three focused sprints, each building upon the last to develop a comprehensive, modern skill set.

### **Month 1: Python Fundamentals & The "Pythonic" Way**

**Objective:** Build a rock-solid foundation by moving beyond the basics to write efficient, idiomatic, and maintainable Python code.

| Weeks | Focus Area                   | Key Skills & Technologies                                  |
| :---- | :--------------------------- | :--------------------------------------------------------- |
| **1-2** | **Core Python Mastery**        | Advanced OOP, Data Structures (`collections`), Error Handling |
| **3-4** | **Idiomatic & Efficient Python** | List Comprehensions, Generators, Context Managers, Decorators |
| **`Job-Ready Skills`** | **Professional Tooling**     | `venv` (Environment Mgmt), `pytest` (Unit Testing)         |

### **Month 2: The Scientific Computing Stack**

**Objective:** Master the essential libraries for high-performance data manipulation and analysis, with a focus on writing vectorized, bottleneck-free code.

| Weeks | Focus Area            | Key Skills & Technologies                          |
| :---- | :-------------------- | :------------------------------------------------- |
| **5-6** | **NumPy Mastery**     | Vectorization, Broadcasting, Advanced Array Indexing |
| **7-8** | **Pandas Mastery**    | `groupby`, Merging/Joining, Multi-level Indexing, Time-Series |
| **`Job-Ready Skills`** | **Performance Tuning** | `cProfile` (Code Profiling & Optimization)         |

### **Month 3: Machine Learning in Practice**

**Objective:** Go from theory to practice by building, training, and deploying a machine learning model using a full-stack, production-oriented approach.

| Weeks   | Focus Area               | Key Skills & Technologies                               |
| :------ | :----------------------- | :------------------------------------------------------ |
| **9-11**  | **Applied Machine Learning** | **PyTorch:** Data Loaders, Custom Training Loops, Evaluation |
| **12-13** | **Project & Deployment**   | Model Serialization, API Development, Testing           |
| **`Job-Ready Skills`** | **ML in Production**       | **FastAPI** (Building & serving ML models via an API)     |

---

## ✅ Q1 Milestone Project: End-to-End ML Pipeline

This repository culminates in a complete, end-to-end machine learning project that demonstrates proficiency across the entire development lifecycle.

*   **Problem:** Predict a real-world outcome (e.g., customer churn, housing prices) using a public dataset.
*   **Data Processing:** A robust data cleaning and feature engineering pipeline built with **Pandas**.
*   **Modeling:** A neural network model built and trained in **PyTorch**.
*   **Deployment:** The trained model is served via a REST API built with **FastAPI**, capable of delivering real-time predictions.
*   **Testing:** The project includes unit tests for the data pipeline and integration tests for the API endpoints using **pytest**.
*   **Documentation:** A professional `README.md` and clear code comments ensure the project is understandable and maintainable.

---

## Navigating This Repository

The repository is organized by week, making it easy to follow the journey and find specific code examples and notes.

```
/Aconite
├── month1_python_mastery/
│   ├── week1_core_python/
│   │   ├── notes.md
│   │   └── code_examples/
│   ├── ...
├── month2_scientific_stack/
│   ├── ...
├── month3_ml_in_practice/
│   ├── ...
├── q1_milestone_project/
│   ├── app/
│   ├── models/
│   ├── tests/
│   └── README.md
└── requirements.txt
```

## Running the Code

To get a local copy up and running, please follow these steps.

### Prerequisites

*   Python 3.10+
*   Git

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/divijg19/Aconite.git
    cd Aconite
    ```
2.  **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install the required dependencies:**
    ```sh
    uv install -r requirements.txt
    ```

## Technology Stack

This project exclusively uses modern, industry-standard tools.

*   **Core Language:** Python 3
*   **Data Science:** NumPy, Pandas
*   **Machine Learning:** PyTorch, Keras
*   **API Development:** FastAPI
*   **Testing & Tooling:** uv, pytest, venv, cProfile

## Let's Connect

I'm actively seeking opportunities where I can apply these skills to solve real-world problems. Let's connect and discuss how I can bring value to your team.

*   **Divij Ganjoo**
*   **LinkedIn:** [linkedin.com/in/divij-ganjoo](https://linkedin.com/in/divij-ganjoo)
*   **Email:** [divijganjoo2003@gmail.com](mailto:divijganjoo2003@gmail.com)
