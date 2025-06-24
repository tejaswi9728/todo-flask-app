pipeline {
    agent any


    stages {
        stage('Clone Repo') {
           steps {
               git 'https://github.com/tejaswi9728/todo-cli-app.git'
           }
        }
        stage('Build Docker Image') {
           steps {
               sh 'docker build -t todo-cli-app .'
           }
        }
        stage('Run Docker Container') {
           steps {
               sh 'docker run -d --name todo-container todo-cli-app'
           }
        }
    }
}
