# Django AI CityClub

This is a small Django app for an AI-powered news page focused on a specific town (e.g., Augsburg, Germany). The site owner can create AI \"reporters\" backed by various AI backends (Grok, ChatGPT, etc.), each with a unique byline, personality, and political leanings. Reporters generate articles on local news topics.

## Features
- Create and manage AI reporters with metadata (name, backend, personality, bias).
- Generate and store articles with title, content, author (reporter), date.
- Simple news feed view for the town.

## Setup
1. Install Django: `pip install django`
2. Run migrations: `python manage.py makemigrations; python manage.py migrate`
3. Start server: `python manage.py runserver`

## Models
- **Reporter**: Stores AI reporter details (name, backend, personality, political_leaning).
- **Article**: Stores generated articles (title, content, reporter, publication_date, town).

Licensed under MIT.