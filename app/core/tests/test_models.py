from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@bakov.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """test create a new user with email"""

        email = 'e@bakov.com'
        password = 'Test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ test email for new user is normalized"""
        email = 'test@BAKOV.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ test creating user with no email raise error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """test create a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@bakov.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_recipeCategory_str(self):
        """Test the recipeCategory string representation"""
        recipeCategory = models.RecipeCategory.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(recipeCategory), recipeCategory.name)

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='carrot'
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """Test the recipe string representation"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            name='Steak and mushroom sauce',
            cookTime=5,
            price=5.00
        )

        self.assertEqual(str(recipe), recipe.name)