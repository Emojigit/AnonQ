from django.db import models

# Create your models here.

class Question(models.Model):
    q_ip = models.CharField(max_length=40,help_text="IP Address of the question asker")
    q_ip.short_description = "IP"
    q_ip.description = "IP Address"
    q_title = models.CharField(max_length=200,help_text="Question Title")
    q_title.short_description = "Title"
    q_content = models.TextField(max_length=500,help_text="Question Content")
    q_content.short_description = "Content"
    def __str__(self):
        return self.q_title

class Answer(models.Model):
    a_question = models.ForeignKey(Question,on_delete=models.CASCADE,help_text="Which question this answer is answering")
    a_question.short_description = "Question"
    a_content = models.TextField(max_length=500,help_text="Question Content")
    a_content.short_description = "Answer"
    a_content.description = "Answer Content"

