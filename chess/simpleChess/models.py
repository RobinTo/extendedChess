from django.db import models
from django.forms import ModelForm

# Create your models here.
class ChessGame(models.Model):
	fen = models.CharField(max_length=100)
	pgn = models.CharField(max_length=600)

class ChessForm(ModelForm):
	class Meta:
		model = ChessGame
		fenField = ['fen']
		pgnField = ['pgn']