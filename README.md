# Query_Rewriter_System
A query rewriter system that takes a user query and rewrites it in a more personalized way.

Personalized Query Rewriter
This project is a backend system designed to personalize user search queries. It takes a generic query from a user and rewrites it into a more specific, context-aware query based on a simulated user profile. The system includes a core rewriting engine, a robust evaluation methodology, and an interactive web demo built with Streamlit.

Features
Rule-Based Personalization: A simple, heuristic-based engine that injects user-specific context (like interests, location, or experience level) into queries.

Synthetic Datasets: Comes with scripts to generate datasets of varying sizes (6, 50+, and 100 queries) to simulate different user personas and query types (knowledge, shopping, support).

Dual Evaluation Framework: Measures performance using both an automatic metric (BERTScore for semantic similarity) and a qualitative, human-in-the-loop rubric.

Interactive Demo: A Streamlit web application allows for real-time, interactive testing of the rewriting engine with different user personas.

Tech Stack
Backend: Python

Web Demo: Streamlit

Data Handling: Pandas

Evaluation: bert-score, transformers, torch

Dataset Description
This project uses synthetically generated data to avoid the privacy and complexity issues associated with real user data. The datasets are stored in CSV format in the /data directory.

Structure
Each row in the CSV represents a single query and has the following structure:

user_id: A unique identifier for the user persona.

context: A JSON string representing the user's profile. This includes their interests, preferences, location, etc.

current_query: The generic, original query typed by the user.

ground_truth_rewrite: The "ideal" personalized query that the system aims to generate. This is used as the reference for evaluation.

Assumptions
Static User Profiles: The user context is pre-defined and static for each persona. In a real-world system, this profile would be dynamically generated and updated based on the user's ongoing activity.

Baseline Heuristic Model: The rewriting engine is a proof-of-concept that uses simple rules (keyword checking and appending). It is not a machine learning model.

Idealized Ground Truth: The ground_truth_rewrite is considered the perfect, grammatically correct target for the purpose of evaluation.
