import streamlit as st
from agent import chat
from db import init_db

init_db()

st.set_page_config(
    page_title="Research AI Assistant",
    page_icon="🧠",
    layout="wide"
)

# ---------- STYLE ----------
st.markdown("""
<style>
body {background-color:#f5f7fb;}
.chatbox{
    padding:15px;
    border-radius:15px;
    margin-bottom:10px;
}
.user{
    background:#808080;
}
.bot{
    background:#A52A2A;
}
</style>
""",unsafe_allow_html=True)

# ---------- TITLE ----------
st.title("🧠 Research AI Assistant")
st.caption("Reliable AI Research Companion")

# ---------- SESSION ----------
if "messages" not in st.session_state:
    st.session_state.messages=[]

# ---------- DISPLAY ----------
for m in st.session_state.messages:
    css="user" if m["role"]=="user" else "bot"
    st.markdown(
        f"<div class='chatbox {css}'>{m['content']}</div>",
        unsafe_allow_html=True
    )

# ---------- INPUT ----------
prompt = st.chat_input("Ask research question...")

if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})

    reply = chat(prompt)

    st.session_state.messages.append({"role":"assistant","content":reply})

    st.rerun()
