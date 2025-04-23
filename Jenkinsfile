pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t weather-app:latest .'
            }
        }
        
        stage('Run Docker Container') {
            steps {
                bat 'docker stop weather-app || true'
                bat 'docker rm weather-app || true'
                bat 'docker run -d -p 5000:5000 --name weather-app weather-app:latest'
            }
        }
    }
    
    post {
        failure {
            echo 'Pipeline failed'
        }
        success {
            echo 'Pipeline succeeded! The application is running at http://localhost:5000'
        }
    }
}