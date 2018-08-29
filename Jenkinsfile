pipeline {
     agent {
       label 'host_1'
    }
    triggers {
        cron('H */1 * * *')
    }
    stages {
        stage('git_clone') {
            steps {
                 git 'https://github.com/zevs00807/DevOps.git'
            }
        }
        stage('docker-up') {
            steps {
                  sh 'users && groups'
                  sh 'docker-compose up --build -d'
            }
        }
            
        }
    }
