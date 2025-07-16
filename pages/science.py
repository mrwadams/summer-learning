import streamlit as st

def science_page():
    st.title("🔬 Science Lab")
    
    # Header with engaging message
    st.markdown("""
    <div style='background-color: #D1FAE5; padding: 1.5rem; border-radius: 12px; margin-bottom: 2rem;'>
        <h3 style='color: #065F46; margin-top: 0;'>Time to explore the world around us!</h3>
        <p style='color: #047857; margin: 0;'>
            Here are some fascinating topics you've covered. Click on one to dive deeper and do some cool research.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Fun fact of the day
    st.markdown("### 💡 Did You Know?")
    fun_facts = [
        "The Earth rotates at about 1,000 miles per hour at the equator!",
        "There are more stars in the universe than grains of sand on all of Earth's beaches!",
        "A pulley system can help you lift objects that are much heavier than you!",
        "The Moon appears to change shape because of how sunlight hits it as it orbits Earth!",
        "Some animals have evolved to live in the deepest, darkest parts of the ocean!"
    ]
    st.info(f"🌟 {fun_facts[0]}")  # You could randomize this
    
    st.markdown("---")
    
    # Topics section
    st.markdown("## 🔍 Topics to Explore")
    
    # Forces
    with st.expander("⚡ Forces", expanded=False):
        st.markdown("#### Contact vs. Non-Contact Forces, Levers, Pulleys, and Gears")
        
        # Visual distinction between force types
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style='background-color: #FEE2E2; padding: 1rem; border-radius: 8px;'>
                <h4 style='color: #991B1B; margin-top: 0;'>👋 Contact Forces</h4>
                <p style='color: #7F1D1D; font-size: 0.9rem;'>
                    Forces that require physical contact:
                    • Friction
                    • Push/Pull
                    • Tension
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style='background-color: #E0E7FF; padding: 1rem; border-radius: 8px;'>
                <h4 style='color: #3730A3; margin-top: 0;'>🌐 Non-Contact Forces</h4>
                <p style='color: #312E81; font-size: 0.9rem;'>
                    Forces that work at a distance:
                    • Gravity
                    • Magnetism
                    • Static electricity
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("#### 🔧 Simple Machines")
        st.markdown("""
        **Explore these questions:**
        - How do levers help us lift heavy objects?
        - Can you find examples of pulleys in your home?
        - Where might you see gears working together?
        """)
        
        # Resources in tabs
        tab1, tab2 = st.tabs(["📚 Websites", "🎥 Videos"])
        
        with tab1:
            st.markdown("""
            - [BBC Bitesize: Forces](https://www.bbc.co.uk/bitesize/topics/znmmn39)
            - [BBC Bitesize: Levers, Pulleys and Gears](https://www.bbc.co.uk/bitesize/topics/zvr3nrd)
            """)
        
        with tab2:
            st.markdown("""
            - [YouTube: Contact and Non-Contact Forces](https://www.youtube.com/watch?v=LIwqZQOnMKc)
            - [YouTube: Introduction to Forces](https://www.youtube.com/watch?v=XAJUzs46nJQ)
            """)
    
    # Earth and Space
    with st.expander("🌍 Earth and Space", expanded=False):
        st.markdown("#### Planets, Day & Night, and Phases of the Moon")
        
        # Interactive challenge
        st.success("🚀 **Space Challenge**: Can you name all 8 planets in order from the Sun?")
        
        # Space facts grid
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style='background-color: #FEF3C7; padding: 1rem; border-radius: 8px; text-align: center;'>
                <h3 style='margin: 0;'>☀️</h3>
                <p style='color: #78350F; font-weight: bold; margin: 0.5rem 0;'>Day & Night</p>
                <p style='color: #92400E; font-size: 0.85rem; margin: 0;'>Earth rotates once every 24 hours</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style='background-color: #E0E7FF; padding: 1rem; border-radius: 8px; text-align: center;'>
                <h3 style='margin: 0;'>🌙</h3>
                <p style='color: #312E81; font-weight: bold; margin: 0.5rem 0;'>Moon Phases</p>
                <p style='color: #3730A3; font-size: 0.85rem; margin: 0;'>8 phases in ~29.5 days</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style='background-color: #F3E8FF; padding: 1rem; border-radius: 8px; text-align: center;'>
                <h3 style='margin: 0;'>🪐</h3>
                <p style='color: #581C87; font-weight: bold; margin: 0.5rem 0;'>Solar System</p>
                <p style='color: #6B21A8; font-size: 0.85rem; margin: 0;'>8 planets orbiting the Sun</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("#### 🔭 Things to Investigate")
        st.markdown("""
        - What causes day and night? (Hint: Think about Earth's rotation)
        - Why does the Moon appear to change shape?
        - What's the difference between a comet, asteroid, and meteor?
        """)
        
        # Resources
        tab1, tab2 = st.tabs(["📚 Websites", "🎥 Videos"])
        
        with tab1:
            st.markdown("[BBC Bitesize: Earth and Space](https://www.bbc.co.uk/bitesize/topics/zkbbkqt)")
        
        with tab2:
            st.markdown("""
            - [YouTube: The Solar System](https://www.youtube.com/watch?v=ErUZVWUP0c4)
            - [YouTube: Day and Night](https://www.youtube.com/watch?v=l64YwNl1wr0)
            - [YouTube: Phases of the Moon](https://www.youtube.com/watch?v=f4ZHdzl6ZWg)
            """)
    
    # Evolution and Inheritance
    with st.expander("🦎 Evolution and Inheritance", expanded=False):
        st.markdown("#### Classification and Evolution")
        
        # Activity box
        st.markdown("""
        <div style='background-color: #EDE9FE; padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;'>
            <h4 style='color: #6366F1; margin-top: 0;'>🐾 Your Pet Research Project</h4>
            <p style='color: #7C3AED; margin-bottom: 1rem;'>
                Pick your favourite animal (it could even be your pet!) and become a scientist:
            </p>
            <ol style='color: #7C3AED;'>
                <li><strong>Classification Quest</strong>: Find its Kingdom, Phylum, Class, Order, Family, Genus, and Species</li>
                <li><strong>Evolution Detective</strong>: Discover how this species has evolved over time</li>
                <li><strong>Adaptation Explorer</strong>: What special features help it survive?</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
        
        # Classification helper
        st.info("""
        💡 **Classification Tip**: Remember "King Philip Came Over For Good Soup"
        (Kingdom, Phylum, Class, Order, Family, Genus, Species)
        """)
        
        # Resources
        tab1, tab2 = st.tabs(["📚 Websites", "🎥 Videos"])
        
        with tab1:
            st.markdown("""
            - [BBC Bitesize: Classification](https://www.bbc.co.uk/bitesize/articles/z3nbcwx)
            - [BBC Bitesize: Evolution](https://www.bbc.co.uk/bitesize/articles/zyxtm39)
            """)
        
        with tab2:
            st.markdown("""
            - [YouTube: Classification](https://www.youtube.com/watch?v=ITrRMiQB8g4)
            - [YouTube: Evolution](https://www.youtube.com/watch?v=pktDqFy5IcE)
            """)
    
    # Science experiment suggestion
    st.markdown("---")
    st.markdown("### 🧪 Try This at Home!")
    
    experiment_col1, experiment_col2 = st.columns([2, 1])
    
    with experiment_col1:
        st.markdown("""
        <div style='background-color: #FEF3C7; padding: 1.5rem; border-radius: 12px;'>
            <h4 style='color: #78350F; margin-top: 0;'>Simple Pulley Experiment</h4>
            <p style='color: #92400E;'>
                <strong>You'll need:</strong> String, a pencil, and a small weight (like a toy)
            </p>
            <p style='color: #92400E;'>
                <strong>Try this:</strong> Tie the string to the weight, loop it over the pencil, and pull down. 
                Notice how the direction of force changes? That's a simple pulley in action!
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with experiment_col2:
        st.image("images/pulley.jpg", use_container_width=True, caption="Simple Pulley System")
    
    # Footer
    st.markdown("""
    <div style='background-color: #F3F4F6; padding: 2rem; border-radius: 12px; text-align: center; margin-top: 2rem;'>
        <h3 style='color: #4B5563; margin-top: 0;'>🔬 Keep Exploring!</h3>
        <p style='color: #6B7280;'>Science is all about asking questions and finding answers. Stay curious!</p>
    </div>
    """, unsafe_allow_html=True)