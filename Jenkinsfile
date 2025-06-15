pipeline {
    agent any

    environment {
        PYTHON = "C:/Users/user/AppData/Local/Programs/Python/Python313/python.exe"
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
                bat "${PYTHON} -m pytest > result.log 2>&1"
            }
        }

        stage('Show Test Results') {
            steps {
                script {
                    def testLog = readFile('result.log')
                    echo "📄 Test Results:\n${testLog}"
                }
            }
        }

        // Optional Deployment Stage
        // stage('Deploy') {
        //     steps {
        //         bat "${PYTHON} app.py"
        //     }
        // }
    }

    post {
        always {
            echo '🧹 Cleaning up workspace...'
            deleteDir()
        }

        success {
            echo '✅ Build succeeded!'
        }

        failure {
            echo '❌ Build failed. Check the test results above.'
        }
    }
}
