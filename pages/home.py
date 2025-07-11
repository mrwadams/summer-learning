import streamlit as st

def home_page():
    # Hero section
    st.title("My Summer Learning Hub 🚀")
    
    # Welcome message in a nice container
    welcome_col1, welcome_col2 = st.columns([2, 1])
    
    with welcome_col1:
        st.markdown("""
        <div style='background-color: #EDE9FE; padding: 2rem; border-radius: 12px; margin-bottom: 2rem;'>
            <h2 style='color: #6366F1; margin-top: 0;'>Welcome to your personal space for fun learning!</h2>
            <p style='font-size: 1.1rem; color: #4B5563;'>
                This little hub has all the cool links and ideas your teachers suggested to help you get ready for the new school year. 
                Think of it as a launchpad for exploring new topics and strengthening your skills.
            </p>
            <p style='font-size: 1rem; color: #6B7280;'>
                Choose a subject from the sidebar on the left to get started. Let's make this a summer of discovery! ✨
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with welcome_col2:
        st.image("https://placehold.co/400x300/A7C7E7/FFFFFF?text=Let's+Explore!", use_container_width=True)
    
    # Quick stats or highlights
    st.markdown("### 📊 Your Learning Journey")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='background-color: #DBEAFE; padding: 1.5rem; border-radius: 8px; text-align: center;'>
            <h3 style='color: #1E40AF; margin: 0;'>🧮</h3>
            <h4 style='color: #1E40AF; margin: 0.5rem 0;'>Maths</h4>
            <p style='color: #3730A3; margin: 0;'>5 Topics Available</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background-color: #D1FAE5; padding: 1.5rem; border-radius: 8px; text-align: center;'>
            <h3 style='color: #065F46; margin: 0;'>🔬</h3>
            <h4 style='color: #065F46; margin: 0.5rem 0;'>Science</h4>
            <p style='color: #047857; margin: 0;'>3 Topics Available</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='background-color: #FEF3C7; padding: 1.5rem; border-radius: 8px; text-align: center;'>
            <h3 style='color: #92400E; margin: 0;'>✨</h3>
            <h4 style='color: #92400E; margin: 0.5rem 0;'>Extra Tools</h4>
            <p style='color: #B45309; margin: 0;'>2 Resources</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Tips section
    st.markdown("### 💡 Learning Tips")
    
    tips_col1, tips_col2 = st.columns(2)
    
    with tips_col1:
        st.info("""
        **📚 Study Smart**
        - Take regular breaks (every 25-30 minutes)
        - Mix different subjects throughout the day
        - Practice a little bit every day
        """)
    
    with tips_col2:
        st.success("""
        **🎯 Stay Motivated**
        - Set small, achievable goals
        - Reward yourself after completing tasks
        - Track your progress
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #6B7280; padding: 1rem;'>
        <p>Remember: Learning is an adventure! Take your time and enjoy the journey. 🌟</p>
    </div>
    """, unsafe_allow_html=True)