import re
from rest_framework import serializers
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from postings.models import BlogPost, LRAQWorker


class BlogPostSerializer(serializers.ModelSerializer): # forms.ModelForm
    url         = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = BlogPost
        fields = [
            'url',
            'id',
            'user',
            'title',
            'content',
            'timestamp',
        ]
        read_only_fields = ['id', 'user']

    # converts to JSON
    # validations for data passed

    def get_url(self, obj):
        # request
        request = self.context.get("request")
        return obj.get_api_url(request=request)

    def validate_title(self, value):
        qs = BlogPost.objects.filter(title__iexact=value) # including instance
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This title has already been used")
        return value

class LRAQWorkerSerializer(serializers.ModelSerializer): # forms.ModelForm
    url         = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = LRAQWorker
        fields = ['url',
                'surveyId',
                'saId',
                'surveyLink']
        #read_only_fields = ['id', 'user']

    # converts to JSON
    # validations for data passed

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

    def validate_surveyId(self, value):  # FIXME the function name needs to be lowercase
        """ Validate the current SA number """
        pattern = re.compile("^SA-[0-9]+$|^$")
        value.upper()
        if not pattern.match(value):
            raise_msg = "Wrong format, currentSaNumber should be SA-XXXXXX where X is a digit."
            raise serializers.ValidationError(raise_msg)
        return value

    def validate_surveyLink(self, value):
        """Validate the Survey's link"""
        validate = URLValidator()
        try:
            validate(value)
        except:
            raise ValidationError(message=msg)
        return value
