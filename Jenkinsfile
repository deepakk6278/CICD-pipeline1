pipeline {
    agent any
    options { timestamps() }

    environment {
        AWS_REGION = 'ap-south-1'
        // Replace with your AWS account ID before running the ECR stages.
        AWS_ACCOUNT_ID = 'YOUR_AWS_ACCOUNT_ID'
        ECR_REPOSITORY = 'image-regi'
        IMAGE_NAME = 'frontend-cicd-project'
        ECR_REGISTRY = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"
        ECR_IMAGE = "${ECR_REGISTRY}/${ECR_REPOSITORY}:${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Build and Test') {
            steps {
                sh 'python3 -m py_compile app.py lambda_function.py'
                sh 'python3 -m pip install --user -r requirements.txt'
                sh '''python3 -c "from app import app; c=app.test_client(); assert c.get('/').status_code == 200; assert c.get('/health').status_code == 200; assert c.get('/api/student').status_code == 200; print('Application tests passed')"'''
            }
        }
        stage('Docker Build') {
            steps { sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .' }
        }
        stage('ECR Login') {
            steps {
                sh '''
                    test "${AWS_ACCOUNT_ID}" != "YOUR_AWS_ACCOUNT_ID"
                    aws ecr get-login-password --region "${AWS_REGION}" |
                    docker login --username AWS --password-stdin "${ECR_REGISTRY}"
                '''
            }
        }
        stage('Tag Image') {
            steps {
                sh 'docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${ECR_IMAGE}'
                sh 'docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${ECR_REGISTRY}/${ECR_REPOSITORY}:latest'
            }
        }
        stage('Push to ECR') {
            steps {
                sh 'docker push ${ECR_IMAGE}'
                sh 'docker push ${ECR_REGISTRY}/${ECR_REPOSITORY}:latest'
            }
        }
    }
    post {
        success { echo 'Build, tests, Docker image build, and ECR push completed.' }
        failure { echo 'Pipeline failed. Review the stage logs.' }
    }
}
