pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                    userRemoteConfigs: [[
                        url: 'https://github.com/rohithreddy-41/ai-devops-mini-project',
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
        bat 'set PYTHONIOENCODING=utf-8 && python ml/analyze_build.py'
    }
}

        stage('Build App') {
            steps {
                bat 'python app/main.py'
            }
        }
    }
}
i
