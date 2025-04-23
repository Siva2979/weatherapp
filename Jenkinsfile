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
                script {
                    if (isUnix()) {
                        sh 'docker build -t weather-app:latest .'
                    } else {
                        bat 'docker build -t weather-app:latest .'
                    }
                }
            }
        }
        
        stage('Run Docker Container') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            docker stop weather-app || true
                            docker rm weather-app || true
                            docker run -d -p 5000:5000 --env-file .env --name weather-app weather-app:latest
                        '''
                    } else {
                        bat '''
                            docker stop weather-app 2>nul || echo Container was not running
                            docker rm weather-app 2>nul || echo No container to remove
                            docker run -d -p 5000:5000 --env-file .env --name weather-app weather-app:latest
                        '''
                    }
                }
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