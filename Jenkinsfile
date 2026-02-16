pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
                echo 'Code checked out'
            }
        }

        stage('Show Changes') {
            steps {
                sh 'git diff --name-status HEAD~1 HEAD || echo "No previous commit to compare"'
            }
        }

        stage('Build') {
            steps {
                echo 'Build step running'
            }
        }
    }
}
