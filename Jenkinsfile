
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'student-management'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv ci-venv
                    ci-venv/bin/pip install -r application/requirements.txt
                    ci-venv/bin/pip install pytest
                '''
            }
        }

        stage('Automated Testing') {
            steps {
                sh '''
                    ci-venv/bin/pytest tests/ -v
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    docker build \
                    -t ${IMAGE_NAME}:${BUILD_NUMBER} \
                    -t ${IMAGE_NAME}:latest \
                    -f docker/Dockerfile .
                '''
            }
        }

        stage('Verify Docker Image') {
            steps {
                sh 'docker images student-management'
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the console output.'
        }

        always {
            echo 'Pipeline execution finished.'
        }
    }
}
