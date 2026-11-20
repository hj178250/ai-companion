import streamlit as st

st.set_page_config(page_title="AI 伴侣", page_icon="🤖")
st.title("🤖 AI 伴侣")

st.session_state.setdefault("messages", [])

# 侧边栏：放"设置"
with st.sidebar:
    st.header("设置")
    model = st.selectbox("模型", ["gpt-4o", "gpt-4o-mini"])
    temperature = st.slider("温度", 0.0, 2.0, 1.0, 0.1)
    st.caption("温度越高回答越随机")

# 显示历史聊天记录
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 输入框 + 提交
user_input = st.chat_input("跟我说点什么...")

if user_input:
    # 1. 记录用户的话
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # 2. 生成回复（先写死，后面换成真大模型 API）
    reply = f"你说的是：{user_input}"
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
