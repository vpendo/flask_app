# AfricaLearn - Multilingual Language Learning Platform

AfricaLearn is a Flask-based web application that provides language learning courses in English, French, Kinyarwanda, and Swahili. The platform features a responsive design and supports multiple languages through internationalization (i18n).

## Features

- Multilingual support (English, French, Kinyarwanda, Swahili)
- Responsive design for all devices
- Interactive language learning courses
- User-friendly interface
- Easy language switching

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.7 or higher
- pip (Python package installer)
- Git (optional, for version control)

## Installation

1. Clone the repository (if using Git):
```bash
git clone <repository-url>
cd flask_app/Group5_i18n
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
- On Windows:
```bash
venv\Scripts\activate
```
- On macOS/Linux:
```bash
source venv/bin/activate
```

4. Install the required packages:
```bash
pip install -r requirements.txt
```

## Setting Up Translations

1. Install Babel (if not already installed):
```bash
pip install Flask-Babel
```

2. Extract messages for translation:
```bash
pybabel extract -F babel.cfg -o messages.pot .
```

3. Initialize translations for each language:
```bash
pybabel init -i messages.pot -d translations -l fr  # For French
pybabel init -i messages.pot -d translations -l rw  # For Kinyarwanda
pybabel init -i messages.pot -d translations -l sw  # For Swahili
```

4. Compile translations:
```bash
pybabel compile -d translations
```

## Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Using the Application

### Language Selection
- The language selector is located in the top-right corner of every page
- Select your preferred language from the dropdown menu:
  - English
  - Français (French)
  - Kinyarwanda
  - Kiswahili (Swahili)

### Navigation
- Home: Main landing page with platform overview
- Courses: Available language courses
- About: Information about AfricaLearn
- Contact: Contact information and social media links

### Features
- Browse available language courses
- View course details and descriptions
- Access learning materials
- Switch between languages seamlessly

## Project Structure

```
flask_app/Group5_i18n/
├── app.py                 # Main application file
├── babel.cfg             # Babel configuration
├── requirements.txt      # Python dependencies
├── translations/         # Translation files
│   ├── fr/              # French translations
│   ├── rw/              # Kinyarwanda translations
│   └── sw/              # Swahili translations
└── templates/           # HTML templates
    ├── index.html       # Home page
    ├── courses.html     # Courses page
    └── about.html       # About page
```

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please contact:
- Email: info@africalearn.com
- Phone: +250 788 123 456
- Address: Kigali, Rwanda

## Acknowledgments

- Flask framework
- Flask-Babel for internationalization
- All contributors and supporters of the project 