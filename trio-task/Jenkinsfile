pipeline {
  agent any
      options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  environment {
    DOCKERHUB_CREDENTIALS = credentials('rihamm80-dockerhub')
        MYSQL_URI = credentials("MYSQL_URI")
        SECRET_KEY = credentials("SECRET_KEY")
	MYSQL_USER= 'root'
	MYSQL_URL = 'mysql'
	MYSQL_DATABASE = 'library'
	MYSQL_PASSWORD = credentials("MYSQL_PASSWORD")
	MYSQL_TEST = credentials("MYSQL_TEST")
  }
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t riham80/databasemysql:latest database'
	    sh 'docker build -t riham80/flask-library:latest . '
 
      }
    }

    stage('RUN') {
      steps {
        sh ' docker network create mynetwork '
	    sh ' docker run -d --name mysql --network mynetwork databasemysql:8'
	    sh 'docker run -d --name flask-app1  -p 5000:5000 --network mynetwork flask-library:latest'
        }
    }
    stage('Push') {
       steps {
          sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
          sh ' docker push riham80/flask-library:latest'
          sh ' docker push riham80/databasemysql:latest'
           }
       } 
    stage('Test') {
       steps {
          sh ' bash test.sh  '
          sh ' echo testing'
           }
       }

  } //stages
  post {
    always {
	junit 'junit_report.xml'
        cobertura autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: 'coverage.xml', conditionalCoverageTargets: '70, 0, 0', failUnhealthy: false, failUnstable: false, lineCoverageTargets: '80, 0, 0', maxNumberOfBuilds: 0, methodCoverageTargets: '80, 0, 0', onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false
      
    }
  }

} //pipeline
