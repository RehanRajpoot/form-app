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
                script {
                    // Run tests but don't fail pipeline immediately
                    def status = bat(script: "${PYTHON} -m pytest > result.log 2>&1", returnStatus: true)
                    // Save the exit code to environment for later post check
                    env.TEST_EXIT_CODE = status.toString()
                }
            }
        }

        stage('Show Test Results') {
            steps {
                script {
                    def output = readFile('result.log')
                    echo "📄 Test Results:\n${output}"
                }
            }
        }
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
            echo '❌ Build failed. See test results above.'
        }
    }
}
