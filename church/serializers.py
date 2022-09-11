from rest_framework import serializers
from django.contrib.auth.models import User
from church.models import ChurchDenomination, ChurchItem, ChurchMembership, ChurchPastorship, DenominationLeadership


class ChurchItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchItem
        fields = '__all__'

class ChurchSerializer(serializers.ModelSerializer): # used to serialize church item in denomination list
    class Meta:
        model = ChurchItem
        fields = ['id','title','church_denomination','pastor']

class ChurchDenominationSerializer(serializers.ModelSerializer):
    churches = ChurchSerializer(source='denomination_churches', many=True, read_only=True, required=False)
    class Meta:
        model = ChurchDenomination
        fields = ['id','title','full_title','leader','head_quoters','church_type','churches']

class DenominationLeadershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = DenominationLeadership
        fields = '__all__'

class ChurchMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchMembership
        fields = ['id','church','created_on','comment']

class AddMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchMembership
        fields = ['comment']

class ChurchPastorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchPastorship
        fields = '__all__'