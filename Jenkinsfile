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
            echo 'This will run only if failed'
            mail to: 'juan.restrepo@digitalamericas.ai',
            subject: "Succeed Pipeline: ${currentBuild.fullDisplayName}",
            body: "To find pipeline execution details: ${env.BUILD_URL}"        }
        failure {
            echo 'This will run only if failed'
            mail to: 'juan.restrepo@digitalamericas.ai',
            subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
            body: "Something is wrong with ${env.BUILD_URL}"
            ${FILE,path=".\\reports\\TESTS-test_resources.features.LogStalker.xml.html"}
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