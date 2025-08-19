# AWS Snowball Edge — Exam Notes

## 1. Purpose & Use Cases
- Physical data transport device for moving large datasets (TB–PB scale) into/out of AWS, especially when network is slow, expensive, or not feasible[9].
- Common use cases: Disaster recovery, data migration, remote edge computing, local analytics, content distribution, and archiving[9].

## 2. Variants
- **Snowball Edge Storage Optimized**: For bulk data transfer and storage.
- **Snowball Edge Compute Optimized**: Adds local processing power for edge analytics, ML, video analysis, etc[5][21].

## 3. Key Features
- Up to 100TB usable storage per device[2].
- Transfer speeds up to 100Gbit/s via local network adapters[2][21].
- Data encryption (256-bit) always enforced at rest and in transit, using AWS KMS. Tamper-proof hardware[9][2].
- Built-in E Ink/LCD display for easy shipment and management[2].
- Direct S3–compatible storage; S3 Adapter and NFS protocol support[2].
- Cluster multiple devices for local durability and expanded compute/storage[2][21].
- EC2-compatible endpoints: Run VM workloads on device using AMIs[2].
- Supports AWS Lambda (edge compute), EKS Anywhere (Kubernetes) on device[21].

## 4. Workflow Overview
1. Order device from AWS Console; device is shipped securely to your site[5].
2. Connect device to local network.
3. Use client software, unlock code, manifest to verify and unlock device[5].
4. Copy data (import/export) via supported protocols[2].
5. Data is always encrypted during transit and at rest[9][5].
6. When done, ship device back; E Ink label auto-updates for return[5].
7. Once AWS receives and processes the device, imported data appears in your S3 bucket[5].
8. Export jobs allow you to transfer data out from S3 to local device[5].

## 5. No-Cost Activities
- Use of device for up to 10–15 days (per job/device type/region)[1].
- Transfer of data from Snowball Edge to Amazon S3 (“import into S3”)[1].

## 6. Charged Activities
- Transfer of data out of Amazon S3 to Snowball Edge and export (“export out of S3”)[14].
- Daily use after free period (per-day charges apply)[1].

## 7. Security
- 256-bit encryption; keys managed through AWS KMS and never stored on device[2][9].
- Tamper-evident, rugged physical hardware[9].
- Manifest and unlock code unique to your account and device[5].
- HIPAA and FedRAMP compliant[21].

## 8. Limitations & Quotas
- Device must be returned to AWS within 360 days or is locked/disabled[19].
- Single device service default limit per region/account; request more via support for clusters[19].
- Static files only: Cannot import files that are actively being modified[19].
- Max Snowball Edge S3 connections: 1,000[19].
- Export limitations: No shipping between non-US regions; cannot ship to PO boxes[19].
- Metadata for exported objects (beyond filename and filesize) is not preserved[19].
- Max instance types for compute: sbe1, sbe-c, sbe-g; supports up to 20 AMIs per device[20][2].

## 9. Supported Protocols & APIs
- NFSv3, NFSv4, NFSv4.1 for file transfer[2].
- Amazon S3 API (via CLI, SDK, OpsHub)[21].
- EC2/EBS compatible local endpoint for compute jobs[2][21].

## Which activities are available at no cost?

- **Use of the Snowball Edge appliance for a 10-day period**
  - The first 10–15 days (region and device dependent) of onsite device usage are included at no cost in the standard service fee. No extra daily charges if you return it within this period[1][3].

- **Transfer of data from the Snowball Edge appliance into Amazon S3**
  - Transferring data from the Snowball Edge device into Amazon S3 is free (no extra fee for imports into S3). Uploading data into Amazon S3 is always free[14].

---

### Not free:

- **Transfer of data out of Amazon S3 and to the Snowball Edge appliance**
  - Retrieving or exporting data from Amazon S3 to a Snowball device incurs a per-GB fee that varies by region[14].

- **Daily use of the Snowball Edge device after 10 days**
  - If you keep the device for more than the 10–15 free days, extra daily usage charges apply until the device is returned to AWS[1][3].

---

## Summary Table

| Activity                                                          | Free?   | Notes                                           |
|-------------------------------------------------------------------|---------|-------------------------------------------------|
| Use for first 10–15 days                                          | Yes     | Included; subject to device type/region   |
| Data transfer: Snowball Edge ➔ Amazon S3                          | Yes     | Imports to S3 are free                    |
| Data transfer: Amazon S3 ➔ Snowball Edge                          | No      | Per-GB export fee applies |
| Daily use after 10–15 days                                        | No      | Daily fee after free period               |
```markdown
[1] https://www.examtopics.com/discussions/amazon/view/123345-exam-aws-certified-cloud-practitioner-clf-c02-topic-1/
[2] https://cloudchipr.com/blog/aws-snowball
[3] https://aws.amazon.com/snowball/faqs/
'''
