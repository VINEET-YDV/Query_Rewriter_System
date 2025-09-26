import streamlit as st
# Import the rewriter function and the user profiles from our src folder
from src.rewriter import rewrite_query_for_user, USER_TOPICS

# --- App UI Configuration ---
st.set_page_config(
    page_title="Personalized Query Rewriter",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Personalized Query Rewriter")
st.markdown("""
This app demonstrates how a user's context can be used to rewrite their search query, 
making it more specific and relevant to their needs.
""")

st.divider()

# --- Interactive Demo ---

# 1. User Selection
st.subheader("1. Select a User Persona")

# Get user IDs from our USER_TOPICS dictionary to create the dropdown
user_ids = list(USER_TOPICS.keys())
selected_id = st.selectbox(
    "Choose a user to see their profile and test the rewriter:",
    options=user_ids,
    format_func=lambda uid: f"User ID: {uid}" # Nicer formatting for the dropdown
)

# Display the context for the selected user to explain the personalization
if selected_id:
    st.info(f"**User Context:** This user's primary topic is `{USER_TOPICS[selected_id]['main_topic']}`. Their modifier is `{USER_TOPICS[selected_id]['modifier']}`.")

# 2. Query Input
st.subheader("2. Enter a Query")
query_input = st.text_input(
    "Enter a generic search query:",
    placeholder="e.g., 'how to get started' or 'best places to visit'"
)

# 3. Rewrite and Display
if st.button("Rewrite Query", type="primary"):
    if query_input:
        # Call our backend function
        rewritten_query = rewrite_query_for_user(selected_id, query_input)
        
        st.subheader("✨ Results")
        
        # --- THIS IS THE UPDATED SECTION ---
        # We replace st.metric with st.markdown for better text display.
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Original Query**")
            st.info(query_input) # Using st.info or st.code gives it a nice box
        with col2:
            st.markdown("**Personalized Query**")
            st.info(rewritten_query)
            
        st.success("Query rewritten successfully based on the user's profile!")
    else:
        st.warning("Please enter a query to rewrite.")