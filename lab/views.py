from rest_framework.generics import ListAPIView
from .models import Profile
from .serializer import ProfileSerializer


class ProfileList(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
