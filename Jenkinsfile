pipeline {
    agent any

    environment {
        AWS_REGION = 'eu-north-1'
        ECR_REPOSITORY = 'cicd-demo'
        AWS_ACCOUNT_ID = '847263216766'
        IMAGE_NAME = '847263216766.dkr.ecr.eu-north-1.amazonaws.com/cicd-demo'
    }

    stages {
        stage('Build and Test') {
            steps {
                sh '''
                    set -e

                    echo "Checking Python version"
                    python3 --version

                    echo "Creating Python virtual environment"
                    python3 -m venv .venv

                    echo "Installing project dependencies"
                    .venv/bin/python -m pip install -r requirements.txt

                    echo "Checking Python files"
                    .venv/bin/python -m py_compile app.py lambda_function.py

                    echo "Build and Test completed successfully"
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    set -e
                    docker build -t ${ECR_REPOSITORY}:${BUILD_NUMBER} .
                    docker tag ${ECR_REPOSITORY}:${BUILD_NUMBER} ${IMAGE_NAME}:${BUILD_NUMBER}
                    docker tag ${ECR_REPOSITORY}:${BUILD_NUMBER} ${IMAGE_NAME}:latest
                '''
            }
        }

        stage('ECR Login') {
            steps {
                sh '''
                    set -e
                    aws ecr get-login-password --region ${AWS_REGION} |
                    docker login \
                        --username AWS \
                        --password-stdin \
                        ${IMAGE_NAME%/*}
                '''
            }
        }

        stage('Push to ECR') {
            steps {
                sh '''
                    set -e
                    docker push ${IMAGE_NAME}:${BUILD_NUMBER}
                    docker push ${IMAGE_NAME}:latest
                '''
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: Pipeline completed successfully!'
        }

        failure {
            echo 'FAILED: Check the Jenkins Console Output for details.'
        }
    }
}
