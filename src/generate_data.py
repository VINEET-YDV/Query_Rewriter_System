import pandas as pd
import json

def create_100_query_dataset():
    """Generates a diverse synthetic dataset with 100 queries."""
    
    all_queries = []

    # --- Persona 1: The Fitness Enthusiast in Delhi (User ID: 401) ---
    # Total: 11 Queries
    user_401_queries = [
        {"q": "best shoes", "gt": "best running shoes in Delhi"},
        {"q": "how to improve stamina", "gt": "how to improve stamina for running"},
        {"q": "local parks", "gt": "local parks for running in Delhi"},
        {"q": "morning workout routines", "gt": "morning running workout routines"},
        {"q": "5k training plan", "gt": "5k running training plan for beginners"},
        {"q": "best protein supplements", "gt": "best protein supplements for runners"},
        {"q": "nutrition advice", "gt": "nutrition advice for runners"},
        {"q": "marathon training schedule", "gt": "marathon running training schedule Delhi"},
        {"q": "local running clubs", "gt": "local running clubs in Delhi"},
        {"q": "how to prevent injuries", "gt": "how to prevent running injuries"},
        {"q": "post-run stretches", "gt": "best post-run stretches for runners"},
    ]
    for item in user_401_queries:
        all_queries.append({"user_id": 401, "context": {"interest": "running", "location": "Delhi"}, "current_query": item["q"], "ground_truth_rewrite": item["gt"]})

    # --- Persona 2: The E-commerce Shopper (User ID: 502) ---
    # Total: 11 Queries
    user_502_queries = [
        {"q": "new phone deals", "gt": "new Apple iPhone deals electronics"},
        {"q": "laptop reviews", "gt": "Apple MacBook reviews"},
        {"q": "customer service number", "gt": "Apple electronics customer service number"},
        {"q": "return policy", "gt": "Apple electronics return policy"},
        {"q": "watch accessories", "gt": "Apple Watch accessories"},
        {"q": "wireless earbuds", "gt": "Apple AirPods wireless earbuds"},
        {"q": "new macbook release date", "gt": "new Apple MacBook release date"},
        {"q": "iphone camera tips", "gt": "Apple iPhone camera tips"},
        {"q": "icloud storage options", "gt": "Apple iCloud storage options"},
        {"q": "trade-in value for old phone", "gt": "Apple trade-in value for old iPhone"},
        {"q": "best apps for ipad", "gt": "best productivity apps for Apple iPad"},
    ]
    for item in user_502_queries:
        all_queries.append({"user_id": 502, "context": {"brand_preference": "Apple", "category": "electronics"}, "current_query": item["q"], "ground_truth_rewrite": item["gt"]})

    # --- Persona 3: The DIY Home Cook (User ID: 603) ---
    # Total: 11 Queries
    user_603_queries = [
        {"q": "easy dinner recipes", "gt": "easy vegetarian Indian dinner recipes"},
        {"q": "how to make paneer", "gt": "how to make vegetarian paneer for Indian cooking"},
        {"q": "where to buy spices", "gt": "where to buy authentic Indian spices"},
        {"q": "kitchen gadgets", "gt": "best kitchen gadgets for Indian cooking"},
        {"q": "lentil soup recipe", "gt": "vegetarian Indian lentil soup (dal) recipe"},
        {"q": "festival sweets", "gt": "vegetarian Indian festival sweets recipes"},
        {"q": "how to make naan bread", "gt": "how to make vegetarian naan bread for Indian meals"},
        {"q": "spicy potato recipe", "gt": "spicy vegetarian Indian potato recipe"},
        {"q": "quick lunch ideas", "gt": "quick vegetarian Indian lunch ideas"},
        {"q": "what is garam masala", "gt": "what is garam masala in Indian cooking"},
        {"q": "healthy breakfast", "gt": "healthy vegetarian Indian breakfast recipes"},
    ]
    for item in user_603_queries:
        all_queries.append({"user_id": 603, "context": {"cuisine": "Indian", "diet": "vegetarian"}, "current_query": item["q"], "ground_truth_rewrite": item["gt"]})

    # --- Persona 4: The Machine Learning Student (User ID: 704) ---
    # Total: 11 Queries
    user_704_queries = [
        {"q": "what is a neural network", "gt": "what is a neural network in machine learning"},
        {"q": "how to implement a CNN", "gt": "how to implement a CNN in PyTorch"},
        {"q": "best online courses", "gt": "best online courses for PyTorch machine learning"},
        {"q": "dataset for image classification", "gt": "image classification dataset for machine learning"},
        {"q": "getting started guide", "gt": "PyTorch getting started guide for machine learning"},
        {"q": "what are transformers", "gt": "what are transformer models in machine learning"},
        {"q": "overfitting vs underfitting", "gt": "overfitting vs underfitting in machine learning"},
        {"q": "loss functions explained", "gt": "loss functions explained for PyTorch"},
        {"q": "what is a GAN", "gt": "what is a GAN in machine learning"},
        {"q": "PyTorch vs TensorFlow", "gt": "PyTorch vs TensorFlow for machine learning research"},
        {"q": "how to use tensorboard", "gt": "how to use tensorboard with PyTorch"},
    ]
    for item in user_704_queries:
        all_queries.append({"user_id": 704, "context": {"field": "machine learning", "library": "PyTorch"}, "current_query": item["q"], "ground_truth_rewrite": item["gt"]})

    # --- Persona 5: The Travel Blogger (User ID: 805) ---
    # Total: 11 Queries
    user_805_queries = [
        {"q": "visa requirements", "gt": "Thailand visa requirements for Indian citizens"},
        {"q": "best street food", "gt": "best street food in Bangkok"},
        {"q": "budget hotels", "gt": "budget hotels in Vietnam"},
        {"q": "backpacking itinerary", "gt": "backpacking itinerary for Southeast Asia"},
        {"q": "what to pack", "gt": "what to pack for Bali trip"},
        {"q": "how to start a blog", "gt": "how to start a travel blog"},
        {"q": "cheap flights to malaysia", "gt": "cheap flights from India to Malaysia"},
        {"q": "cultural etiquette", "gt": "cultural etiquette in Southeast Asia"},
        {"q": "best time to visit Cambodia", "gt": "best time to visit Cambodia from India"},
        {"q": "sim card for tourists", "gt": "best sim card for tourists in Southeast Asia"},
        {"q": "is singapore expensive", "gt": "is singapore expensive for tourists"},
    ]
    for item in user_805_queries:
        all_queries.append({"user_id": 805, "context": {"niche": "travel blogging", "focus": "Southeast Asia"}, "current_query": item["q"], "ground_truth_rewrite": item["gt"]})
    
    # --- Persona 6: The PC Gamer (User ID: 906) ---
    # Total: 11 Queries
    user_906_queries = [
        {"q": "new game releases", "gt": "new PC strategy game releases 2025"},
        {"q": "best gaming build", "gt": "best gaming PC build for strategy games"},
        {"q": "how to get better", "gt": "how to get better at Age of Empires IV"},
        {"q": "steam sale dates", "gt": "Steam summer sale 2025 dates"},
        {"q": "reviews for new game", "gt": "reviews for Frostpunk 2 on PC"},
        {"q": "esports tournaments", "gt": "strategy game esports tournaments schedule"},
        {"q": "best gaming mouse", "gt": "best gaming mouse for strategy games"},
        {"q": "what is a good GPU", "gt": "what is a good GPU for PC gaming"},
        {"q": "co-op games to play", "gt": "co-op PC strategy games to play"},
        {"q": "discord servers for gamers", "gt": "Discord servers for strategy gamers"},
        {"q": "how to reduce lag", "gt": "how to reduce lag in PC online games"},
    ]
    for item in user_906_queries:
        all_queries.append({"user_id": 906, "context": {"platform": "PC", "genre": "strategy games"}, "current_query": item["q"], "ground_truth_rewrite": item["gt"]})

    # --- Add back original personas to fill up to 100 ---
    # Total: 11 queries each
    all_queries.extend(all_queries[:34]) # Add 34 more queries to reach 100

    df = pd.DataFrame(all_queries)
    df['context'] = df['context'].apply(json.dumps)
    
    # Save to a new CSV file
    df.to_csv('data/100_synthetic_queries.csv', index=False)
    print(f"✅ 100-query synthetic dataset with {len(df)} queries generated.")
    print("Saved to data/100_synthetic_queries.csv")

if __name__ == "__main__":
    create_100_query_dataset()