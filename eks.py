from kubernetes import client, config

# Loading the Kubernetes Configuration
config.load_kube_config()

# Creating Kubernetes API client
api_client = client.ApiClient()

# The deployment
deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="cloud-monitor-flask-app"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "cloud-monitor-flask-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": "cloud-monitor-flask-app"}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="flask-container",
                        image="326473773557.dkr.ecr.us-west-1.amazonaws.com/cloud-native-monitor-repo:latest",
                        ports=[client.V1ContainerPort(container_port=5000)]
                    )
                ]
            )
        )
    )
)

# Deploy the Application
api_instance = client.AppsV1Api(api_client)
api_instance.create_namespaced_deployment(
    namespace="default",
    body=deployment
)

# Service definition
service = client.V1Service(
    metadata=client.V1ObjectMeta(name="cloud-flask-service"),
    spec=client.V1ServiceSpec(
        selector={"app": "cloud-monitor-flask-app"},
        ports=[client.V1ServicePort(port=5000)]
    )
)

# Service Creation
api_instance = client.CoreV1Api(api_client)
api_instance.create_namespaced_service(
    namespace="default",
    body=service
)