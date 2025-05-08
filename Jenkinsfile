pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                    userRemoteConfigs: [[
                        url: 'https://github.com/rohithreddy-41/ai-devops-mini-project.git-',
                        credentialsId: 'github-token'
                    ]],
                    branches: [[name: '*/main']]
                ])
            }
        }

        stage('Install Requirements') {
            steps {
                bat 'pip install -r requirements.txt'
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
i
