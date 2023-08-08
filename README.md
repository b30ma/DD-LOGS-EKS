# Connect Datadog logs to Amazon Elastic Kubernetes Service (EKS):
  you need to configure the Datadog Agent to collect logs from your EKS pods and send them to Datadog. Below is a step-by-step guide along with a code file to help you   set up the connection.

 1- Install Datadog Agent:

    You need to install the Datadog Agent as a DaemonSet in your EKS cluster to collect logs from all the nodes.(datadog.yaml)

 2- in bash:
 
  $ kubectl apply -f datadog.yaml

 3- Collect Logs from EKS Pods:

    Now, you need to configure Datadog to collect logs from specific EKS pods.(logs.yaml)

 4- in bash:
 
  $ kubectl create configmap datadog-agent-config --from-file=logs.yaml
  $ kubectl label configmap datadog-agent-config "app=datadog-agent"

 5- Monitor Logs in Datadog:

    After the Datadog Agent is running and configured, you can start monitoring logs in the Datadog dashboard.

 6- Python Code for Integration:

    To demonstrate how to use Datadog's Python library to interact with Datadog

This setup will allow you to connect Datadog logs to your EKS cluster and monitor logs from your Kubernetes pods. Remember to replace placeholders with actual values, and make sure you've reviewed and adapted these steps based on your specific environment and requirements.
