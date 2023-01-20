from django.shortcuts import render
from .models import Question, Questionnaire
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage



def index(request):
    return render(request, 'pages/index.html')

def success(request):
    return render(request, 'pages/success.html')


def questions(request):
    if request.method == 'POST':
        questionnaire = Questionnaire()
        questionnaire.first_name = request.POST.get('first_name')
        questionnaire.last_name = request.POST.get('last_name')
        questionnaire.changed_name = (True if request.POST.get('changed_name') == 'Да' else False)
        questionnaire.changed_firstname = request.POST.get('changed_firstname')
        questionnaire.changed_lastname = request.POST.get('changed_lastname')
        questionnaire.passport_no = request.POST.get('passport_no')
        questionnaire.nation = request.POST.get('nation')
        questionnaire.religion = request.POST.get('religion')
        questionnaire.is_tattoo = True if request.POST.get('is_tattoo') == 'Да' else False
        questionnaire.education = request.POST.get('education')
        questionnaire.citizenship = request.POST.get('citizenship')
        questionnaire.present_address = request.POST.get('present_address')
        questionnaire.phone_number = request.POST.get('phone_number')
        questionnaire.father_data = request.POST.get('father_data')
        questionnaire.mother_data = request.POST.get('mother_data')
        questionnaire.marital_status = request.POST.get('marital_status')
        questionnaire.spouse_name = request.POST.get('spouse_name')
        questionnaire.spouse_nation = request.POST.get('spouse_nation')
        questionnaire.spouse_country = request.POST.get('spouse_country')
        questionnaire.spouse_city = request.POST.get('spouse_city')
        questionnaire.occupation = request.POST.get('occupation')
        questionnaire.company_name = request.POST.get('company_name')
        questionnaire.company_position = request.POST.get('company_position')
        questionnaire.company_address = request.POST.get('company_address')
        questionnaire.company_number = request.POST.get('company_number')
        questionnaire.is_served = True if request.POST.get('is_served') == 'Да' else False
        questionnaire.is_booked = True if request.POST.get('is_booked') == 'Да' else False
        questionnaire.tour_name = request.POST.get('tour_name')
        questionnaire.tour_address = request.POST.get('tour_address')
        questionnaire.hotel_name = request.POST.get('hotel_name')
        questionnaire.hotel_location = request.POST.get('hotel_location')
        questionnaire.is_visited = True if request.POST.get('is_visited') == 'Да' else False
        questionnaire.is_visited_address = request.POST.get('is_visited_address')
        questionnaire.is_visited_cities = request.POST.get('is_visited_cities')
        questionnaire.is_visited_visa_no = request.POST.get('is_visited_visa_no')
        questionnaire.is_visited_visa_type = request.POST.get('is_visited_visa_type')
        questionnaire.is_visited_visa_place = request.POST.get('is_visited_visa_place')
        is_visited_visa_date = request.POST.get('is_visited_visa_date')
        questionnaire.is_visited_visa_date = None if is_visited_visa_date == '' else is_visited_visa_date
        questionnaire.is_refused = True if request.POST.get('is_refused') == 'Да' else False
        questionnaire.is_refused_no = request.POST.get('is_refused_no')
        is_refused_date = request.POST.get('is_refused_date')
        questionnaire.is_refused_date = None if is_refused_date == '' else is_refused_date
        questionnaire.visited_countries = request.POST.get('visited_countries')
        questionnaire.visited_countries_saarca = request.POST.get('visited_countries_saarca')
        questionnaire.is_deported = True if request.POST.get('is_deported') == 'Да' else False
        questionnaire.is_criminal = True if request.POST.get('is_criminal') == 'Да' else False
        # image = request.FILES['image']
        # fs1 = FileSystemStorage()
        # filename1 = fs1.save(image.name, image)
        # questionnaire.image = filename1

        # passport_image = request.FILES['passport_image']
        # fs2 = FileSystemStorage()
        # filename2 = fs2.save(passport_image.name, passport_image)
        # questionnaire.passport_image = filename2

        questionnaire.save()
        return render(request, 'pages/success.html')
    else:
        questions = Question.objects.order_by('id')
        return render(request, 'pages/questions.html', {'questions': questions})
