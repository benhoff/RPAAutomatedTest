pipeline {
    agent {
        label 'Windows10'
    }

    stages {

        stage ("Test pull"){
            steps{
                echo 'checkout the Test'
                checkout scm
            }
        }

        stage('Robot Pull') {
            steps {
                echo 'checkout the robot'
                dir('Robot') {
                git branch: 'master', url: 'https://github.com/petoandroide/giftList'
                }
            }
        }
        stage('Create virtual env') {
            steps {
                echo 'Testing'
                    sh """
                        python -m virtualenv env
                        """
                    
                    sh """
                        .env/Scripts/activate
                        python -m pip install -r requirements.txt
                        """
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
            }
        }
    }
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}