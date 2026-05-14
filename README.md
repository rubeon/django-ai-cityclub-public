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

## Developer notes
- This repository contains a Django *app* (the `cityclub/` package), not a full Django project. There is no `manage.py` or project `settings.py` in this repo.
- To run or test this app locally, include `cityclub` in INSTALLED_APPS of a Django project and provide project-level settings (DATABASES, MEDIA_ROOT/MEDIA_URL, etc.), then run migrations from that project.
- `Reporter.api_key` is stored on the model as an optional field; treat it as a secret. Prefer wiring runtime keys via environment variables or Django settings rather than committing real keys to the database or source.
- `profile_pic` uses `upload_to='reporter_pics/'` — ensure your Django project's MEDIA_ROOT and MEDIA_URL are configured when handling uploads.

## Models
- **Reporter**: Stores AI reporter details (name, backend, personality, political_leaning).
- **Article**: Stores generated articles (title, content, reporter, publication_date, town).

Licensed under MIT.