from kubernetes import client, config

# Loading the Kubernetes Configuration
config.load_kube_config()

# Creating Kubernetes API client
api_client = client.ApiClient()

# The deployment
deployment = client.V1Deployment(
    metadata=client.V1DeploymentSpec(name="cloud-monitor-flask-app"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "cloud-monitor-flask-app"}
        ),
        template=client.V1LabelSelector(
            metadata=client.V1ObjectMeta(
                labels={"app": "cloud-monitor-flask-app"}
            ),
            spec=client.V1PodSpec(
                conntainers=[
                    client.V1Container(
                        name="flask-container",
                        image="326473773557.dkr.ecr.us-west-1.amazonaws.com/cloud-native-monitor-repo:latest",
                        ports=[client.V1ContainerPorrt(container_port=5000)]
                    )
                ]
            )
        )
    )

)