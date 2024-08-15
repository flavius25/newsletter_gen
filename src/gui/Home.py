import streamlit as st

def main():
    st.set_page_config(page_title="Landing Page", page_icon="🏠")
    
    # Custom CSS for navigation bar
    st.markdown("""
        <style>
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #333;
            overflow: hidden;
        }
        .navbar a {
            float: left;
            color: #f2f2f2;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
            font-size: 17px;
        }
        .navbar a:hover {
            background-color: #ddd;
            color: black;
        }
        </style>
        
        <div class="navbar">
            <a href="javascript:void(0);" onclick="parent.window.location.href='app'">Go to App</a>
        </div>
        """, unsafe_allow_html=True)
    
    st.title("Multiple-AI agents at work")
    
    st.write("Choose your feature: ")
    # Navigation button
    if st.button("Generate a newsletter"):
        st.switch_page("pages/app.py")
    if st.button("Email AI Assistant"):
        st.switch_page("Home.py")
        # st.switch_page("pages/app.py")

if __name__ == "__main__":
    main()