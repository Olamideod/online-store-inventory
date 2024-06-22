from rest_framework import serializers
from .models import Item, Supplier

class SupplierSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Supplier
        fields = ['id', 'name', 'contact_info', 'items']

class ItemSerializer(serializers.ModelSerializer):
    suppliers = SupplierSerializer(many=True, read_only=True)
    supplier_ids = serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=Supplier.objects.all())

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'date_added', 'suppliers', 'supplier_ids']

    def create(self, validated_data):
        supplier_ids = validated_data.pop('supplier_ids')
        item = Item.objects.create(**validated_data)
        item.suppliers.set(supplier_ids)
        return item

    def update(self, instance, validated_data):
        supplier_ids = validated_data.pop('supplier_ids', None)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.save()

        if supplier_ids is not None:
            instance.suppliers.set(supplier_ids)
        
        return instance
