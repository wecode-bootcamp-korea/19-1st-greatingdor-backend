import json
import bcrypt
import re
import jwt

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from .models     import Member
from my_settings import SECRET_KEY
from .validation import validator_date_birth, validator_name, validator_account, validator_password, validator_email, validator_phone_number


class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if not validator_name(data['name']):
                return JsonResponse({'MESSAGE' : 'INVALID_NAME'}, status=400)

            if not validator_account(data['account']):
                return JsonResponse({'MESSAGE' : 'INVALID_ACCOUNT'}, status=400)

            if not validator_password(data['password']):
                return JsonResponse({'MESSAGE' : 'INVALID_PASSWORD'}, status=400)

            if not validator_email(data['email']):
                return JsonResponse({'MESSAGE' : 'INVALID_EMAIL'}, status=400)

            if not validator_date_birth(data['date_birth']):
                return JsonResponse({'MESSAGE' : 'INVALID_DATE_BIRTH'}, status=400)

            if not validator_phone_number(data['phone_number']):
                return JsonResponse({'MESSAGE' : 'INVALID_PHONE_NUMBER'}, status=400)

            if Member.objects.filter(
                    Q(account      = data['account']) |
                    Q(email        = data['email']) |
                    Q(phone_number = data['phone_number'])
                    ):
                return JsonResponse({'MESSAGE' : 'DUPLICATED_USER'}, status=400)

            Member.objects.create(
                    name         = data['name'],
                    account      = data['account'],
                    password     = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
                    email        = data['email'],
                    date_birth   = data['date_birth'],
                    phone_number = data['phone_number'],
                    )
            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=201)
        
        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status=400)


class SignInView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            account  = data['account']
            password = data['password']
            
            if not Member.objects.filter(account=account).exists():
                return JsonResponse({'MESSAGE' : 'NOT_FOUND'}, status=404)

            member = Member.objects.get(account=account)
            
            if bcrypt.checkpw(password.encode('utf-8'), member.password.encode('utf-8')):
                token = jwt.encode({'member_id' : member.id}, SECRET_KEY, 'HS256').decode('utf-8')
                return JsonResponse({'MESSAGE' : 'SUCCESS', 'Token' : token}, status=200)

            return JsonResponse({'MESSAGE' : 'INVALID_USER'}, status=401)

        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status=400)
