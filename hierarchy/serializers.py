from .models import Table
from rest_framework import fields, serializers


class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = ('si_no', 'title', 'parent_id')
