pipeline{
    agent any
    parameters {
        string(
            defaultValue: 'main', 
            name: 'branch_name', 
            trim: true
            )
    }
    environment {
        dockerImage = ''
        registry    = 'amitsharma17133129/apache-app-citymall'
        registryCredential = 'docker_hub_cred'
    }
    stages{
        stage("Checkout"){
            steps{ 
                checkout([
                    $class: 'GitSCM', 
                    branches: [[name: '*/${branch_name}']], 
                    extensions: [], 
                    userRemoteConfigs: [[
                        url: 'https://github.com/amit17133129/Build-Deploy-Apps-Jenkins-K8s-Docker.git'
                        ]]
                    ]
                )
            }
        }
        stage("Build Docker Image"){
            steps{
                script {
                    dockerImage = docker.build registry
                }
            }
        }

        stage("Push Docker Image"){
            steps{
                script {
                    docker.withRegistry('', registryCredential){
                        dockerImage.push()
                    }
                }
            }
        }
    }

}