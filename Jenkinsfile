pipeline {
    agent any
    environment {
        NEW_VERSION = '1.2.1'
        // SERVER_CREDENTIALS = credentials('server-shuja')
    }
    stages {
        stage("build") {
            steps {
                echo 'building the app...'
                echo "building version ${NEW_VERSION}"
            }
        }
        stage("test") {
            when {
                expression {
                    BRANCH_NAME == 'test' || BRANCH_NAME == 'main'
                }
            }
            steps {
                echo 'testing the app...'
            }
        }
        stage("deploy") {
            steps {
                echo 'deploying the app...'
                withCredentials([
                    usernamePassword(credentials: 'server-shuja', usernameVariable: USER, passwordVariable: PWD)
                ]) {
                    echo "some shell command ${USER} ${PWD}"
                }
            }
        }
    }
    post {
        always {
            // Some task which needs, to be executed after all stages
        }
        success {
            // Task to be executed on succes only
        }
        failure {
            // Task to be executed on failure only
        }
    }
}
