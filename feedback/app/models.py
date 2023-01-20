from django.db import models

#
class Question(models.Model):
    TYPE_CHOICES = (
        ("is_text", "is_text"),
        ("is_radio", "is_radio"),
        ("is_select", "is_select"),
        ("is_date", "is_date"),
    )
    title = models.CharField('Вопрос', max_length=256, null=True)
    name = models.CharField('name', max_length=256, null=True, blank=True)
    placeholder = models.CharField('placeholder', max_length=256, null=True, blank=True)
    types = models.CharField('Тип',choices=TYPE_CHOICES, default='is_text', max_length=10 )


    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.title if self.title != None else '--'



class Subquestion(models.Model):
    TYPE_CHOICES = (
        ("is_text", "is_text"),
        ("is_radio", "is_radio"),
        ("is_select", "is_select"),
        ("is_date", "is_date"),
    )
    questions = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name='Вопрос',
        related_name='subquestions')
    title = models.CharField('Подвопрос', max_length=256, null=True, blank=True)
    answer = models.CharField('Ответ', max_length=256, null=True, blank=True)
    is_radio_activate = models.BooleanField('Hidden', default=False)
    name = models.CharField('name', max_length=256, null=True, blank=True)
    placeholder = models.CharField('placeholder', max_length=256, null=True, blank=True)

    types = models.CharField('Тип',choices=TYPE_CHOICES, default='is_text', max_length=10 )


    class Meta:
        verbose_name = 'Подвопрос'
        verbose_name_plural = 'Подвопросы'

    def __str__(self):
        return  self.title if self.title else self.answer



class Questionnaire(models.Model):
    first_name = models.CharField('Имя', max_length=50, blank=True)
    last_name = models.CharField('Фамилия', max_length=50, blank=True)
    changed_name = models.BooleanField('Смена имени', default=False)
    changed_firstname = models.CharField('Прошлое имя', max_length=50)
    changed_lastname = models.CharField('Прошлое имя', max_length=50)
    passport_no = models.CharField('Серия паспорта', max_length=10)
    nation = models.CharField('Нация', max_length=50)
    religion = models.CharField('Религия', max_length=50)
    is_tattoo = models.BooleanField('Татуировка или родимые пятна', default=False)
    education = models.CharField('Оброзование', max_length=50)
    citizenship = models.CharField('Гражданство', max_length=50)
    present_address = models.CharField('Действующий адрес', max_length=256)
    phone_number = models.CharField('Номер телефона', max_length=15)
    father_data = models.CharField('Данные отца ', max_length=50)
    mother_data = models.CharField('Данные матери ', max_length=50)
    marital_status = models.CharField('Семейный статус ', max_length=50)
    spouse_name = models.CharField('Имя супруга ', max_length=50, blank=True)
    spouse_nation = models.CharField('Нация супруга ', max_length=50, blank=True)
    spouse_country = models.CharField('Страна рождения супруга ', max_length=50, blank=True)
    spouse_city = models.CharField('Город рождения супруга ', max_length=50, blank=True)
    occupation = models.CharField('Профессия ', max_length=50)
    company_name = models.CharField('Название компании ', max_length=70, blank=True)
    company_position = models.CharField('Должность ', max_length=70, blank=True)
    company_address = models.CharField('Адрес ', max_length=100, blank=True)
    company_number = models.CharField('Номер компании ', max_length=100, blank=True)
    is_served = models.BooleanField('Служил в армии', default=False)
    is_booked = models.BooleanField('Бронирование отели', default=False)
    tour_name = models.CharField('Название тур оператора ', max_length=100, blank=True)
    tour_address = models.CharField('Адрес тур оператора ', max_length=100, blank=True)
    hotel_name = models.CharField('Название гостиницы ', max_length=100, blank=True)
    hotel_location = models.CharField('Расположение гостиницы ', max_length=100, blank=True)
    is_visited = models.BooleanField('Визит в индию(было/не было)', default=False)
    is_visited_address = models.CharField('Адрес проживания', max_length=256, blank=True)
    is_visited_cities = models.CharField('Посещенные города ', max_length=256, blank=True)
    is_visited_visa_no = models.CharField('Номер последней визы ', max_length=100, blank=True)
    is_visited_visa_type = models.CharField('Тип визы ', max_length=100, blank=True)
    is_visited_visa_place = models.CharField('Место выдачи визы ', max_length=100, blank=True)
    is_visited_visa_date = models.DateField('Дата визы ',  blank=True, null=True)
    is_refused = models.BooleanField('Отказ на въезд(было/не было)', default=False)
    is_refused_no = models.CharField('Контрольный номер ', max_length=100, blank=True)
    is_refused_date = models.CharField('Дата отказа ', max_length=100, blank=True, null=True)
    visited_countries = models.TextField('Визиты за последние 10 лет ')
    visited_countries_saarca = models.TextField('Визиты в SARCA ')
    is_deported = models.BooleanField('Депорт(было/не было)', default=False)
    is_criminal = models.BooleanField('Судимость(было/не было)', default=False)
    passport_image = models.ImageField('Фото паспорта:', upload_to='passport_images/', null=True, blank=True)
    image = models.ImageField('Фото:', upload_to='images/', null=True, blank=True)
    date = models.DateTimeField('Дата регистрации: ', auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'

    def __str__(self):
        return  f'{self.first_name} {self.last_name}'