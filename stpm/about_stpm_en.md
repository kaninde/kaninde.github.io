# About SafeText: Private Messages (STPM)

Welcome to **SafeText: Private Messages (STPM)** — an app that adds an extra privacy layer to the conversations you already use every day.

STPM is **not** a full messenger. You encrypt messages and files **on your phone**, then send protected content through WhatsApp, Telegram, SMS, email, or any other app — as a `SAFE://` text payload or a `.safe` file. There is **no sign-up**, **no login**, **no phone number**, **no email**, and **no central server** holding your keys.

STPM helps you manage **secure conversations** (local contact names, key exchange via QR Code, fingerprint verification), **protected messages**, **`.safe` files** (photos, videos, audio, documents), **privacy settings** (hide sensitive text, app lock, clipboard auto-clear, screen capture limits), and **encrypted backup** export/restore. **Conversation metadata**, **public keys**, **settings**, and optional **local history** (opt-in) are stored **locally** on your device (SQLite database `stpm.db`).

---

## Highlights

- **Secure conversations:** Create conversations, exchange keys via QR Code, verify the security fingerprint, archive or revoke access, renew your local key when needed.
- **Protected messages:** Write text, generate an encrypted payload, copy or share; open received `SAFE://` content with signature and integrity checks.
- **`.safe` files:** Encrypt media and documents; open shared files in the app; preview decrypted content; explicit warning before sharing plaintext.
- **Open message:** Paste or receive protected text from other apps and decrypt locally.
- **Privacy by default:** Sensitive text stays hidden until you reveal it; private keys use the system secure storage; plaintext is not persisted by default.
- **Settings:** App lock (biometrics or PIN), clipboard auto-clear, optional local message history, advanced technical details, encrypted backup, onboarding guide.
- **Privacy-first core:** Your keys and conversation data stay on the device unless you export a backup or use features that need the internet (see the Privacy Policy).

---

## Included features and limits (summary)

The app may offer **free**, **premium subscription**, **lifetime offline purchase**, or **ad-supported** access depending on the build and store configuration. On the free tier, limits may apply (for example rewarded ads before encrypt/decrypt actions, or gated premium settings). **Premium** or **lifetime** unlocks broader access, including ad-free crypto flows and advanced privacy features, as described in the store listing and in-app paywall.

Limits and entitlements can change with app updates; the **in-app** experience and store listing prevail over this page.

---

## FAQ

**Do I need an account?**  
No. You can use STPM without creating an account.

**Do I need internet?**  
Core encryption and decryption work **offline**. Internet is used when you choose features that need it (for example **ads**, **in-app purchases** or **subscriptions**, optional **remote configuration** such as an “other apps” carousel, or opening external links).

**Will I lose my data if I uninstall?**  
Local data lives on your device. Uninstalling the app can **permanently remove** conversations, keys, and settings unless you have exported an **encrypted backup**.

**Is STPM a messaging service?**  
No. STPM is a **local encryption tool**. It does not deliver messages, host chats, or replace WhatsApp or other messengers. You remain responsible for how you share protected content and for verifying contacts via QR and fingerprint.

---

## Contact

For support or feedback:

**Email:** samirtf.dev@gmail.com
