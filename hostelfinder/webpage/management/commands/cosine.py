from django.core.management.base import BaseCommand
from hostelAdmin.models import Hostel, Location
from webpage.models import User, Student, Rating
import csv
import random


def similar_hostel(user_id):
    user_rated_hostel = []
    similar_rating_student_id = []
    similar_student_rated_hostels = []
    user = []
    student = Student.objects.get(user_id=user_id)
    rating = Rating.objects.filter(user=student.user_id)

    if student.gender == 'M':
        hostel_type = 'B'
    else:
        hostel_type = 'G'

    #get the hostels rated by active user
    for rating in rating:
        user_rated_hostel.append(rating.hostel)

    #get the similar users who rated the hostels rated by active user
    similar_rating = Rating.objects.filter(hostel__in=user_rated_hostel,user__student__gender=student.gender).order_by('user_id').exclude(user_id=user_id)

    #prepare the list of similar rating users and the hostels they rated
    for s in similar_rating:
        similar_rating_student_id.append(s.user_id)

        for h in Rating.objects.filter(user_id=s.user_id,hostel__hostel_type='B'):
            similar_student_rated_hostels.append(h.hostel_id)

    # removing duplicates
    similar_rating_student_id = list(dict.fromkeys(similar_rating_student_id))
    similar_student_rated_hostels = list(dict.fromkeys(similar_student_rated_hostels))
    similar_rating_student_id.sort()
    similar_student_rated_hostels.sort()

    #create user-item matrix for both active user and similar users
    similar_user =  [[0] * len(similar_student_rated_hostels) for i in range(len(similar_rating_student_id))]

    for i,similar_user_id in enumerate(similar_rating_student_id):
        for j,hostel_id in enumerate(similar_student_rated_hostels):
            if Rating.objects.filter(user_id=similar_user_id,hostel_id=hostel_id).exists():
                r = Rating.objects.values('rating').get(user_id=similar_user_id,hostel_id=hostel_id)
                rate = r['rating']
            else:
               rate = 0
            similar_user[i][j] = rate


    for j in similar_student_rated_hostels:
        if Rating.objects.filter(user_id=4013, hostel_id=j).exists():
            r = Rating.objects.values('rating').get(user_id=user_id, hostel_id=j)
            rate = r['rating']
        else:
            rate = 0
        user.append(rate)


    print(similar_user[0][19])
    print(user)

class Command(BaseCommand):

    def handle(self,*args,**kwargs):
        similar_hostel(4013)

