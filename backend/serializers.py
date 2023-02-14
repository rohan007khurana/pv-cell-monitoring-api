from rest_framework import serializers
from .models import Reading

class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ['id', 'v_oc', 'i_sc','created_at', 'created_date', 'created_time']    