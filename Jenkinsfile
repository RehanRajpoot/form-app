pipeline {
    agent any

    environment {
        PYTHON = "C:/Python311/python.exe"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/RehanRajpoot/form-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat "${env.PYTHON} -m pip install --upgrade pip"
                bat "${env.PYTHON} -m pip install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                bat "${env.PYTHON} -m pytest > result.log"
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            deleteDir()
        }

        success {
            echo 'Build succeeded!'
        }

        failure {
            echo 'Build failed. Check the logs.'
        }
    }
}
