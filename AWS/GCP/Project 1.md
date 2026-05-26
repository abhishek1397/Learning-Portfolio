Here is your definitive, end-to-end command reference sheet. You can use this for clean execution or save it for your final project documentation report.

---

## Phase 1: Authentication & Local Setup

Run these commands to log into Google Cloud and point your PowerShell terminal to your workspace.

```powershell
# 1. Log in to your Google Account
gcloud auth login

# 2. Bind your terminal context to your specific project ID
gcloud config set project walmart-forecast-new

```

---

## Phase 2: Complete Project Permissions & API Initialization

This block enables the core backend microservices and explicitly breaks through the default GCP "Zero-Trust" security barriers for your project number (`792843073682`).

```powershell
# 3. Turn on the 3 fundamental structural APIs
gcloud services enable cloudbuild.googleapis.com run.googleapis.com artifactregistry.googleapis.com

# 4. Unshackle the compiler account to read raw deployment source files
gcloud projects add-iam-policy-binding walmart-forecast-new --member="serviceAccount:792843073682-compute@developer.gserviceaccount.com" --role="roles/storage.admin"

# 5. Grant permission to stream compiler logs to Cloud Logging 
gcloud projects add-iam-policy-binding walmart-forecast-new --member="serviceAccount:792843073682-compute@developer.gserviceaccount.com" --role="roles/logging.logWriter"

# 6. Grant permission to write/push artifacts to the security registry
gcloud projects add-iam-policy-binding walmart-forecast-new --member="serviceAccount:792843073682-compute@developer.gserviceaccount.com" --role="roles/artifactregistry.writer"

```

---

## Phase 3: Building and Deploying

This safely initializes a modern Artifact Registry container box and builds/deploys the code straight out of the Mumbai server (`asia-south1`).

```powershell
# 7. Create the mandatory target Docker repository folder box
gcloud artifacts repositories create cloud-run-source-deploy --repository-format=docker --location=asia-south1 --description="Walmart App Repository"

# 8. Submit your directory, install requirements.txt, and build the image
gcloud builds submit --tag asia-south1-docker.pkg.dev/walmart-forecast-new/cloud-run-source-deploy/sales-forecaster:v1

# 9. Take that compiled image and turn it into a public serverless URL
gcloud run deploy sales-forecast-app --image asia-south1-docker.pkg.dev/walmart-forecast-new/cloud-run-source-deploy/sales-forecaster:v1 --platform managed --region asia-south1 --allow-unauthenticated --port 8501

```

---

## Phase 4: Toggle Internet Visibility (Public HTTPS Control)

Use these commands like a network firewall light-switch to freeze or unfreeze access to your public link without losing your work.

```powershell
# 10. TURN OFF Global Views (Locks the HTTPS link with a "403 Forbidden" error)
gcloud run services update sales-forecast-app --ingress=internal --region=asia-south1

# 11. TURN BACK ON Global Views (Restores internet routing instantly for presentations)
gcloud run services update sales-forecast-app --ingress=all --region=asia-south1

```

---

## Phase 5: The Master Purge (Wipe Out Everything)

The absolute final step when your evaluation is over. Running this stops every background engine, halts all billing meters to zero, and triggers automated permanent deletion.

```powershell
# 12. Delete the entire project workspace, services, and associated data layers
gcloud projects delete walmart-forecast-new

```

*(When prompted, type **`Y`** and press **Enter** to confirm).*

---

You can check out [How to delete a project](https://www.youtube.com/watch?v=Ubp_krp83vs) to visually understand exactly how Google handles the underlying data freeze, billing shutdown, and safety mechanisms during a project termination.
