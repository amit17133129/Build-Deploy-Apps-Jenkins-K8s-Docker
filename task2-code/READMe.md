## Task 2:
Find the resources in aws which is untagged and tag them respectively.
list of resources to check:
- ec2
- volume
- snapshot
- asg

## 1. Ec2 instances:

```
# checking instances which is untagged
aws ec2 describe-instances   --output text   --query 'Reservations[].Instances[?!not_null(Tags[?Key == `Name`].Value)] | [].[InstanceId]'

# tagging intagged instances
aws ec2 create-tags --resources instance-id --tags 'Key="env",Value=test'
```
<p align="center">
  <img width="1000" height="200" src="https://github.com/amit17133129/Build-Deploy-Apps-Jenkins-K8s-Docker/blob/main/task-images/task2-images/ec2-tagging.png?raw=true">
</p>

## 2. Volumes:

```
# checking instances which is untagged
aws ec2 describe-volumes  --output text  --query 'Volumes[?!not_null(Tags[?Key == `Name`].Value)] | [].[VolumeId,Size]'

# tagging intagged instances
aws ec2 create-tags --resources vol-id --tags 'Key="env",Value=test'
```
<p align="center">
  <img width="1000" height="200" src="https://github.com/amit17133129/Build-Deploy-Apps-Jenkins-K8s-Docker/blob/main/task-images/task2-images/untagged-volume-tagging-final.png?raw=true">
</p>

## 3. Snapshot:

```
# checking instances which is untagged
aws ec2 describe-snapshots  --output text  --owner-ids self  --query 'Snapshots[?!not_null(Tags[?Key == `Name`].Value)] | [].[SnapshotId,StartTime]'

# tagging intagged instances
aws ec2 create-tags --resources snapchot-id --tags 'Key="env",Value=test'
```
<p align="center">
  <img width="1000" height="175" src="https://github.com/amit17133129/Build-Deploy-Apps-Jenkins-K8s-Docker/blob/main/task-images/task2-images/snapshhot-tags.png?raw=true">
</p>
