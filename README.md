# CityMall Assignment

In this article you find below topics:
- How to create a pipeline.
- How to integrate docker with jenkins.
- How to build docker image and push to docker hub.
- How to deploy an application inside kubernetes cluster.

So, lets start by creating an simple application wriiten in `html`. Below is the code of the appliction.
I have installed jenkins and minikube in different servers over aws as you can see below.

<p align="center">
  <img width="1000" height="85" src="https://github.com/amit17133129/Build-Deploy-Apps-Jenkins-K8s-Docker/blob/main/task-images/servers.png?raw=true">
</p>

![html](https://github.com/amit17133129/Build-Deploy-Apps-Jenkins-K8s-Docker/blob/main/task-images/application.png?raw=true)

## Application Code
```
<!DOCTYPE html>
<html>
    <head> <h1> <center>Welcome to Apache running inside minikube</center></h1></head>
</html>
```

Now lets create a Dockerfile. Below code will you to create dockerfile.

![dockerfile](https://github.com/amit17133129/Build-Deploy-Apps-Jenkins-K8s-Docker/blob/main/task-images/dockerfile.png?raw=true)

## Dockerfile Code
```
FROM centos:7
RUN yum install httpd -y && \
    yum install net-tools -y
COPY ./index.html /var/www/html/
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
EXPOSE 80
```
After creating docker image lets create jenkinsfile to create pipeline job in jenkins dashboard.

![jenkins1](https://github.com/amit17133129/Build-Deploy-Apps-Jenkins-K8s-Docker/blob/main/task-images/jenkinsfile-1.png?raw=true)

![jenkins2](https://github.com/amit17133129/Build-Deploy-Apps-Jenkins-K8s-Docker/blob/main/task-images/jenkinsfile-2.png?raw=true)

## Jenkinsfile Code
```
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
```
## Adding GitHub Webhook in jenkins

<p align="center">
  <img width="800" height="200" src="https://github.com/amit17133129/Build-Deploy-Apps-Jenkins-K8s-Docker/blob/main/task-images/Course-OutLine.png?raw=true">
</p>

## Adding Dockerhub credentials in jenkins

<p align="center">
  <img width="1000" height="150" src="https://github.com/amit17133129/Build-Deploy-Apps-Jenkins-K8s-Docker/blob/main/task-images/docker-hub-cred.png?raw=true">
</p>

## Using Git as a SCM in pipeline script to pull jenkinsfile

<p align="center">
  <img width="1000" height="650" src="https://github.com/amit17133129/Build-Deploy-Apps-Jenkins-K8s-Docker/blob/main/task-images/pipeline-script.png?raw=true">
</p>

After saving the job run the job as soon as you commit the code from vscode then the jenkins pipeline will run automatically. Here how its look like.

<p align="center">
  <img width="1000" height="550" src="https://github.com/amit17133129/Build-Deploy-Apps-Jenkins-K8s-Docker/blob/main/task-images/jenkins-task.gif?raw=true">
</p>

## JOb run sucessfully 


<p align="center">
  <img width="1000" height="100" src="https://github.com/amit17133129/Build-Deploy-Apps-Jenkins-K8s-Docker/blob/main/task-images/job.png?raw=true">
</p>

<p align="center">
  <img width="1000" height="400" src="https://github.com/amit17133129/Build-Deploy-Apps-Jenkins-K8s-Docker/blob/main/task-images/job-2.png?raw=true">
</p>

## Docker image pushed 
<p align="center">
  <img width="1000" height="350" src="https://github.com/amit17133129/Build-Deploy-Apps-Jenkins-K8s-Docker/blob/main/task-images/docker-images-pushed.png?raw=true">
</p>
## Application-Status

<p align="center">
  <img width="1000" height="200" src="https://github.com/amit17133129/Build-Deploy-Apps-Jenkins-K8s-Docker/blob/main/task-images/pods-svc.png?raw=true">
</p>

## Application-Output

<p align="center">
  <img width="1000" height="100" src="https://github.com/amit17133129/Build-Deploy-Apps-Jenkins-K8s-Docker/blob/main/task-images/running-application.png?raw=true">
</p>
