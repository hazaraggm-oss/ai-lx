import streamlit as st

# تنظیمات اصلی صفحه
st.set_page_config(
    page_title="AI LX - Future Assistant",
    page_icon="🚀",
    layout="centered"
)

# طراحی هدر سایت
st.markdown("<h1 style='text-align: center; color: #007bff;'>🚀 AI LX Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Welcome to the future of analysis. Ask AI LX anything!</p>", unsafe_allow_html=True)

st.write("---")

# کادر ورودی برای کاربر
user_query = st.text_input("What would you like AI LX to analyze for you?", placeholder="e.g. Digital Marketing in 2026")

if user_query:
    with st.spinner('AI LX is thinking...'):
        st.write("---")
        # نمایش نتیجه تحلیل
        st.info(f"🔍 **Topic:** {user_query}")
        
        # پاسخ هوشمند
        response = f"**AI LX Analysis:** The subject of '{user_query}' is projected to be a major breakthrough in 2026. Data suggests a significant shift towards AI integration in this field."
        
        st.success(response)
        
        # افکت بادکنک برای جذابیت
        st.balloons()

# پاورقی سایت
st.write("---")
st.caption("Powered by AI LX Technology | Afghanistan 2026")