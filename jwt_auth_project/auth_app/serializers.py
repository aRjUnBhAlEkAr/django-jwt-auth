# third-party package imports
from rest_framework import serializers
from django.contrib.auth import authenticate

# local imports
from auth_app.models import User

# Define serializers here.
class UserRegistrationSerializer(serializers.ModelSerializer):
    # Users often type their password incorrectly.
    # A confirm password field helps avoid mistakes.
    password2 = serializers.CharField(style={"input_type":"password"}, write_only=True)
    
    # The Meta class tells Django REST Framework how to handle the serializer.
    class Meta:
        # model :
        # -> This tells the serializer which database model it represents.
        # -> Create/Validate data for the User model.
        model = User
        
        # fields = [...]
        # -> This specifies which model fields should be included in API request/response.
        # -> If a field is not in this list → API will ignore it.
        fields = ['id', 'email', 'name', 'password', 'password2']
        
        # extra_kwargs = {...}
        # -> Used to give extra rules/behavior for individual fields.
        extra_kwargs = {
            # When someone registers -> email must be provided
            'email': {
                'required':True
                },
        
            'password':{
                # Field will not show in GET response (useful for password)
                'write_only':True,
                'style':
                    {
                        'input_type':'password'
                    }
            }
        }
        
    # validate() method:
    # -> validate() is a build-in method in Django REST Framework serializers/
    # -> It is used to apply custom validation rules on all fields together - known as object-level validation
    # -> This is useful when:
    #       - You need to compare multiple fields
    #       - Validation depends on more than one field
    def validate(self, attrs):
        # Gets the value of password field from request data
        password1 = attrs.get('password')
        # Gets the value of password2 (confirm password field)
        password2 = attrs.get('password2')
        
        # Checks if both passwords match
        if password1 != password2:
            # If not matching, show an error response and stop the process
            raise serializers.ValidationError("Password and Confirm password must match!")
        
        # If valid, return updated attrs data to next process
        # Why do we return attrs?
        # Because if validation succeeds, we must pass the cleaned data forward so DRF can continue to:
        # -> Call create() method
        # -> save user into database
        # -> Hash password
        return attrs
    
    # After validation passes, DRF calls the create() method to:
    # DRF sends validated & cleaned data here to create an object
    def create(self, validated_data):
        # Extracts email value from validated data
        email = validated_data.get('email')
        # Extracts name value
        name = validated_data.get('name')
        # Extracts password (plain text temporarily)
        password = validated_data.get('password')
        
        # Calls CustomUserManager method to create user correctly
        user = User.objects.create_user(
            email=email,
            name=name,
            password=password
        )
        
        # Return the new saved user instance
        return user

# user login serializer
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    # user validation function
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        
        # authenticating user using 'authenticate()' method of django.contrib.auth
        user = authenticate(username=username, password=password)
        
        if not user:
            raise serializers.ValidationError("Invalid Username or Password!")
        
        attrs['user'] = user
        
        return attrs