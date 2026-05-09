# About Social Media Safe Text (SMST)

Welcome to **Social Media Safe Text (SMST)** — an app to review and prepare text before you post on social networks.

SMST helps you replace or obfuscate words and phrases you do not want to expose literally, using a **personal dictionary** (keywords and replacements), optional **character substitution rules** (similar to “leetspeak”), and an **editor** with automatic or manual modes. Your **dictionary** and **history** are stored **locally** on your device (SQLite).

---

## Highlights

- **Editor:** Write freely, highlight matches from active dictionaries, replace in bulk or step by step, copy and share.
- **Dictionary:** Organize entries in named groups, set multiple replacements with priority, activate or deactivate whole groups for the editor, import/export JSON (`smst.dictionary`), and optionally install packs from a **remote catalog** (HTTP).
- **Leetspeak rules:** Define character-to-character rules, reorder them, and apply them together with dictionary replacements.
- **History:** Keep a local list of prepared texts for quick reuse (copy from a tap).
- **Privacy-first core:** Dictionary, rules, and history stay on your device; there is no mandatory account for the main flow described in onboarding.

---

## Included features and limits (summary)

The app may offer **free**, **trial**, **premium**, or **ad-supported** access depending on the build and store configuration. Examples of gated areas (see in-app labels and paywalls for the exact rules in your version):

- **Dictionaries:** Limit on how many dictionary groups you can use in free mode; **import** may be limited on free tier then unlocked via premium or rewarded ads; **remote catalog sync** is typically a premium (or ad-unlocked) path.
- **Editor / history:** Actions such as **copy**, **share**, **save to history**, or **full history** may require premium or watching a rewarded ad, depending on feature flags.
- **Ads and subscriptions:** Third-party ads and/or in-app purchases may be shown in line with `feature_config` and store policies.

Limits and entitlements can change with app updates; the **in-app** experience and store listing prevail over this page.

---

## FAQ

**Do I need an account?**  
No. You can use SMST for the core local workflow without creating an account.

**Do I need internet?**  
Much of the app works **offline**. Internet is used when you choose features that need it (for example **remote dictionary catalog**, **ads**, or **in-app purchases**).

**Will I lose my data if I uninstall?**  
Local data (dictionary, history, settings) lives on your device. Uninstalling the app can **permanently remove** that data unless you have exported a backup.

**Does the app moderate what I write?**  
No. You choose dictionary entries and replacements. You are responsible for how you use prepared text on each platform and under applicable law.

---

## Contact

For support or feedback:

**Email:** samirtf.dev@gmail.com
