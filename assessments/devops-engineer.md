# DevOps Engineer Technical Assessment: AWS Infrastructure & EKS Microservices

## Overview

In this assessment, you will design and propose a basic architecture setup for a microservices-based application deployed on AWS. The application’s microservices will run on Amazon EKS (Elastic Kubernetes Service) and expose public API endpoints for external clients. Your design should address key requirements around scalability, security, and best practices in AWS.

---

## Scenario

Imagine you are tasked with deploying a new microservices application on AWS. The application consists of multiple containerized services that are deployed into an EKS cluster. These services need to be accessible to external clients via public API endpoints. The system must be highly available, scalable, and secure.

---

## Tasks

### 1. Architecture Proposal

- **Objective**: Design a high-level architecture for hosting microservices
  on Amazon EKS with public API endpoints.
- **Requirements**:
    - **EKS Cluster Setup**:
        - Describe how you will set up your EKS cluster including worker
          nodes, networking (VPC, subnets, etc.), etc.
        - Explain your container image management and deployment strategy (e.g.,
          CI/CD pipeline, container registries).
    - **Public API Exposure**:
        - Detail how microservices will be exposed to the public internet.
        - Cover DNS management and TLS termination.
    - **High-Level Diagram**:
        - Provide a clear, well-labeled diagram that includes major AWS
          services and illustrates the flow of traffic from external clients to
          the microservices.

### 2. Scalability Considerations

- **Objective**: Demonstrate how your architecture scales to meet varying loads.
- **Requirements**:
    - **Auto Scaling**:
        - Explain how you will implement scaling for both the EKS cluster and
          the containerized applications.
    - **Load Balancing**:
        - Describe your strategy for distributing incoming traffic across the
          microservices, ensuring even load distribution and high availability.
    - **Fault Tolerance**:
        - Address how your design accounts for fault tolerance and high
          availability.

### 3. Security Measures

- **Objective**: Design the architecture with robust security controls to
  protect public API endpoints and internal resources.
- **Requirements**:
    - **Network Security**:
        - Describe your VPC design, including the segmentation of public and
          private subnets, configuration of security groups, etc.
    - **API Security**:
        - Detail methods to secure public API endpoints.
    - **Container and Cluster Security**:
        - Outline best practices for securing container images.
    - **Secrets Management**:
        - Explain how sensitive information (e.g., database credentials, API
          keys) will be securely managed.

---

## Deliverables

1. **Architecture Diagram**:
    - A visual representation of your proposed AWS architecture (image file or
      embedded diagram).

2. **Written Proposal**:
    - A document (Markdown, PDF, or similar) explaining your design choices.
      This should include:
        - An overview of the architecture and rationale behind key decisions.
        - Details on how your solution meets the requirements for scalability
          and security.
        - Any additional AWS services or strategies you would employ.

3. **Optional Code Snippets**:
    - Provide any sample code or infrastructure-as-code (IaC) templates (e.g.,
      Terraform) that illustrate how you might deploy key components of your
      solution.

---

## Submission Guidelines

- **Format**:
    - Submit your diagram (as an image or embedded in the document) along with
      your written proposal.
    - Include any code snippets or IaC templates as separate files or as part of
      the document.

- **Deadline**:
    - By [date].

- **Submission Method**:
    - Please send your completed assessment to
      glsnxt-engineering-leads@teams.gls-global.com.

---

## Final Notes

There is no single “correct” answer—this assessment is designed to understand
your approach to solving complex infrastructure problems. We are interested in
your thought process, design trade-offs, and how you justify your decisions.
Focus on clarity, detail, and adherence to best practices.

Good luck, and we look forward to reviewing your solution!
