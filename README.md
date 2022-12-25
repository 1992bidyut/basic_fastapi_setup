# pmps-backend setup

#Step 1: Commands
1. sudo pip install pipenv
2. pipenv install --three fastapi fastapi-sqlalchemy pydantic alembic psycopg2 uvicorn
3. pip install virtualenv
4. python3.6 -m venv pvenv
5. pip install -r requirements.txt
6. source pvenv/bin/activate

#Step 2: Install the DOCKER in your system
Docker Commands
1. docker-compose build [for build the containers]
2. docker-compose up [for run the containers]

#RUN project with UVICORN
uvicorn app.main:app --host 0.0.0.0 --port 9000 --reload

#Alembic Migration Command
1. alembic revision --autogenerate -m "message"
2. alembic upgrade head
3. alembic upgrade heads
4. alembic downgrade -1 [back to previous]
5. alembic merge heads [If multiple heads exists]
6. alembic history [to see all migration history and sequence]


#Alembic migration with Docker
1. docker-compose run pmps_api alembic revision --autogenerate -m "message"
2. docker-compose run pmps_api alembic heads