from rest_framework import serializers
from ExamApp.models import QuestionsDb


class QuestionSerializer(serializers.Serializer):
        question = serializers.CharField(max_length=200)
        option_a = serializers.CharField(max_length=200)
        option_b = serializers.CharField(max_length=200)
        option_c = serializers.CharField(max_length=200)
        option_d = serializers.CharField(max_length=200)
        correct_answer = serializers.CharField(max_length=200)