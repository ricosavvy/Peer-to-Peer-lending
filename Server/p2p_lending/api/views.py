# backend/app/views.py
from django.http import JsonResponse
from machine_learning.predict import predict_value, generate_graph

def get_prediction(request):
    input_value = float(request.GET.get('value', 0))
    prediction = predict_value(input_value)
    return JsonResponse({'prediction': prediction})

def get_graph(request):
    graph_image = generate_graph()
    return JsonResponse({'graph': graph_image})
