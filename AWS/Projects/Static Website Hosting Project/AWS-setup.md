# 🌐 Static Website Hosting on AWS S3 with Route 53 & CloudFront

## 📌 Project Overview

This project demonstrates how to **host a static website on AWS** using:
- **Amazon S3** for storage and static website hosting
- **Amazon Route 53** for custom domain DNS management
- **Amazon CloudFront** for global content delivery and HTTPS security

---

## 🧰 Technologies Used

| Service            | Purpose                                       |
|--------------------|-----------------------------------------------|
| Amazon S3          | Store static website files (HTML/CSS/JS)     |
| Amazon Route 53    | DNS & domain management                       |
| Amazon CloudFront  | CDN with HTTPS using AWS Certificate Manager |
| AWS Certificate Manager (ACM) | SSL certificate provisioning       |

---

## 🚀 Website Preview

> 🌍 https://your-custom-domain.com  
> *(Replace with your actual domain after DNS propagation)*

---

## 🛠️ Step-by-Step Deployment Guide

### ✅ Step 1: Create an S3 Bucket

1. Go to **S3 Console** → Create Bucket
2. Bucket Name: `yourdomain.com`
3. Region: Choose your AWS region
4. Uncheck **Block all public access**
5. Go to **Properties** → Enable **Static Website Hosting**
   - Hosting type: `Host a static website`
   - Index document: `index.html`
6. Click **Create Bucket**

---

### ✅ Step 2: Upload Website Files

1. Open your newly created bucket
2. Click **Upload** → Add `index.html`, `style.css`, etc.
3. Click **Upload**

---

### ✅ Step 3: Configure Public Bucket Policy

Paste the following in **Permissions > Bucket Policy**:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::yourdomain.com/*"
    }
  ]
}
````

Replace `yourdomain.com` with your bucket name.

---

### ✅ Step 4: Register a Domain in Route 53 (if needed)

* Go to **Route 53 → Register domain**
* Search and purchase a domain (e.g., `yourdomain.com`)
* Wait for registration to complete

---

### ✅ Step 5: Create a Hosted Zone in Route 53

* Open **Route 53 → Hosted Zones**
* Click **Create Hosted Zone**
* Enter your domain name
* Type: `Public Hosted Zone`

---

### ✅ Step 6: Set Up CloudFront Distribution

1. Go to **CloudFront → Create Distribution**
2. **Origin domain**: Select your S3 bucket
3. **Viewer Protocol Policy**: Redirect HTTP to HTTPS
4. **Alternate Domain (CNAME)**: `yourdomain.com`
5. **SSL Certificate**: Request via AWS Certificate Manager (ACM)

   * Validate via DNS (recommended)
6. Click **Create Distribution**
7. Wait for deployment to finish

---

### ✅ Step 7: Point Route 53 DNS to CloudFront

1. Open **Route 53 → Hosted Zone**
2. Click **Create Record**
3. Routing Type: `Simple`
4. Record Type: `A – IPv4`
5. Route traffic to: `Alias to CloudFront`
6. Choose your CloudFront distribution

---

### ✅ Step 8: Test Your Website

* Visit `https://yourdomain.com`
* DNS changes may take up to an hour to propagate

---

## ✅ Summary of Setup

| Task                             | Status |
| -------------------------------- | ------ |
| S3 Bucket with Static Hosting    | ✅      |
| Website Files Uploaded           | ✅      |
| Bucket Policy Configured         | ✅      |
| Route 53 Domain and Hosted Zone  | ✅      |
| SSL Certificate via ACM          | ✅      |
| CloudFront Configured            | ✅      |
| DNS Routing from Route 53 to CDN | ✅      |

---

## 🔒 Security and Performance

* Website traffic is served over **HTTPS**
* Cached globally via **CloudFront**
* No server provisioning required

---



---


## 🔗 Resources

* [Static Website Hosting on S3 Docs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)
* [Route 53 Docs](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)
* [CloudFront + ACM SSL Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-cloudfront-to-custom-origin.html)


