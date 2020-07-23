from rest_framework import serializers
from .models import Post, User
# from django.conf import settings
# from django.contrib.auth.models import User

# User = settings.AUTH_USER_MODEL

# User serializer


class UserSerializer(serializers.ModelSerializer):

    # following = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'bio',
            'display_pic',
            'birth_date',
            'followers_count',
            'following_count',
            # 'following',
        )
        read_only_fields = ('followers_count', 'following_count')

    # def get_following(self, obj):
    #     if 'request' in self.context:
    #         request = self.context['request']
    #         if obj in request.user.following.all():
    #             return True
    #     return False


# Post Serializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user


# # # Following serializer
# # class FollowingSerializer(serializers.ModelSerializer):

# #     class Meta:
# #         model = UserFollowing
# #         fields = ("id", "following_user_id", "created")

    
# # # Followers serializer
# # class FollowersSerializer(serializers.ModelSerializer):

# #     class Meta:
# #         model = UserFollowing
# #         fields = ("id", "user_id", "created")


# # User serializer
# class UserSerializer(serializers.ModelSerializer):
    
#     # following = serializers.SerializerMethodField()
#     # followers = serializers.SerializerMethodField()

#     class Meta:
#         model = User
#         fields = (
#             "id",
#             "email",
#             "username",
#             "password",
#             # "following",
#             # "followers",
#         )
#         extra_kwargs = {"password": {"write_only": True}}

#     # def get_following(self, obj):
#     #     return FollowingSerializer(obj.following.all(), many=True).data

#     # def get_followers(self, obj):
#     #     return FollowersSerializer(obj.followers.all(), many=True).data


# # User Profile serializer
# class UserProfileSerializer(serializers.ModelSerializer):

#     user = UserSerializer(required=True)

#     class Meta:
#         model = Profile
#         fields = ['bio', 'display_pic', 'user']

#     def create(self, validated_data):
#         user_data = validated_data.pop('user')
#         profile = Profile.objects.create(**validated_data)
#         User.objects.create(profile=profile, **user_data)

#         return profile





