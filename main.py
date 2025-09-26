import pandas as pd
from src.rewriter import rewrite_query_for_user
from bert_score import score

def run_pipeline():
    """Loads data, runs the rewriter, and evaluates the output."""
    # 1. Load the data
    # Note: You can change the filename to 'data/large_synthetic_queries.csv' to run the larger dataset
    try:
        df = pd.read_csv('data/synthetic_queries.csv')
    except FileNotFoundError:
        print("Error: CSV file not found. Have you run one of the generate_data scripts?")
        return

    # 2. Run the rewriter on each query
    df['generated_rewrite'] = df.apply(
        lambda row: rewrite_query_for_user(row['user_id'], row['current_query']),
        axis=1
    )

    # 3. Evaluate the results
    evaluate_rewrites(df)

def evaluate_rewrites(df):
    """Performs automatic and qualitative evaluation."""
    print("--- Query Rewrite Evaluation ---")
    
    # ----- Qualitative Evaluation (Human Judgment Table) -----
    print("\n📊 Qualitative Review Table:")
    print("="*120)
    print(f"{'Original Query':<30} | {'Generated Rewrite':<45} | {'Ground Truth Rewrite':<45}")
    print("-"*120)
    for index, row in df.iterrows():
        print(f"{row['current_query']:<30} | {row['generated_rewrite']:<45} | {row['ground_truth_rewrite']:<45}")
    print("="*120)
    
    # ----- Automatic Evaluation (BERTScore) -----
    print("\n📈 Automatic Metric: BERTScore")
    
    # Get lists of candidate and reference sentences
    candidates = df['generated_rewrite'].tolist()
    references = df['ground_truth_rewrite'].tolist()
    
    # Calculate scores
    # Using a distilled model for faster performance
    P, R, F1 = score(candidates, references, lang='en', model_type='distilbert-base-uncased')
    
    print(f"\nAverage BERTScore Precision: {P.mean():.4f}")
    print(f"Average BERTScore Recall:    {R.mean():.4f}")
    print(f"Average BERTScore F1-Score:  {F1.mean():.4f}")

if __name__ == "__main__":
    run_pipeline()