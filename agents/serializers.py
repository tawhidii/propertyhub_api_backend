from rest_framework import serializers
from .models import Agents


class AgentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Agents
        fields = '__all__'
