# Recipe Uploader

**Recipe Uploader** is a Django-based web application that allows users to share and discover recipes. The platform supports easy recipe uploads, exploration of diverse recipes, and community interaction.

## Features

- **Easy Recipe Submission**: Users can upload recipes with ingredients, instructions, and photos.
- **Recipe Exploration**: Browse and filter recipes by various criteria such as cuisine, ingredients, and meal type.
- **Personal Recipe Box**: Save your favorite recipes for easy access.
- **Recipe Reviews and Tips**: Read and write reviews to help improve the culinary experience.

## Technologies Used

- **Backend**: [Django](https://www.djangoproject.com/)
- **Frontend**: [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML), [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- **Database**: [SQLite]((https://www.sqlite.org/)) (or your preferred database)
- **Authentication**: Django’s built-in authentication system

## Getting Started

To set up the project locally, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/AbidHussain07/Recipe-uploader.git
   cd Receipe

2. **Set-up virtual environment**
 ```bash
 python -m venv venv
 source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**

 ```bash
 pip install -r requirements.txt
 
4. **Run the server**

 ```bash
 python manage.py makemigrations
 python manage.py migrate
 python manage.py runserver






