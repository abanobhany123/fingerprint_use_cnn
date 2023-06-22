from django.shortcuts import render, redirect,get_object_or_404
from .models import Finger
import tempfile
from django.shortcuts import render
from django.http import JsonResponse
import joblib
import tensorflow as tf
from PIL import Image
import numpy as np

def load_model(model_path):
    """
    Load a machine learning model from a .h5 or .pkl file

    Args:
        model_path (str): Path to the model file
        
    Returns:
        The loaded machine learning model
    """
    if model_path.endswith('.pkl'):
        # Load a scikit-learn model from a .pkl file
        return joblib.load(model_path)
    elif model_path.endswith('.h5'):
        # Load a Keras model from a .h5 file
        return tf.keras.models.load_model(model_path)
    else:
        raise ValueError('Invalid model file format')

def predict(request):
    if request.method == 'POST':
        # Get input image from the request
        input_image = request.FILES.get('image')
        img = Image.open(input_image)

        # Convert the image to a 3D numpy array
        img_array = np.array(img)
        if img_array.ndim == 2:
            # Grayscale image
            img_array = np.expand_dims(img_array, axis=-1)
        elif img_array.shape[2] == 4:
            # RGBA image
            img_array = img_array[:, :, :3]
        img_array = img_array.astype('float32') / 255.

        # Make a prediction using the model
        model_path = 'C:/Users/abanob/Desktop/tesst/project/model_cb.pkl' # or 'path/to/model.h5'
        model = load_model(model_path)
        prediction = model.predict(np.expand_dims(img_array, axis=0))

        # Return the prediction as a JSON response
        return JsonResponse({'prediction': prediction.tolist()})
    else:
        # Render the form for image input
        return render(request, 'prediction_form.html')

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        address = request.POST.get('add')
        image = request.FILES.get('photo')
        finger = Finger.objects.create(name=name, age=age, adress=address, image=image, phone=phone)
        finger.save()
    return render(request,'pages/index.html')

def scan(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('imagefile')
        if uploaded_file is not None:
            temp_file = tempfile.NamedTemporaryFile(delete=False)

            with open(temp_file.name, 'wb') as f:
                for chunk in uploaded_file.chunks():
                    f.write(chunk)

            # uploaded image path = the path of the uploaded image
            uploaded_image_path = temp_file.name

            # Search for the Finger instance with the uploaded image
            try:
                finger_instance = Finger.objects.get(image=uploaded_file)
            except Finger.DoesNotExist:
                # If the image is not found, display an error message
                return render(request, 'pages/scan.html', {'error': 'Image not found.'})

            # Store the Finger instance in the session and redirect to view_results
            request.session['finger'] = finger_instance
            return redirect('view_results')

    return render(request, 'pages/scan.html')

def view_results(request):
   # finger = request.session.get('finger')
    #finger = get_object_or_404(Finger,id= id)
   # if finger is not None:
      #  context = {'ffinger': finger}
        return render(request, 'pages/viewdata.html')
def id_results(request ,id):
   # finger = request.session.get('finger')
    finger = get_object_or_404(Finger,id= id)
    if finger is not None:
        context = {'finger': finger}
        return render(request, 'pages/viewdata.html' ,context)