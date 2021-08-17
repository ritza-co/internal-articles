---
hide:
  - navigation
---

# Kubernetes vs Docker vs OpenShift vs ECS vs Jenkins vs Terraform

To better understand the differences between these services, let's first look at the difference between **containerization** and **container orchestration**.

In short, **containers** contain code and the resources needed to run the code, while **container orchestration** is the automation of the management tasks of many containers (clusters).

**Containerization** or **containers** are a method of building, packaging and deploying software. In essence, a container includes code and everything the code needs to run properly. A container is completely isolated and abstracts away the underlying infrastructure and operating system. Furthermore, it is a portable container that can be deployed on almost any infrastructure or public cloud service.

**Container orchestration** is the automation of many of the underlying operational tasks required to run containerized workloads or services. This includes a wide range of tasks required to manage a container’s lifecycle including provisioning, deployment, scaling, networking, load balancing and more.

## Kubernetes vs Docker

**Kubernetes** is an open-source technology for orchestrating containers and deploying distributed applications, while **Docker** is an open-source technology for automating the deployment of applications as portable, self-sufficient containers that can run in the cloud or on-premises.

In short, **Docker** is used to containerize applications and **Kubernetes** is used to manage clusters of containers. **Docker** can run on its own while **Kubernetes** needs a container runtime in order to orchestrate. **Kubernetes** is most commonly used with **Docker** but it can also be used with any container runtime. ie. [RunC](https://www.docker.com/blog/runc/) or [cri-o](https://cri-o.io/).

Although **Kubernetes** vs **Docker** is a common question these days, they are not directly comparable; in fact, they are complementary. While **Docker** provides an open standard for containerization of applications, **Kubernetes** provides the standardised means of orchestrating (managing) clusters of containers from a central platform.

A more logical comparison would be **Kubernetes** vs **Docker Swarm**, Docker's native clustering solution. However, **Kubernetes** was designed to work well with **Docker**. **Docker** has since embraced **Kubernetes** and they are, in fact, offering their own integrated **Kubernetes** distribution in place of **Docker** Swarm as the default orchestration tool for **Docker** Enterprise.

Consider **Docker** only, for smaller projects where the overhead of spinning up **Kubernetes** is unnecessary or unwanted.

Consider **Docker** + **Kubernetes** for larger projects with multiple containers and where you need high-availability and efficient scaling. 

![Docker vs Kubernetes](https://i.ritzastatic.com/Ritza-Comparisons/kubernetes-vs/kubernetes-vs-docker.png)

## Kubernetes vs OpenShift

**Kubernetes** and **OpenShift** are both container orchestration platforms or Container-as-a-Service (CaaS) providers. However, **OpenShift** offers a Platform-as-a-Service (PaaS) too, that utilizes **Kubernetes** to manage and run applications more efficiently. While **OpenShift** also has an open-source version, their core focus is to provide a commercial container management platform with added functionality such as stricter security policies, commercial support, networking and container image management.

**OpenShift** is a RedHat Linux product and can only run on RedHat Atomic or Enterprise Linux (RHEL) for the commercial versions, and CentOS for the open-source version. On the contrary, **Kubernetes** is supported by most major cloud service providers like AWS, Azure, and Google Cloud Platform, and can run on any Linux distribution.

Furthermore, even with **Kubernetes**' large open-source community, deploying and managing **Kubernetes** is a very complex and resource-intensive undertaking while **OpenShift** provides an abstracted user interface where it is easier to visualise and manage application clusters and containers. 

Consider **Kubernetes** for high-demand applications if you have the resources to correctly manage it while taking advantage of their flexible deployment options.

Consider **OpenShift** for a commercial, all-inclusive solution that offers constant and dedicated support.

![Kubernetes vs OpenShift](https://i.ritzastatic.com/Ritza-Comparisons/kubernetes-vs/kubernetes-vs-openshift.png)

## Kubernetes vs Amazon ECS and EKS

**Kubernetes** and **Amazon Elastic Container Service (ECS)** are both highly scalable container management solutions. **ECS** is an Amazon Web Services (AWS) solution for managing containers and is tightly integrated with other AWS services like Route53, Elastic Load Balancer (ELB), Identity and Access Management (IAM) and many more. This makes it a little easier to add container orchestration to your solution, provided your whole solution runs on AWS. 

While **Amazon ECS** is an AWS opinionated container orchestration solution that only supports Docker containers on AWS, they also offer **Amazon Elastic Kubernetes Service (EKS)** which is **Kubernetes** on AWS. This allows you the flexibility to orchestrate clusters across many different cloud service providers and on-premises servers. Essentially, **EKS** is **Kubernetes** that runs on AWS infrastructure.

**Kubernetes** brings more to the table than just container management. It provides a complete, managed execution environment for deploying, running, managing and orchestrating containers. While it also supports AWS, you have the added advantage of being able to move applications managed by **Kubernetes** to any other cloud service provider (GCP, Azure, etc.) or Linux distribution.  

Furthermore, **Kubernetes** is open-source and has a plug-in architecture that allows for many different open-source solutions to be added to its core functionality, such as OpenVSwitch for a network model and NFS for storage. It also boasts some unique features like shared secrets, config maps, auto-scaling and auto-healing of containers using cluster- and application-specific probes.

A lot of the **Kubernetes** features can also be integrated with **ECS**, however, you'll have to combine quite a few AWS services like AWS Lambda to get the same features.

Consider **Kubernetes** for a highly customisable and portable container solution that can be set up to meet all your needs. Keep in mind, though, that you'll have to build your solution yourself which means you need to have the necessary skills and resources.

Consider **Amazon ECS** if you'll be running everything on AWS and you don't have the skills or resources to build your own **Kubernetes** solution. This also means you can take advantage of all the easily integrated services that AWS offers.

Consider **Amazon EKS** for a hybrid solution that integrates easily with other AWS services but allows you the flexibility of also orchestrating containers across other cloud platforms and on-premises infrastructure.

![Kubernetes vs Amazon ECS](https://i.ritzastatic.com/Ritza-Comparisons/kubernetes-vs/kubernetes-vs-ECS.png)

## Kubernetes vs Jenkins

**Kubernetes** is a complete, managed execution environment for deploying, running, managing and orchestrating containers while **Jenkins** is an open-source continuous integration and deployment (CI/CD) server that enforces automation in building, testing and deployment of applications. 

**Kubernetes** and **Jenkins** are mostly used in unison where **Kubernetes** takes care of the container management and orchestration, while **Jenkins** ensures continuous integration and deployment through automating the building, testing and deployment pipelines. 

In this case, it's not a question of either/or but rather using a combination of the two for an automated and efficient software release cycle that follows modern Agile methodologies.

![Kubernetes vs Jenkins](https://i.ritzastatic.com/Ritza-Comparisons/kubernetes-vs/kubernetes-vs-jenkins.png)

## Kubernetes vs Terraform

**Kubernetes** is a container orchestration platform that allows developers to manage clusters of containers like Docker containers, while **Terraform** is an open-source infrastructure-as-code software tool that provides developers with a consistent CLI workflow to manage hundreds of cloud services. 

**Terraform** allows developers to manage, deploy and orchestrate infrastructure as code. This means they codify cloud APIs into declarative configuration files that enable developers to manage infrastructure with human-readable code. Furthermore, this allows for any output generated by the infrastructure to be used as input to configure other infrastructure including **Kubernetes** clusters. 

**Terraform** integrates seamlessly into any cloud service provider including each of their own **Kubernetes** solutions. For this reason, **Kubernetes** and **Terraform** are often used in unison. However, **Terraform** can be used to manage almost any cloud infrastructure and **Kubernetes** can be used on its own to manage any containerized infrastructure like Docker containers.

Consider **Kubernetes** if your infrastructure solely consists of containers and you have the resources to build and maintain your own container orchestration solution.

Consider **Terraform** if your infrastructure consists of a combination of many different types of infrastructure, including **Kubernetes**, from different providers. This will allow you to easily manage and automate most of your infrastructure with human-readable code.

![Kubernetes vs Terraform](https://i.ritzastatic.com/Ritza-Comparisons/kubernetes-vs/kubernetes-vs-terraform.png)

## Docker vs OpenShift

**Docker** is an open-source technology for automating the deployment of applications as portable, self-sufficient containers that can run in the cloud or on-premises.

**OpenShift** is a PaaS that allows developers to deploy and scale applications easily through their platform which also makes use of container orchestration technology, Kubernetes, to manage **Docker** containers.

While both technologies use the same underlying container technology, **Docker** is simply the container technology itself. **OpenShift**, on the other hand, adds abstracted container cluster orchestration, management and some other features to form a whole software development and deployment solution.

Consider **Docker** alone for smaller projects and prototyping where there is no need to rapidly scale.

Consider **OpenShift** for a complete container management platform that offers many additional services including dedicated support.

![Docker vs OpenShift](https://i.ritzastatic.com/Ritza-Comparisons/kubernetes-vs/docker-vs-openshift.png)

As an example of how many of these technologies can work together let's consider the following:

You can use **Terraform** to manage all of your infrastructure which includes **Kubernetes**. **Kubernetes** will handle the container orchestration and receive its instructions from **Terraform**. Our services are all contained in **Docker** containers which are managed automatically by **Kubernetes**. Furthermore, we can integrate **Terraform** with **Jenkins** to add CI/CD workflows and automation.

This is just a simple example of how these technologies and services complement each other. There are multiple ways of building a development and deployment pipeline and most cloud providers each provide their own combinations and services specially designed for this.

