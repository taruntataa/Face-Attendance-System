# Face Recognition Attendance System

An automated **Attendance Management System** that uses **Face Recognition** to mark and store attendance securely. 
This project helps replace manual roll calls with a faster and more reliable solution.

## 🚀 Features
- 📸 Face detection & recognition using OpenCV
- 📝 Automatic attendance logging in CSV/Excel format
- 🕒 Real-time recognition via webcam
- 🗂️ Easy-to-use project structure
- ✅ Human-friendly and customizable

## 🛠️ Tech Stack
- Python 3.x  
- OpenCV – for face detection & recognition  
- NumPy & Pandas – for data handling  
- Tkinter / Flask (if UI included) – for interface  

## 📂 Project Structure
```

face-attendance/
│── data/               # Stores face data/images
│── attendance/         # CSV/Excel attendance logs
│── src/                # Main source code
│   ├── train.py        # Train face recognition model
│   ├── recognize.py    # Recognize faces & mark attendance
│   └── utils.py        # Helper functions
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation
│── main.py             # Entry point

````

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/face-attendance.git
   cd face-attendance
```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the system:

   ```bash
   python main.py
   ```

## 🎯 Usage

* Run `main.py` to start webcam face recognition.
* When a registered face is detected, attendance is automatically recorded in the `attendance/` folder.
* To add a new student/employee, capture their images in `data/` and retrain the model with `train.py`.

## 📊 Output Example

* **Attendance file** (`attendance/2025-09-10.csv`)

  ```
  Name, ID, Time
  John Doe, 101, 09:45:23
  Jane Smith, 102, 09:47:10
  ```

## 🔮 Future Improvements

* Cloud integration for attendance storage
* Mobile app sync
* Improved face recognition with Deep Learning

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

## 📜 License

This project is licensed under the **MIT License**.

## Project Done By -
Tarun Tata and Priya Darshini Sadula
