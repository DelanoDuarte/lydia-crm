# Running

## Running separated environments

### Setup 
```
python install -r requirements.txt
```

#### Execute Django Migrations
```
python manage.py makemigrations

python manage.py migrate
```

#### Run Local Server
```
python manage.py runserver
```

### Web

#### Project setup
```
npm install
```

#### Compiles and hot-reloads for development
```
npm run serve
```

#### Compiles and minifies for production
```
npm run build
```

#### Run your unit tests
```
npm run test:unit
```

## Running with Docker

#### Build Image
```
docker-compose build
```

#### Start Container
```
docker-compose up
```

#### Testing on Browser

http://127.0.0.1:8080