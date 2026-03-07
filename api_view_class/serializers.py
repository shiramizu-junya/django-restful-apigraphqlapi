from rest_framework import serializers

from api_view_class.models import Item


def validate_count(value):
    print(f"validate_count: {value}")
    if value % 5 != 0:
        raise serializers.ValidationError("count must be a multiple of 5")


class ItemSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=20)
    description = serializers.CharField()
    price = serializers.IntegerField(min_value=0)
    count = serializers.IntegerField(min_value=0)

    def validate_name(self, value):
        if self.partial and value is None:
            return value

        if value == "django":
            raise serializers.ValidationError("name must be django")
        return value

    def validate_price(self, value):
        if self.partial and value is None:
            return value

        if value < 1000:
            raise serializers.ValidationError(
                "price must be greater than or equal to 1000"
            )
        return value

    def validate(self, data):
        price = data.get("price", self.instance.price if self.instance else None)
        count = data.get("count", self.instance.count if self.instance else None)
        if price is not None and count is not None and price * count < 10000:
            raise serializers.ValidationError(
                "total price must be greater than or equal to 10000"
            )
        return data

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
