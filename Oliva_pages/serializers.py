from rest_framework import serializers

from Oliva_pages.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'title', 'review_text', 'pub_date']
        read_only_fields = ['id', 'pub_date']

    def create(self, validated_data):
        user = self.context['request'].user
        return Review.objects.create(user=user, **validated_data)


