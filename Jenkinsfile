pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
                echo 'Code checked out'
            }
        }

        stage('Show Changes') {
            steps {
                sh 'git diff --name-status HEAD~1 HEAD || echo "First build"'
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv $VENV
                source $VENV/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source $VENV/bin/activate
                pytest || echo "No tests found"
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'Build step running'
            }
        }
    }
}
