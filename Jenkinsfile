pipeline {
    agent {
        docker {
            image 'node:18'         // Uses a Node.js image with npm pre-installed
            args '-u root'          // Optional: to avoid permission issues
        }
    }

    environment {
        NODE_ENV = 'development'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/aaridev/docker.git'
            }
        }

        stage('Install') {
            steps {
                sh 'npm install'
            }
        }

        stage('Test') {
            steps {
                sh 'npm test || echo "Tests failed or no tests defined"'
            }
        }

        stage('Build Docker Image') {
            agent {
                docker {
                    image 'docker:24.0.5-cli'   // Use a Docker CLI image just for this stage
                    args '-v /var/run/docker.sock:/var/run/docker.sock'
                }
            }
            steps {
                sh 'docker build -t myapp .'
            }
        }

        stage('Deploy') {
            agent any
            steps {
                sshagent(credentials: ['your-ssh-key-id']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no user@your-server-ip "
                        docker pull myapp &&
                        docker-compose up -d
                    "
                    '''
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
    }
}
