<div class="hero-icon" align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</div>

<h1 align="center">
AI Query Backend - MVP
</h1>
<h4 align="center">A Python backend service that simplifies user interactions with OpenAI's language models.</h4>
<h4 align="center">Developed with the software and tools below.</h4>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Framework-FastAPI-blue" alt="Framework: FastAPI">
  <img src="https://img.shields.io/badge/Language-Python-red" alt="Language: Python">
  <img src="https://img.shields.io/badge/Database-PostgreSQL-blue" alt="Database: PostgreSQL">
  <img src="https://img.shields.io/badge/LLMs-OpenAI-black" alt="LLMs: OpenAI">
</div>
<div class="badges" align="center">
  <img src="https://img.shields.io/github/last-commit/coslynx/AI-Query-Backend-MVP?style=flat-square&color=5D6D7E" alt="git-last-commit" />
  <img src="https://img.shields.io/github/commit-activity/m/coslynx/AI-Query-Backend-MVP?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
  <img src="https://img.shields.io/github/languages/top/coslynx/AI-Query-Backend-MVP?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

## 📑 Table of Contents
- 📍 Overview
- 📦 Features
- 📂 Structure
- 💻 Installation
- 🏗️ Usage
- 🌐 Hosting
- 📄 License
- 👏 Authors

## 📍 Overview

This repository contains a Minimum Viable Product (MVP) for an AI Query Backend. It simplifies the process of interacting with OpenAI's language models by providing a Python-based backend service. 

## 📦 Features
|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a layered architecture with separate directories for API routes, schemas, utilities, and database interactions, promoting modularity and maintainability. |
| 📄 | **Documentation**  | The repository includes a README file providing a detailed overview of the MVP, its dependencies, and usage instructions.|
| 🔗 | **Dependencies**   | The codebase utilizes essential libraries like `fastapi`, `openai`, `jwt`, `sqlalchemy`, `psycopg2-binary`, and `python-dotenv` for API development, OpenAI integration, authentication, database management, and environment configuration. |
| 🧩 | **Modularity**     | The modular structure promotes easier maintenance and code reusability, with dedicated sections for API routes, data schemas, utility functions, and database interactions. |
| 🧪 | **Testing**        | Includes unit tests using Pytest to ensure the reliability and robustness of the codebase.       |
| ⚡️  | **Performance**    | Employs efficient coding practices and considers performance optimization strategies for efficient data processing and response generation. |
| 🔐 | **Security**       | Enhances security through input validation, secure data storage, and authentication using JWT. |
| 🔀 | **Version Control**| Utilizes Git for version control with automated CI/CD workflows for building and deploying the application.|
| 🔌 | **Integrations**   |  Integrates with the OpenAI API for generating responses to user queries.|
| 📶 | **Scalability**    | The backend is designed to handle increasing user load and data volume, utilizing efficient database management techniques and caching strategies.           |

## 📂 Structure
```text
└── api
    ├── routers
    │   ├── query_router.py
    │   └── auth_router.py
    ├── schemas
    │   └── schemas.py
    ├── utils
    │   └── utils.py
    ├── database
    │   ├── database.py
    │   └── models.py
    └── main.py
```

## 💻 Installation
### 🔧 Prerequisites
- Python 3.9+
- PostgreSQL 15+
- Docker (recommended)

### 🚀 Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/coslynx/AI-Query-Backend-MVP.git
   cd AI-Query-Backend-MVP
   ```
2. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   ```
3. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit the .env file with your OpenAI API key, database credentials, and JWT secret key. 
   ```

## 🏗️ Usage
### 🏃‍♂️ Running the MVP
1. Start the FastAPI application:
   ```bash
   uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
   ```

### ⚙️ Configuration
- The `.env` file is used for storing sensitive environment variables such as OpenAI API key, database connection URL, and JWT secret key.
- Modify these values in the `.env` file before running the application.

### 📚 Examples
- **Send a query to the AI Query Backend:**
   ```bash
   curl -X POST http://localhost:8000/query \
   -H "Content-Type: application/json" \
   -d '{"model": "text-davinci-003", "query": "What is the meaning of life?", "temperature": 0.7, "max_tokens": 256}' 
   ```
   **Response:**
   ```json
   {
     "id": 1,
     "model": "text-davinci-003",
     "query": "What is the meaning of life?",
     "response": "The meaning of life is a question that has been pondered by philosophers and theologians for centuries. There is no one definitive answer, as each individual must ultimately decide for themselves what meaning they find in life.",
     "created_at": "2024-01-01T12:00:00.000Z"
   }
   ```

## 🌐 Hosting
### 🚀 Deployment Instructions
1.  **Build the Docker image:** 
    ```bash
    docker build -t ai-query-backend .
    ```
2.  **Push the Docker image to a registry (e.g., Docker Hub):**
    ```bash
    docker push your_dockerhub_username/ai-query-backend:latest
    ```
3.  **Deploy to a cloud platform (e.g., Heroku):**
    - Follow Heroku's deployment instructions for Docker images.
    - Ensure that the required environment variables are set in the Heroku app's settings.
    - Refer to the [Heroku documentation](https://devcenter.heroku.com/articles/container-registry-and-runtime) for detailed instructions.

### 🔑 Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key.
- `DATABASE_URL`: The connection URL for your PostgreSQL database.
- `JWT_SECRET_KEY`: A strong, unique secret key for JWT authentication.

## 📜 API Documentation
### 🔍 Endpoints
- **POST /query**:
    - Description: Sends a query to the chosen OpenAI model and returns the response.
    - Body:
        ```json
        {
          "model": "text-davinci-003", // OpenAI model name
          "query": "What is the meaning of life?", // User query
          "temperature": 0.7, // Controls the creativity of the response
          "max_tokens": 256 // Maximum number of tokens in the response
        }
        ```
    - Response:
        ```json
        {
          "id": 1,
          "model": "text-davinci-003",
          "query": "What is the meaning of life?",
          "response": "The meaning of life is a question that has been pondered by philosophers and theologians for centuries. There is no one definitive answer, as each individual must ultimately decide for themselves what meaning they find in life.",
          "created_at": "2024-01-01T12:00:00.000Z"
        }
        ```
- **POST /token**:
    - Description: Generates a JWT token for authentication.
    - Body:
        ```json
        {
          "username": "your_username",
          "password": "your_password"
        }
        ```
    - Response:
        ```json
        {
          "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0dXNlciIsImV4cCI6MTY3NzU3NjI0N30.U4R70F7v3K_C0xR2bLq972843q66u6o98V0jD2o9s_w"
        }
        ```

### 🔒 Authentication
- JWT (JSON Web Token) is used for authentication.
- Upon successful registration or login, a JWT token is issued to the user.
- This token should be included in the Authorization header of subsequent requests to protected API endpoints.

### 📝 Examples
```bash
# Register a new user
curl -X POST http://localhost:8000/token \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "password": "testpassword"}' 

# Response
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0dXNlciIsImV4cCI6MTY3NzU3NjI0N30.U4R70F7v3K_C0xR2bLq972843q66u6o98V0jD2o9s_w"
}

# Send a query using the generated JWT token 
curl -X POST http://localhost:8000/query \
-H "Content-Type: application/json" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0dXNlciIsImV4cCI6MTY3NzU3NjI0N30.U4R70F7v3K_C0xR2bLq972843q66u6o98V0jD2o9s_w" \
-d '{"model": "text-davinci-003", "query": "What is the meaning of life?", "temperature": 0.7, "max_tokens": 256}' 
```


## 📜 License & Attribution

### 📄 License
This Minimum Viable Product (MVP) is licensed under the [GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/) license.

### 🤖 AI-Generated MVP
This MVP was entirely generated using artificial intelligence through [CosLynx.com](https://coslynx.com).

No human was directly involved in the coding process of the repository: AI-Query-Backend-MVP

### 📞 Contact
For any questions or concerns regarding this AI-generated MVP, please contact CosLynx at:
- Website: [CosLynx.com](https://coslynx.com)
- Twitter: [@CosLynxAI](https://x.com/CosLynxAI)

<p align="center">
  <h1 align="center">🌐 CosLynx.com</h1>
</p>
<p align="center">
  <em>Create Your Custom MVP in Minutes With CosLynxAI!</em>
</p>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Developers-Drix10,_Kais_Radwan-red" alt="">
  <img src="https://img.shields.io/badge/Website-CosLynx.com-blue" alt="">
  <img src="https://img.shields.io/badge/Backed_by-Google,_Microsoft_&_Amazon_for_Startups-red" alt="">
  <img src="https://img.shields.io/badge/Finalist-Backdrop_Build_v4,_v6-black" alt="">
</div>