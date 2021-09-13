from .models import Dataset, Brand, Link, Source
from rest_framework import serializers


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = "__all__"

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class DatasetSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=True, required=False)
    link = LinkSerializer(many=True, required=False)
    source = SourceSerializer(many=True, required=False)

    class Meta:
        model = Dataset
        fields = ('id', 'country', 'category', 'brand', 'link', 'source')

    def create(self, validated_data):
        new_dataset = Dataset.objects.create(country=validated_data['country'], category=validated_data['category'])
        for b in validated_data['brand']: new_dataset.brand.create(**b)
        for l in validated_data['link']: new_dataset.link.create(**l)
        for s in validated_data['source']: new_dataset.source.create(**s)
        return new_dataset