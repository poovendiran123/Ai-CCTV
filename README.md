# AI CCTV Surveillance System

An AI-powered CCTV surveillance system built using **Python**, **YOLOv8**, **OpenCV**, and **Streamlit**. The system automatically detects people in real time, captures evidence, records video with timestamps, sends instant alerts via WhatsApp and Email, and stores detection history in Excel.

---

## 🚀 Features

* 🎯 Real-time person detection using YOLOv8
* 📷 Automatic image capture on detection
* 🎥 10-second video recording with date & time watermark
* 🌙 Night vision enhancement for low-light environments
* 📧 Email alert with image and video attachments
* 💬 WhatsApp notification using Twilio
* 📊 Detection history stored in Excel
* ⏳ Cooldown mechanism to prevent repeated alerts
* 🖥️ Streamlit dashboard to Start/Stop the CCTV system

---

## 🛠️ Technologies Used

* Python 3.x
* OpenCV
* YOLOv8 (Ultralytics)
* Streamlit
* Twilio API
* SMTP (Gmail)
* OpenPyXL
* FFmpeg

---

## 📂 Project Structure

```text
AI-CCTV/
│
├── main.py                 # AI CCTV detection system
├── app.py                  # Streamlit dashboard
├── email.env               # Environment variables (Not uploaded)
├── detection_history.xlsx  # Detection logs
├── alert.jpg               # Captured image
├── alert.mp4               # Recorded video
├── status.txt              # Camera ON/OFF status
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AI-CCTV.git

cd AI-CCTV
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Download FFmpeg and update the FFmpeg executable path inside the project.

Create an `email.env` file and configure:

```env
SENDER_EMAIL=your_email@gmail.com
APP_PASSWORD=your_app_password
RECEIVER_EMAIL=receiver@gmail.com

TWILIO_ACCOUNT_SID=xxxxxxxxxxxx
TWILIO_AUTH_TOKEN=xxxxxxxxxxxx

TWILIO_FROM=whatsapp:+14155238886
TWILIO_TO=whatsapp:+91xxxxxxxxxx
```

---

## ▶️ Run the Project

Run the AI CCTV system:

```bash
python main.py
```

Or launch the Streamlit dashboard:

```bash
streamlit run app.py
```

---

## 📷 Workflow

1. Camera captures live video.
2. YOLOv8 detects people in real time.
3. Bounding boxes and confidence scores are displayed.
4. Snapshot is captured.
5. A 10-second video is recorded with timestamp.
6. WhatsApp alert is sent.
7. Email with image and video attachments is sent.
8. Detection details are stored in an Excel log.
9. Cooldown timer prevents duplicate alerts.

---

## 📊 Detection Log

Each detection records:

* Detection Time
* Person Count
* Alert Status
* Image Name
* Video Name

---

## 🔐 Security

* Store credentials in `.env`.
* Never commit `.env` to GitHub.
* Add `.env`, generated videos, images, and Excel logs to `.gitignore`.

Example:

```gitignore
.env
*.xlsx
*.mp4
*.jpg
__pycache__/
```

---

## 📌 Future Improvements

* Mobile application integration
* Live video streaming
* Cloud storage support
* Face recognition
* Intrusion detection
* Multi-camera monitoring
* Remote control dashboard
* SMS and Push notifications

---

## 👨‍💻 Author

**Surya Pachai**

AI Developer | Computer Vision | Python | YOLOv8 | OpenCV | Streamlit

---

## ⭐ If you like this project

Please give this repository a ⭐ on GitHub.
