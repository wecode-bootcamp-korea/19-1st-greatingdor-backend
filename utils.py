import jwt
import json

from django.http    import JsonResponse

from my_settings    import SECRET_KEY
from members.models import Member


def login_check(func):

    def wrapper(self, request, *args, **kwargs):

        try:
            access_token   = request.header.get('Authorization', None)
            payload        = jwt.decode(access_token, SECRET_KEY, algorithms='HS256')
            Member_id      = Member.objects.get(id=payload['Member_id'])
            request.member = Member_id

        except jwt.exceptions.DecodeError:
            return JsonResponse({'MESSAGE' : 'INVALID TOKEN'}, status=400)

        except Member.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'INVALID MEMBER'}, status=400)

        return func(self, request, *args, **kwargs)

    return wrapper
