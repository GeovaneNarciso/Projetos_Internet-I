from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import Account
from accounts.serializers import AccountSerializer


@api_view(['GET', 'POST'])
def account_list(request):
    if request.method == 'GET':
        accounts = Account.objects.all()
        accounts_serializer = AccountSerializer(accounts, many=True)
        return Response(accounts_serializer.data)

    elif request.method == 'POST':
        accounts_serializer = AccountSerializer(data=request.data)
        if accounts_serializer.is_valid():
            # Validação do creation_date  -------------------------------------------------------
            if "creation_date" in request.data:
                msg = {"message": "Não é necessário informar a data de criação."}
                return Response(msg, status=status.HTTP_406_NOT_ACCEPTABLE)

            accounts_serializer.save()
            return Response(accounts_serializer.data, status=status.HTTP_201_CREATED)
        return Response(accounts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def account_detail(request, pk):
    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        account_serializer = AccountSerializer(account)
        return Response(account_serializer.data)

    elif request.method == 'PUT':
        account_serializer = AccountSerializer(account, data=request.data)
        if account_serializer.is_valid():
            account_serializer.save()
            return Response(account_serializer.data)
        return Response(account_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        account_serializer = AccountSerializer(account, data=request.data, partial=True)
        if account_serializer.is_valid():
            account_serializer.save()
            return Response(account_serializer.data)
        return Response(account_serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    elif request.method == 'DELETE':
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
