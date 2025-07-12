import streamlit as st

def maths_page():
    st.title("🧮 Maths Zone")
    
    # Header with motivational message
    st.markdown("""
    <div style='background-color: #DBEAFE; padding: 1.5rem; border-radius: 12px; margin-bottom: 2rem;'>
        <h3 style='color: #1E40AF; margin-top: 0;'>Let's have some fun with numbers!</h3>
        <p style='color: #3730A3; margin: 0;'>
            Here are some topics to explore. Click on any of them to see activities and helpful links.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    
    # Topics section
    st.markdown("## 📚 Topics to Explore")
    
    # Area and Perimeter
    with st.expander("📐 Area and Perimeter", expanded=False):
        tab1, tab2 = st.tabs(["🎯 Activities", "📖 Resources"])
        
        with tab1:
            st.markdown("#### Shapes with missing lengths")
            st.markdown("""
            **🏗️ Hands-on Activities:**
            - **Build & Measure**: Create different shapes using LEGO, string, or straws and measure them
            - **Calculate**: Once you've made a shape, calculate its area and perimeter
            - **Room Designer**: Plan a new layout for your bedroom! Draw the room and furniture, then describe movements (e.g., 'move the bed 3 units right')
            """)
            
            # Interactive tip
            st.info("💡 **Pro Tip**: Start with simple rectangles and squares, then try more complex shapes!")
        
        with tab2:
            st.markdown("#### 📚 Helpful Resources")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**📏 Perimeter**")
                st.markdown("[BBC Bitesize: Calculating Perimeter](https://www.bbc.co.uk/bitesize/articles/zj6ff82)")
            with col2:
                st.markdown("**➡️ Translation**")
                st.markdown("[BBC Bitesize: Translation](https://www.bbc.co.uk/bitesize/articles/zk7dg7h#z6fxfdm)")
    
    # Working with Decimals
    with st.expander("🔢 Working with Decimals", expanded=False):
        tab1, tab2 = st.tabs(["🎯 Activities", "📖 Resources"])
        
        with tab1:
            st.markdown("#### Adding, subtracting, and ordering decimals")
            st.markdown("""
            **💰 Real-world Practice:**
            - **Shopping Challenge**: Add up prices of items when you're at the shops
            - **Day Out Planning**: Plan a fun day and calculate the total cost
            - **Change Calculator**: Practice calculating change after purchases
            - **Home Shop**: Set up a pretend shop at home and be the shopkeeper!
            """)
            
            # Challenge box
            st.success("🎮 **Challenge**: Can you add up 5 items and calculate the change from £20?")
        
        with tab2:
            st.markdown("#### 📚 Helpful Resources")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**🔄 Comparing Decimals**")
                st.markdown("[BBC Bitesize: Comparing and Ordering](https://www.bbc.co.uk/bitesize/articles/zgn7wnb)")
            with col2:
                st.markdown("**➕➖ Add & Subtract**")
                st.markdown("[BBC Bitesize: Decimal Operations](https://www.bbc.co.uk/bitesize/articles/zk9bg7h)")
    
    # Multiplication
    with st.expander("✖️ Multiplying 2-digit by 2-digit numbers", expanded=False):
        st.markdown("#### Three key methods to master!")
        st.warning("🎯 Your school uses these three methods. Getting comfortable with them will be a superpower!")
        
        # Method cards
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style='background-color: #FEE2E2; padding: 1rem; border-radius: 8px;'>
                <h4 style='color: #991B1B; margin-top: 0;'>1️⃣ Partitioning</h4>
                <p style='color: #7F1D1D; font-size: 0.9rem;'>Break numbers into parts</p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("[Learn Partitioning →](https://www.bbc.co.uk/bitesize/articles/zyk8pbk)")
        
        with col2:
            st.markdown("""
            <div style='background-color: #FEFCE8; padding: 1rem; border-radius: 8px;'>
                <h4 style='color: #713F12; margin-top: 0;'>2️⃣ Grid Method</h4>
                <p style='color: #854D0E; font-size: 0.9rem;'>Use area model</p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("[Learn Grid Method →](https://www.bbc.co.uk/bitesize/guides/zkqf6g8/revision/2)")
        
        with col3:
            st.markdown("""
            <div style='background-color: #F0FDF4; padding: 1rem; border-radius: 8px;'>
                <h4 style='color: #14532D; margin-top: 0;'>3️⃣ Long Multiplication</h4>
                <p style='color: #166534; font-size: 0.9rem;'>Formal written method</p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("[Learn Long Multiplication →](https://www.bbc.co.uk/bitesize/articles/z4chnrd)")
    
    # Time Calculations
    with st.expander("⏰ Calculating with Time", expanded=False):
        tab1, tab2 = st.tabs(["🎯 Activities", "📖 Resources"])
        
        with tab1:
            st.markdown("#### Finding durations of time")
            st.markdown("""
            **🕐 Time Activities:**
            - **Cooking Planner**: Plan a meal, calculate cooking times and when to start each part
            - **TV Guide Explorer**: Calculate the duration of your favourite shows
            - **Daily Schedule**: Create a schedule for your perfect day with time durations
            """)
            
            # Example problem
            st.info("📝 **Try This**: If a cake takes 45 minutes to bake and needs 20 minutes to cool, what time should you start if you want it ready by 3:00 PM?")
        
        with tab2:
            st.markdown("#### 📚 Helpful Resources")
            st.markdown("[BBC Bitesize: Finding Durations of Time](https://www.bbc.co.uk/bitesize/articles/zpxbydm)")
    
    # Times Tables
    with st.expander("🎲 Times Tables Fun", expanded=False):
        st.markdown("#### Learn your square numbers and practice all your tables!")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.success("🎯 **Goal**: Learn all square numbers up to 15×15!")
            st.markdown("""
            Knowing your times tables makes everything in maths easier. Here's why square numbers are special:
            - 1² = 1
            - 2² = 4
            - 3² = 9
            - ...and so on!
            """)
        
        with col2:
            st.markdown("""
            <div style='background-color: #EDE9FE; padding: 1.5rem; border-radius: 8px; text-align: center;'>
                <h2 style='color: #6366F1; margin: 0;'>15²</h2>
                <h3 style='color: #7C3AED; margin: 0;'>= 225</h3>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("#### 🎮 Practice Games")
        st.markdown("[Times Tables Games: Learn them all here! →](https://www.timestables.co.uk/)")
    
    # Footer with encouragement
    st.markdown("---")
    st.balloons()
    st.markdown("""
    <div style='background-color: #F3F4F6; padding: 2rem; border-radius: 12px; text-align: center; margin-top: 2rem;'>
        <h3 style='color: #4B5563; margin-top: 0;'>🌟 You're Doing Amazing!</h3>
        <p style='color: #6B7280;'>Remember: Every expert was once a beginner. Keep practicing and you'll see improvement!</p>
    </div>
    """, unsafe_allow_html=True)