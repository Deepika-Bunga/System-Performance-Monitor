# 🖥️ System Performance Monitor 🚀

A real-time system monitoring tool that tracks **CPU, RAM, and Disk usage** dynamically. The data is displayed in an **interactive graph**, and a final report is saved as an image.

## 📌 Features
✅ **Real-time Monitoring** – Continuously tracks **CPU, RAM, and Disk usage**.  
✅ **Graphical Representation** – Uses `matplotlib` to visualize system performance.  
✅ **Efficient Data Handling** – Stores only the last 100 values to **prevent memory overflow**.  
✅ **Automated Report Generation** – Saves the final performance graph as `performance_report.png`.  

---

## 🔧 Installation
Make sure you have **Python 3+** installed. Then, install the required libraries:
```sh
pip install psutil matplotlib

**To run the program**
```sh
python monitor.py
