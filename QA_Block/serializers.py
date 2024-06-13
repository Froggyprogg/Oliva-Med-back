from QA_Block.models import Question, Answer
from rest_framework import serializers


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['question', 'answer_text', 'pub_date', 'doctor']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'description', 'pub_date', 'closed', 'answers']

    def create(self, validated_data):
        user = self.context['request'].user
        return Question.objects.create(user=user, **validated_data)


