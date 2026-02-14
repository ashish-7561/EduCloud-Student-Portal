 ☁️ EduCloud: Cloud-Native Student Records Application

A Decoupled, Serverless Web Application built for the Microsoft Elevate AICTE Internship Program.**

Project Overview
EduCloud is a modern, scalable cloud application designed to solve the data management bottlenecks faced by educational institutions. By transitioning from rigid on-premise servers to a decoupled Platform-as-a-Service (PaaS) architecture, this application ensures 99.99% high availability during peak traffic periods (e.g., admission cycles).

The architecture actively separates the storage of heavy, unstructured media files (ID photos) from structured JSON metadata (student profiles) to achieve enterprise-grade performance and eliminate database locking.

 Cloud Architecture & Tech Stack
1. Frontend (Client-Side)
* **Technologies:** HTML5, CSS3, Vanilla JavaScript.
* **Cloud Integration:** Azure Blob Storage REST APIs.
* **Mechanism:** Utilizes Shared Access Signature (SAS) tokens to enable secure, direct-to-cloud image uploads. By bypassing the backend server entirely for media payloads, the system drastically reduces compute costs and network latency.

 2. Backend (Server-Side Data Orchestration)
* **Technologies:** Python 3.
* **Cloud Integration:** Microsoft Azure Cosmos DB Core (SQL) API.
* **Mechanism:** Employs the `azure-cosmos` Python SDK to manage JSON-based active directory records. The NoSQL database is partitioned using a logical partition key (`/city`) to ensure horizontal scalability and single-digit millisecond query execution.

 Key Features
* **Direct-to-Cloud Uploads:** Secure image transmission directly from the browser to an Azure Blob container (`aictestorage1`).
* **Dynamic NoSQL Schemas:** Adaptable student records management that does not require rigid SQL table migrations.
* **Interactive Dashboard:** A responsive, tab-based UI with built-in upload previews and live database visualizations.
* **High Availability:** Fully decoupled architecture engineered for fault tolerance.

 How to Run the Application

 Running the Frontend UI
1. Clone this repository or download the source code.
2. Navigate to the `frontend` directory.
3. Open `index.html` in any modern web browser (Chrome, Edge, Firefox).
4. Note: Ensure the Azure SAS token in the JavaScript block is active for live cloud uploads.*

Running the Backend Database Script
1. Ensure Python 3.x is installed on your local machine or run the script in a Jupyter/Google Colab environment.
2. Install the required Azure Cosmos library:
   ```bash
   pip install azure-cosmos==4.5.1
