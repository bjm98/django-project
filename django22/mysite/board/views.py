from django.shortcuts import render
from .models import Board

# Create your views here.

def board_list(request):
    board = Board.objects.all()
    return render(request, 'board/board_list.html',{'board': board})


