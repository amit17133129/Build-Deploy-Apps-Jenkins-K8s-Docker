pipeline{
    agent any
    parameters {
        string(
            defaultValue: 'main',
            name: 'branch_name', 
            trim: true
            )
        string(
            defaultValue: 'citymall-app', 
            name: 'deployment_name',  
            trim: true
            )
        string(
            defaultValue: 'default', 
            name: 'namespace', 
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

        stage("Deploying Application to K8S Cluster"){
            steps{
                script {
                    sh 'kubectl create deploy ${deployment_name} --image=${registry}    -n  ${namespace}'
                    sh 'kubectl expose deploy ${deployment_name} --type=NodePort --port=80   -n   ${namespace}'
                    }
                }
            }
        
        stage("Verifying application"){
            steps{
                script {
                    sh 'kubectl get pods -n ${namespace}'
                    sh 'kubectl get svc  -n ${namespace}'
                    }
                }
            }
        }
}
    
