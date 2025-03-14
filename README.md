# StartupMania 🚀  
**Your gateway to automating startup creation and exploring innovation!**  

StartupMania is a Django-powered platform that enables users to discover, track, and support the automation of startup creation. With a focus on transparency and community engagement, this project demonstrates the power of AI in entrepreneurship by showcasing automated startup creation.  

--- 

## Features

- **Home Page**: Includes a user-friendly landing page with:  
  - A form to subscribe with an email for updates.  
  - An option to financially support the project.  
  - Live counters displaying:  
    - Total startups created.  
    - Startup creation rate.  
    - Total site visits.  
    - Most popular startup.

- **Startups Page**: A list of all created startups with:  
  - Detail views for each startup.  
  - Links to visit the startup websites. 

  - **Challenge Page**: A dedicated section for the project’s blog, where the journey and challenges are documented. 

  - **Documentation Page**: Comprehensive guides on the project, explaining its technical aspects and usage.  

  - **Contact Page**: A form for users to reach out with queries or suggestions.  

## Admin Dashboard  
- **Accessible only by Admins**:  
  - Manage startups, users, and site content.  
  - Monitor alerts and notifications set by users.  
  - View metrics for startups and site visits.

## Registered Users Features  
- **User Alerts**: Set notifications for project progress updates. 

### Backend Features  
- **Automated Startup Creation**:  
  - Integrated workflows for scraping ideas, generating web apps, and deploying them automatically.  
  - All automated processes are centralized in the `core` app.

---

## Installation 

### Installation Steps  

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/yourusername/StartupMania.git
   cd StartupMania
   ```
2. **Set Up a Virtual Environment**:
```bash
python -m venv venv
venv\Scripts\activate # for linux, use source venv/bin/activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Set up Environmental Variables**:
- Create a .env file in the project root directory with the following variables:
```plaintext
SECRET_KEY=
DEBUG=True
DB_USER=
DB_PASSWORD=
OPENAI_API_KEY=
```

5. **Run Migrations**:

```bash
python manage.py migrate
```

6. **Start the server**:
```bash
python manage.py runserver
```

## Usage

### Access the plateform
1. Open a web browser and navigate to http://127.0.0.1:8000

### Admin Dashboard
1. Log as an admin to access advanced features and manage the plateform
2. Use python manage.py createsuperuser to create an admin account
