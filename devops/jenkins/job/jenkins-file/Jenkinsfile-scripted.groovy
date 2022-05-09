node {
  def mvnHome
  stage('Preparation') { // for display purposes
    // Get some code from a GitHub repository
    git 'https://github.com/jglick/simple-maven-project-with-tests.git'
    mvnHome = tool 'my-maven'
  }
  stage('Build') {
    // Run the maven build
    withEnv(["MVN_HOME=$mvnHome"]) {
      if (isUnix()) {
        sh '"$MVN_HOME/bin/mvn" -Dmaven.test.failure.ignore clean package'
        } else {
        bat(/"%MVN_HOME%\bin\mvn" -Dmaven.test.failure.ignore clean package/)
      }
    }
    sh(script: '''
      echo "Hello:
      git clone https://github.com/hvitoi/test.git
      cd test
      docker build . -t test
    ''')
  }
  stage('Results') {
    junit '**/target/surefire-reports/TEST-*.xml'
    archiveArtifacts 'target/*.jar'
  }
}
