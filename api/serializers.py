import datetime

from rest_framework import serializers

from credit.models import Borrower, Blacklist


class CreditSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField(allow_null=True, required=True)

    class Meta:
        model = Borrower
        fields = ['iin', 'price']

    def validate_birthday(self, iin):
        print("iin:", iin)
        iin = str(iin)
        print(iin)
        if int(iin[:2]) < 99:
            print(int("19" + iin[:2]), int(iin[2:4]), int(iin[4:6]))
            birthday = datetime.datetime(int("19" + iin[:2]), int(iin[2:4]), int(iin[4:6]))
        else:
            print(int("19" + iin[:2]), int(iin[2:4]), int(iin[4:6]))
            birthday = datetime.datetime(int("20" + iin[:2]), int(iin[2:4]), int(iin[4:6]))
        if datetime.datetime.now() < birthday:
            raise serializers.ValidationError('Заемщик не подходит по возрасту')

        return birthday.date()

    def validate_iin(self, iin):
        print("iin in iin:", iin)
        if Blacklist.objects.filter(iin=iin).exists():
            raise serializers.ValidationError('Заемщик в черном списке')
        return iin

    def validate(self, data):
        """
        Check that start is before finish.
        """
        birthday = self.validate_birthday(data['iin'])
        data['birthday'] = birthday
        return data

    def save(self, commit=True):
        price = self.validated_data.pop('price')
        super().save()
        # Bid.objects.create()
