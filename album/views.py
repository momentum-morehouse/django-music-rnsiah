from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm




def home(request):
  albums = Album.objects.all()
  return render(request, 'album/home.html', {'albums':albums})

def add_album(request):
  if request.method =='GET':
    return render(request, 'album/add_album.html', {'form':AlbumForm})
  else:
    form = AlbumForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect(to='home')
  return render(request, 'album/add_album.html', {'form':form})


def edit_album(request, pk):
  album= get_object_or_404(Album, pk=pk)
  if request.method == "GET":
    form=AlbumForm(instance=album)
  else:
    form= AlbumForm(data=request.POST, instance=album)
    if form.is_valid():
      form.save()
      return redirect(to='home')
  return render(request, 'album/edit_album.html',{'form':form, "album":album})





def delete_album(reuest, pk):
  album = get_object_or_404(Album, pk=pk)
  if reuest.method=='POST':
    album.delete()
    return redirect(to='home')
  return render(reuest, 'album/delete_album.html', {'album':album})








def signupuser(request):
  pass
 # if request.method =='GET':
  #  return render(request, 'album/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords Did Not Match, Please Enter A Different Password'})
  #else:
   # if request.POST['password1']== request.POST['password2']:
    #  user = User.objects._create_user(request.POST['username'], password= request.POST['password1']
      #user.save()
    #else:
     # print('hello')
      # Tell user password didnt match #
