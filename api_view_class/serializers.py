from rest_framework import serializers

class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    price = serializers.IntegerField(min_value=0)
    count = serializers.IntegerField(min_value=0)

    def validate_name(self, value):
        print(f"validate_name: {value}")
        if value != "django":
            raise serializers.ValidationError("name must be django")
        return value

    def validate_price(self, value):
        print(f"validate_price: {value}")
        if value < 1000:
            raise serializers.ValidationError("price must be greater than or equal to 1000")
        return value

    def validate(self, data):
        print(f"validate: {data}")
        price = data.get("price")
        count = data.get("count")
        if price * count < 10000:
            raise serializers.ValidationError("total price must be greater than or equal to 10000")
        return data
