from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.password_validation import validate_password

from .serializers import UserSerialzer,ChangePassword


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerialzer

    @action(detail=False, methods=['delete'], permission_classes=[IsAuthenticated])
    
    def delete_account(self, request):
        request.user.delete()
        return Response({"message": "Account deleted successfully"}, status=204)


class PasswordViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['put'])
    
    def change(self,request):
        serializer = ChangePassword(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = request.user
        old_password = serializer.validated_data['old_password']
        new_password = serializer.validated_data['new_password']

        if not user.check_password(old_password):
            return Response({'old_password':'Wrongpassword'}, status=400)

        try:
            validate_password(new_password)
        except Exception as e:
            return Response({'new_password':list(e.messages)})
        
        user.set_password(new_password)
        user.save()

        return Response({'message':'Password changed successfully'}, status=200)
        





