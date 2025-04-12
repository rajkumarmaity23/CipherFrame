# CipherFrame  
**_"Give your message a path into encrypted silence"_**

Welcome to **CipherFrame**, an innovative encryption and decryption system that transforms your secret messages into encrypted images — giving your message a visual path into encrypted silence. This project showcases how messages can travel securely, hidden within images, and later be decoded by the intended receiver.

---

## 📌 Project Highlights

### 🎨 Key Features  
- **Text-to-Image Encryption**: Converts any text message into a uniquely encrypted grayscale image using a simple encryption logic.
- **Image-to-Text Decryption**: Upload an encrypted image to decode and retrieve the original message instantly.
- **Real-time Web Interface**: A sleek, user-friendly interface for both the sender and receiver, facilitating easy interaction.
- **Secure Key Mapping**: Each image is generated with a unique encryption key stored safely alongside its image ID for precise decryption.

---

## 🔍 How It Works  

### 📤 Sender Side:
1. Enter a text message.
2. The system converts the message into ASCII values, encrypts them with a key, and saves them as pixel values in a grayscale image.
3. The image is downloadable and ready to send.

### 📥 Receiver Side:
1. Upload the received encrypted image.
2. The system decodes the pixel values using the stored key and reconstructs the original message.

---

## 🌟 Why It Matters  

In an age where information security is paramount, **CipherFrame** demonstrates an alternative visual encryption approach. This project explores steganographic principles combined with basic encryption to securely transmit sensitive messages in a creative and visual way.

---

## 🚀 How to Use  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/rajkumarmaity23/CipherFrame.git
```

### 2️⃣ Navigate to the Project Directory  
```bash
cd CipherFrame
```

### 3️⃣ Install Dependencies  
Make sure to install the required Python libraries:
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application  
```bash
python App_v2.py
```

Now open your browser and visit `http://127.0.0.1:5000/` to access the CipherFrame interface!

---

## 🤝 Get Involved  

We welcome all contributions and feedback!  
- Found a bug?  
- Have a suggestion?  
- Want to add new encryption schemes or enhancements?

Feel free to fork this repo, submit a pull request, or open an issue — let’s make **CipherFrame** even better together.

---

## 🙌 Acknowledgements  

Special thanks to the open-source community and Python’s powerful libraries like **Flask**, **NumPy**, and **Pillow** for making projects like these possible. Together, we’re shaping creative and secure ways to communicate.

---

**Thank you for exploring CipherFrame. Let’s give your messages a path into encrypted silence!**

