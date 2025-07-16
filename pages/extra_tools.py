import streamlit as st

def extra_tools_page():
    st.title("✨ Extra Tools")
    
    # Header
    st.markdown("""
    <div style='background-color: #FEF3C7; padding: 1.5rem; border-radius: 12px; margin-bottom: 2rem;'>
        <h3 style='color: #78350F; margin-top: 0;'>Other cool resources to check out!</h3>
        <p style='color: #92400E; margin: 0;'>
            Your school provides access to these amazing learning platforms. Use your school login to explore!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Resources grid
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='background-color: #DBEAFE; padding: 2rem; border-radius: 12px; margin-bottom: 1rem;'>
            <h2 style='color: #1E40AF; margin-top: 0;'>📺 ClickView</h2>
            <p style='color: #3730A3; margin-bottom: 1.5rem;'>
                Your school subscribes to ClickView, which has tons of great educational videos on almost any subject.
            </p>
            <p style='color: #1E40AF; font-weight: bold; margin-bottom: 1rem;'>
                ✅ Log in with your school email
            </p>
            <p style='color: #3730A3; margin-bottom: 0;'>
                Perfect for visual learners who love watching videos to understand concepts better!
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### [🔗 Go to ClickView](https://www.clickview.co.uk/)")
    
    with col2:
        st.markdown("""
        <div style='background-color: #E9D5FF; padding: 2rem; border-radius: 12px; margin-bottom: 1rem;'>
            <h2 style='color: #6B21A8; margin-top: 0;'>✏️ Spellzone</h2>
            <p style='color: #7C3AED; margin-bottom: 1.5rem;'>
                A great tool for practicing your spellings and becoming a spelling champion!
            </p>
            <p style='color: #6B21A8; font-weight: bold; margin-bottom: 1rem;'>
                🏆 Features games and challenges
            </p>
            <p style='color: #7C3AED; margin-bottom: 0;'>
                Practice tricky words, learn spelling rules, and track your progress over time.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### [🔗 Go to Spellzone](https://www.spellzone.com/)")
    
    with col3:
        st.markdown("""
        <div style='background-color: #D1FAE5; padding: 2rem; border-radius: 12px; margin-bottom: 1rem;'>
            <h2 style='color: #065F46; margin-top: 0;'>🦉 Duolingo</h2>
            <p style='color: #047857; margin-bottom: 1.5rem;'>
                We have a family subscription! Learn new languages with fun, bite-sized lessons and games.
            </p>
            <p style='color: #065F46; font-weight: bold; margin-bottom: 1rem;'>
                🌍 Learn Spanish, French, or any language!
            </p>
            <p style='color: #047857; margin-bottom: 0;'>
                Just 5-10 minutes a day can help you become fluent in a new language!
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### [🔗 Go to Duolingo](https://www.duolingo.com/)")
    
    # Tips for using the resources
    st.markdown("---")
    st.markdown("### 💡 How to Make the Most of These Tools")
    
    tips_col1, tips_col2, tips_col3 = st.columns(3)
    
    with tips_col1:
        st.info("""
        **📅 Set a Schedule**
        Try to use one of these tools for 15-20 minutes each day
        """)
    
    with tips_col2:
        st.success("""
        **🎯 Track Progress**
        Many of these tools show your improvement over time
        """)
    
    with tips_col3:
        st.warning("""
        **🔐 Keep Login Safe**
        Remember to keep your school login details secure
        """)
    
    # Additional resources section
    st.markdown("---")
    st.markdown("### 🌟 Looking for More?")
    
    st.markdown("""
    <div style='background-color: #F3F4F6; padding: 2rem; border-radius: 12px;'>
        <h4 style='color: #4B5563; margin-top: 0;'>Other Great Learning Websites</h4>
        <p style='color: #6B7280; margin-bottom: 1rem;'>
            While these aren't provided by your school, they're still fantastic free resources:
        </p>
        <ul style='color: #6B7280;'>
            <li><strong>Khan Academy</strong> - Free courses on maths, science, and more</li>
            <li><strong>Scratch</strong> - Learn coding by creating games and animations</li>
            <li><strong>National Geographic Kids</strong> - Explore the world and learn about nature</li>
        </ul>
        <p style='color: #9CA3AF; font-style: italic; margin-top: 1rem; margin-bottom: 0;'>
            💡 Always ask a parent or guardian before signing up for new websites!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Fun challenge
    st.markdown("---")
    st.markdown("### 🎮 Weekly Challenge")
    
    challenge_col1, challenge_col2 = st.columns([3, 1])
    
    with challenge_col1:
        st.markdown("""
        <div style='background-color: #D1FAE5; padding: 1.5rem; border-radius: 12px;'>
            <h4 style='color: #065F46; margin-top: 0;'>This Week's Challenge</h4>
            <p style='color: #047857;'>
                <strong>Spelling Bee Champion:</strong> Can you get a perfect score on 5 Spellzone activities in a row?
            </p>
            <p style='color: #065F46; font-size: 0.9rem; margin-bottom: 0;'>
                Complete the challenge and treat yourself to something special! 🏆
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with challenge_col2:
        st.markdown("""
        <div style='text-align: center; padding-top: 2rem;'>
            <h1 style='font-size: 3rem; margin: 0;'>🏆</h1>
        </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div style='background-color: #F9FAFB; padding: 2rem; border-radius: 12px; text-align: center; margin-top: 2rem;'>
        <p style='color: #6B7280; margin: 0;'>
            Remember: These tools are here to help you learn and have fun. Explore at your own pace! 🚀
        </p>
    </div>
    """, unsafe_allow_html=True)