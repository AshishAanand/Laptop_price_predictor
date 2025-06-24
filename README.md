
---

# 💻 Laptop Price Predictor 🧠

A machine learning project that predicts the price of laptops based on key specifications like brand, RAM, CPU, storage type, GPU, screen resolution, and more. Built using a fully modular pipeline architecture, this project demonstrates feature engineering, data cleaning, model building, and end-to-end deployment readiness.

---

## 🚀 Features

- Cleans and preprocesses real-world messy laptop data
- Extracts structured features like CPU brand, Height, Width, Weight, GPU type, etc.
- One-hot encodes categorical variables and scales numerical features
- Fully integrated sklearn `Pipeline`
- Saves and loads the entire pipeline using `joblib`
- Ready for prediction on raw user input

---

## 📁 Project Structure

<pre>Laptop_price_predictor/
  ├── src/ 
  ├── data/ # Raw and cleaned datasets 
  ├── models/ # Saved pipeline (.pkl) 
  ├── notebooks/ # Data exploration and model training 
  └── utils/ # Helper functions (clean_data) 
  ├── main.py # Entry script for training or pipeline usage 
  ├── requirements.txt 
  └── README.md</pre>


---

## 🧠 Tech Stack

- **Python 3.11+**
- **scikit-learn**
- **pandas**
- **NumPy**
- **Matplotlib / Seaborn (EDA)**
- **Jupyter Notebook**
- **joblib**

---

## 📊 Model Evaluation Metrics

- **R² Score**
- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**

---

## 🔧 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Laptop_price_predictor.git
   cd Laptop_price_predictor

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Or open the notebooks:

   ```bash
   jupyter notebook src/notebooks/model_releated/model.ipynb
   ```

---

## 📂 Dataset

* Used a dataset with features like:

  * `Company`, `TypeName`, `ScreenResolution`, `Cpu`, `Ram`, `Memory`, `Gpu`, `Weight`, `OpSys`, and `Price`.

---

## 📌 Future Work

* Add Streamlit or Flask deployment for user input + live predictions
* Export prediction results in CSV format
* Add support for model explainability (SHAP, LIME)

---

## 🤝 Contributing

Feel free to fork this repo, submit pull requests, or suggest features or improvements.

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments

* Inspired by real-world product price prediction challenges
* Guided by scikit-learn best practices and modular ML design

---

### Made with ❤️ by [Ashish Anand](https://github.com/yourusername)
