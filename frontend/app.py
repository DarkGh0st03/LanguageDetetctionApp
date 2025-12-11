import streamlit as st
import requests
import os

# --- 1. Import Logic from External Files ---
# Questi file devono essere nella cartella /frontend insieme a app.py
from language_map import LABEL_TO_NAME
from dialect_map import DIALECT_TO_PARENT

# Configurable Backend URL (Default to local Docker network)
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

# --- 2. Configuration & Caching ---
st.set_page_config(
    page_title="Language Detector App",
    page_icon="🌍",
    layout="wide", # Use wide mode for a more modern look
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling (ESATTAMENTE COME IL TUO ORIGINALE)
st.markdown("""
<style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
    }
    .result-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #f0f2f6;
        border-left: 5px solid #4CAF50;
        margin-top: 20px;
    }
    .info-text {
        font-size: 14px;
        color: #555;
    }
</style>
""", unsafe_allow_html=True)

# NOTA: Ho rimosso la funzione load_model() perché ora il modello è nel backend

# --- 3. Sidebar UI (ESATTAMENTE COME IL TUO ORIGINALE) ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/language.png", width=80)
    st.title("About")
    st.info(
        """
        This AI-powered app detects the language of any text you enter.
        
        **Model:** Naive Bayes (91% Accuracy)
        **Dataset:** WiLi-2018
        **Features:** Smart Dialect Grouping
        """
    )
    st.markdown("---")
    st.markdown("### How to use")
    st.markdown("1. Paste text in the main area.")
    st.markdown("2. Click **'Detect Language'**.")
    st.markdown("3. View the prediction.")

# --- 4. Main UI (ESATTAMENTE COME IL TUO ORIGINALE) ---
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.title("🌍 Language Detector App")
    st.markdown("#### Instant language identification powered by Machine Learning")
    
    st.write("") # Spacer

    user_text = st.text_area("✍️ Enter your text here:", "", height=200, placeholder="Type or paste text (e.g., 'Bonjour le monde', 'Ciao come stai?')...")

    if st.button("🔍 Detect Language", use_container_width=True, type="primary"):
        if user_text.strip():
            try:
                with st.spinner('Analyzing text pattern...'):
                    # --- CORE LOGIC (MODIFICATA PER MICROSERVIZI) ---
                    
                    # Invece di model.predict, chiamiamo il Backend
                    payload = {"text": user_text}
                    # FIX: Added timeout=10 to prevent indefinite hanging (DoS mitigation)
                    response = requests.post(f"{BACKEND_URL}/predict", json=payload, timeout=10)
                    
                    if response.status_code == 200:
                        # 1. Get Raw Prediction from API
                        data = response.json()
                        prediction_code = data["language_code"]
                        
                        # 2. Apply Dialect Grouping (Logic remains in Frontend)
                        final_code = DIALECT_TO_PARENT.get(prediction_code, prediction_code)

                        # 3. Get Full Name
                        final_name = LABEL_TO_NAME.get(final_code, final_code)

                        # 4. Display Result (TUO STILE ORIGINALE)
                        st.markdown(f"""
                        <div class="result-box">
                            <h2 style='color: #2E7D32; margin:0;'>Detected Language: {final_name}</h2>
                            <p style='color: #555; margin-top:5px;'>ISO Code: <code>{final_code}</code></p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Bonus: Show dialect info if re-routing happened
                        if final_code != prediction_code:
                            original_name = LABEL_TO_NAME.get(prediction_code, prediction_code)
                            st.info(f"ℹ️ **Note:** The model detected specific features of **{original_name}** ({prediction_code}), which has been grouped under **{final_name}**.")
                    
                    else:
                        st.error(f"⚠️ Backend Error ({response.status_code}): {response.text}")

            except Exception as e:
                st.error(f"⚠️ Connection Error: Is the backend running? {e}")
        else:
            st.warning("⚠️ Please enter some text to analyze.")

    st.markdown("---")
    st.markdown("<div style='text-align: center; color: #888;'>Powered by Streamlit & Scikit-learn</div>", unsafe_allow_html=True)