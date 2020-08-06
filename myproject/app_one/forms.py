from django import forms

# class ContactForm(forms.Form):
#     corp_choice = [
#         ('Всі корпуса', 'Всі корпуса'),
#         ('Корпус 1', 'Корпус 1'),
#         ('Корпус 2', 'Корпус 2'),
#         ('Корпус 3', 'Корпус 3'),
#         ('Корпус 4', 'Корпус 4'),
#         ('Корпус 5', 'Корпус 5'),
#     ]
#     zone_choice = [
#         ('Всі зони', 'Всі зони'),
#         ('Зона 1', 'Зона 1'),
#         ('Зона 2', 'Зона 2'),
#         ('Зона 3', 'Зона 3'),
#         ('Зона 4', 'Зона 4'),
#         ('Зона 5', 'Зона 5'),
#     ]
    
#     choice_corp = forms.ChoiceField(choices=corp_choice, label='Оберіть корпус')
#     choice_zone = forms.ChoiceField(choices=zone_choice, label='Обреть зону', disabled=True)
#     print(choice_corp)
#     text = forms.CharField(max_length=30)
#     print(text)


class Search(forms.Form):
    MY_CHOICES = [
        ('Всі зони', 'Всі зони'),
        ('Зона 1', 'Зона 1'),
        ('Зона 2', 'Зона 2'),
        ('Зона 3', 'Зона 3'),
        ('Зона 4', 'Зона 4'),
        ('Зона 5', 'Зона 5'),
    ]
    field = forms.ChoiceField(choices=MY_CHOICES,
        widget=forms.Select(attrs={'onchange': 'submit();'}))



