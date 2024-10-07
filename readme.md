🧑‍🦳 UTK Face Age & Gender Detection 👩‍🦱
<!-- You can replace this with a link to an image or banner -->

🚀 Project Overview
UTK Face Age & Gender Detection is an AI-powered system that predicts the age and gender of individuals based on their facial images using deep learning techniques. The system is built using the UTKFace dataset, trained with TensorFlow/Keras, and deployed using Flask for the back-end. This solution leverages both facial recognition and machine learning to provide accurate results.

But that’s not all! 🚀

We've integrated Blockchain technology to ensure the integrity and security of the model’s predictions and data storage, providing a robust, transparent, and tamper-proof solution for sensitive facial recognition applications.

🔥 Key Features
🔍 Age & Gender Prediction: Predicts age and gender from images with high accuracy.
🎯 Deep Learning: Powered by a Convolutional Neural Network (CNN) trained on the UTKFace dataset.
🛡 Blockchain Integration: Secures model predictions and logs them into a blockchain ledger, ensuring tamper-proof results.
📈 Scalable: Flask-based backend for easy API integration and scalable deployment.
💻 Frontend: Simple, user-friendly interface for users to upload images and receive predictions.
Tech Stack 🛠
Technology	Usage
Python	Core programming language
TensorFlow	For building and training the deep learning model
Keras	High-level API for training the CNN
Flask	Web framework for building RESTful APIs
HTML/CSS/JS	Frontend for image uploads and visualization
Blockchain	For immutable data logging of predictions
Node.js	For managing blockchain nodes and transactions
🧠 Machine Learning Pipeline
Preprocessing:

The model takes an input image of a face, resizes it to 200x200 pixels, and normalizes pixel values.
CNN Model Architecture:

Conv Layers: Extracts important features from the image.
Dense Layers: Fully connected layers to interpret those features.
Output Layers:
Age prediction (numerical)
Gender prediction (binary: male/female)
Training:

The model is trained using the UTKFace Dataset, containing over 20,000 labeled images with varying ages, genders, and ethnicities.
Blockchain Integration:

How Blockchain is used: Every prediction result (age and gender) is logged onto a blockchain node, making it immutable and auditable for future use. Each prediction transaction is time-stamped and verified by the network, ensuring tamper-resistant model logs.
🎨 How It Works
Upload your image via the user-friendly interface.
The image is sent to the Flask backend and processed by the pre-trained model.
The age and gender predictions are returned and displayed in real-time.
Blockchain Logging: Every prediction is securely stored in a blockchain ledger to ensure data integrity.
<!-- Replace with your GIF/Video of how the app works -->

🛠 Installation & Setup
Prerequisites
Make sure you have the following installed:

Python 3.x
Node.js
TensorFlow/Keras
Flask
Clone the Repository
bash
Copy code
git clone https://github.com/your-username/utk-face-age-gender-blockchain.git
cd utk-face-age-gender-blockchain
Install Dependencies
bash
Copy code
pip install -r requirements.txt
Train or Load Model
You can either load the pre-trained model or train the model yourself:

bash
Copy code
# For training (optional)
python train.py

# For running the app
python app.py
Run Blockchain Node
Ensure blockchain node is up and running:

bash
Copy code
node blockchain.js
🎯 Blockchain Architecture
Decentralized Ledger: Each prediction is stored in a decentralized ledger, ensuring data immutability and protection from tampering.
Consensus Algorithm: Proof of work (PoW) ensures the integrity of the prediction logs before they are added to the blockchain.
Smart Contracts: Implemented to facilitate the validation and trust of facial recognition data.
💻 Folder Structure
bash
Copy code
📦 UTK-Face-Age-Gender-Blockchain
 ┣ 📂 model          # Trained model files
 ┣ 📂 blockchain     # Blockchain node and smart contracts
 ┣ 📂 static         # Static frontend files
 ┣ 📂 templates      # HTML templates for the app
 ┣ 📜 app.py         # Flask backend
 ┣ 📜 train.py       # Model training script
 ┣ 📜 requirements.txt # Dependencies
 ┗ 📜 README.md      # This file
🔐 Blockchain Integration: Why?
Data Integrity: Every prediction (age and gender) is stored in an immutable blockchain ledger, ensuring that once stored, the data cannot be altered or tampered with.
Transparency: The entire transaction history is transparent and verifiable by all parties, fostering trust.
Security: Leveraging the decentralized nature of blockchain adds an extra layer of security to sensitive prediction data.
🌟 Future Enhancements
Real-time Streaming: Implement real-time video feeds for continuous age and gender predictions.
Blockchain Scalability: Move from Proof of Work to a more efficient consensus mechanism like Proof of Stake (PoS).
Additional Features: Emotion detection, ethnicity prediction, and more advanced facial features.
📢 Contributing
We welcome contributions! Feel free to:

Fork the project
Create a new branch (git checkout -b feature-branch)
Make changes and submit a pull request.
🎉 Hackathon Impact
By combining AI and Blockchain, this project tackles real-world problems in a secure and innovative way. Our system ensures that the results generated by our facial recognition model are accurate, secure, and tamper-proof, paving the way for safer and more reliable facial recognition systems in the future!

🙌 Acknowledgments
Special thanks to:

The UTKFace dataset for providing the data.
The TensorFlow and Keras communities for open-source support.
Blockchain enthusiasts for inspiring the secure implementation of AI models.
📧 Contact Us
If you have any questions, feel free to reach out at:
📧 Email: your-email@example.com
🐦 Twitter: @YourUsername

Give us a ⭐ on GitHub if you like this project!
Happy Coding! 👨‍💻👩‍💻
