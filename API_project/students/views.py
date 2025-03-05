import os
import json
from django.conf import settings
from django.http import HttpResponse, JsonResponse


def data_json():
    file_path = os.path.join(settings.BASE_DIR, 'students', 'student.json')  # Adjust path as needed
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return {"error": str(e)}

def students(request):
    return JsonResponse(data_json(), safe=False)
