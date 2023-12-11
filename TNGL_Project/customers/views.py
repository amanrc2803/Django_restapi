from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomerSerializer
from .models import Customer

class CustomerView(CreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def get(self, request, *args, **kwargs):
        # Check if the URL contains a customer_number (pk)
        if 'pk' in kwargs:
            customer_id = kwargs['pk']
            customer = self.get_object(customer_id)
            serializer = self.serializer_class(customer)
            return Response(serializer.data)
        
        customers = self.get_queryset()
        serializer = self.serializer_class(customers, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Customer created successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, customer_id):
        return self.get_queryset().get(pk=customer_id)
