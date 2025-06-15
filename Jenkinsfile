pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/RehanRajpoot/form-app.git'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest > result.log'
            }
        }
    }
}
