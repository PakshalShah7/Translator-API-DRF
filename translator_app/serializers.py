""" This file contains translate serializer which is used in project. """

from rest_framework.serializers import ModelSerializer
from translate import Translator
from translator_app.models import Translate


class TranslateSerializer(ModelSerializer):
    """
    This is model serializer for translate model.
    """

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        model = Translate
        fields = ['from_language', 'text', 'to_language', 'translation']

    def create(self, validated_data):
        """
        This method just creates the actual model instance using the validated data.
        """
        from_language = validated_data['from_language']
        to_language = validated_data['to_language']
        text = validated_data['text']
        translator = Translator(from_lang=from_language,
                                to_lang=to_language)
        translation = translator.translate(text)
        translate = Translate.objects.create(from_language=from_language, to_language=to_language,
                                             text=text, translation=translation)
        return translate
