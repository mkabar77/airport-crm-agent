import streamlit as st
from agent.crm_agent import AirportCRMAgent
import os

# Page configuration
st.set_page_config(
    page_title="Airport CRM AI Agent",
    page_icon="✈️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='main-header'>✈️ Airport CRM AI Agent</h1>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")
    
    api_provider = st.radio("API Provider", ["OpenAI", "Anthropic (Claude)"])
    
    api_key = st.text_input(f"{api_provider} API Key", type="password", 
                            help=f"Enter your {api_provider} API key")
    
    if api_provider == "OpenAI":
        model_choice = st.selectbox("Model", ["gpt-4-turbo-preview", "gpt-3.5-turbo"])
    else:
        model_choice = st.selectbox("Model", ["claude-sonnet-4-5-20250929", "claude-haiku-4-5-20251001"])
    
    st.markdown("---")
    st.subheader("📋 Quick Info")
    st.info("""
    **Demo Data Available:**
    - Email: john.smith@email.com
    - Booking: BK001
    - Flight: AA101
    
    **Try asking:**
    - "Check my booking BK001"
    - "What's the status of flight AA101?"
    - "I need wheelchair assistance"
    - "What's my frequent flyer status for john.smith@email.com?"
    """)
    
    if st.button("🔄 Reset Conversation"):
        st.session_state.messages = []
        if 'agent' in st.session_state:
            st.session_state.agent.reset_conversation()
        st.rerun()

# Initialize agent
if 'agent' not in st.session_state and api_key:
    st.session_state.agent = AirportCRMAgent(api_key, model_choice, api_provider.lower())

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("How can I help you today?"):
    if not api_key:
        st.error(f"Please enter your {api_provider} API key in the sidebar.")
    else:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get agent response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.agent.chat(prompt)
                st.markdown(response)
        
        # Add assistant message
        st.session_state.messages.append({"role": "assistant", "content": response})

# Footer
st.markdown("---")
st.caption("Airport CRM AI Agent Demo | Built with LangChain & Streamlit")
