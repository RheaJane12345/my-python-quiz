import streamlit as st

st.set_page_config(page_title="Step-by-Step Elite Quiz", page_icon="🧠")

# --- QUIZ DATA ---
# Using a list of dictionaries to store questions, options, answers, and reasons
quiz_data = [
    {
        "question": "What is the only metal that is liquid at room temperature?",
        "options": ["Gallium", "Mercury", "Bromine", "Cesium"],
        "answer": "Mercury",
        "reason": "Mercury has a very low melting point (-38.8°C) due to its unique electronic structure."
    },
    {
        "question": "Which country has the most natural lakes in the world?",
        "options": ["USA", "Russia", "Canada", "Finland"],
        "answer": "Canada",
        "reason": "Canada contains over 2 million lakes, accounting for about 60% of the world's total!"
    },
    {
        "question": "How many hearts does an octopus have?",
        "options": ["1", "2", "3", "8"],
        "answer": "3",
        "reason": "Two hearts pump blood to the gills, while the third pumps it to the rest of the body."
    }
    # You can add the other 7 questions here following this same format!
]

# --- INITIALIZE SESSION STATE ---
if 'q_idx' not in st.session_state:
    st.session_state.q_idx = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False

# --- QUIZ LOGIC ---
st.title("🧠 One-by-One Elite Challenge")

if st.session_state.q_idx < len(quiz_data):
    item = quiz_data[st.session_state.q_idx]
    
    st.subheader(f"Question {st.session_state.q_idx + 1} of {len(quiz_data)}")
    st.write(item["question"])
    
    # Show options
    choice = st.radio("Choose your answer:", item["options"], key=f"q_{st.session_state.q_idx}")

    # Submit Answer Button
    if not st.session_state.answered:
        if st.button("Check Answer"):
            st.session_state.answered = True
            st.rerun()

    # Show result and explanation after clicking
    if st.session_state.answered:
        if choice == item["answer"]:
            st.success(f"✅ Correct!")
            # Increase score only once
            if 'last_scored_idx' not in st.session_state or st.session_state.last_scored_idx < st.session_state.q_idx:
                st.session_state.score += 1
                st.session_state.last_scored_idx = st.session_state.q_idx
        else:
            st.error(f"❌ Wrong! The correct answer was {item['answer']}.")
        
        st.info(f"**Explanation:** {item['reason']}")

        # Next Question Button
        if st.button("Next Question →"):
            st.session_state.q_idx += 1
            st.session_state.answered = False
            st.rerun()

else:
    # --- FINAL SCORE ---
    st.balloons()
    st.header("🎊 Quiz Finished!")
    st.write(f"Your final score is {st.session_state.score} out of {len(quiz_data)}.")
    
    if st.button("Restart Quiz"):
        st.session_state.q_idx = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.rerun()