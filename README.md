# text--video-generator

AI Video Generation with CogVideoX & AnimateDiff 🎥
This project provides a Gradio interface to generate AI-powered videos using CogVideoX and AnimateDiff. Users can enter a text prompt, and the system will generate corresponding animations using the latest AI models.

🚀 Features
✅ Generate AI videos from text prompts
✅ Uses CogVideoX and AnimateDiff pipelines
✅ Outputs high-quality .mp4 video files
✅ Simple and interactive Gradio UI

📦 Installation
Clone the Repository

# Kaggle Notebook
Create a Virtual Environment (Optional but Recommended)


Install Dependencies

pip install torch diffusers gradio
Download the Pretrained Models
The script will automatically download the required models (THUDM/CogVideoX-2b, emilianJR/epiCRealism) the first time you run it.

🛠️ Usage
Run the Gradio app:


python app.py
Then, open the Gradio UI in your browser and enter a text prompt to generate AI videos.


app.py → Main script that runs the Gradio interface.
requirements.txt → List of required dependencies.
README.md → Documentation (this file).
🎯 Example Prompt
📝 Prompt:

A panda, dressed in a small, red jacket and a tiny hat, sits on a wooden stool in a serene bamboo forest. The panda's fluffy paws strum a miniature acoustic guitar, producing soft, melodic tunes... 🎶

🎥 Expected Output:
A short AI-generated video based on the given description.

🔗 References
Hugging Face - CogVideoX
Hugging Face - AnimateDiff
Diffusers Library
Gradio Documentation
📌 Notes
Ensure you have a GPU for better performance.
If using Google Colab, enable T4 or A100 GPU.
If running on Kaggle, make sure the Accelerator is set to GPU.
👨‍💻 Author
Meruva Peddababu

If you like this project, ⭐️ Star this repo and share your feedback! 😊🚀
