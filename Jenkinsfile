pipeline {
	agent any
	stages {
		stage('sonar'){
			steps {
				//invoke sonar plugin
			    script {
                  def tagCommand = 'git describe --exact-match --tags HEAD'
                  def rc = sh(script: tagCommand, returnStatus: true)
                  def tagExists = (rc == 0)
        
                  if (tagExists) {
                      env.TAG = sh(script: tagCommand, returnStdout: true).trim()
                      sh("echo ${env.TAG} >> VERSION")
                  } else {
                      def dirtyTag = sh(script: 'git describe --tags --always HEAD', returnStdout: true).trim()
                      sh("echo ${dirtyTag}-SNAPSHOT >> VERSION")
                	}
              	}
				sh "cat VERSION"
			}
		}
		stage('build'){
			agent any
			when{
                branch 'master'
            }
			steps {
				sh "touch BUILD"
				sh "ls -al"
				sh "pwd"
			}
		}
		stage('unit-tests'){
			when{
                branch 'master'
            }
			steps {
				sh "echo unit-tests"
				sh "ls -la"
				sh "pwd"
			}
		}
		stage('signing'){
		    when{
                branch 'master'
            }
			steps {
				sh "echo python ci/image-signing.py"
			}
		}
    }
}
