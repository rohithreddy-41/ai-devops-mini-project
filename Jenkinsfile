pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/rohithreddy-41/ai-devops-mini-project.git-'
            }
        }

        stage('Install Requirements') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run AI Prediction') {
            steps {
                sh 'python3 ml/analyze_build.py'
            }
        }

        stage('Build App') {
            steps {
                sh 'python3 app/main.py'
            }
        }
    }
}

