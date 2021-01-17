from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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