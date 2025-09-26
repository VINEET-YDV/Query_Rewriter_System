# **Personalized Query Rewriter**

This project is a backend system designed to personalize user search queries. It takes a generic query from a user and rewrites it into a more specific, context-aware query based on a simulated user profile. The system includes a core rewriting engine, a robust evaluation methodology, and an interactive web demo built with Streamlit.

### **Features**

* **Rule-Based Personalization:** A simple, heuristic-based engine that injects user-specific context (like interests, location, or experience level) into queries.  
* **Synthetic Datasets:** Comes with scripts to generate datasets of varying sizes (6, 50+, and 100 queries) to simulate different user personas and query types (knowledge, shopping, support).  
* **Dual Evaluation Framework:** Measures performance using both an automatic metric (BERTScore for semantic similarity) and a qualitative, human-in-the-loop rubric.  
* **Interactive Demo:** A Streamlit web application allows for real-time, interactive testing of the rewriting engine with different user personas.

### **Tech Stack**

* **Backend:** Python  
* **Web Demo:** Streamlit  
* **Data Handling:** Pandas  
* **Evaluation:** bert-score, transformers, torch

## **Dataset Description**

This project uses synthetically generated data to avoid the privacy and complexity issues associated with real user data. The datasets are stored in CSV format in the /data directory.

### **Structure**

Each row in the CSV represents a single query and has the following structure:

* user\_id: A unique identifier for the user persona.  
* context: A JSON string representing the user's profile. This includes their interests, preferences, location, etc.  
* current\_query: The generic, original query typed by the user.  
* ground\_truth\_rewrite: The "ideal" personalized query that the system aims to generate. This is used as the reference for evaluation.

## **Setup and Usage Instructions**

### **1\. Prerequisites**

* Python 3.8+  
* pip and venv

### **2\. Installation**

Clone the repository and set up the virtual environment.

\# Clone the repository  
git clone \<your-repo-url\>  
cd query\_rewriter

\# Create and activate a virtual environment  
python \-m venv venv  
source venv/bin/activate  \# On Windows, use \`venv\\Scripts\\activate\`

\# Install the required packages  
pip install \-r requirements.txt

### **3\. Generate Data**

Before running the application or evaluation, generate one of the synthetic datasets.

\# Generate the larger dataset (100 queries)  
python src/generate\_100\_queries.py

### **4\. Run the Evaluation Script**

To run the full evaluation pipeline on the terminal (using the small dataset by default), execute main.py. This will print the qualitative review table and the final BERTScore results.

python main.py

*To evaluate the larger dataset, you will need to modify the filename inside main.py from synthetic\_queries.csv to 100\_synthetic\_queries.csv.*

### **5\. Launch the Interactive Web App**

To start the Streamlit demo, run the app.py file. Make sure you have updated src/rewriter.py with all the user personas you want to test.

streamlit run app.py

Your browser will open a new tab with the interactive application.

### **Quantitative Findings (BERTScore)**

The system's output was compared against the ground truth dataset using BERTScore, which measures semantic similarity.

* **Average F1-Score:** **\~0.98**

An F1-score this high indicates that the generated queries are **semantically very close** to the ideal target queries. It confirms that the system is adding the correct *meaning*, even if the phrasing isn't perfect.

Deployed Web\_App Link \- https://queryrewritersystem.streamlit.app/
