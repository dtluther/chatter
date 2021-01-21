from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User

# A Custom Claim for JWT, so we can see the handle passed along with the token
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        """
        docstring
        """
        token = super(CustomTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claim
        token['handle'] = user.handle
        return token

class UserSerializer(serializers.ModelSerializer):
    # writing the attributes here will remove any defaults
    email = serializers.EmailField(required=True)
    handle = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    
    class Meta:
        model = User # required
        fields = ['email', 'handle', 'password'] # fields or exclude required

        # # adding things to extra_kwargs will override overlap, but maintain existing defaults
        # extra_kwargs = {
        #     'password': {'write_only': True},
        #     'handle': {'required': True},
        #     'email': {'required': True},
        # }
    
    def create(self, validated_data):
        password = validated_data.pop('password') # pop this so we can hash it
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
