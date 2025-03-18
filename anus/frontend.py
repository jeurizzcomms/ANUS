import streamlit as st
import os
from anus.core.orchestrator import AgentOrchestrator

def main():
    # Configuratie van de pagina
    st.set_page_config(
        page_title="ANUS - Autonomous Networked Utility System",
        page_icon="🤖",
        layout="centered"
    )

    # Custom CSS voor Stripe-achtige styling
    st.markdown("""
    <style>
        .stTextInput > div > div > input {
            background-color: #f6f9fc;
            border: 1px solid #e3e8ee;
            border-radius: 4px;
            padding: 12px;
            font-size: 16px;
        }
        .stButton > button {
            background-color: #635bff;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 12px 24px;
            font-weight: 600;
        }
        .stButton > button:hover {
            background-color: #5851db;
        }
        .output-container {
            background-color: #f6f9fc;
            border: 1px solid #e3e8ee;
            border-radius: 4px;
            padding: 20px;
            margin: 20px 0;
        }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.title("ANUS AI")
    st.subheader("Autonomous Networked Utility System")

    # Initialiseer sessie state
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Initialiseer de orchestrator
    @st.cache_resource
    def get_orchestrator():
        return AgentOrchestrator()

    orchestrator = get_orchestrator()

    # Chat interface
    st.markdown("### Chat met ANUS")

    # Toon chat geschiedenis
    for message in st.session_state.chat_history:
        with st.container():
            if message["role"] == "user":
                st.markdown(f"**You:** {message['content']}")
            else:
                st.markdown(f"**ANUS:** {message['content']}")

    # Input veld
    with st.form(key="chat_form"):
        user_input = st.text_area("Typ je vraag of opdracht:", height=100)
        mode = st.selectbox("Mode:", ["single", "multi"], index=0)
        submit_button = st.form_submit_button("Verstuur")

        if submit_button and user_input:
            # Voeg user input toe aan geschiedenis
            st.session_state.chat_history.append({
                "role": "user",
                "content": user_input
            })
            
            # Verwerk de vraag
            with st.spinner("ANUS denkt na..."):
                try:
                    result = orchestrator.execute_task(user_input, mode=mode)
                    
                    # Voeg antwoord toe aan geschiedenis
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": result
                    })
                    
                    # Toon het nieuwe antwoord
                    st.markdown(f"**ANUS:** {result}")
                except Exception as e:
                    st.error(f"Er is een fout opgetreden: {str(e)}")

    # Footer
    st.markdown("---")
    st.markdown(
        "ANUS is een AI framework dat gebruik maakt van geavanceerde technieken "
        "om je te helpen met diverse taken. Gebruik de chat hierboven om vragen "
        "te stellen of opdrachten te geven."
    )

if __name__ == "__main__":
    main() 