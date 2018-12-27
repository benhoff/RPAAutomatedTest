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
                dir('giftList') {
                git branch: 'master', url: 'https://github.com/petoandroide/giftList'
                }
            }
        }
        stage('Create virtual env') {
            steps {
                echo 'Downloading dependencies'
                withPythonEnv('C:\\Program Files\\Python37\\python') {
	                bat 'pip install -r requirements.txt'
                }

            }
        }
        stage('Testing') {
            steps {
                echo 'Testing'
                withPythonEnv('C:\\Program Files\\Python37\\python') {
	                bat 'behave test --junit'
                }
            }
        }
    }
    post {
        always {
            echo 'This will always run'
            echo 'Generating test report'
            withPythonEnv('C:\\Program Files\\Python37\\python') {
                bat 'python -m junit2htmlreport .\\reports\\TESTS-test_resources.features.LogStalker.xml'
            }
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