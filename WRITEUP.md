

Overview

This project deploys an Article Content Management System (CMS) built with Python and Flask to Microsoft Azure. The application allows users to create and manage articles, upload images to Azure Blob Storage, and store article information in an Azure SQL Database. Microsoft Authentication was also configured to provide secure login functionality.



Deployment Choice: App Service vs Virtual Machine

For this project, Azure App Service was chosen instead of deploying the application on a Virtual Machine (VM).

Why App Service Was Chosen

1. Simpler Deployment

Azure App Service allows web applications to be deployed quickly without manually configuring servers. The platform supports direct deployment from development tools such as Visual Studio Code or GitHub.

2. Managed Infrastructure

With App Service, Azure manages the operating system, runtime environment, and platform updates automatically. This reduces infrastructure management and allows developers to focus on application development.

3. Built-in Integration

Azure App Service integrates easily with other Azure services such as Azure SQL Database, Azure Blob Storage, and Azure Authentication. This makes it easier to build cloud-based applications.

4. Scalability

Azure App Service provides built-in scaling options. The application can automatically scale to handle increased traffic without requiring manual infrastructure management.



When a Virtual Machine Would Be Used Instead of App Service

Although Azure App Service works well for this CMS application, there are situations where a Virtual Machine would be required.

For example, if the application required a specific operating system configuration, custom server software, or legacy dependencies that are not supported by Azure App Service, then a Virtual Machine would be a better choice.

A Virtual Machine provides full control over the infrastructure, allowing developers to install custom tools, modify system settings, and configure specialized networking environments.



Why a Virtual Machine Was Not Used

While a Virtual Machine provides greater control over the server environment, it requires additional setup and maintenance. Developers must manually configure the operating system, web server, Python runtime, security updates, and scaling.

Since this project focuses on efficiently deploying a web application, Azure App Service was the more practical and efficient solution.


Comparison: Azure App Service vs Virtual Machine

Cost

Azure App Service is generally more cost-effective because Microsoft manages the infrastructure and resources. With Virtual Machines, users are charged for the full compute instance even when the application is idle, which can increase operational costs.

Scalability

Azure App Service supports automatic scaling, allowing the application to scale up or out when traffic increases. Virtual Machines require manual configuration or the use of additional services such as VM scale sets to scale effectively.

Availability

Azure App Service provides built-in high availability and platform maintenance. Microsoft manages the infrastructure to ensure reliability. In a Virtual Machine setup, developers must configure load balancing, redundancy, and monitoring to maintain availability.

Workflow

Azure App Service simplifies deployment through integration with development tools and CI/CD pipelines. In contrast, deploying to a Virtual Machine requires additional configuration such as server setup, runtime installation, security configuration, and manual deployment of application updates.


Conclusion

Using Azure App Service simplified the deployment process and allowed the CMS application to integrate smoothly with Azure services such as Azure SQL Database, Azure Blob Storage, and Microsoft Authentication. This platform provides a scalable, reliable, and efficient environment for hosting web applications.
