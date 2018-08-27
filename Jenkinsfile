node('host_1') {
    agent any

    stages {
        stage('Build') {
            steps {
            
             sh 'docker_compose up --build' 
            }
        }
    }
}
