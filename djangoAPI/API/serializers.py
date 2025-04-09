from rest_framework import serializers
from API.models import AppDetails

class AppDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = AppDetails
        fields = ['id','app_name','version','description']