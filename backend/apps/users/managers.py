from django.contrib.auth.models import UserManager as Manager


class UserManager(Manager):

    def create_user(self, email=None, password=None, **extra_fields):

        if not email:
            raise ValueError('Email must have an email')

        if not password:
            raise ValueError('Email must have a password')
        #normalize for email

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password) #hash for password
        user.save()
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields['is_active'] is not True:
            raise ValueError('Superuser must have is_active=True')
        if extra_fields['is_staff'] is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields['is_superuser'] is not True:
            raise ValueError('Superuser must have is_superuser=True')

        user = self.create_user(email=email, password=password, **extra_fields)

        return user