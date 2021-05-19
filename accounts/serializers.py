from django.contrib.auth.models import Group
from rest_framework.exceptions import ValidationError
from .servises import mailing
from major.serializers import *
from major.models import *
from .models import *


class CarSerializer(serializers.ModelSerializer):
    car_id = serializers.IntegerField(source='id', required=False)

    class Meta:
        model = Car
        fields = ['car_id', 'brand', 'model', 'year', 'number', 'color', 'type']


class DossierSerializer(serializers.ModelSerializer):
    car = CarSerializer(many=True)
    schools = EducationSerializer(many=True)
    war_crafts = WarcraftSerializer(many=True)

    class Meta:
        model = Dossier
        fields = ['id', 'full_name', 'date_birth', 'image', 'gender', 'user', 'car', 'schools', 'war_crafts']

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        cars_data = validated_data.pop('car')
        schools_data = validated_data.pop('schools')
        warcrafts_data = validated_data.pop('war_crafts')
        ids_list = [car.id for car in instance.car.all()]
        current_ids = [car['id'] for car in cars_data]
        final_list = [car_id for car_id in ids_list if car_id not in current_ids]
        for car in cars_data:
            car_id = car['id']
            car_data = Car.objects.get(id=car_id)
            for delete_id in final_list:
                delete_car = Car.objects.get(id=delete_id)
                delete_car.delete()
            car_data.brand = car['brand']
            car_data.model = car['model']
            car_data.year = car['year']
            car_data.number = car['number']
            car_data.color = car['color']
            car_data.type = car['type']
            car_data.save()
        instance.save()
        return instance



class RegisterSerializer(serializers.ModelSerializer):
    check_password = serializers.CharField(write_only=True)
    full_name = serializers.CharField(write_only=True)
    image = serializers.ImageField(write_only=True)
    date_birth = serializers.DateField(write_only=True)
    gender = serializers.ChoiceField(choices=(
        ('Male', 'Male'),
        ('Female', 'Female')
    ), write_only=True)
    user_type = serializers.ChoiceField(choices=(
        ('Common', 'Common'),
        ('Warrior', 'Warrior')
    ), write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'check_password', 'full_name',
                  'date_birth', 'gender', 'image', 'user_type']

    def create(self, validated_data):
        user_type = validated_data.pop('user_type')
        image = validated_data.pop('image')
        password = validated_data.pop('password')
        check_password = validated_data.pop('check_password')
        full_name = validated_data.pop('full_name')
        date_birth = validated_data.pop('date_birth')
        gender = validated_data.pop('gender')
        user = User.objects.create(**validated_data)
        if password != check_password:
            raise ValidationError("Password don't match")
        user.set_password(password)
        if user_type == 'Warrior':
            user.is_active = False
            group = Group.objects.get(name='sergeant')
            user.groups.add(group)
            mailing(user.username)
        user.save()
        Dossier.objects.create(full_name=full_name, date_birth=date_birth,
                               gender=gender, image=image, user=user)
        return user
