from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from users.models import Profile
from django.core import serializers
from django.http import HttpResponse



class UserRecordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


class GetUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):

        username = request.data["username"]
        if username:
            user = User.objects.get(username=username)
            serializer = UserSerializer(user)
            res = serializer.data
            res["userId"] = user.id
            return Response(res)
        return Response({"error": True, "error_msg": "username is required"})


class GetProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):

        username = request.data["username"]
        if username:
            profile = Profile.objects.get(user__username=username)
            data = serializers.serialize("json", [profile])

            return HttpResponse(data, content_type="application/json")
        return Response({"error": True, "error_msg": "username is required"})


class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        username = request.data["username"]
        if username:
            Profile.objects.filter(user__username=username).update(
                name=request.data["name"],
                email=request.data["email"],
                address=request.data["address"],
                bio=request.data["bio"],
                short_intro=request.data["short_intro"],
            )
            return Response({"success": True})
        return Response({"error": True, "error_msg": "username is required"})
