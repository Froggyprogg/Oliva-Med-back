from QA_Block.models import Question
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'slug', 'title', 'description', 'pub_date', 'user', 'closed']
        read_only_fields = ['id', 'slug', 'pub_date']

    def create(self, validated_data):
        user = self.context['request'].user
        return Question.objects.create(user=user, **validated_data)


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question', 'answer_text', 'pub_date', 'doctor']