from rest_framework import serializers
from django.db.models import Q
from items.models import (
        Item,
        CheckIn,
        TypeItem,
        Brand,
        LostItem
)


class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    reference = serializers.CharField(max_length=30)
    color = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=255)
    lost = serializers.BooleanField(default=False)
    type_item = serializers.CharField(max_length=30)
    brand = serializers.CharField(max_length=30)
    registered_in_seat_id = serializers.IntegerField()
    company_id = serializers.IntegerField()
    registered_in_seat = serializers.CharField(max_length=100)
    registration_date = serializers.DateTimeField()
    registered_by = serializers.IntegerField()
    owner_name = serializers.CharField(max_length=50)
    owner_last_name = serializers.CharField(max_length=50)
    owner_dni = serializers.CharField(max_length=30)

    class Meta:
        model = Item
        fields = ('__all__')

    @staticmethod
    def has_read_permission(request):
        group = request.user.groups.filter(Q(name="Developer") | Q(name="Manager"))
        parameters = [parameter for parameter in request.path_info if parameter.isdigit()]
        user_company_id = str(request.user.customuser.seathasuser.seat.company_id)
        if group and user_company_id == parameters[0]:
            return True
        return False

    def has_object_read_permission(self, request):
        group = request.user.groups.filter(Q(name="Developer") | Q(name="Manager"))
        parameters = [parameter for parameter in request.path_info if parameter.isdigit()]
        user_company_id = str(request.user.customuser.seathasuser.seat.company_id)
        if group and user_company_id == parameters[0]:
            return True
        return False

    def has_object_write_permission(self, request):
        group = request.user.groups.filter(Q(name="Developer") | Q(name="Manager"))
        parameters = [parameter for parameter in request.path_info if parameter.isdigit()]
        user_company_id = str(request.user.customuser.seathasuser.seat.company_id)
        if group and user_company_id == parameters[0]:
            return True
        return False

    @staticmethod
    def has_write_permission(request):
        group = request.user.groups.filter(Q(name="Developer") | Q(name="Manager"))
        parameters = [parameter for parameter in request.path_info if parameter.isdigit()]
        user_company_id = str(request.user.customuser.seathasuser.seat.company_id)
        if group and user_company_id == parameters[0]:
            return True
        return False


class ChekinSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    seat_id = serializers.IntegerField()
    seat_dir = serializers.CharField(max_length=30)
    item = serializers.IntegerField()
    type_item = serializers.CharField(max_length=255)
    lost = serializers.BooleanField(default=False)
    owner_name = serializers.CharField(max_length=50)
    owner_last_name = serializers.CharField(max_length=50)
    owner_dni = serializers.CharField(max_length=30)
    go_in = serializers.BooleanField()
    date = serializers.DateTimeField()


class CheckInCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CheckIn
        fields = ('__all__')
        extra_kwargs = {
            'id': {'read_only': True},
            'date': {'read_only': True},
            }


class TypeItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeItem
        fields = ('__all__')


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ('__all__')


class RegisterItem(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('__all__')


class RegisterItemTest(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('type_item',
                  'owner',
                  'brand',
                  'reference',
                  'color',
                  'description',
                  'lost',
                  'enabled',
                  'seat_registration',
                  'registration_date',
                  'registered_by')


class LostItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = LostItem
        fields = ('__all__')

        extra_kwargs = {
            'enabled': {'read_only': True},
            'closed_case': {'read_only': True},
            }


class LostItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    description = serializers.CharField(max_length=255)
    item_reference = serializers.CharField(max_length=30)
    item_color = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=255)
    type_item = serializers.CharField(max_length=30)
    owner_name = serializers.CharField(max_length=50)
    owner_last_name = serializers.CharField(max_length=50)
    owner_dni = serializers.CharField(max_length=30)
    item_brand = serializers.CharField(max_length=30)
    date = serializers.DateTimeField()
    lost_in_seat = serializers.CharField(max_length=100)
    lost_in_seat_id = serializers.IntegerField()
    email = serializers.EmailField()
    visitor_phone = serializers.CharField(max_length=20)
    closed_case = serializers.BooleanField(default=False)
