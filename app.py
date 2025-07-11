import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Summer Learning Hub",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
/* Custom color scheme */
:root {
    --primary-color: #6366F1;
    --secondary-color: #A78BFA;
    --background-color: #F9FAFB;
    --text-color: #1F2937;
}

/* Sidebar styling */
.css-1d391kg {
    background-color: #F3F4F6;
}

/* Main content area */
.main {
    padding: 2rem;
}

/* Custom headers */
h1 {
    color: var(--primary-color);
    font-weight: 700;
    margin-bottom: 1rem;
}

h2 {
    color: var(--text-color);
    font-weight: 600;
    margin-top: 1.5rem;
}

/* Expander styling */
.streamlit-expanderHeader {
    background-color: #EDE9FE;
    border-radius: 8px;
    font-weight: 600;
}

/* Links */
a {
    color: var(--primary-color);
    text-decoration: none;
}

a:hover {
    color: var(--secondary-color);
    text-decoration: underline;
}

/* Cards */
.stExpander {
    border: 1px solid #E5E7EB;
    border-radius: 8px;
    margin-bottom: 1rem;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

/* Navigation */
[data-testid="stSidebarNav"] {
    padding-top: 2rem;
}

[data-testid="stSidebarNav"] > div {
    padding: 0.5rem 1rem;
}

[data-testid="stSidebarNav"] a {
    color: var(--text-color);
    font-weight: 500;
    border-radius: 8px;
    transition: all 0.3s ease;
}

[data-testid="stSidebarNav"] a:hover {
    background-color: #EDE9FE;
    color: var(--primary-color);
}

[data-testid="stSidebarNav"] a[aria-selected="true"] {
    background-color: var(--primary-color);
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Import pages
from pages import home, maths, science, extra_tools

# Create navigation
pg = st.navigation({
    "Main": [
        st.Page(home.home_page, title="Home", icon="🏠"),
    ],
    "Subjects": [
        st.Page(maths.maths_page, title="Maths", icon="🧮"),
        st.Page(science.science_page, title="Science", icon="🔬"),
    ],
    "Resources": [
        st.Page(extra_tools.extra_tools_page, title="Extra Tools", icon="✨"),
    ]
})

# Run the navigation
pg.run()