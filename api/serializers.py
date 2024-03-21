from api.models import JDUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = JDUser
        fields = '__all__'
