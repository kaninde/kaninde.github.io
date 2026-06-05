# Privacy Policy – SafeText: Private Messages (STPM)

Last updated: June 5, 2026

---

## 1. Introduction

This Privacy Policy describes how **SafeText: Private Messages** (“STPM”, “App”) handles information on your device and, when you use certain features, limited interactions over the internet.

By using the App, you agree to the practices described in this Privacy Policy.

We are committed to protecting your privacy and being transparent about how data is handled.

---

## 2. Data Collection and Storage

### 2.1 Local data storage

- The App is designed so that **core content** — including **secure conversation records** (local display names, key states, fingerprints, archive status), **cryptographic key material** (private keys in system secure storage; public keys and related metadata locally), **protected message and file handling metadata** (when you opt in to local history), **settings**, and related records — is stored **locally** on your device (for example in a local SQLite database named `stpm.db`).
- **Plaintext message content** is **not persisted by default**; sensitive text is shown only when you choose to reveal it, subject to your settings.
- Where available, you can **export** an **encrypted backup**, **restore** a compatible backup, or **delete** data from within the App (including wipe-all options where provided).

### 2.2 Accounts

- The App **does not require** you to create an account, phone number, email, or login for the main local workflow.

### 2.3 Data we do not operate as a messaging backend

- STPM is **not** a messenger, key server, or cloud backup service operated by us for your day-to-day encrypted content. We **do not** run a central service whose purpose is to store your conversations, private keys, or decrypted messages on **our** servers as part of normal use.
- When you use **share**, **export**, **copy**, or open a file, content is sent through **your** device’s operating system (for example to WhatsApp, email, or a path you choose). That is under **your** control.

### 2.4 Network use (store, ads, optional remote content)

When you choose features that need connectivity, the App may connect to the internet, for example to:

- **In-app purchases / subscriptions / lifetime purchase:** handled by **Google Play** or **Apple App Store** under their terms and privacy policies.
- **Advertising (if enabled):** ad SDKs may process **device and usage signals** as described in their own policies.
- **Optional remote JSON or links:** for example a lightweight **“other apps”** carousel or similar configuration hosted on a **third-party** URL included in the build; such requests go to whoever operates that host. Opening **documentation**, **support**, or **store** links also uses the network.

### 2.5 Permissions

Depending on the features and platform, the App may request access to capabilities such as:

- **Camera:** for scanning QR Codes to exchange public keys with contacts.
- **Photos / gallery / files (as required by the OS):** for selecting media or documents to protect, opening `.safe` files, or saving exports, using system pickers where available.
- **Microphone:** for recording audio to protect as encrypted media when you use that feature.
- **Biometrics / device credentials:** for optional **app lock** when you enable it.
- **Internet:** for **ads**, **billing**, optional remote configuration, or opening links.
- **Notifications (optional):** only if a feature you enable uses notifications, in line with the permissions declared for your build.

The App does not access these resources without **your** action where the system requires explicit consent.

---

## 3. Data usage

Data you provide is used to:

- Run **secure conversations**, **encrypt/decrypt** flows, **QR key exchange**, **fingerprint verification**, **backup/restore**, and **settings**;
- Apply optional **local message history** when you opt in;
- Show **ads**, **premium subscription**, or **lifetime** purchase flows when enabled in your build.

We do **not** use your conversation or message content to build an advertising profile **on our side**; third-party ad networks may process data under **their** policies when ads are shown.

---

## 4. Data sharing

- We **do not sell** your personal information.
- Your **conversation, key, and message content** is not uploaded to **our** servers as part of the default local workflow described above.
- **App stores**, **ad networks**, and **hosts of optional remote URLs** you fetch may process data according to **their** policies when you use those services.

Any sharing of protected payloads, `.safe` files, backups, or screenshots happens only when **you** initiate share, export, or copy.

---

## 5. Third-party services

The App may rely on third parties, including:

- **Advertising:** may collect identifiers or usage data for ad delivery and measurement.
- **Payments:** processed by the platform store.
- **Hosts of optional configuration JSON:** whoever operates the URL you fetch may see **technical request data** (such as IP address) like any web server.
- **Messaging and file apps you choose:** WhatsApp, email, cloud storage, and similar services process content **you** send through them under **their** policies.

Those services operate under their own terms and privacy policies.

---

## 6. Data retention and deletion

- Local data remains on your device until you delete it or uninstall the App.
- You can use in-app options to **clear data**, **delete conversations**, or **wipe all SafeText data** where provided.
- Uninstalling the App typically **permanently removes** local databases and secure storage entries from the device.

---

## 7. Security

We apply reasonable practices in the App, including keeping keys and conversation data **on-device** by default, using system secure storage for private keys, and minimizing unnecessary collection.

You are responsible for securing your device (PIN, password, biometrics), verifying contacts via QR and fingerprint, and keeping the OS updated.

---

## 8. Children’s privacy

The App is intended for a general audience and is **not directed** to children under **13**.

We do not knowingly collect personal information from children in a way that violates this intent.

---

## 9. Changes to this policy

We may update this Privacy Policy from time to time. The “Last updated” date will change. Continued use of the App after updates constitutes acceptance of the revised policy.

---

## 10. Contact

Questions about this Privacy Policy:

**Email:** samirtf.dev@gmail.com

---

## 11. Disclaimer

The App is provided **“as is”** without warranties of any kind. You are solely responsible for **verifying contacts**, **protecting backup passwords**, and any **decisions** you make when sharing encrypted or decrypted content. STPM does not provide legal or security advice; no tool can guarantee confidentiality if your device or channel is compromised.
