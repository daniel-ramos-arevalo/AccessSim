from rest_framework import serializers

from leads.models import Leads
from origin.models import Origin
from status.models import Status


class OriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origin
        fields = ['origin_id', 'origin_name']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['status_id', 'status_name']


class LeadSerializer(serializers.ModelSerializer):
    status = StatusSerializer(read_only=True)
    origin = OriginSerializer(read_only=True)

    class Meta:
        model = Leads
        fields = [
            'lead_id',
            'lead_name',
            'email',
            'lead_message',
            'telefone',
            'is_active',
            'created_at',
            'status',
            'origin',
        ]
