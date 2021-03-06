import uuid
import os

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.conf import settings


def recipe_image_file_path(instance, filename):
    """"generate file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/recipe/', filename)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that suppors using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class AggregateRating(models.Model):
    name = models.CharField(max_length=254)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class RecipeCategory(models.Model):
    """RecipeCategory to be used for a recipe"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Ingredient to be used in a recipe"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Recipe object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    aggregateRating = models.ManyToManyField('AggregateRating', blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(null=True, blank=True)
    prepTime = models.IntegerField(null=True, blank=True)
    cookTime = models.IntegerField(null=True, blank=True)
    totalTime = models.IntegerField(null=True, blank=True)
    link = models.CharField(max_length=255, blank=True)
    ingredients = models.ManyToManyField('Ingredient', blank=True)
    recipeYield = models.IntegerField(blank=True, null=True)
    recipeCategorys = models.ManyToManyField('RecipeCategory', blank=True)
    recipeInstruction = models.TextField(blank=True)
    recipeIngredient = models.TextField(blank=True)
    image_id = models.IntegerField(null=True)
    image_x = models.URLField( blank=True)
    image_url = models.URLField( blank=True)
    image = models.ImageField(blank=True, upload_to=recipe_image_file_path)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name
