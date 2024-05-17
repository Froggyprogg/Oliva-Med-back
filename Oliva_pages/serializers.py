from rest_framework import serializers

from Oliva_pages.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'title', 'review_text', 'pub_date', 'user']
        read_only_fields = ['id', 'pub_date', 'user']

    def create(self, validated_data):
        user = self.context['request'].user
        return Review.objects.create(user=user, **validated_data)


