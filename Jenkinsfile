pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/tejaswi9728/todo-flask-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t todo-flask-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 todo-flask-app'
            }
        }
    }
}