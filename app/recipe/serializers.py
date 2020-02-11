from rest_framework import serializers

from core.models import RecipeCategory, Ingredient, Recipe


class RecipeCategorySerializer(serializers.ModelSerializer):
    """Serializer for tag object"""

    class Meta:
        model = RecipeCategory
        fields = ('id', 'name')
        read_only_Fields = ('id',)

class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for an ingredient object"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)

class RecipeSerializer(serializers.ModelSerializer):
    """Serialize a recipe"""
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )
    recipeCategorys = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=RecipeCategory.objects.all()
    )

    class Meta:
        model = Recipe
        fields = (
            'id', 'title','prepTime','cookTime','totalTime', 'ingredients', 'recipeInstruction', 'recipeIngredient', 'recipeCategorys', 'price',
            'link','recipeYield', 
        )
        read_only_fields = ('id',)
        
class RecipeDetailSerializer(RecipeSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    recipeCategorys = RecipeCategorySerializer(many=True, read_only=True)        

class RecipeImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to recipe"""

    class Meta:
        model = Recipe
        fields = ('id', 'image')
        read_only_fields = ('id',)