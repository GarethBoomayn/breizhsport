# Breizhsport Project

## Overview
Breizhsport is an e-commerce platform for selling sports equipment online. This project modernizes the system by implementing a cloud-native architecture, integrating CI/CD, and ensuring security best practices.

## Features
- User authentication & management
- Product catalog with stock tracking
- Order processing
- RESTful API using FastAPI
- Database integration with SQLAlchemy
- Dockerized deployment

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd breizhsport-main
   ```
2. Start services using Docker:
   ```bash
   docker-compose up --build
   ```
3. Access API documentation:
   - Open [http://localhost:8000/docs](http://localhost:8000/docs)

## Contributing
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with detailed changes.

## Future Enhancements
- Implement authentication & authorization
- Add unit and integration tests
- Deploy to a cloud provider (AWS/GCP)

For more details, refer to the `docs/` folder.

