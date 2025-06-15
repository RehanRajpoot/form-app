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
                bat 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python311\\python.exe -m pytest > result.log'
            }
        }
    }
}
