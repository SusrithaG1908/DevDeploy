
pipeline {
    agent any

    environment {
        PIP_DISABLE_PIP_VERSION_CHECK = '1'
        DOCKER_IMAGE = 'susrithag/devdeploy-app'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh 'python3 -m pip install --break-system-packages --default-timeout=300 --retries=10 -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running application tests...'
                sh 'python3 -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build --build-arg BUILDKIT_INLINE_CACHE=1 --tag $DOCKER_IMAGE:$BUILD_NUMBER --tag $DOCKER_IMAGE:latest .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_TOKEN'
                )]) {
                    sh '''
                        echo "$DOCKER_TOKEN" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push "$DOCKER_IMAGE:$BUILD_NUMBER"
                        docker push "$DOCKER_IMAGE:latest"
                        docker logout
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'CI/CD pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
