import json

# This dictionary is the "single source of truth" for the Streamlit app.
# We've added all the new personas here.
USER_TOPICS = {
    # Original Personas
    101: {"main_topic": "python", "modifier": "for beginners"},
    202: {"main_topic": "coffee", "modifier": "in New York"},
    305: {"main_topic": "react", "modifier": None},

    # --- New Personas from the larger datasets ---
    # Fitness Enthusiast
    401: {"main_topic": "running", "modifier": "in Delhi"},
    # E-commerce Shopper
    502: {"main_topic": "Apple", "modifier": "electronics"},
    # DIY Home Cook
    603: {"main_topic": "vegetarian Indian", "modifier": "cooking"},
    # Machine Learning Student
    704: {"main_topic": "machine learning", "modifier": "PyTorch"},
    # Travel Blogger
    805: {"main_topic": "Southeast Asia", "modifier": "travel"},
    # PC Gamer
    906: {"main_topic": "PC gaming", "modifier": "strategy games"}
}

def rewrite_query_for_user(user_id, current_query):
    """
    Rewrites a query based on a simplified user profile.
    
    Args:
        user_id (int): The ID of the user.
        current_query (str): The user's original query.
        
    Returns:
        str: The personalized rewritten query.
    """
    if user_id not in USER_TOPICS:
        return current_query

    profile = USER_TOPICS[user_id]
    rewritten_query = current_query
    
    # Heuristic 1: Inject the main topic if not present
    main_topic = profile.get("main_topic")
    if main_topic and main_topic.lower() not in rewritten_query.lower():
        rewritten_query = f"{current_query} {main_topic}"

    # Heuristic 2: Inject a modifier
    modifier = profile.get("modifier")
    if modifier and modifier.lower() not in rewritten_query.lower():
        rewritten_query = f"{rewritten_query} {modifier}"
        
    # Clean up any extra spaces
    return " ".join(rewritten_query.split())