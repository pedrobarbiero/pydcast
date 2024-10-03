# Pydcast Aggregator

## Overview
Pydcast Aggregator is a tool designed to collect and organize the latest tech podcasts from various sources, making it easy for users to stay updated with the latest trends and discussions in the tech world.

## Features
- Aggregates podcasts from multiple sources
- User-friendly interface
- Regular updates with the latest episodes

## Running local
To run Pydcast Aggregator locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone git@github.com:pedrobarbiero/pydcast.git
    ```
2. Navigate to the project directory:
    ```bash
    cd pydcast
    ```
3. Build docker:
    ```bash
    docker-compose build
    ```
4. Start the application:
    ```bash
    docker-compose up -d
    ```
5. Start jobs to fetch episodes:
    ```bash
    docker-compose exec web python manage.py startjobs
    ```

## Usage
1. Open your browser and go to `http://localhost:8000/`.
2. Browse through the list of available tech podcasts.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
If you have any questions or suggestions, feel free to reach out to us at [pedrohenriquebarbiero@hotmail.com].

