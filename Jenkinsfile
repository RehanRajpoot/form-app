pipeline {
    agent any

    environment {
        PYTHON = "C:/Users/user/AppData/Local/Programs/Python/Python313/python.exe"
        PIP = "C:/Users/user/AppData/Local/Programs/Python/Python313/Scripts/pip.exe"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/RehanRajpoot/form-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat "${PYTHON} -m pip install --upgrade pip"
                bat "${PYTHON} -m pip install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                bat "${PYTHON} -m pytest > result.log"
            }
        }

        stage('Show Test Results') {
            steps {
                bat 'type result.log'
            }
        }

        // Optional future stage
        // stage('Deploy') {
        //     steps {
        //         echo "Deploying Flask app..."
        //         // You can run: bat "${PYTHON} app.py" or use a deploy script
        //     }
        // }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            deleteDir()
        }

        success {
            echo '✅ Build succeeded!'
        }

        failure {
            echo '❌ Build failed. Check the result.log output.'
        }
    }
}
