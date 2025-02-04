# Reddit Data Engineering Project

A data engineering project that collects and processes Reddit data using modern data engineering tools and practices.

## Technologies Used
- Apache Airflow
- Docker & Docker Compose
- PostgreSQL
- Python
- PRAW (Python Reddit API Wrapper)

## Project Structure
```
reddit_analytics/
├── docker-compose.yml      # Docker services configuration
├── Dockerfile             # Airflow container configuration
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (not in git)
├── dags/                 # Airflow DAGs
│   ├── __init__.py
│   └── reddit_dag.py     # Main DAG file
└── scripts/              # Utility scripts
    └── reddit_fetcher.py # Reddit data collection script
```

## Setup Instructions

1. Clone the repository:
```bash
git clone [your-repo-url]
cd reddit_analytics
```

2. Create a `.env` file with your Reddit API credentials:
```
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=MyBot/1.0
```

3. Build and start the containers:
```bash
docker-compose up --build
```

4. Access Airflow web interface:
- URL: http://localhost:8080
- Username: airflow
- Password: airflow
