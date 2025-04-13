import os
import cv2
import uuid
import json
import math
import random
import numpy as np
from PIL import Image
from sympy import symbols, Eq, solve
from flask import Flask, request, render_template, jsonify,url_for


#Souce Path
###############################################################################################
key_file_path = '/home/rajkumar_maity/Programming/S&T_Project/secur/Code/Keys/image_keys.json'
root_path='/home/rajkumar_maity/Programming/S&T_Project/secur/Code'
save_dir ='/home/rajkumar_maity/Programming/S&T_Project/secur/Code/static/image' #folder for image storing
template_folder='/home/rajkumar_maity/Programming/S&T_Project/secur/Code/templates'
###############################################################################################



# json file to store image keys
##############################################################################################
# Load existing keys if the file exists, else initialize an empty dict
if os.path.exists(key_file_path):
    with open(key_file_path, 'r') as f:
        image_dict = json.load(f)
else:
    image_dict = {}
image_dict={}
#################################################################################################



#Functions for Encryption and Decryption
##################################################################################################
def generate_polynomial_with_real_root():
    x = symbols('x')  # Define the symbolic variable
    
    # Generate random coefficients
    a = random.randint(1, 10)  # Random integer coefficient
    b = random.randint(-10, 10)  # Random integer coefficient
    c = random.randint(-10, 10)  # Random integer coefficient
    
    # Ensure the discriminant is non-negative to guarantee real roots
    discriminant = b**2 - 4*a*c
    
    # If discriminant is negative, adjust coefficients to ensure real roots
    while discriminant < 0:
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        discriminant = b**2 - 4*a*c
    
    polynomial = Eq(a*x**2 + b*x + c, 0)
    
    # Solve for roots
    roots = solve(polynomial, x)
    
    # Filter for real roots
    real_roots = [root.evalf() for root in roots if root.is_real]
    
    # Return the first real root
    return float(real_roots[0])


def encrypt(input_value):
    if not isinstance(input_value, int):
        raise ValueError("Input must be an integer.")
    x = generate_polynomial_with_real_root()
    return x

def decrypt(input_value, key1):
    return input_value - key1
###########################################################################################################




#Functions for image and text transformation logic
###########################################################################################################
def text_to_image(text):
    msg_list = [ord(i) for i in text]
    len_msg = len(msg_list)
    rows = 1 if len_msg <= 2 else int(math.sqrt(len_msg))  # Calculate the rows in the final image/matrix
    if len_msg % rows == 0:
        column = (len_msg // rows)
    else:
        column = (len_msg // rows) + 1  # Calculate the column in the final matrix/image
    msg_list.extend([32] * (rows * column - len_msg))  # Add padding with 32 (space)

    # Encryption step
    final_list = []
    for i in msg_list:
        key = int(encrypt(i))  # Calculate the encryption key for the first pixel value
        break
    for i in msg_list:
        final_list.append(i + key)  # Encrypt the remaining ASCII values

    img_id = str(uuid.uuid4())  # Generate a unique ID for an image
    pixel_matrix = np.array(final_list).reshape(rows, column)
    image = Image.fromarray(np.squeeze(np.array(pixel_matrix, dtype=np.uint8)), mode='L')

    save_path = os.path.join(save_dir, f'{img_id}.png')
    image.save(save_path)

    image_dict[img_id] = key #Stor the image is with key in dict of json file

    # Write updated dictionary to JSON file
    with open(key_file_path, 'w') as f:
        json.dump(image_dict, f)
     # Generate URL for downloading
    download_url = url_for('static', filename=f'image/{img_id}.png')
    return download_url

def image_to_text(image_source):
    image = cv2.imread(image_source, cv2.IMREAD_GRAYSCALE)
    initial_pixel_value = np.array(image)
    pixel_matrix = np.squeeze(initial_pixel_value)
    matrix_list = pixel_matrix.flatten().tolist()
    filename = os.path.basename(image_source)
    id = os.path.splitext(filename)[0]

    # Load the JSON mapping
    with open(key_file_path, 'r') as f:
        image_dict = json.load(f)
    if id not in image_dict:
        raise ValueError(f"No key found for image ID: {id}")

    key = image_dict[id]

    #Decryption Logic
    Matrix_final = []
    for i in matrix_list:
        get_real = decrypt(i, key)
        Matrix_final.append(get_real)
    string_output = ''.join(chr(i) for i in Matrix_final)
    return string_output
############################################################################################################



#Flask API connections with frontend code
#############################################################################################################
app = Flask(__name__, static_folder='static',template_folder=template_folder)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/text_to_image', methods=['POST'])
def handle_text_to_image():
    data = request.get_json()
    text = data.get('textinput')
    img_url = text_to_image(text)
    return jsonify({'processed_img': img_url})

@app.route('/image_to_text', methods=['POST'])
def handle_image_to_text():
    file = request.files['imageInput']
    filepath = os.path.join(save_dir, file.filename)
    file.save(filepath)
    
    result = image_to_text(filepath)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
####################################################################################################


