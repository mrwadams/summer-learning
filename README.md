# Summer Learning Hub 🚀

A personalized educational web application built with Streamlit to help students prepare for the new school year through interactive learning modules.

## Features

- **Interactive Dashboard**: Clean, modern interface with custom CSS styling
- **Subject Modules**: Organized learning content for different subjects
  - 🧮 **Maths**: Mathematical concepts and practice
  - 🔬 **Science**: Scientific topics and experiments
  - ✨ **Extra Tools**: Additional learning resources

## Project Structure

```
summer-learning/
├── app.py              # Main Streamlit application
├── pages/              # Page modules
│   ├── __init__.py
│   ├── home.py         # Home page with dashboard
│   ├── maths.py        # Mathematics learning module
│   ├── science.py      # Science learning module
│   └── extra_tools.py  # Additional resources
└── venv/               # Virtual environment
```

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install streamlit
   ```

## Usage

Run the application:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Navigation

- **Home**: Welcome page with learning tips and progress overview
- **Subjects**: Access math and science learning modules
- **Resources**: Extra tools and additional learning materials

## Design

The application features a modern, student-friendly design with:
- Custom color scheme (purple/indigo primary theme)
- Responsive layout
- Interactive navigation
- Clean typography and spacing
- Visual progress indicators

## Contributing

This is a personal learning project. Feel free to fork and adapt for your own educational needs.