from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from chess.simpleChess.models import ChessGame, ChessForm

# Create your views here.
def chess(request):

	if (request.method == 'POST'):
		game = ChessGame.objects.all()[0]
		f = ChessForm(request.POST, instance=game)
		f.save()
	else:
		if(len(ChessGame.objects.all()) > 0 ):
			game = ChessGame.objects.all()[0];
		else:
			game = ChessGame()
			game.fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
			game.save()
	f = ChessForm()
	return render(request, 'chess.html', {'gameData' : game, 'f' : f})


def getGameFen(request):
	if(len(ChessGame.objects.all()) > 0):
	    game = ChessGame.objects.all()[0]
	    fenString = game.fen
		return HttpResponse(fenString);
	else:
		return HttpResponse("No game found.");