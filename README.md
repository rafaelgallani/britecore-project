# Britecore Project
Welcome! 
This is a project built for one of the Britecore interview steps.

It's a system that enables insurers to define their custom data into the system without being limited to a rigid pre-defined model.

It uses [PostgreSQL](https://www.postgresql.org/) as a database for the custom data, [Django](https://www.djangoproject.com/) + [Django REST Framework](https://www.django-rest-framework.org/) for the backend, and [Vue.js](https://vuejs.org/) (`v2`) as the frontend framework. 

All the development was containerized, so [cloud deployment](https://github.com/rafaelgalani/britecore-project/blob/master/README.md#cloud-platforms) can be done seamlessly.

## Data:

### Data model (ER diagram)

![er-diagram](docs/data/ER_diagram.png?raw=true)

### ORM classes

You can find the ORM classes in the [`models`](backend/api/models) folder.

## Backend: 

Since it was built with Django, most of the hard work of handling all HTTP verbs and RESTful concepts was already done OOTB. But you can find out more by reading the [backend docs](backend/README.md).

## Frontend: 

- Home 
  - Dashboard (number of created risks/risk types/fields)
  - Navigation
    - Create a Risk Type
    - Create a Risk
    - Manage Risk

You can find more specific information about it [here](frontend/README.md).

## Cloud platforms:

It can be easily set up using any cloud platform. Here's an example of the installation script to AWS platform (using ECS), considering you already have `aws cli` installed and configured at your system:

```
$ ecs-cli configure --cluster britecore-project-cluster --region us-east-1 --config-name britecore-project-config --cfn-stack-name britecore-project-stack --default-launch-type EC2
```
Firstly, you need to create an ECS cluster so you can deploy the containers to it. This command will save the configuration files so the cluster can be created later with `ecs-cli up`. Also, using `ecs-cli` can easily allow you to integrate the whole process with [CloudFormation](https://aws.amazon.com/cloudformation/) using the `cfn-stack-name` flag, which comes in handy to handle the AWS resources. You can also change the `region` and other flags values since these were only used as an example.


```
$ ecs-cli up --keypair YOUR_KEYPAIR_PATH --capability-iam --size 1 --instance-type YOUR_INSTANCE_TYPE --cluster-config britecore-project-config
```
Running this command will create the ECS cluster and the resources it requires. Some permissions are required to run this command. For this example, you can find the defined permissions in the [aws_default_permissions.json](aws_default_permissions.json) file. These might not be suitable for a production environment.
`YOUR_INSTANCE_TYPE` refers to an AWS instance type. For this example, I opted for `t2.medium`. It was removed from the example above because it involves cost, so it shouldn't be copy/pasted without thinking :)

Also, the `keypair` param is not required, but it's strongly recommended. If you don't specify a keypair, you will not be able to `ssh` to your container later in case something goes wrong. You never know...


```
$ ecs-cli compose --ecs-params ./ecs-params.yml up --cluster-config britecore-project-config
```
If everything went OK until here, then all you need to do is run `ecs-cli compose up`, so the task definitions will be created and up, according to the compose file. _(Disclaimer: at the time of writing, `ecs-cli` version `1.21.0` always looks for `docker-compose.yml` in the current path. The `docker-compose.yml` file in this repository was only kept for convenience. Currently, there's not a documented way to change this behavior)_.

The `ecs-params` flag specifies a `.yml` path for overriding the default `ecs-cli` generated ones. For this example, it's needed to add dependency between the containers, since, at the time of writing, `ecs-cli` cannot handle the `depends_on` property - that's why `link` and the `ecs-params` file `depends_on` property were also used: with these, containers can find each other through the defined alias name (e.g. `backend`, `db`, `frontend`).

In case some of the steps failed, you can always rollback with `ecs-cli down`.