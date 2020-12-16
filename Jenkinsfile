pipeline {
	agent any
	stages {
		stage('Sonarqube') {
		    steps {
		        sh "echo sonarr"
		    }
		}
		stage('Gather version info'){
			steps {
				//identify version info from git tag
			    script {
                  def tagCommand = 'git describe --exact-match --tags HEAD'
                  def retCode = sh(script: tagCommand, returnStatus: true)
                  def tagExists = (retCode == 0)
        
                  if (tagExists) {
                      env.TAG = sh(script: tagCommand, returnStdout: true).trim()
                      sh("echo ${env.TAG} >> VERSION")
                  } else {
                      def dirtyTag = sh(script: 'git describe --tags --always HEAD', returnStdout: true).trim()
                      sh("echo ${dirtyTag}-SNAPSHOT >> VERSION")
                	}
              	}
				stash includes: 'VERSION', name: 'version'
			}
		}
		stage('Multi-platform build'){
			parallel {
				stage ('Windows') {
					agent any						
					stages {
						stage('Build') {
							steps {
								checkout scm
								unstash version
								// we assume the build scripts
								// use VERSION file to identify
								// version of app
								sh 'echo conan build app/'
								sh 'echo conan test app/'
								//stash includes: 'build/app/*', name: 'win-build'

							}
						}
						stage('Package') {
							steps {
								unstash 'version'
								//unstash 'win-build'
								// a python script that calls
								// reads version from the VERSION file
								// and creates platform specific package
								sh 'echo python create-package.py'
								//stash includes: 'package/*', name: 'win-pkg'
							}
						}
						stage('Sign') {
							steps {
								//unstash: 'win-pkg'
								// use a wrapper script for uploading
								// files to signing server
								echo 'python sign-app.py win-pkg/'
								//stash includes: 'signed-win-pkg/*', name: 'signed-win-pkg'
							}
						}
					}
				}
				stage ('MacOSX') {
					agent any							
					stages {
						stage('Build') {
							steps {
								checkout scm
								unstash version
								// we assume the build scripts
								// use VERSION file to identify
								// version of app
								sh 'echo conan build app/'
								sh 'echo conan test app/'
								//stash includes: 'build/app/*', name: 'osx-build'

							}
						}
						stage('Package') {
							steps {
								unstash 'version'
								//unstash 'osx-build'
								// a python script that calls
								// reads version from the VERSION file
								// and creates platform specific package
								sh 'python create-package.py'
								stash includes: 'package/*', name: 'osx-pkg'
							}
						}
						stage('Sign & Notarize') {
							steps {
								//unstash: 'osx-pkg'
								// use a wrapper script for uploading
								// files to signing server and notarize
								// the app
								sh 'echo python sign-app.py osx-pkg/'
								//stash includes: 'signed-osx-pkg/*', name: 'signed-osx-pkg'
							}
						}
					}
				}
			}
		}
		stage('upload-to-artifactory'){
			steps {
				unstash 'signed-win-pkg'
				unstash 'signed-osx-pkg'
				sh 'echo upload to artifactory'
			}
		}
		stage('ansible-qa'){
			steps {
				sh "echo ansiblePlaybook(credentialsId: 'ansible_private_key', inventory: 'inventories/qa/hosts', playbook: 'app.yml')"
			}
		}
		stage('Functional Testing'){
			steps {
				sh "echo running functional tests"
			}
		}
		stage('Publish'){
			steps {
				sh "echo publishing stuff"
			}
		}
	}
}
