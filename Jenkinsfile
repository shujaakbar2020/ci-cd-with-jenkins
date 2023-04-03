pipeline {
    agent any
    environment {
        NEW_VERSION = 'v1'
    }
    stages {
        stage("remove") {
            steps {
                sh "docker rmi saakbar/flask_rest_api:v1"
            }
        }
        stage("build") {
            steps {
                echo 'building the app...'
                echo "building version ${NEW_VERSION}"
                sh "docker build -t saakbar/flask_rest_api:v1 ."
                // sh "docker-compose build"
            }
        }
        stage("push") {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh "docker login -u $USERNAME -p $PASSWORD"
                    sh "docker push saakbar/flask_rest_api:v1"
                }
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
            environment {
                ANSIBLE_HOST_KEY_CHECKING = "False"
            }
            steps {
                // echo 'deploying the app...'
                // sh "docker-compose up -d"
                ansiblePlaybook (
                    playbook: 'first-playbook.yml'
                    inventory: 'hosts.ini'
                )
            }
        }
    }
    // post {
    //     always {
    //         // Some task which needs, to be executed after all stages
    //     }
    //     success {
    //         // Task to be executed on succes only
    //     }
    //     failure {
    //         // Task to be executed on failure only
    //     }
    // }
}
