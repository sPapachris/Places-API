# Places API

## Requirements
- blinker           1.6.2
- click             8.1.6
- colorama          0.4.6
- Flask             2.3.2
- Flask-SQLAlchemy  3.0.5
- greenlet          2.0.2
- itsdangerous      2.1.2
- Jinja2            3.1.2
- MarkupSafe        2.1.3
- pip               23.1.2
- setuptools        65.5.0
- SQLAlchemy        2.0.19
- typing_extensions 4.7.1
- Werkzeug          2.3.7

## Getting Started

1. **Clone the Repository:**

   Clone your GitHub repository to your local machine. You can do this by using the following command in your terminal:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```

   Replace `your-username` and `your-repo` with your actual GitHub username and repository name.

2. **Navigate to Project Directory:**

   Navigate to the cloned repository directory:

   ```bash
   cd your-repo
   ```

3. **Create and Activate Virtual Environment:**

   Create a virtual environment named `venv`:

   On macOS or Linux:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   On Windows:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   After activation, your terminal prompt should change, indicating that you are now within the virtual environment.

4. **Install Dependencies:**

   While the virtual environment is active, install the required packages from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Flask App:**

   Now you can run the Flask app:

   ```bash
   python main.py
   ```

   Flask app should start running, and you'll see output indicating that the development server is running.

6. **Access the App:**

   Open your web browser and navigate to `http://127.0.0.1:5000/` (or `http://localhost:5000/`). You should see the output of your running Flask app.

Remember that whenever you want to work on your project, you should activate the virtual environment first using the appropriate activation command (`source venv/bin/activate` on macOS/Linux or `venv\Scripts\activate` on Windows).

When you're done working on your project, you can deactivate the virtual environment:

```bash
deactivate
```

This will return you to your system's global Python environment.

By following these steps, you're setting up your Flask project within a virtual environment, ensuring that the project's dependencies are isolated from your system-wide Python environment.