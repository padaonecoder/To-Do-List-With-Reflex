# 📝 Reflex To-Do List

A simple and elegant to-do list web app built with [Reflex](https://reflex.dev), a Python framework for building reactive web applications.

---

## 🚀 Features

- ✅ Add tasks  
- 🔄 Mark tasks as completed  
- ❌ Delete tasks  
- 🌗 Toggle between light and dark mode  
- ⚡ Built with Python and Reflex


## 📦 Installation

### 1. Clone the repository
git clone https://github.com/tu_usuario/reflex-todo-list.git
cd reflex-todo-list

### 2. Install dependencies
Make sure you have Python 3.10+ and Reflex installed. If not, install Reflex:
pip install reflex

### 3. Run the app
reflex run


🧠 How It Works
The app uses a reactive state (State) to manage tasks. Each task is a dictionary with text and done fields. Users can:
- Add a task via the input field.
- Toggle completion status by clicking the checkbox.
- Delete a task by clicking the ❌ icon.
The UI is built using Reflex components like vstack, hstack, input, button, and foreach.


📂 Project Structure
reflex-todo-list/
├── __init__.py
├── main.py         # Contains the app logic and UI
├── README.md

🌐 Deployment
You can deploy the app using Reflex's built-in deployment tools or host it on platforms like Vercel or Netlify after exporting it as a static site:
reflex export

🛠 Technologies Used
- 🐍 Python 3.10+
- ⚛️ Reflex
- 💡 Reactive programming

🤝 Contributing
Pull requests are welcome! If you find a bug or want to suggest a feature, feel free to open an issue.

