from django.db import models

class Reporter(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Byline name
    backend = models.CharField(max_length=50, choices=[('grok', 'Grok'), ('chatgpt', 'ChatGPT'), ('other', 'Other')])  # AI backend
    personality = models.TextField()  # Description of personality
    political_leaning = models.CharField(max_length=50, choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right'), ('neutral', 'Neutral')])  # Political bias
    api_key = models.CharField(max_length=200, blank=True)  # Optional API key for backend
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    town = models.CharField(max_length=100)  # e.g., 'Augsburg'
    publication_date = models.DateTimeField(auto_now_add=True)
    generated_by = models.CharField(max_length=50)  # Backend used for generation

    def __str__(self):
        return self.title